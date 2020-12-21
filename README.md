# basic-course  

## Webtoon Image Segmentation  

**First**, here is information about [webtoon literary property](https://m.help.naver.com/support/contents/contentsView.help?contentsNo=1846) of naver webtoon.  
please just use the code for research purposes, never distribute the toon data.  

**Second**, we created webcrawling and cut detector only use computer vision(no deep learning)  
see more information, go to title ['Get Webtoon Image'](#get-webtoon-image)  

**Third**, we learned segmentation model.  
see more information, go to title ['Webtoon-Segmentation'](#webtoon-segmentation)  
  


## Prerequisites  
It need to download driver.exe.  
If you use the chrome, you might use chromedriver.exe.  
In this [here](https://chromedriver.chromium.org/downloads), you can download chromedriver with your same chrome version.  
  

## Get Webtoon Image  
If you want to use the webtoon data, run 'get_toon_data.py'  

```
python get_toon_data.py
```
  
#### function:  
webcrawling: webcrawling function  
linkimg: link the all webcrawling image at same episode  
cutdetector_rough: cutdect rougly. get speech bubble, big cut detected image  
cutdetector: final output cutdetector   
  
  
#### output images:  
coming soon!    

webcrawling:  
linkimg:  
cutdetector_rough:  
cutdetector:  

  
  
#### output directories:  

		get_toon_data.py
		chromedriver.exe
            └── webcrawlingimg
                └── Episode100
                    └── 0.jpg(webcrawling image)
                    └── 1.jpg(webcrawling image)
                    └── '...'.jpg(webcrawling image)
                └── Episode101
                └── ...
            └── cuts
                └── Episode100
                    └── outputs(final cutdetector)
                        └── 592.jpg(final cutdetector)
                        └── '...'.jpg(final cutdetector)
                    └── 592.jpg(rough cutdetector)
                    └── '...'.jpg(rough cutdetector)
                └── Episode101
                └── ...

  
## Webtoon-Segmentation  
coming soon!


### Author(team players)  
[nh9k](https://github.com/nh9k), [haechunchung](https://github.com/haechunchung), [minqukanq](https://github.com/minqukanq)  
  

