HRV의 개념 및 분석 Standard에 대하여 설명한다.

# HRV 지표


# HRV 분석과정
### 1.Data Recording
### 2. (for low sampled signal -> signal interpolation)
### 3. R-peak detection
: 신호값의 기울기가 + 에서 -로 바뀌는 구간을 찾는것
- [Pan & Tomkins Algorithm](https://ieeexplore.ieee.org/abstract/document/4122029)
1. 미분 : data[n]-data[n-1]\
![image](https://user-images.githubusercontent.com/70633080/119080034-53af5f80-ba34-11eb-9613-86deb8ce9cf5.png)\
![image](https://user-images.githubusercontent.com/70633080/119080110-72adf180-ba34-11eb-8779-fc321858e643.png)
- 파란색 : 원본신호, 빨간색 : 미분값
2. 절대값씌우기\
![image](https://user-images.githubusercontent.com/70633080/119080148-7f324a00-ba34-11eb-83f7-ace94a773a39.png)
3. 이동평균구하기
  - window를 씌워서 window안의 평균값을 구하고 sliding\
  ![image](https://user-images.githubusercontent.com/70633080/119080288-c0c2f500-ba34-11eb-95f4-3cc9b72366e8.png)\
  ![image](https://user-images.githubusercontent.com/70633080/119080329-d6d0b580-ba34-11eb-9f92-840eff0d72c4.png)
4. R-peak 검출
  - 기준선 이상에서 기울기가 변하는 점 찾기
  - data[n-1]<data[n]>data[n+1] 이면  n이 peak라는것
  - data[n] > 0.06 , 0.06은 임의의 임계갑스로 기준값을 넘는것 중 꼭짓점 찾기\
  ![image](https://user-images.githubusercontent.com/70633080/119080490-26af7c80-ba35-11eb-81f4-be337f391bd1.png)\
  ![image](https://user-images.githubusercontent.com/70633080/119080371-e9e38580-ba34-11eb-8a9b-01a70973cffe.png)
  - 해당 점을 기준으로 심전도 앞뒤에서 꼭짓점 찾기\
  ![image](https://user-images.githubusercontent.com/70633080/119080553-3e870080-ba35-11eb-9918-13e86894e1db.png)
### 4. RRI calculation
- R-peak간의 시간간격을 의미함
- (peak_index[n] - peak_index[n+1]) * Fs  = RRI[n]
- index에 Fs를 곱하면 해당 시간이 된다.(sec) 
- 단위는 msec로 변환해야함
### 5. NN interval calculation
- RRI에서 이상점을 제거한 것을 NNI\
![image](https://user-images.githubusercontent.com/70633080/119081177-6c207980-ba36-11eb-86a6-683879672b2e.png)
### 6. RRI or NNI interpolation
- RRI 또는 NNI사이사이를 interpolation한다.
- interpolation을 해야하는 이유
1. 주파수 해상도
  - data수 : 12000개
  - R peak수 : 60개
  - 이는 1HZ 샘플링 느낌 (60 * 1 = 60)
  - 볼수있는대역은 1HZ/2 = 0.5Hz이다.
  - 따라서 데이터 수를 늘리면 주파수 대역의 x축사이가 촘촘해짐 > 볼수있는 주파수 대역이 늘어남 
  - 주파수해상도를 높일 수 있다는 것\
  ![image](https://user-images.githubusercontent.com/70633080/119081459-f7017400-ba36-11eb-9149-4c9ca257b657.png)\
  ![image](https://user-images.githubusercontent.com/70633080/119081495-07195380-ba37-11eb-8efa-11c5b206cbbc.png)
2.  Missing data 처리
  - 이상 RRI를 제거후 앞 뒤를 이어 붙이게 되면 새로운 주파수 성분이 추가된다. 
  - 이는 분석에 영향을 미칠 수 있음
  - 따라서 이 제거 구간의 data를 채워줘야함
### 7. FFT
### 8. Power in target range

# HRV analysis with low sampling rate

# interploation
