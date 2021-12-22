# HRV analysis using remote PPG
비접촉식 PPG(RPPG) 측정 기술을 이용하여 원격으로 HRV를 분석한다.
## 관련 실적
- [Yu, S. G., Kim, S. E., Kim, N. H., Suh, K. H., & Lee, E. C. (2021). Pulse Rate Variability Analysis Using Remote Photoplethysmography Signals. Sensors, 21(18), 6241.](https://www.mdpi.com/1424-8220/21/18/6241)
- "원격 광용적맥파 측정을 이용한 비접촉 심박 변이도 분석 장치 및 방법", 국내특허출원 (출원번호: 10-2021-0125000, 출원일: 2021.10.22), 발명자(이의철, 유수경), 출원인(상명대학교산학협력단)

## 목차
1. [HRV 개념](https://github.com/sugyeong-yu/RPPG-HRV_analysis/blob/main/Readme.md#hrv-%EB%9E%80)
2. [Code inform](https://github.com/sugyeong-yu/RPPG-HRV_analysis/blob/main/Readme.md#code-inform)
3. [Protocol](https://github.com/sugyeong-yu/RPPG-HRV_analysis/blob/main/Readme.md#protocol)
4. [Result](https://github.com/sugyeong-yu/RPPG-HRV_analysis/blob/main/Readme.md#result)
5. [관련 모듈](https://github.com/sugyeong-yu/RPPG-HRV_analysis/blob/main/Readme.md#%EA%B4%80%EB%A0%A8-%EB%AA%A8%EB%93%88)
6. [참고문헌](https://github.com/sugyeong-yu/RPPG-HRV_analysis/blob/main/Readme.md#%EC%B0%B8%EA%B3%A0%EB%AC%B8%ED%97%8C)

## HRV 란
- HRV분석은 동방절 수준의 교감-미주신경 균형평가의 간단하고 비침습성 방법으로 주목받고있다.
- 교감신경계는 자율성을 향상하는 반면 부교감신경계는 그것을 억제시킨다. 
- 심장보조 조정기 세포에 대한 미주신경 자극효과는 과다분근을 일으키고 탈분극율을 감소시키며 교감신경 자극은 심장보조조정기 세포의 탈분극율을 증가시켜 심장박동수 변동효과를 일으킨다.
- 심장박동변화는 비침습성 심전도 표기로서 심장방실결절에 있는 ANS구성성분인 교감신경과 미주신경의 활동을 반영한다.
- 이는 순간 심박수와 RR간격변화의 총량을 표현한다. 
- 따라서 HRV는 자율신경기능의 기본 긴장성을 분석할 수 있다.
### 1. 시간영역 분석
- 시간 내의 심박 수 혹은 연속된 정상 심장 주기 사이의 간격변화를 측정한다.
- 연속된 심전도 기록에서 매개QRS파형이 검측됨으로 하여 방실결절 탈분극으로부터 온 정상 RR간격 혹은 순간 심박수가 결정된다.

|변수|단위|설명|
|------|---|---|
|SDNN|ms|모든 NN간격의 표준편차|
|SDANN|ms|전체기록의 5분간의 NN간격 평균 표준편차|
|SD|ms|인접한 NN간격 사이 차이의 표준편차|
|RMSSD|ms|인접한 NN간격 사이의 차이 제곱 합 평균의 제곱근|
|pnn50|%|50ms 이상의 인접한 NN간격 차이의 퍼센트치|

### 2. 주파수영역 분석
- 주파수역 분석은 심장의 방실결절 리듬에서 다양한 주파수와 진동으로 분해 한 심장박동신호의 주기적인 진동을 설명하여 그들의 상대강도량의 정보를 제공한다.
- FFT를 사용할때 RR간격은 다양한 스펙트럼 주파수 대역으로 전환된다.
- 파워 스펙트럼은 0~0.5Hz의 주파수 대역으로 이루어졌으며 4개의 대역으로 분해될 수 있다.
    - 초저 주파수 대역(ULF), 초장파대역(VLF), 저주파 대역(LF), 고주파 대역(HF)

|변수|단위|설명||
|------|---|---|---|
|Total Power|ms|모든 NN간격의 변화|<0.4Hz|
|ULF|ms|초저주파|<0.003Hz|
|VLF|ms|초장파|0.003-0.04Hz|
|LF|ms|저주파|0.04-0.15Hz|
|HF|ms|고주파|0.15-0.4Hz|
|LF/HF|-|저주파, 고주파 파워의 비율|-|

- [for mor detail about HRV analysis method]() 

## Code inform
- utils.py : 데이터 전처리 및 ppi 계산 등 필요한 함수를 구현해놓은 python file
- video.ipynb : 실시간 웹캠으로 얼굴 image를 촬영하는 동시에 접촉식ppg data를 실시간 시간과 함께 기록한다.
- rppg.ipynb : 캡처된 얼굴 image들을 불러와 ppg신호를 추출하여 시간과 함께 기록하는 rppg추출
- variable_sampling_rate.ipynb : sr이 가변적인 rppg의 신호를 불러와 시간정보에 맞추어 초당 sr을 추출하여 그룹화한다.
- hrv_analysis.ipynb : 추출한 PPG신호들을 불러와 전처리과정 수행, HRV계산 , rppg와 cppg의 결과를 비교하는 main파일이다.
- error_rate.ipynb : MAPE를 구하는 과정
## Protocol

<p align="center"><img src="https://user-images.githubusercontent.com/70633080/147058214-6c76e625-7f1e-4694-9d24-46424cd87af3.png" weight="30%" height="30%">

1. PPG 측정 (CPPG/RPPG) : 11분 측정
    - cppg와 rppg의 시간 기록 및 맞춰주기
2. Data shift
3. 신호 전처리(동잡음 제거)
    - Interpolation(2차 spline) : 30 sr의 RPPG data를 255 sr의 CPPG data와 동일한 갯수가 되도록 보간
    - bandfass filtering (0.5Hz~2.0Hz)
4. **Peak detection**
5. Peak to Peak interval (PPI) 및 Normal to Normal interval 계산
    - 이상값 제거 및 보간: zscore T 이상 > median값으로 대체
6. PRV feature extract
    - Time domain feature
    - Frequency domain feature(FFT)

[for more detail](https://github.com/sugyeong-yu/RPPG-HRV_analysis/blob/main/HRV_concepts.md)


## Result

### 전체 분석 결과 (Time/Frequency)
![image](https://user-images.githubusercontent.com/70633080/147063993-3931ba33-a4bf-4886-8168-e39e2a070cdc.png)

    

### Error_MAPE
- MAPE(평균 절대 오차 퍼센트): 유사도를 오차의 백분율로 나타내는 지표

[PPI 사용]
|Subject|MeanNN|SDNN|LFnu|HFnu|LF/HF Ratio|
|------|---|---|---|---|---|
|0|0.03|5.63|3.35|2.81|6.03|
|1|0.02|10.89|11.11|6.19|16.18|
|**2**|0.02|20.10|14.62|16.43|26.60|
|**3**|0.08|19.22|9.61|17.89|21.83|
|**4**|0.01|40.25|35.88|50.01|46.42|
|5|0.10|14.86|6.37|7.60|12.54|
|6|0.02|9.62|3.38|6.73|9.44|
|7|0.01|10.53|4.70|7.38|11.24|
|8|0.01|8.35|7.12|8.00|13.94|
|9|0.16|9.87|7.83|2.91|10.53|

- 대체적으로 높은 MAPE를 보임 (특히, 2,3,4)
- 이는 RPPG 신호 측정 시 혼합된 노이즈로 인한 것으로 유추
    
    
[NNI 사용]
|Subject|MeanNN|SDNN|LFnu|HFnu|LF/HF Ratio|
|------|---|---|---|---|---|
|0|0.05|1.58|2.20|2.32|4.36|
|1|0.08|1.70|7.89|4.65|13.00|
|2|0.11|2.50|3.41|2.56|5.94|
|3|0.11|9.92|5.70|8.89|12.44|
|4|0.19|4.79|7.96|6.53|12.89|
|5|0.13|2.89|5.56|6.99|11.43|
|6|0.13|2.58|2.20|3.40|5.71|
|7|0.10|6.98|3.86|5.83|9.02|
|8|0.09|3.24|7.74|5.57|12.65|
|9|0.16|9.87|7.83|2.91|10.53|

- 대부분의 MAPE가 크게 감소됨
- 잘못된 PPI를 제거하고 보간함으로써 데이터 품질 
    
### 상관 계수
#### 1. 두 PPG의 NNI 간의 상관계수
![image](https://user-images.githubusercontent.com/70633080/147082857-a8df7950-e139-4317-a622-ed0a01bb1f62.png)

#### 2. 두 PPG의 HRV features 간의 상관계수 
![image](https://user-images.githubusercontent.com/70633080/147083224-fcce692a-7ba6-4ec3-8fa4-ef0b4c925f5e.png)

- HRV 분석 feature들의 상관계수가 약 0.97~1.00
- RPPG를 이용한 HRV가 CPPG를 이용한 HRV 수준으로 수행 가능함을 확인

## 관련 모듈
### 1. pyserial
- serial port connection을 도와주는 모듈 
- python으로 usb직렬포트에 연결된 장치를 동작시킬 수 있도록 한다.
### 2. Heartpy
### 3. Scipy.signal.find_peaks
## 참고문헌
- http://www.vitalscan.kr/dt_hrv1_kr.htm
- https://blog.orikami.nl/exploring-heart-rate-variability-using-python-483a7037c64d
