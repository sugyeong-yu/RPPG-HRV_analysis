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
### 5. NN interval calculation
### 6. RRI or NNI interpolation
### 7. FFT
### 8. Power in target range
# 분석 시 주의해야할점

# HRV analysis with low sampling rate

# interploation
