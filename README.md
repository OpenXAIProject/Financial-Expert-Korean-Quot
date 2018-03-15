## 인용문 태거

거시 경제 지표 및 전문가 여론 자료 추출하기 위해 문장에서 인용문을 찾습니다. 

## Initial setup

python 2.7, theano

## 사용법

from korean_quot_tagger import korean_quot_tagger

quot_tagger = korean_quot_tagger()
	quot_tagger.predicts(u'양기인 신한금융투자 리서치센터장은 29일 \"소재, 산업재 등 경기 민감주가 상승하는 가운데 IT 업종이 반등하면서 코스피지수가 최고치를 경신했다\"고 설명했다.')
	
	<양기인 신한금융투자 리서치센터장:talker>은 29일 <"소재, 산업재 등 경기 민감주가 상승하는 가운데 IT 업종이 반등하면서 코스피지수가 최고치를 경신했다":quot>고 설명했다.


<img src="http://xai.unist.ac.kr/static/img/logos/XAIC_logo.png" width="300" height="100">

# XAI Project 

### **Project Name** 
> A machine learning and statistical inference framework for explainable artificial intelligence(의사결정 이유를 설명할 수 있는 인간 수준의 학습·추론 프레임워크 개발)
### **Managed by** 
> Ministry of Science and ICT/XAIC
### **Participated Affiliation** 
> UNIST, Korean Univ., Yonsei Univ., KAIST., AItrics
### **Web Site** 
> <http://openXai.org>

