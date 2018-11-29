## Quoatation Tagger

This Python code finds quotation phrase from sentences in order to extract macro economic indicator and expert opinions.

## Reference Code
Based on code by [Guilaume Lample](https://github.com/glample/tagger)

## Result
This code extract experts and their mentions from sentences as fllow:
<양기인 신한금융투자 리서치센터장:talker>은 29일 <"소재, 산업재 등 경기 민감주가 상승하는 가운데 IT 업종이 반등하면서 코스피지수가 최고치를 경신했다":quot>고 설명했다.


## Dataset
We will use the Korean quoatation dataset.

## Installation

**1. Fork & Clone** : Fork this project to your repository and colne to your work directory.

```https://github.com/OpenXAIProject/Financial-Expert-Korean-Quot.git```

**2. Run** : Add the following Python scirpt to your code.

from korean_quot_tagger import korean_quot_tagger

quot_tagger = korean_quot_tagger()
	quot_tagger.predicts(u'양기인 신한금융투자 리서치센터장은 29일 \"소재, 산업재 등 경기 민감주가 상승하는 가운데 IT 업종이 반등하면서 코스피지수가 최고치를 경신했다\"고 설명했다.')
	
## Requirements 
+ Theano (1.0.0)
+ numpy (1.15.0)

## License
[Apache License 2.0](https://github.com/OpenXAIProject/tutorials/blob/master/LICENSE "Apache")

## Contacts
If you have any question, please contact Sunjae Kwonn(soon91jae@unist.ac.kr).

<br /> 
<br />

# XAI Project 

**This work was supported by Institute for Information & Communications Technology Promotion(IITP) grant funded by the Korea government(MSIT) (No.2017-0-01779, A machine learning and statistical inference framework for explainable artificial intelligence)**

+ Project Name : A machine learning and statistical inference framework for explainable artificial intelligence(의사결정 이유를 설명할 수 있는 인간 수준의 학습·추론 프레임워크 개발)

+ Managed by Ministry of Science and ICT/XAIC <img align="right" src="http://xai.unist.ac.kr/static/img/logos/XAIC_logo.png" width=300px>

+ Participated Affiliation : UNIST, Korea Univ., Yonsei Univ., KAIST, AItrics  

+ Web Site : <http://openXai.org>
