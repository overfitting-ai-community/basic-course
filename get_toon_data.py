from selenium import webdriver
import time
import urllib.request
import cv2
import numpy as np
import os
import math
import argparse

def webcrawling(inputurl, episodelastname, episodenum, outputdir):
    if not os.path.exists('./' + outputdir):
        os.mkdir('./' + outputdir)
    if not os.path.exists('./' + outputdir + '/Episode' + str(episodenum)):
        os.mkdir('./' + outputdir + '/Episode' + str(episodenum))

    driver = webdriver.Chrome()
    driver.get(inputurl)
    episode = episodenum    # bonus episode not included, i.e. special edition, ...

    while 1:
        # waiting for loading time
        time.sleep(1)
        title = driver.find_element_by_css_selector(".view h3")
        print(title.text)

        # download image
        for cuts in range(len(driver.find_elements_by_css_selector(".wt_viewer img"))-1):
            imgUrl = driver.find_elements_by_css_selector(".wt_viewer img")[cuts].get_attribute("src")
            print(imgUrl)
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent',
                                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgUrl, outputdir + '/Episode' + str(episode) + '/' + str(cuts) + '.jpg')

        # go to the next page
        if (title.text == episodelastname):
            break
        episode -= 1
        driver.find_element_by_css_selector(".pre").click()
        if not os.path.exists('./' + outputdir + '/Episode' + str(episode)):
            os.mkdir('./' + outputdir + '/Episode' + str(episode))

    driver.close()


def linkimg(inputdir, episodedir):
    imglist = os.listdir('./' + inputdir + '/' + episodedir)

    # sorted with image name
    imgtype = imglist[0][-4:]
    sortedimg = [int(img[0:-4]) for img in imglist]
    sortedimg.sort()

    # entire height of new image
    entire_height = 0
    for img in sortedimg:
        _img = cv2.imread('./' + inputdir + '/' + episodedir + '/' + str(img) + imgtype)
        height, width, _ = _img.shape
        entire_height += height

    # create new image
    newimg = np.zeros((entire_height, width, 3), np.uint8)

    # linking all crawling image
    hp = 0
    for img in sortedimg:
        _img = cv2.imread('./' + inputdir + '/' + episodedir + '/' + str(img) + imgtype)
        height, width, _ = _img.shape
        newimg[hp:(hp + height), :, :] = _img[:]
        hp += height

    # cv2.imwrite("all_cut_.jpg", newimg)
    return newimg


def cutdetector_rough(inputimg, outputdir, episodedir):
    if not os.path.exists('./' + outputdir):
        os.mkdir('./' + outputdir)
    if not os.path.exists('./' + outputdir + '/' + episodedir):
        os.mkdir('./' + outputdir + '/' + episodedir)

    spt, ept = 0, 0
    val = 0
    for row in range(len(inputimg[:,0,:])):
        if (len(np.unique(inputimg[row, :, :])) != 1) & (val == 0):
            spt = row
            val = 1
        elif (len(np.unique(inputimg[row, :, :])) == 1) & (val == 1):
            ept = row
            val = 0

        if (spt != 0) & (ept != 0) & ((ept - spt - 1) > 0):
            newimg = np.zeros((ept - spt - 1, len(inputimg[0,:,:]), 3), np.uint8)
            newimg[:] = inputimg[spt:ept - 1, :, :]
            cv2.imwrite('./' + outputdir + '/' + episodedir + '/' + str(row) + '.jpg', newimg)
            spt, ept = 0, 0


def cutdetector(inputdir, outputdir):
    imglist = os.listdir('./' + inputdir)
    print('all file length', len(imglist))

    if not os.path.exists('./' + inputdir + '/'+ outputdir):
        os.mkdir('./' + inputdir + '/'+ outputdir)

    if '.DS_Store' in imglist:
        imglist.remove('.DS_Store')
        print('.DS_Store erased!')

    for k in range(len(imglist)):
        print('{} image processing: {}'.format(k + 1, imglist[k]))
        image = cv2.imread('./' + inputdir + '/{}'.format(imglist[k]), cv2.IMREAD_UNCHANGED)
        print('./' + inputdir + '/{}'.format(imglist[k]))
        if imglist[k] == 'outputs':
            continue
        height, width, channel = image.shape

        output = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        canny = cv2.Canny(gray, 3000, 2000, apertureSize=5, L2gradient=True)

        lines = []
        lines = cv2.HoughLines(canny, 0.8, np.pi / 180, 200, srn=100, stn=200, min_theta=0, max_theta=np.pi)

        y_list = []

        if isinstance(lines, np.ndarray):
            for i in lines:
                rho, theta = i[0][0], i[0][1]

                if not math.isnan(rho) and not math.isnan(theta):
                    a, b = np.cos(theta), np.sin(theta)
                    x0, y0 = a * rho, b * rho

                    scale = image.shape[0] + image.shape[1]

                    x1 = int(x0 + scale * -b)
                    y1 = int(y0 + scale * a)
                    x2 = int(x0 - scale * -b)
                    y2 = int(y0 - scale * a)

                    if y1 == y2 and 0 <= y1 <= height:
                        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
                        y_list.append(y1)

        if y_list != []:
            output = output[min(y_list):max(y_list), 0:width]
            # plt.axis('off')
            # plt.imshow(output)
            # plt.show()
            try:
                output = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)
                cv2.imwrite('./' + inputdir + '/'+ outputdir + '/' + imglist[k], output)
            except:
                print("cv2.cvtColor error!")
                f = open("error_list.txt", 'a')
                f.write('./' + inputdir + '/{}'.format(imglist[k]) + "\n")
        else:
            print('no image cut')
        print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--web_dir', default='webcrawlingimg', type = str,
                        help='webcrawling image directory name.')
    parser.add_argument('--roughcut_dir', default='cuts', type = str,
                        help='rough cut image directory name.')
    parser.add_argument('--cutdector_dir', default='outputs', type = str,
                        help='final cut image directory name.')
    parser.add_argument('--start_website_url', default='https://comic.naver.com/webtoon/detail.nhn?titleId=597447&no=104&weekday=sat', type = str,
                        help='start website url. if you want to get episode100~101, put episode 101 url!')
    parser.add_argument('--end_website_title', default='제100화 작년 미술부에서 있었던 일 (3)', type = str,
                        help='end website title. if you want to get episode100~101, put episode 101 title!')
    parser.add_argument('--start_episode_num', default=101, type = int,
                        help='start episode number.')
    args = parser.parse_args()

    webdir = args.web_dir
    roughcutdir = args.roughcut_dir
    cutdir = args.cutdector_dir
    webcrawling(args.start_website_url,args.end_website_title, args.start_episode_num, webdir)


    episodelist = os.listdir(webdir)
    for elist in episodelist:
        print(elist)
        linkedIMG = linkimg(webdir, elist)
        cutdetector_rough(linkedIMG, roughcutdir, elist)
        cutdetector(roughcutdir + '/' + elist, cutdir)