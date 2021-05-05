# basic-course  

## Webtoon Image Segmentation  

Here is information about [webtoon literary property](https://m.help.naver.com/support/contents/contentsView.help?contentsNo=1846) of naver webtoon.  
please just use the code for research purposes, never distribute the toon data.  

And then, We can provide the step 
'Get Webtoon Image -> Webtoon-Segmentation -> Create Segmentation Datasets'

**First**, we created webcrawling and cut detector only use computer vision(no deep learning)  
see more information, go to title ['Get Webtoon Image'](#get-webtoon-image)  

**Second**, we learned segmentation model.  
see more information, go to title ['Webtoon-Segmentation'](#webtoon-segmentation)  
  
**Third**, we created segmentation results. it can be used at colorization datasets, etc...   
see more information, got to title ['Create Segmentation Results'](#create-segmentation-results)
  

## Get Webtoon Image  

If you want to use the webtoon data, run 'get_toon_data.py'  

## Prerequisites  
It needs to download driver.exe.  
If you use the chrome, you might use chromedriver.exe.  
In this [here](https://chromedriver.chromium.org/downloads), you can download chromedriver with your same chrome version.  


```
pip install selenium
pip install opencv-python
python get_toon_data.py
```
  
#### Functions:  
- webcrawling: webcrawling function  
- linkimg: link the all webcrawling image at same episode  
- cutdetector_rough: cutdect rougly. get speech bubble, big cut dected image  
- cutdetector: final output cutdector   
  
  
#### Examples of output images:

| webcrawling | linkimg (short example) | cutdetector_rough | cutdetector |
|:---:|:---:|:---:|:---:|
|![0](https://user-images.githubusercontent.com/56310078/115051573-edf12480-9f17-11eb-98f2-7a6e0ba50fa0.jpg)|![image](https://user-images.githubusercontent.com/56310078/115052397-dc5c4c80-9f18-11eb-9945-81f828294e1d.png)|![1041](https://user-images.githubusercontent.com/56310078/115051600-f8abb980-9f17-11eb-9ed1-787a4b817f0a.jpg)|![1041](https://user-images.githubusercontent.com/56310078/115051620-fe090400-9f17-11eb-9618-175496c46b32.jpg)|  
|-|-|![1440](https://user-images.githubusercontent.com/56310078/115051605-f9dce680-9f17-11eb-97f6-20ad2172681f.jpg)|-|  
|-|-|![1768](https://user-images.githubusercontent.com/56310078/115051608-f9dce680-9f17-11eb-8fec-4dc97a6ccfd2.jpg)|-|  
  
  
#### output directories:  

		get_toon_data.py
		chromedriver.exe
            ├── webcrawlingimg
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

### Class 

    0 : hair
    1 : dress-shirt
    2 : T-shirt
    3 : pants
    4 : skirt
    5 : outer
    6 : tie
    7 : vest

### Results

#### Trained dataset
- Note: Free draw 프리드로우 (episode: random part(0.9 percent of entire images) of 1,2,3,4,5,102,201)
- Note: Love revolution 연애혁명 (episode: random part(0.9 percent of entire images) of 2,3,4,5,6,7,8)

#### Test dataset
- Note: Free draw 프리드로우 (episode: another random part(0.1 percent of entire images) of 1,2,3,4,5,102,201)
- Note: Love revolution 연애혁명 (episode: another random part(0.1 percent of entire images) of 2,3,4,5,6,7,8)
- Free draw + Love revolution  
  <img src="https://user-images.githubusercontent.com/56310078/115048075-27279580-9f14-11eb-92a1-248a249bd5cb.png" width="500">  
- Only Free draw  
  <img src="https://user-images.githubusercontent.com/56310078/115048076-2858c280-9f14-11eb-84bd-8024f9bba330.png" width="500">
- Love revolution  
  <img src="https://user-images.githubusercontent.com/56310078/115048079-2989ef80-9f14-11eb-9d9e-b5e8bec67819.png" width="500">  
  

#### experiment 1) Trained(Free draw + Love Revolution) -> Test(Free draw + Love Revolution)
- Evaluation results for bbox:

![bbox1](https://user-images.githubusercontent.com/56310078/115056462-dc128000-9f1d-11eb-8cb8-a866291ff459.png)  
![bbox2](https://user-images.githubusercontent.com/56310078/115056464-dd43ad00-9f1d-11eb-8142-afabd021bcdc.png)  
![bbox3](https://user-images.githubusercontent.com/56310078/115056466-dd43ad00-9f1d-11eb-8e18-79aa8a35b528.png)  
  
- Evaludation results for Segm:

![segm1](https://user-images.githubusercontent.com/56310078/115056469-dddc4380-9f1d-11eb-93ee-c1f4f8b2d5fb.png)  
![segm2](https://user-images.githubusercontent.com/56310078/115056471-dddc4380-9f1d-11eb-9edf-2d09a0b37840.png)  
![segm3](https://user-images.githubusercontent.com/56310078/115056473-de74da00-9f1d-11eb-9ab7-c6785634a255.png)  


#### experiment 2) Trained(Free draw + Love Revolution) -> Test(Free draw)
- Evaluation results for bbox:

![bbox1](https://user-images.githubusercontent.com/56310078/115056644-10863c00-9f1e-11eb-94d6-cb8cdfdff8a2.png)  
![bbox2](https://user-images.githubusercontent.com/56310078/115056647-11b76900-9f1e-11eb-84cd-2a716050fb39.png)  
![bbox3](https://user-images.githubusercontent.com/56310078/115056649-11b76900-9f1e-11eb-89ab-3ade7d31b50f.png)  
  
- Evaludation results for Segm:

![segm1](https://user-images.githubusercontent.com/56310078/115056651-124fff80-9f1e-11eb-9ec1-3a7973a60146.png)  
![segm2](https://user-images.githubusercontent.com/56310078/115056655-124fff80-9f1e-11eb-9bec-9285e909220a.png)  
![segm3](https://user-images.githubusercontent.com/56310078/115056656-12e89600-9f1e-11eb-9487-1f677c78b236.png)  


#### experiment 3) Trained(Free draw + Love Revolution) -> Test(Love Revolution)
- Evaluation results for bbox:

![bbox1](https://user-images.githubusercontent.com/56310078/115056748-2b58b080-9f1e-11eb-9ec2-4874aead2431.png)  
![bbox2](https://user-images.githubusercontent.com/56310078/115056752-2bf14700-9f1e-11eb-9081-7faa8c4a42e6.png)  
![bbox3](https://user-images.githubusercontent.com/56310078/115056754-2c89dd80-9f1e-11eb-9dac-2868cc55a94b.png)  

- Evaludation results for Segm:


![segm1](https://user-images.githubusercontent.com/56310078/115056757-2dbb0a80-9f1e-11eb-981c-4f2ebbb4c4dc.png)  
![segm2](https://user-images.githubusercontent.com/56310078/115056758-2dbb0a80-9f1e-11eb-8f83-7ad01a3fcdb4.png)  
![segm3](https://user-images.githubusercontent.com/56310078/115056759-2e53a100-9f1e-11eb-9ea8-5a5f9aeb9ee4.png)  


#### experiment 4) Trained(Only Free draw) -> Test(Only Free draw)
- Evaluation results for bbox:

![bbox1](https://user-images.githubusercontent.com/56310078/115056816-3f9cad80-9f1e-11eb-9923-1589f2487fae.png)  
![bbox2](https://user-images.githubusercontent.com/56310078/115056817-40cdda80-9f1e-11eb-8596-aa5a5f7289ea.png)  
![bbox3](https://user-images.githubusercontent.com/56310078/115056820-40cdda80-9f1e-11eb-92f5-18bcde94964b.png)  

- Evaludation results for Segm:

![segm1](https://user-images.githubusercontent.com/56310078/115056823-41667100-9f1e-11eb-8149-ec44feb9ee2c.png)  
![segm2](https://user-images.githubusercontent.com/56310078/115056824-41667100-9f1e-11eb-890a-4402d4bedeed.png)  
![segm3](https://user-images.githubusercontent.com/56310078/115056827-41ff0780-9f1e-11eb-91c6-3b4026687fba.png)  


#### experiment 5) Pretrained(Free draw) + Transfer learning(Love Revolution) -> Test(Love Revolution)
- Evaluation results for bbox:

![bbox1](https://user-images.githubusercontent.com/56310078/115056885-50e5ba00-9f1e-11eb-8db1-98a77495fe64.png)  
![bbox2](https://user-images.githubusercontent.com/56310078/115056889-5216e700-9f1e-11eb-942a-150d56d3bca2.png)  
![bbox3](https://user-images.githubusercontent.com/56310078/115056890-52af7d80-9f1e-11eb-96a8-0d54760eb26b.png)  

- Evaludation results for Segm:

![segm1](https://user-images.githubusercontent.com/56310078/115056893-52af7d80-9f1e-11eb-9f79-818e42ae84b8.png)  
![segm2](https://user-images.githubusercontent.com/56310078/115056895-53481400-9f1e-11eb-835d-d6cbe3c6ed81.png)  
![segm3](https://user-images.githubusercontent.com/56310078/115056897-53481400-9f1e-11eb-9696-d16615e2356b.png)  


#### experiment 6) Trained(Only Love Revolution) -> Test(Only Love Revolution)
- Evaluation results for bbox:

![bbox1](https://user-images.githubusercontent.com/56310078/115056982-707ce280-9f1e-11eb-9401-e95e229e9abd.png)  
![bbox2](https://user-images.githubusercontent.com/56310078/115056988-71ae0f80-9f1e-11eb-86aa-3d5d5847aede.png)  
![bbox3](https://user-images.githubusercontent.com/56310078/115056989-71ae0f80-9f1e-11eb-9532-58f7dfabbebf.png)  

- Evaludation results for Segm:

![segm1](https://user-images.githubusercontent.com/56310078/115056991-7246a600-9f1e-11eb-8c35-e3374868ef00.png)  
![segm2](https://user-images.githubusercontent.com/56310078/115056992-7246a600-9f1e-11eb-808f-93b5d9408275.png)  
![segm3](https://user-images.githubusercontent.com/56310078/115056993-72df3c80-9f1e-11eb-8334-bd2ef12c72fb.png)  


#### experiment 7) Pretrained(Love Revolution) + Transfer learning(Free draw) -> Test(Free draw)
- Evaluation results for bbox:

- Evaludation results for Segm:


#### Examples of output images (experiment 1):

- Results of Experiment 1(Trained(Free draw + Love Revolution) -> Test(Free draw + Love Revolution)) 
- Free draw

| model prediction | label | 
|:---:|:---:|
|![11661](https://user-images.githubusercontent.com/56310078/115060858-5560a180-9f23-11eb-9b3b-ad49ce8c7af1.jpg)|![11661](https://user-images.githubusercontent.com/56310078/115060892-5e517300-9f23-11eb-810c-4ae2ed1967f2.jpg)|
|![12197](https://user-images.githubusercontent.com/56310078/115058443-3a406280-9f20-11eb-9d76-00dfcca0e0b4.jpg)|![12197](https://user-images.githubusercontent.com/56310078/115060274-a328da00-9f22-11eb-8130-379421202bf4.jpg)|
|![14289](https://user-images.githubusercontent.com/56310078/115058445-3ad8f900-9f20-11eb-87a4-380760ea40d9.jpg)|![14289](https://user-images.githubusercontent.com/56310078/115060276-a328da00-9f22-11eb-9d2f-15da67b06310.jpg)|
|![15991](https://user-images.githubusercontent.com/56310078/115058448-3ad8f900-9f20-11eb-9406-abafc93e3cc7.jpg)|![15991](https://user-images.githubusercontent.com/56310078/115060278-a3c17080-9f22-11eb-90ef-dad7d8757cc9.jpg)|
|![16205](https://user-images.githubusercontent.com/56310078/115058451-3ca2bc80-9f20-11eb-80a2-f110da8f41b2.jpg)|![16205](https://user-images.githubusercontent.com/56310078/115060280-a3c17080-9f22-11eb-971e-253819587916.jpg)|
|![17759](https://user-images.githubusercontent.com/56310078/115058455-3d3b5300-9f20-11eb-8d98-01f0c5de1028.jpg)|![17759](https://user-images.githubusercontent.com/56310078/115060281-a45a0700-9f22-11eb-8dbd-84714ada74bc.jpg)|
|![21912](https://user-images.githubusercontent.com/56310078/115058459-3d3b5300-9f20-11eb-9d84-3fdc7fd6da2f.jpg)|![21912](https://user-images.githubusercontent.com/56310078/115060283-a4f29d80-9f22-11eb-9759-5796e5574a33.jpg)|
|![22515](https://user-images.githubusercontent.com/56310078/115058462-3dd3e980-9f20-11eb-9ab5-bcf6c0afccef.jpg)|![22515](https://user-images.githubusercontent.com/56310078/115060284-a58b3400-9f22-11eb-98ef-f1a832be1f96.jpg)|
|![22861](https://user-images.githubusercontent.com/56310078/115058465-3dd3e980-9f20-11eb-99cf-2856101f659d.jpg)|![22861](https://user-images.githubusercontent.com/56310078/115060287-a58b3400-9f22-11eb-8c01-89342b69d7e2.jpg)|
|![23968](https://user-images.githubusercontent.com/56310078/115058469-3f051680-9f20-11eb-8e5c-522aa6948f4b.jpg)|![23968](https://user-images.githubusercontent.com/56310078/115060288-a623ca80-9f22-11eb-95cc-7135175905e4.jpg)|
|![24213](https://user-images.githubusercontent.com/56310078/115058471-3f9dad00-9f20-11eb-8b97-351b7b3c4f81.jpg)|![24213](https://user-images.githubusercontent.com/56310078/115060289-a623ca80-9f22-11eb-835c-209f23585702.jpg)|
|![25413](https://user-images.githubusercontent.com/56310078/115058473-40364380-9f20-11eb-8ac0-2ea67c719e99.jpg)|![25413](https://user-images.githubusercontent.com/56310078/115060290-a6bc6100-9f22-11eb-9c5e-5e8d49a9bf88.jpg)|
|![27575](https://user-images.githubusercontent.com/56310078/115058477-41677080-9f20-11eb-97ed-80c643d2fc5a.jpg)|![27575](https://user-images.githubusercontent.com/56310078/115060292-a6bc6100-9f22-11eb-994d-a0ea9530444d.jpg)|
|![30278](https://user-images.githubusercontent.com/56310078/115058479-42000700-9f20-11eb-927b-5ac14986f5e2.jpg)|![30278](https://user-images.githubusercontent.com/56310078/115060295-a754f780-9f22-11eb-891c-01887586503f.jpg)|
|![34111](https://user-images.githubusercontent.com/56310078/115058480-42989d80-9f20-11eb-9405-55605a279eea.jpg)|![34111](https://user-images.githubusercontent.com/56310078/115060298-a7ed8e00-9f22-11eb-9b52-4886ad007a6b.jpg)|
|![35419](https://user-images.githubusercontent.com/56310078/115058482-42989d80-9f20-11eb-9f0b-98cc7428a2de.jpg)|![35419](https://user-images.githubusercontent.com/56310078/115061094-a8d2ef80-9f23-11eb-82be-7a6be52db8cd.jpg)|
|![36317](https://user-images.githubusercontent.com/56310078/115058483-43313400-9f20-11eb-9372-7bb2fde0dff3.jpg)|![36317](https://user-images.githubusercontent.com/56310078/115060307-a8862480-9f22-11eb-9c05-f3181bec6a8e.jpg)|
|![37949](https://user-images.githubusercontent.com/56310078/115058487-44626100-9f20-11eb-9757-b097124c4e00.jpg)|![37949](https://user-images.githubusercontent.com/56310078/115060308-a8862480-9f22-11eb-9839-32a587b9e48e.jpg)|
|![48075](https://user-images.githubusercontent.com/56310078/115058489-44faf780-9f20-11eb-86a5-188377bc17f1.jpg)|![48075](https://user-images.githubusercontent.com/56310078/115060311-a91ebb00-9f22-11eb-94b2-1754fe57a559.jpg)|
|![48683](https://user-images.githubusercontent.com/56310078/115058490-44faf780-9f20-11eb-9e5e-1c8c48b44712.jpg)|![48683](https://user-images.githubusercontent.com/56310078/115060313-a91ebb00-9f22-11eb-8fae-20c426ece8b2.jpg)|
|![53380](https://user-images.githubusercontent.com/56310078/115058491-45938e00-9f20-11eb-8945-8ca83beffb0f.jpg)|![53380](https://user-images.githubusercontent.com/56310078/115060315-a9b75180-9f22-11eb-853e-b165855cd132.jpg)|

- Love revolution

| model prediction | label | 
|:---:|:---:|
|![1288](https://user-images.githubusercontent.com/56310078/115059285-509aee00-9f21-11eb-9790-4ff6518cffdc.jpg)|![1288](https://user-images.githubusercontent.com/56310078/115059722-e767aa80-9f21-11eb-83ef-7651f1b9d8fb.jpg)|
|![8181](https://user-images.githubusercontent.com/56310078/115059288-51338480-9f21-11eb-81a6-7fd5a1219e0c.jpg)|![8181](https://user-images.githubusercontent.com/56310078/115059725-e8004100-9f21-11eb-9a15-b7be4c55ec12.jpg)|
|![12241](https://user-images.githubusercontent.com/56310078/115059290-51cc1b00-9f21-11eb-905a-a6792321b921.jpg)|![12241](https://user-images.githubusercontent.com/56310078/115059727-e898d780-9f21-11eb-970e-884062b8312c.jpg)|
|![12602](https://user-images.githubusercontent.com/56310078/115059293-5264b180-9f21-11eb-8e42-8cd6f18f566a.jpg)|![12602](https://user-images.githubusercontent.com/56310078/115059729-e9316e00-9f21-11eb-83b8-5bb3dc3a3dd9.jpg)|
|![13143](https://user-images.githubusercontent.com/56310078/115059295-5264b180-9f21-11eb-913b-5a89ca6e37b5.jpg)|![13143](https://user-images.githubusercontent.com/56310078/115059731-e9316e00-9f21-11eb-92d8-17aa39537f44.jpg)|
|![16515](https://user-images.githubusercontent.com/56310078/115059298-52fd4800-9f21-11eb-9f6f-21d9d4c477de.jpg)|![16515](https://user-images.githubusercontent.com/56310078/115059733-e9ca0480-9f21-11eb-9efe-e0bbba2f3270.jpg)|
|![30354](https://user-images.githubusercontent.com/56310078/115059303-542e7500-9f21-11eb-90cd-57f6c645a5cd.jpg)|![30354](https://user-images.githubusercontent.com/56310078/115059734-ea629b00-9f21-11eb-8909-9c42724e039b.jpg)|
|![34234](https://user-images.githubusercontent.com/56310078/115059305-54c70b80-9f21-11eb-8195-18dd0049cab0.jpg)|![34234](https://user-images.githubusercontent.com/56310078/115059738-ea629b00-9f21-11eb-963d-a05f27318f6a.jpg)|


### Download Pre-trained models

Download pre-trained model from [Google Drive](https://drive.google.com/drive/folders/1CmxGzSGyCafVI5UpFFGUiAWSAh3BS3eR?usp=sharing)

### Run  
- Here is the [Colab Notebook](https://github.com/overfitting-ai-community/basic-course/blob/main/Webtoon_Segmentation_Detectron2_Tutorial.ipynb) to run Detectron2.
- Here is the [Colab Notebook](#) to run Mask-RCNN.

## Create Segmentation Results

#### Examples of output images:

refer to the last cell of [detectron2 colab guide](https://github.com/overfitting-ai-community/basic-course/blob/main/Webtoon_Segmentation_Detectron2_Tutorial.ipynb).  

| Free draw (only hair) | Love revolution (only shirts) | No trained webtoon (etc) |
|:---:|:---:|:---:|
| ![19028](https://user-images.githubusercontent.com/56310078/115044584-9bf8d080-9f10-11eb-9b3b-afc8515879d7.jpg)|![10435](https://user-images.githubusercontent.com/56310078/115045380-6b656680-9f11-11eb-9f5f-8d8604df12bd.jpg)|![12296](https://user-images.githubusercontent.com/56310078/115046022-fba3ab80-9f11-11eb-9dc1-55a1e286d463.jpg)||
| ![63842](https://user-images.githubusercontent.com/56310078/115044595-9ef3c100-9f10-11eb-85d8-aaca15c35b92.jpg)|![12280](https://user-images.githubusercontent.com/56310078/115045385-6c969380-9f11-11eb-8a52-e28b18a412d1.jpg)|![5233](https://user-images.githubusercontent.com/56310078/115046551-8c7a8700-9f12-11eb-9b91-ab98e5ce3fb0.jpg)|| 
| ![50152](https://user-images.githubusercontent.com/56310078/115044610-a1eeb180-9f10-11eb-8001-97049a71c0c4.jpg)|![20404](https://user-images.githubusercontent.com/56310078/115045438-76b89200-9f11-11eb-8b68-b15be23e8162.jpg)|![86848](https://user-images.githubusercontent.com/56310078/115046577-943a2b80-9f12-11eb-8ed6-0c298669f0f1.jpg)||
| ![24992](https://user-images.githubusercontent.com/56310078/115044626-a61acf00-9f10-11eb-816f-83737f2d1478.jpg)|![38444](https://user-images.githubusercontent.com/56310078/115045455-7a4c1900-9f11-11eb-88f2-a2028d73ea1a.jpg)|![7649](https://user-images.githubusercontent.com/56310078/115045972-f3e40700-9f11-11eb-87d2-40115ecde7b6.jpg)||
| ![28738](https://user-images.githubusercontent.com/56310078/115044551-9602ef80-9f10-11eb-8585-1f82c9d6bae0.jpg) |![33124](https://user-images.githubusercontent.com/56310078/115045464-7d470980-9f11-11eb-8f93-63db110e8a84.jpg)|![18688](https://user-images.githubusercontent.com/56310078/115045823-d9119280-9f11-11eb-9bef-3cc0bc3f41d9.jpg)||


## Conclusion(Our insight)  

- 웹툰에서 등장인물에 대한 신체 특징(헤어), 의상을 자동채색하기 위해서, 웹툰 등장인물에 대한 Segmentation을 진행하였다. 
- 자동채색을 위해 데이터셋을 Segmentation 하는 것까지 진행하였고, 그 결과가 'Create Segmentation Results' 부분이다.
- 우리의 목표는 한 컷의 이미지를 전부 자동채색하는 것이 아닌 특정 부분, 부분을 자동채색하는 것이다. 따라서 모델의 학습을 위해 특정 클래스로 세분화 하였다.
- 웹툰은 무한히 상상할 수 있는 세계로, 뿔, 날개, 꼬리 등과 같이 인물이 가질 수 있는 다양한 특징들이 무수히 많다. 이것을 모두 클래스화 하기에는 무리가 있다.
- 따라서 웹툰 이미지의 인물의 특징 중에서도 '헤어'와 '교복'으로 그 범위를 한정하여 데이터를 수집, 클래스화 하였다.
- Detectron2의 Weight를 가져온 이후에, 모델이 해당 데이터셋에 대하여 오버피팅이 되도록 의도하였다. 그 이유는 하나의 웹툰에 대해서 더 잘 Segmentation 하기 위함이다.
- 다양한 장르의 현존하는 모든 웹툰에 대하여 Robust하게 Segmentation을 할 수는 없다고 판단하였기 때문이다.
- 또한 각각의 웹툰은 그 웹툰만의 고유한 특징(그림체, 장르 등)이 있다. 그 웹툰만의 고유한 특징을 잘 살리는 것(하나의 웹툰에 오버피팅)이 중요하다고 판단하였다.
- 수집한 웹툰의 데이터셋은 하나의 웹툰에서도 회차가 진행될 수록 작가의 그림체가 바뀌는 것을 고려하였다.


## Team players  
[nh9k](https://github.com/nh9k), [haechunchung](https://github.com/haechunchung), [minqukanq](https://github.com/minqukanq)  
  

## Citing Detectron2
We use detectron2 in our research

```BibTeX
@misc{wu2019detectron2,
  author =       {Yuxin Wu and Alexander Kirillov and Francisco Massa and
                  Wan-Yen Lo and Ross Girshick},
  title =        {Detectron2},
  howpublished = {\url{https://github.com/facebookresearch/detectron2}},
  year =         {2019}
}
```

