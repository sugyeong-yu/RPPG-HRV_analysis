# RPPG_HRV
- 비접촉식 ppg(rppg)로도 hrv분석이 가능함을 증명한다.

## hrv 분석
- HRV분석은 동방절 수준의 교감-미주신경 균형평가의 간단하고 비침습성 방법으로 주목받고있다.
- 교감신경계는 자율성을 향상하는 반면 부교감신경계는 그것을 억제시킨다. 
- 심장보조 조정기 세포에 대한 미주신경 자극효과는 과다분근을 일으키고 탈분극율을 감소시키며 교감신경 자극은 심장보조조정기 세포의 탈분극율을 증가시켜 심장박동수 변동효과를 일으킨다.
- 심장박동변화는 비침습성 심전도 표기로서 심장방실결절에 있는 ANS구성성분인 교감신경과 미주신경의 활동을 반영한다.
- 이는 순간 신박수와 RR간격변화의 총량을 표현한다. 
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

## Code inform
- utils.py : 데이터 전처리 및 ppi 계산 등 필요한 함수를 구현해놓은 python file
- video.ipynb : 실시간 웹캠으로 얼굴 image를 촬영하는 동시에 접촉식ppg data를 실시간 시간과 함께 기록한다.
- rppg.ipynb : 캡처된 얼굴 image들을 불러와 ppg신호를 추출하여 시간과 함께 기록하는 rppg추출
- variable_sampling_rate.ipynb : sr이 가변적인 rppg의 신호를 불러와 시간정보에 맞추어 초당 sr을 추출하여 그룹화한다.
- hrv_analysis.ipynb : 추출한 hrv신호들을 불러와 rppg와 cppg의 결과를 비교한다.

## Protocol


## Process
1. Matching Time
    - cppg와 rppg의 시간 기록 및 맞춰주기
2. Data shift
    - Data 수 늘리기
3. 신호 전처리(동잡음 제거)
    - bandfass filtering
    - normalization(0~1)
    - **interpolation**
4. **Peak detection**
5. rr interval 계산
    - 이상값 제거
    - **rri interpolation**
6. hrv feature extract
    - 주파수 변환(FFT)
    - 각 지표값 계산

## Result

<details>
<summary>0. 유수경_1(자세히)</summary>

 - Total : lf_hf_Ratio가 유사함. **(0.8577113522342822 , 0.8144823574325695)**
 - After Shift **(파랑 : c, 주황 : r)**
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/113984510-280e5680-9886-11eb-8475-d1092a82ab4a.png" weight="50%" height="50%">
</p>
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/113984544-30669180-9886-11eb-9516-b3b8190bd0e4.png" weight="50%" height="50%">
</p>
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/113984696-54c26e00-9886-11eb-9109-d532a2864223.png" weight="50%" height="50%">
</p>

<details>
<summary>Total(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113838042-61cd5780-97c9-11eb-8fba-d741ff7cc8e1.png)\
![image](https://user-images.githubusercontent.com/70633080/113838066-672aa200-97c9-11eb-8ee7-b383f5c757a4.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113838111-6eea4680-97c9-11eb-99ba-507933ce1013.png)\
![image](https://user-images.githubusercontent.com/70633080/113838130-73aefa80-97c9-11eb-8d8a-f44e89bc84b9.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113838164-7ad60880-97c9-11eb-9d8e-e60fe84360d3.png)\
![image](https://user-images.githubusercontent.com/70633080/113838183-80335300-97c9-11eb-9b4c-353fae498da0.png)

- lf/hf
  - cppg : 0.8577113522342822
  - rppg : 0.8144823574325695
- lf보다 hf의 차이가 3.599346289022882 배 크다.

</div>
</details>

<details>
<summary>0_0.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113959747-5d9f4980-985e-11eb-8db7-4c2d6976a478.png)\
![image](https://user-images.githubusercontent.com/70633080/113959760-62fc9400-985e-11eb-82fa-c5bc36d94391.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113959783-70198300-985e-11eb-8ef3-35156fb581a1.png)\
![image](https://user-images.githubusercontent.com/70633080/113959790-74de3700-985e-11eb-8299-fb459e00d91e.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113959819-7c054500-985e-11eb-9ce2-b5f45b6610d5.png)\
![image](https://user-images.githubusercontent.com/70633080/113959838-80316280-985e-11eb-8fe1-f0fd391fb06c.png)

- lf/hf
  - cppg : 0.6061275294173079
  - rppg : 0.6219338230041517
- lf보다 hf의 차이가 0.07605181760827674 배 크다.

</div>
</details>

<details>
<summary>0_1.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113959914-9e975e00-985e-11eb-8cf5-709d1e6533e8.png)\
![image](https://user-images.githubusercontent.com/70633080/113959932-a48d3f00-985e-11eb-8136-0e5e9e522a29.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113959961-aeaf3d80-985e-11eb-8f7b-0373247be89d.png)\
![image](https://user-images.githubusercontent.com/70633080/113959977-b373f180-985e-11eb-9cc6-f7dc05c01d45.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113959998-ba026900-985e-11eb-9414-10ca80628f0a.png)\
![image](https://user-images.githubusercontent.com/70633080/113960012-be2e8680-985e-11eb-8a53-d203fdd4024c.png)

- lf/hf
  - cppg : 0.6993321577953525
  - rppg : 0.7367330503806484
- lf보다 hf의 차이가 0.1530190133260979 배 크다.

</div>
</details>

<details>
<summary>0_2.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113960089-e0280900-985e-11eb-9d85-20491c514085.png)\
![image](https://user-images.githubusercontent.com/70633080/113960103-e5855380-985e-11eb-90d5-85637abbb326.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113960122-ee762500-985e-11eb-80d9-3371f754c671.png)\
![image](https://user-images.githubusercontent.com/70633080/113960135-f46c0600-985e-11eb-8d5e-b76ac97646d3.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113960156-fc2baa80-985e-11eb-9687-a9f3d28fff5c.png)\
![image](https://user-images.githubusercontent.com/70633080/113960169-00f05e80-985f-11eb-97e2-54ac315f7db1.png)

- lf/hf
  - cppg : 0.7607115114633478
  - rppg : 0.7659971061482973
- lf보다 hf의 차이가 1.151564463751257 배 크다.

</div>
</details>

<details>
<summary>0_3.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113960237-254c3b00-985f-11eb-8275-412aff316a85.png)\
![image](https://user-images.githubusercontent.com/70633080/113960249-2aa98580-985f-11eb-935f-4065be50e4f1.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113960272-339a5700-985f-11eb-8ccf-d45efabf4827.png)\
![image](https://user-images.githubusercontent.com/70633080/113960285-39903800-985f-11eb-96ae-38da6321c7d5.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113960300-40b74600-985f-11eb-8a63-acda52351ede.png)\
![image](https://user-images.githubusercontent.com/70633080/113960315-44e36380-985f-11eb-9db3-6691204613fa.png)

- lf/hf
  - cppg : 0.9516837971841224
  - rppg : 0.938398534243762
- lf보다 hf의 차이가 1.3371262957368917 배 크다.

</div>
</details>

<details>
<summary>0_4.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113980239-33ab4e80-9881-11eb-91a5-6b68d24b56a6.png)\
![image](https://user-images.githubusercontent.com/70633080/113980254-39089900-9881-11eb-80f1-50a8fb4054a1.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113980286-432a9780-9881-11eb-8f93-3feeb15e2232.png)\
![image](https://user-images.githubusercontent.com/70633080/113980323-4a51a580-9881-11eb-9015-8dd38b075404.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113980345-53427700-9881-11eb-97a9-27f5d1d46b21.png)\
![image](https://user-images.githubusercontent.com/70633080/113980366-589fc180-9881-11eb-847a-f327ddc87e11.png)

- lf/hf
  - cppg : 0.8407684772419656
  - rppg : 0.8125881203279546
- lf보다 hf의 차이가 2.08978197887601 배 크다.

</div>
</details>

<details>
<summary>0_5.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113980457-7b31da80-9881-11eb-9601-a52820add0f2.png)\
![image](https://user-images.githubusercontent.com/70633080/113980485-808f2500-9881-11eb-8422-af06efca3337.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113980525-8d137d80-9881-11eb-8187-8ca4eeb15087.png)\
![image](https://user-images.githubusercontent.com/70633080/113980541-93a1f500-9881-11eb-8429-f231297f78f7.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113980565-9bfa3000-9881-11eb-9fba-5680f4bbc78f.png)\
![image](https://user-images.githubusercontent.com/70633080/113980585-a1f01100-9881-11eb-965a-e1ae6e704830.png)

- lf/hf
  - cppg : 0.8645918507199178
  - rppg : 0.8473216138165628
- lf보다 hf의 차이가 1.6181499324993556 배 크다.

</div>
</details>

<details>
<summary>0_6.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113980693-c2b86680-9881-11eb-9f60-8ac501dfefd3.png)\
![image](https://user-images.githubusercontent.com/70633080/113980720-c946de00-9881-11eb-9a8e-de483d4bccc8.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113980761-d368dc80-9881-11eb-8c49-4f473a30536a.png)\
![image](https://user-images.githubusercontent.com/70633080/113980775-d8c62700-9881-11eb-9bf8-23e632971e02.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113980815-e24f8f00-9881-11eb-8255-b1f8fe0b6300.png)\
![image](https://user-images.githubusercontent.com/70633080/113980832-e8457000-9881-11eb-9c08-62d166ed0bf0.png)

- lf/hf
  - cppg : 1.070734407669084
  - rppg : 1.0086067709251159
- lf보다 hf의 차이가 2.0931820267532224 배 크다.

</div>
</details>

<details>
<summary>0_7.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113980969-12972d80-9882-11eb-94b8-e149388b0001.png)\
![image](https://user-images.githubusercontent.com/70633080/113980988-188d0e80-9882-11eb-9963-7f53136cd036.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113981028-2347a380-9882-11eb-8d4a-2c10b82446bc.png)\
![image](https://user-images.githubusercontent.com/70633080/113981050-28a4ee00-9882-11eb-9545-f64d0ec2b32a.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113981074-2fcbfc00-9882-11eb-906a-24a9ca296e7c.png)\
![image](https://user-images.githubusercontent.com/70633080/113981088-33f81980-9882-11eb-93e4-259cab7d3984.png)

- lf/hf
  - cppg : 1.1761962719351868
  - rppg : 1.0431207653462449
- lf보다 hf의 차이가 3.239050521945546 배 크다.

</div>
</details>

<details>
<summary>0_8.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113981192-58ec8c80-9882-11eb-94b3-9b9a7e0d13e4.png)\
![image](https://user-images.githubusercontent.com/70633080/113981226-5ee26d80-9882-11eb-892e-cb3b9bc3da1a.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113981294-76215b00-9882-11eb-8e6f-d848b0117708.png)\
![image](https://user-images.githubusercontent.com/70633080/113981315-7b7ea580-9882-11eb-964b-b43f2cdd2729.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113981359-89342b00-9882-11eb-8de6-d9763b256476.png)\
![image](https://user-images.githubusercontent.com/70633080/113981376-8e917580-9882-11eb-922d-499fe8f37f8e.png)

- lf/hf
  - cppg : 1.0793585895163822
  - rppg : 0.9339141898656892
- lf보다 hf의 차이가 7.045379630808728 배 크다.

</div>
</details>

<details>
<summary>0_9.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113981526-bbde2380-9882-11eb-8709-11238f142618.png)\
![image](https://user-images.githubusercontent.com/70633080/113981545-c13b6e00-9882-11eb-8387-1701097fb7bf.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113981589-cb5d6c80-9882-11eb-96e4-369b792a8e10.png)\
![image](https://user-images.githubusercontent.com/70633080/113981618-d0bab700-9882-11eb-8373-fb31f0d63fee.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113981639-d9ab8880-9882-11eb-8f65-a58dd3d3dccc.png)\
![image](https://user-images.githubusercontent.com/70633080/113981656-ddd7a600-9882-11eb-8041-d834bd0aff89.png)

- lf/hf
  - cppg : 1.2944013571443196
  - rppg : 1.1188114045042885
- lf보다 hf의 차이가 3.9013113756180453 배 크다.

</div>
</details>

<details>
<summary>0_10.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113981897-22fbd800-9883-11eb-9e2f-995e3c716161.png)\
![image](https://user-images.githubusercontent.com/70633080/113981924-2a22e600-9883-11eb-813a-e60910903e2e.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113981972-33ac4e00-9883-11eb-8d92-eb9b28616772.png)\
![image](https://user-images.githubusercontent.com/70633080/113981995-39099880-9883-11eb-8a5e-e1a6813b2ff1.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113982029-4161d380-9883-11eb-8685-38a91d0c73b4.png)\
![image](https://user-images.githubusercontent.com/70633080/113982050-46268780-9883-11eb-9944-0df6a351db8d.png)

- lf/hf
  - cppg : 1.175117768813192
  - rppg : 1.0050865702069962
- lf보다 hf의 차이가 12.203796344990089 배 크다.

</div>
</details>

</div>
</details>

<details>
<summary>1. 김나혜(자세히)</summary>
    
- After Shift **(파랑 : c, 주황 : r)**
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/113959234-71967b80-985d-11eb-8898-880cf7b823c4.png" weight="50%" height="50%">
</p>
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/113959254-79eeb680-985d-11eb-9881-4bdf0bab86cb.png" weight="50%" height="50%">
</p>
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/113959272-81ae5b00-985d-11eb-8be9-8febd7e568ff.png" weight="50%" height="50%">
</p>

<details>
<summary>Total(자세히)</summary> 

![image](https://user-images.githubusercontent.com/70633080/113558403-97900600-963a-11eb-857c-fc127a82965b.png)\
![image](https://user-images.githubusercontent.com/70633080/113558373-8b0bad80-963a-11eb-8a9b-71303f8d56dd.png)

- lf/hf
    - cppg : 0.9445302760107445
    - rppg : 0.761142338986123
- lf 보다 hf의 차이가 4.183740904432091 배 크다.

</div>
</details>

<details>
<summary>1_0.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113566848-72a28f80-9648-11eb-89c5-c0c8da2f1402.png)\
![image](https://user-images.githubusercontent.com/70633080/113566870-7b936100-9648-11eb-890f-7bc4f6f4d212.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113566890-83530580-9648-11eb-88b2-b419a956362b.png)\
![image](https://user-images.githubusercontent.com/70633080/113566898-89e17d00-9648-11eb-8c68-e20c7e65513e.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113566914-906ff480-9648-11eb-9f81-58bc5f553b5b.png)\
![image](https://user-images.githubusercontent.com/70633080/113566930-9665d580-9648-11eb-807f-d17ae6a2ad49.png)

- lf/hf
  - cppg : 1.1056689482333162
  - rppg : 1.059755776873923
- lf보다 hf의 차이가 1.697243166328554 배 크다.

</div>
</details>

<details>
<summary>1_1.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113567119-f492b880-9648-11eb-9b73-3fdd7abdb03e.png)\
![image](https://user-images.githubusercontent.com/70633080/113567128-fceaf380-9648-11eb-9c4d-f35862aac7b3.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113567153-07a58880-9649-11eb-9d72-271d45942351.png)\
![image](https://user-images.githubusercontent.com/70633080/113567169-0ecc9680-9649-11eb-9fd8-3a51d4772331.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113567193-1855fe80-9649-11eb-8724-3ae3517b0f42.png)\
![image](https://user-images.githubusercontent.com/70633080/113567201-1db34900-9649-11eb-9f18-d38aa8f3aa52.png)

- lf/hf
  - cppg : 1.02703356595913
  - rppg : 0.8838075662435998
- lf보다 hf의 차이가 22.90322985685127 배 크다.

</div>
</details>

<details>
<summary>1_2.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113567259-44717f80-9649-11eb-9a29-89c877d457d3.png)\
![image](https://user-images.githubusercontent.com/70633080/113567274-4afff700-9649-11eb-9a2a-c52818e6310e.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113567299-57844f80-9649-11eb-840c-c94b6fbc7901.png)\
![image](https://user-images.githubusercontent.com/70633080/113567544-c6fa3f00-9649-11eb-968f-21734ae3e8a1.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113567573-d37e9780-9649-11eb-9a32-dfe51b913441.png)\
![image](https://user-images.githubusercontent.com/70633080/113567589-d9747880-9649-11eb-91fd-7b3223e755f6.png)

- lf/hf
  - cppg : 0.9896243726015197
  - rppg : 0.7874195686840051
- lf보다 hf의 차이가 260.2205612659931 배 크다.

</div>
</details>

<details>
<summary>1_3.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113567683-06289000-964a-11eb-9f31-4e2fd2e4d390.png)\
![image](https://user-images.githubusercontent.com/70633080/113567698-0cb70780-964a-11eb-9a7f-9dbae157d5a1.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113567719-19d3f680-964a-11eb-81c4-269751b076c1.png)\
![image](https://user-images.githubusercontent.com/70633080/113567734-20626e00-964a-11eb-9b6f-50963fa0067a.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113567766-2c4e3000-964a-11eb-8034-480862f8cc68.png)\
![image](https://user-images.githubusercontent.com/70633080/113567778-32441100-964a-11eb-9d58-653a1bd11019.png)

- lf/hf
  - cppg : 1.1062126884052037
  - rppg : 0.9463178498773316
- lf보다 hf의 차이가 4.9893419147841165 배 크다.

</div>
</details>

<details>
<summary>1_4.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113567855-5dc6fb80-964a-11eb-87e2-355f54c78a95.png)\
![image](https://user-images.githubusercontent.com/70633080/113567867-63bcdc80-964a-11eb-97b5-eac4a8ffdcd1.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113567889-6f100800-964a-11eb-9efa-e046ef54a7c3.png)\
![image](https://user-images.githubusercontent.com/70633080/113567903-759e7f80-964a-11eb-8ec4-a0becce0c164.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113567929-7df6ba80-964a-11eb-942e-e777440b55a7.png)\
![image](https://user-images.githubusercontent.com/70633080/113567942-83ec9b80-964a-11eb-8f5e-6f7bbb046b56.png)

- lf/hf
  - cppg : 0.8017291176253322
  - rppg : 0.6724339570489628
- lf보다 hf의 차이가 5.60337203139542 배 크다.

</div>
</details>

<details>
<summary>1_5.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113568021-b0a0b300-964a-11eb-9357-4517163030e0.png)\
![image](https://user-images.githubusercontent.com/70633080/113568041-ba2a1b00-964a-11eb-9372-1c0791e0cdf4.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113568064-c4e4b000-964a-11eb-9e53-13f006a2dedc.png)\
![image](https://user-images.githubusercontent.com/70633080/113568084-cb732780-964a-11eb-9c78-b84eef7528a3.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113568142-ecd41380-964a-11eb-91d0-eee67c5ae4f6.png)\
![image](https://user-images.githubusercontent.com/70633080/113568153-f2c9f480-964a-11eb-82f4-8bd829957c43.png)

- lf/hf
  - cppg : 0.8442601876122368
  - rppg : 0.6744778416952577
- lf보다 hf의 차이가 14.19942336376959 배 크다.

</div>
</details>

<details>
<summary>1_6.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113568220-18ef9480-964b-11eb-868c-f1041f9ead66.png)\
![image](https://user-images.githubusercontent.com/70633080/113568229-2016a280-964b-11eb-869b-4ae1032d8607.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113568260-2efd5500-964b-11eb-98ac-1beb93b686c7.png)\
![image](https://user-images.githubusercontent.com/70633080/113568286-3886bd00-964b-11eb-9b8f-ad0706d33b69.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113568303-42a8bb80-964b-11eb-96e6-f7185e5c7f38.png)\
![image](https://user-images.githubusercontent.com/70633080/113568312-489e9c80-964b-11eb-9862-ab8b22305670.png)

- lf/hf
  - cppg : 0.9846157512991539
  - rppg : 0.7992707664301267
- lf보다 hf의 차이가 148.11178070332952 배 크다.

</div>
</details>

<details>
<summary>1_7.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113568393-6ff56980-964b-11eb-9987-a56bd180254a.png)\
![image](https://user-images.githubusercontent.com/70633080/113568425-7f74b280-964b-11eb-9bf3-d4a495ffd100.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113568673-f0b46580-964b-11eb-89a0-37b1553fbc41.png)\
![image](https://user-images.githubusercontent.com/70633080/113568689-f742dd00-964b-11eb-842d-d037d0c3bb78.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113568750-1fcad700-964c-11eb-8c20-8dab3f9f3f3b.png)\
![image](https://user-images.githubusercontent.com/70633080/113568762-248f8b00-964c-11eb-98c0-d7cedddf11cc.png)

- lf/hf
  - cppg : 0.8226608703474294
  - rppg : 0.6302925838339463
- lf보다 hf의 차이가 6.1590413695118675 배 크다.

</div>
</details>

<details>
<summary>1_8.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113568821-47ba3a80-964c-11eb-8f72-e5eb1d26a726.png)\
![image](https://user-images.githubusercontent.com/70633080/113568834-4d178500-964c-11eb-94a7-1b58a29de660.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113568866-5acd0a80-964c-11eb-9988-a0c51f7de8c8.png)\
![image](https://user-images.githubusercontent.com/70633080/113568885-64567280-964c-11eb-9954-ab7c4f3dae3d.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113568912-6e787100-964c-11eb-8fd7-be12eea3edfb.png)\
![image](https://user-images.githubusercontent.com/70633080/113568919-73d5bb80-964c-11eb-8fe7-855b6de89ff6.png)

- lf/hf
  - cppg : 0.6472484037311803
  - rppg : 0.4480216476569237
- lf보다 hf의 차이가 8.948438569053211 배 크다.

</div>
</details>

<details>
<summary>1_9.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113569173-fc545c00-964c-11eb-809a-830a3e68ccdf.png)\
![image](https://user-images.githubusercontent.com/70633080/113569185-024a3d00-964d-11eb-8a37-b8bf92fe192b.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113569199-0d9d6880-964d-11eb-8558-4f60ada58547.png)\
![image](https://user-images.githubusercontent.com/70633080/113569228-1726d080-964d-11eb-84e3-3fd24f08c9ec.png)
- graph\
![image](htps://user-images.githubusercontent.com/70633080/113569256-20b03880-964d-11eb-8e82-fe2413ccf69b.png)\
![image](https://user-images.githubusercontent.com/70633080/113569266-273eb000-964d-11eb-9797-759c7cfd9b9c.png)

- lf/hf
  - cppg : 0.8061749948150531
  - rppg : 0.5660957228411531
- lf보다 hf의 차이가 10.21241540717127 배 크다.

</div>
</details>

<details>
<summary>1_10.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113569337-4b01f600-964d-11eb-988c-c5ec78971ad4.png)\
![image](https://user-images.githubusercontent.com/70633080/113569356-5523f480-964d-11eb-938b-21d647833c8f.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113569392-68cf5b00-964d-11eb-9bfc-b41bd5305ec5.png)\
![image](https://user-images.githubusercontent.com/70633080/113569407-6e2ca580-964d-11eb-87de-e2ffb7335521.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113569426-771d7700-964d-11eb-9079-59a2bad4c5b4.png)\
![image](https://user-images.githubusercontent.com/70633080/113569441-7be22b00-964d-11eb-8e0f-b668d273cc3d.png)

- lf/hf
  - cppg : 0.9228060563403587
  - rppg : 0.647825197902874
- lf보다 hf의 차이가 11.903374348202586 배 크다.

</div>
</details>

</div>
</details>

<details>
<summary>2. 이미경(자세히)</summary>

 - Total : lf_hf_Ratio에 차이가 있음. **(1.1749836066737231 , 0.7444784253594657)**
 - After Shift **(파랑 : c, 주황 : r)**
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/114128001-58153280-9936-11eb-860f-2c8f354863db.png" weight="50%" height="50%">
</p>
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/114128014-606d6d80-9936-11eb-9ca9-891722a140d4.png" weight="50%" height="50%">
</p>
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/114128028-682d1200-9936-11eb-9c4e-15bbd3ce4ab3.png" weight="50%" height="50%">
</p>

<details>
<summary>Total(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114125354-40877b00-9931-11eb-8fa8-44453043f6ec.png)\
![image](https://user-images.githubusercontent.com/70633080/114125362-45e4c580-9931-11eb-8a29-86cb1c442911.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114125371-4d0bd380-9931-11eb-9cd0-2beb18e596ca.png)\
![image](https://user-images.githubusercontent.com/70633080/114125385-51d08780-9931-11eb-9edd-88d8bb34a1a4.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114125392-57c66880-9931-11eb-8295-feeee3666212.png)\
![image](https://user-images.githubusercontent.com/70633080/114125402-5d23b300-9931-11eb-90a5-361a25314c5e.png)

- lf/hf
  - cppg : 1.1749836066737231
  - rppg : 0.7444784253594657
- lf보다 hf의 차이가 6.9984848018172805 배 크다.

</div>
</details>

<details>
<summary>2_0.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114125613-ce636600-9931-11eb-94e0-5dbc513c1077.png)\
![image](https://user-images.githubusercontent.com/70633080/114125628-d4594700-9931-11eb-877b-d85605950801.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114125655-dc18eb80-9931-11eb-8d8a-f77cdacb977c.png)\
![image](https://user-images.githubusercontent.com/70633080/114125668-e1763600-9931-11eb-82c9-977684e01bfd.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114125685-ea670780-9931-11eb-9ba3-259ea75de001.png)\
![image](https://user-images.githubusercontent.com/70633080/114125696-efc45200-9931-11eb-8c61-dd3bb02fa324.png)

- lf/hf
  - cppg : 1.3746083765659165
  - rppg : 0.8979248176917615
- lf보다 hf의 차이가 6.0166605923535545 배 크다.

</div>
</details>

<details>
<summary>2_1.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114125779-171b1f00-9932-11eb-9b3e-9d4e38967a8b.png)\
![image](https://user-images.githubusercontent.com/70633080/114125789-1c786980-9932-11eb-905d-f899061c8883.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114125808-2601d180-9932-11eb-8c9b-1d956d4eb111.png)\
![image](https://user-images.githubusercontent.com/70633080/114125816-2ac68580-9932-11eb-810f-02e4b16e71df.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114125849-3914a180-9932-11eb-946d-81d2ed60d155.png)\
![image](https://user-images.githubusercontent.com/70633080/114125865-3d40bf00-9932-11eb-86c0-c063be7a2ea7.png)

- lf/hf
  - cppg : 1.2185911939088678
  - rppg : 0.8212798402922231
- lf보다 hf의 차이가 5.4713030953395405 배 크다.

</div>
</details>

<details>
<summary>2_2.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114125933-5f3a4180-9932-11eb-8fe8-bb353ec65823.png)\
![image](https://user-images.githubusercontent.com/70633080/114125942-65302280-9932-11eb-9de8-771d511b9114.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114125953-6f522100-9932-11eb-908b-74351be36b27.png)\
![image](https://user-images.githubusercontent.com/70633080/114125961-75e09880-9932-11eb-8253-77a9871043a9.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114125974-7e38d380-9932-11eb-88a6-20a3823d45da.png)\
![image](https://user-images.githubusercontent.com/70633080/114125992-8264f100-9932-11eb-9fe2-6f7541d4afb7.png)

- lf/hf
  - cppg : 1.3191954158752923
  - rppg : 0.875393787371213
- lf보다 hf의 차이가 5.214060850927755 배 크다.

</div>
</details>

<details>
<summary>2_3.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114126059-9e689280-9932-11eb-859c-d5fe882d4358.png)\
![image](https://user-images.githubusercontent.com/70633080/114126068-a32d4680-9932-11eb-8bc6-6128d495fea0.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114126080-ad4f4500-9932-11eb-9eb0-6c04e9295ddc.png)\
![image](https://user-images.githubusercontent.com/70633080/114126092-b50ee980-9932-11eb-82f6-97a3d1f2a2ba.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114126105-bcce8e00-9932-11eb-9e45-b626f0322235.png)\
![image](https://user-images.githubusercontent.com/70633080/114126116-c0faab80-9932-11eb-9e49-cb6ee6175533.png)

- lf/hf
  - cppg : 1.5042186133857107
  - rppg : 1.0028732748649856
- lf보다 hf의 차이가 5.335358243918124 배 크다.

</div>
</details>

<details>
<summary>2_4.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114126167-e2f42e00-9932-11eb-8630-4e4c45a95843.png)\
![image](https://user-images.githubusercontent.com/70633080/114126178-e7b8e200-9932-11eb-95e2-efb2eb573e4a.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114126197-f1424a00-9932-11eb-8417-2ffc530a841b.png)\
![image](https://user-images.githubusercontent.com/70633080/114126206-f69f9480-9932-11eb-8d97-7009268e9881.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114126229-fd2e0c00-9932-11eb-8015-871b5d9c5394.png)\
![image](https://user-images.githubusercontent.com/70633080/114126237-015a2980-9933-11eb-920b-f886729bcc08.png)
- lf/hf
  - cppg : 1.3705675443639804 
  - rppg : 0.852342410556146
- lf보다 hf의 차이가 8.43754191100555 배 크다.

</div>
</details>

<details>
<summary>2_5.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114126303-2189e880-9933-11eb-8c79-9b36dbfc8748.png)\
![image](https://user-images.githubusercontent.com/70633080/114126313-25b60600-9933-11eb-8590-664a17a2f5c6.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114126339-31093180-9933-11eb-9c6d-43e54d2cb863.png)\
![image](https://user-images.githubusercontent.com/70633080/114126345-35cde580-9933-11eb-9930-2bb5fcb1de36.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114126360-3cf4f380-9933-11eb-840b-3d3128cefa5e.png)\
![image](https://user-images.githubusercontent.com/70633080/114126367-41211100-9933-11eb-9a3e-cee1c4f1a7a5.png)
- lf/hf
  - cppg : 1.4880087100063135
  - rppg : 0.9893906298390217
- lf보다 hf의 차이가 4.818087640749465 배 크다.

</div>
</details>

<details>
<summary>2_6.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114126423-5d24b280-9933-11eb-8586-aa8ccfa0920d.png)\
![image](https://user-images.githubusercontent.com/70633080/114126437-61e96680-9933-11eb-9c39-3b5163ade75f.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114126461-6dd52880-9933-11eb-8874-9954614db7b3.png)\
![image](https://user-images.githubusercontent.com/70633080/114126471-73327300-9933-11eb-8fc7-796937fcef14.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114126489-7ded0800-9933-11eb-8dfa-eecbcbfb6e3b.png)\
![image](https://user-images.githubusercontent.com/70633080/114126498-82b1bc00-9933-11eb-8da5-3c81f5a008aa.png)

- lf/hf
  - cppg : 1.0642955665273506
  - rppg : 0.7839279537221782
- lf보다 hf의 차이가 3.2953071124922912 배 크다.

</div>
</details>

<details>
<summary>2_7.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114126566-9f4df400-9933-11eb-8b29-c9a5ff85a6d4.png)\
![image](https://user-images.githubusercontent.com/70633080/114126573-a4ab3e80-9933-11eb-8559-6255ee26ce57.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114126588-af65d380-9933-11eb-85ec-df023fdaea8c.png)\
![image](https://user-images.githubusercontent.com/70633080/114126596-b4c31e00-9933-11eb-9f68-8bbedc415f67.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114126705-ef2cbb00-9933-11eb-8f7a-67209c14aa93.png)\
![image](https://user-images.githubusercontent.com/70633080/114126723-f3f16f00-9933-11eb-9506-710db4a739fe.png)

- lf/hf
  - cppg : 0.8535040476183139
  - rppg : 0.5591282786451874
- lf보다 hf의 차이가 5.684560266044967 배 크다.

</div>
</details>

<details>
<summary>2_8.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114127363-40897a00-9935-11eb-9639-2fa89f10e5a1.png)\
![image](https://user-images.githubusercontent.com/70633080/114127383-4717f180-9935-11eb-8243-e6288f2194ea.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114127413-54cd7700-9935-11eb-9167-c874c0770e0b.png)\
![image](https://user-images.githubusercontent.com/70633080/114127421-5a2ac180-9935-11eb-894d-947e74b63eac.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114127451-6151cf80-9935-11eb-90ca-a15108d7b257.png)\
![image](https://user-images.githubusercontent.com/70633080/114127471-66af1a00-9935-11eb-8812-59cae0378f3e.png)

- lf/hf
  - cppg : 1.0208917809854507
  - rppg : 0.6559935593821812
- lf보다 hf의 차이가 5.832656395087866 배 크다.

</div>
</details>

<details>
<summary>2_9.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114127588-834b5200-9935-11eb-9f46-be2a955bf584.png)\
![image](https://user-images.githubusercontent.com/70633080/114127607-89413300-9935-11eb-9473-61bb23edb810.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114127641-93633180-9935-11eb-9c15-f1189aa24f90.png)\
![image](https://user-images.githubusercontent.com/70633080/114127653-99f1a900-9935-11eb-94da-cf37455c5b59.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114127666-a249e400-9935-11eb-81c3-25231b5c1caa.png)\
![image](https://user-images.githubusercontent.com/70633080/114127679-a7a72e80-9935-11eb-9c6b-ca11ae9e48ee.png)
- lf/hf
  - cppg : 0.8940970897193802
  - rppg : 0.570475506549078
- lf보다 hf의 차이가 6.577401202667224 배 크다.

</div>
</details>

<details>
<summary>2_10.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114127728-c3aad000-9935-11eb-87e5-4330f6ce5943.png)\
![image](https://user-images.githubusercontent.com/70633080/114127741-c7d6ed80-9935-11eb-820e-1d414900a066.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114127756-d32a1900-9935-11eb-881a-cb407c65b1e8.png)\
![image](https://user-images.githubusercontent.com/70633080/114127801-eb019d00-9935-11eb-9c78-fc6a16e22717.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114127809-f228ab00-9935-11eb-85cf-775d4f95a8d7.png)\
![image](https://user-images.githubusercontent.com/70633080/114127820-f654c880-9935-11eb-9974-22bc274c0767.png)

- lf/hf
  - cppg : 0.7867883835281293
  - rppg : 0.48460042026717975
- lf보다 hf의 차이가 9.097898517377166 배 크다.

</div>
</details>

</div>
</details>

<details>
<summary>3. 복진영(자세히)</summary>

- lf/hf에 차이가 있음.
- lf에도 약간의 차이가 있음
- 그러나 lf에 비해 hf가 더 차이가 있었음.

- After Shift **(파랑 : c, 주황 : r)**
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/113958677-760e6480-985c-11eb-9b26-5bfe1542ea2c.png" weight="50%" height="50%">
</p>
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/113958703-7e669f80-985c-11eb-9259-dedbba1f7628.png" weight="50%" height="50%">
</p>
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/113958723-86264400-985c-11eb-87ed-02c33836f972.png" weight="50%" height="50%">
</p>

<details>
<summary>3_0.csv(자세히)</summary>
  
- ppg\
![cppg](https://user-images.githubusercontent.com/70633080/113540950-28a3b480-961c-11eb-9e33-3073da3d06f5.png) \
![rppg](https://user-images.githubusercontent.com/70633080/113540961-30fbef80-961c-11eb-9602-34c3c9cfb411.png)
- ppi\
![ppi](https://user-images.githubusercontent.com/70633080/113541055-5f79ca80-961c-11eb-8ed4-dd06bb429657.png)\
![image](https://user-images.githubusercontent.com/70633080/113541013-50931800-961c-11eb-983a-0ea0408083a9.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113541288-dd3dd600-961c-11eb-8f63-f022e74ec4d2.png)\
![graph](https://user-images.githubusercontent.com/70633080/113541077-75878b00-961c-11eb-9b2c-bd98a01d07de.png)

- lf/hf
  - cppg : 0.8540033614154223
  - rppg : 0.7041700836991194
- lf보다 hf의 차이가 3.516480812275286 배 크다.

</div>
</details>

<details>
<summary>3_1.csv(자세히)</summary>
  
- ppg\
![cppg](https://user-images.githubusercontent.com/70633080/113541455-3279e780-961d-11eb-8efd-44bbf0efdaa7.png)\
![rppg](https://user-images.githubusercontent.com/70633080/113541488-4aea0200-961d-11eb-86ad-383e84c79e45.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113541544-66eda380-961d-11eb-89bb-7979c01afd4b.png)\
![image](https://user-images.githubusercontent.com/70633080/113541518-5b9a7800-961d-11eb-8ae6-ac819cb42366.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113541581-7ec52780-961d-11eb-953a-09b5c8de9560.png)\
![image](https://user-images.githubusercontent.com/70633080/113541564-75d45600-961d-11eb-9a77-cc9aea98781e.png)

- lf/hf
  - cppg : 1.033527829403157
  - rppg : 0.8293054837343359
- lf보다 hf의 차이가 3.2185882110633375 배 크다.

</div>
</details>

<details>
<summary>3_2.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113541703-bdf37880-961d-11eb-8cb1-060b2e44ac60.png)\
![image](https://user-images.githubusercontent.com/70633080/113541722-c8157700-961d-11eb-94d7-fb38d2514ba3.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113541781-debbce00-961d-11eb-90dc-886e64c58f22.png)\
![image](https://user-images.githubusercontent.com/70633080/113541746-d06db200-961d-11eb-9f1d-76b720afe70d.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113541823-f1360780-961d-11eb-8029-baec268d636e.png)\
![image](https://user-images.githubusercontent.com/70633080/113541809-ebd8bd00-961d-11eb-9943-6d684a0eea05.png)

- lf/hf
  - cppg : 1.0602372135957556
  - rppg : 0.7888237852614745
- lf보다 hf의 차이가 19.02585904312811  크다.

</div>
</details>

<details>
<summary>3_3.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113541961-378b6680-961e-11eb-9801-6128537efe2b.png)\
![image](https://user-images.githubusercontent.com/70633080/113541978-440fbf00-961e-11eb-862b-3c8d35605d76.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113542008-4eca5400-961e-11eb-9cb7-1daef3ee1e8b.png)\
![image](https://user-images.githubusercontent.com/70633080/113542014-5558cb80-961e-11eb-9f56-d2974b856459.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113542033-5e499d00-961e-11eb-81b4-a309810517ec.png)\
![image](https://user-images.githubusercontent.com/70633080/113542046-643f7e00-961e-11eb-9f38-1fff07d54e23.png)

- lf/hf
  - cppg : 1.1286745376196776
  - rppg : 0.9269687172246385
- lf보다 hf의 차이가 3.0763283077454577 배 크다.

</div>
</details>

<details>
<summary>3_4.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113542175-b1235480-961e-11eb-93b3-4d542967dcb8.png)\
![image](https://user-images.githubusercontent.com/70633080/113542226-c8624200-961e-11eb-8e7b-a10276bb4f20.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113542254-da43e500-961e-11eb-8d7e-d334aebd0355.png)\
![image](https://user-images.githubusercontent.com/70633080/113542243-d0ba7d00-961e-11eb-8252-a2ea3fc45a3c.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113542272-e29c2000-961e-11eb-996f-8736b67db540.png)\
![image](https://user-images.githubusercontent.com/70633080/113542283-e6c83d80-961e-11eb-9816-a290c02044e7.png)

- lf/hf
  - cppg : 1.6106443178946281
  - rppg : 1.356876722338862
- lf보다 hf의 차이가 1.7583936969561647 배 크다.

</div>
</details>

<details>
<summary>3_5.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113542348-08292980-961f-11eb-800d-962969091bda.png)\
![image](https://user-images.githubusercontent.com/70633080/113542360-0f503780-961f-11eb-88ef-e25131e11c7c.png
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113542384-1e36ea00-961f-11eb-8bf0-841a71985718.png)\
![image](https://user-images.githubusercontent.com/70633080/113542403-255df800-961f-11eb-9b78-41ef55d8f736.png)
- graph\
![image](https://ser-images.githubusercontent.com/70633080/113542413-2e4ec980-961f-11eb-89c5-5c2fedfe68ab.png)\
![image](https://user-images.githubusercontent.com/70633080/113542427-3575d780-961f-11eb-9b23-375ff65a0c7c.png)

- lf/hf
  - cppg : 1.6898782620763513
  - rppg : 1.3462283480453312
- lf보다 hf의 차이가 3.153394636687946 배 크다.

</div>
</details>

<details>
<summary>3_6.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113542479-576f5a00-961f-11eb-8b4f-ae3502269621.png)\
![image](https://user-images.githubusercontent.com/70633080/113542493-60602b80-961f-11eb-974f-a35c7ce37675.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113542513-6a822a00-961f-11eb-9429-2d778d4e79da.png)\
![image](https://user-images.githubusercontent.com/70633080/113542524-7110a180-961f-11eb-9ec7-fc2759538260.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113542541-7a017300-961f-11eb-8b76-b5c98ccab2d8.png)\
![image](https://user-images.githubusercontent.com/70633080/113542559-82f24480-961f-11eb-95ce-391fb17d5bec.png)

- lf/hf
  - cppg : 2.048295348131425
  - rppg : 1.5719779895900903
- lf보다 hf의 차이가 1.7871168185623163 배 크다.

</div>
</details>

<details>
<summary>3_7.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113542642-aae1a800-961f-11eb-8bd7-777e3fb98b76.png)\
![image](https://user-images.githubusercontent.com/70633080/113542653-b2a14c80-961f-11eb-8db3-8db27ad59fad.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113542696-c9e03a00-961f-11eb-8de0-e58f950a0285.png)\
![image](https://user-images.githubusercontent.com/70633080/113542678-c056d200-961f-11eb-8c4b-1494f70dc7b8.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113542718-d2387500-961f-11eb-8e0b-b0d0562d1050.png)\
![image](https://user-images.githubusercontent.com/70633080/113542731-d6fd2900-961f-11eb-94a3-d286948e56ba.png)

- lf/hf
  - cppg : 1.9873748259643222
  - rppg : 1.4715230980802194
- lf보다 hf의 차이가 2.058929491591993 배 크다.

</div>
</details>

<details>
<summary>3_8.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113542833-11ff5c80-9620-11eb-89ca-a908884b08f6.png)\
![image](https://user-images.githubusercontent.com/70633080/113542846-19266a80-9620-11eb-822c-4ff7b7c14d3e.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113542871-27748680-9620-11eb-87c7-0e1cc933f459.png)\
![image](https://user-images.githubusercontent.com/70633080/113542884-2f342b00-9620-11eb-942d-8805bf314705.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113542907-3b1fed00-9620-11eb-9f10-6b61350fecde.png)\
![image](https://user-images.githubusercontent.com/70633080/113542914-3fe4a100-9620-11eb-982c-968ca145b7c3.png)

- lf/hf
  - cppg : 2.030258352307812
  - rppg : 1.4217888141341395
- lf보다 hf의 차이가 2.084605340586623 배 크다.

</div>
</details>

<details>
<summary>3_9.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113542971-63a7e700-9620-11eb-851c-5067e99f06d0.png)\
![image](https://user-images.githubusercontent.com/70633080/113542985-699dc800-9620-11eb-9992-195bd41f3494.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113543017-791d1100-9620-11eb-880c-f5791517b170.png)\
![image](https://user-images.githubusercontent.com/70633080/113543025-7fab8880-9620-11eb-9062-474884a9ed68.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113543045-889c5a00-9620-11eb-9395-b082494c63ad.png)\
![image](https://user-images.githubusercontent.com/70633080/113543058-8e923b00-9620-11eb-9f2a-66aedbb72805.png)

- lf/hf
  - cppg : 2.1230953052420674
  - rppg : 1.3377572736144339
- lf보다 hf의 차이가 1.8561989997298647 배 크다.

</div>
</details>

<details>
<summary>3_10.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113543166-c39e8d80-9620-11eb-8110-a676d53d70c2.png)\
![image](https://user-images.githubusercontent.com/70633080/113543177-cbf6c880-9620-11eb-8869-7a52ced7f88f.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113543199-d6b15d80-9620-11eb-9f7d-afeb0725db08.png)\
![image](https://user-images.githubusercontent.com/70633080/113543281-fea0c100-9620-11eb-9092-105f2e03bcb3.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113543293-08c2bf80-9621-11eb-9a94-0b02764967a7.png)\
![image](https://user-images.githubusercontent.com/70633080/113543309-0eb8a080-9621-11eb-8fb2-a338fb767257.png)

- lf/hf
  - cppg : 2.6910120529048536
  - rppg : 1.1421227111394363
- lf보다 hf의 차이가 2.7005614089126144 배 크다.

</div>
</details>

</div>
</details>

<details>
<summary>4. 이승건(자세히)</summary>

 - Total : lf_hf_Ratio가 차이가 있음. **(1.4807216224170776 , 0.6178131036269046)**
    - lf는 거의 유사하지만 hf에서 큰 차이를 보임
    - cppg data개수 모자람 168199개
    - rppg data개수 모자람 19793개
- After Shift **(파랑 : c, 주황 : r)**
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/113956940-532e8100-9859-11eb-967e-ddf0ce62fcc9.png" weight="50%" height="50%">
</p>
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/113956905-40b44780-9859-11eb-9e37-a3069b73dbaf.png" weight="50%" height="50%">
</p>
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/113956923-490c8280-9859-11eb-91d6-164452793d20.png" weight="50%" height="50%">
</p>

<details>
<summary>Total(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113837506-e2d81f00-97c8-11eb-8ba1-6f05b2b4cb9d.png)\
![image](https://user-images.githubusercontent.com/70633080/113837528-e9ff2d00-97c8-11eb-84ba-e273920b653b.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113837581-f4b9c200-97c8-11eb-8bbc-b879b8c68c68.png)\
![image](https://user-images.githubusercontent.com/70633080/113837606-fa170c80-97c8-11eb-8a7b-34a8f8be0d04.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113837635-013e1a80-97c9-11eb-8ee0-2201de5c8d4c.png)\
![image](https://user-images.githubusercontent.com/70633080/113837662-07cc9200-97c9-11eb-8842-78b78cf5cbe7.png)

- lf/hf
  - cppg : 1.4807216224170776
  - rppg : 0.6178131036269046
- lf보다 hf의 차이가 9.043222563802672 배 크다.

</div>
</details>

<details>
<summary>4_0.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113954854-9e469500-9855-11eb-8c0d-f1bf2d6f0346.png)\
![image](https://user-images.githubusercontent.com/70633080/113954869-a7376680-9855-11eb-9c7a-bea78d0b7c37.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113954890-b1596500-9855-11eb-986f-105139eff479.png)\
![image](https://user-images.githubusercontent.com/70633080/113954901-b74f4600-9855-11eb-90fb-0b032ffa3205.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113954922-bdddbd80-9855-11eb-9c2c-bffaedadaf72.png)
![image](https://user-images.githubusercontent.com/70633080/113954930-c2a27180-9855-11eb-8785-85b4deac948f.png)
- lf/hf
  - cppg : 2.005099109541857
  - rppg : 0.8401541896151794
- lf보다 hf의 차이가 8.756404761842356 배 크다.

</div>
</details>

<details>
<summary>4_1.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113954999-e2d23080-9855-11eb-9394-71d2e4e54792.png)\
![image](https://user-images.githubusercontent.com/70633080/113955010-e82f7b00-9855-11eb-88df-f7627662e2a4.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113955027-f2517980-9855-11eb-9107-f4c029ec9b14.png)\
![image](https://user-images.githubusercontent.com/70633080/113955039-f7162d80-9855-11eb-81a0-62cab1f64a82.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113955060-fe3d3b80-9855-11eb-94b5-b6999d3b167b.png)\
![image](https://user-images.githubusercontent.com/70633080/113955070-02695900-9856-11eb-81a2-4d72ce8c35ca.png)

- lf/hf
  - cppg : 1.8783380359477833
  - rppg : 0.7328914544861282
- lf보다 hf의 차이가 8.4834307327353 배 크다.

</div>
</details>

<details>
<summary>4_2.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113955138-24fb7200-9856-11eb-92e7-d06e2c459b2f.png)\
![image](https://user-images.githubusercontent.com/70633080/113955155-2a58bc80-9856-11eb-9128-3fc94274db9d.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113955185-33e22480-9856-11eb-8b4c-fc66be749e80.png)\
![image](https://user-images.githubusercontent.com/70633080/113955194-393f6f00-9856-11eb-9655-5d65a2227eb1.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113955209-40ff1380-9856-11eb-91a6-d3f807b351ab.png)\
![image](https://user-images.githubusercontent.com/70633080/113955216-45c3c780-9856-11eb-871b-79ba263ff97e.png)

- lf/hf
  - cppg : 2.024228399770128
  - rppg : 0.6482339902699656
- lf보다 hf의 차이가 10.65184630499792 배 크다.

</div>
</details>

<details>
<summary>4_3.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113955285-625fff80-9856-11eb-927c-fa0d595ba6aa.png)\
![image](https://user-images.githubusercontent.com/70633080/113955297-6855e080-9856-11eb-9dc2-ba49251edf93.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113955317-7572cf80-9856-11eb-95ee-86a351079c47.png)\
![image](https://user-images.githubusercontent.com/70633080/113955330-7b68b080-9856-11eb-9dd6-174be8eb39b5.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113955347-83c0eb80-9856-11eb-8ee3-2d50ab080507.png)\
![image](https://user-images.githubusercontent.com/70633080/113955372-8de2ea00-9856-11eb-8e5f-0a2465fc3238.png)

- lf/hf
  - cppg : 1.4142514447494299
  - rppg : 0.5390426981813736
- lf보다 hf의 차이가 8.251689442433776 배 크다.

</div>
</details>


<details>
<summary>4_4.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113955506-d00c2b80-9856-11eb-83d5-8acb9cd755ae.png)\
![image](https://user-images.githubusercontent.com/70633080/113955526-d5697600-9856-11eb-8c49-f032271d6161.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113955552-e9ad7300-9856-11eb-9ead-b7b82556b0f9.png)\
![image](https://user-images.githubusercontent.com/70633080/113955558-ef0abd80-9856-11eb-9927-656066227dab.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113955571-f6ca6200-9856-11eb-8cdd-28719ea7e719.png)\
![image](https://user-images.githubusercontent.com/70633080/113955579-faf67f80-9856-11eb-9f47-63c8278b3c67.png)

- lf/hf
  - cppg : 1.3640838367077854
  - rppg : 0.4782604967846557
- lf보다 hf의 차이가 8.43203572897734 배 크다.

</div>
</details>

<details>
<summary>4_5.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113955646-1c576b80-9857-11eb-84f9-7449dfe284cc.png)\
![image](https://user-images.githubusercontent.com/70633080/113955659-237e7980-9857-11eb-999d-94b2ef699c40.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113955687-309b6880-9857-11eb-84a9-1705b4cfc0e2.png)\
![image](https://user-images.githubusercontent.com/70633080/113955699-36914980-9857-11eb-8008-fcadb611d0f2.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113955717-3d1fc100-9857-11eb-89d2-d33d2d37dac2.png)\
![image](https://user-images.githubusercontent.com/70633080/113955728-427d0b80-9857-11eb-8166-7507802e32cf.png)

- lf/hf
  - cppg : 1.3783500157515736
  - rppg : 0.5559871506086673
- lf보다 hf의 차이가 8.324726788277568 배 크다.

</div>
</details>

<details>
<summary>4_6.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113955790-5fb1da00-9857-11eb-8b70-0c12c81fa056.png)\
![image](https://user-images.githubusercontent.com/70633080/113955805-650f2480-9857-11eb-823a-a45a33801bc3.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113955838-6f312300-9857-11eb-871a-50e7354f2af7.png)\
![image](https://user-images.githubusercontent.com/70633080/113955850-73f5d700-9857-11eb-813d-2d0766849c6c.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113955862-7bb57b80-9857-11eb-9000-d37733e836a0.png)\
![image](https://user-images.githubusercontent.com/70633080/113955869-807a2f80-9857-11eb-966f-d93dafc7a893.png)

- lf/hf
  - cppg : 1.1630184681116564
  - rppg : 0.5169296856584894
- lf보다 hf의 차이가 8.678153328357265 배 크다.

</div>
</details>

<details>
<summary>4_7.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113955973-b7504580-9857-11eb-88b8-bebc475ba93f.png)\
![image](https://user-images.githubusercontent.com/70633080/113955988-bcad9000-9857-11eb-9432-62ced40fcded.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113956012-c8995200-9857-11eb-9108-433398cff501.png)\
![image](https://user-images.githubusercontent.com/70633080/113956026-cdf69c80-9857-11eb-9070-50db81055114.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113956041-d5b64100-9857-11eb-8c7a-30d4d83b7998.png)\
![image](https://user-images.githubusercontent.com/70633080/113956053-da7af500-9857-11eb-9ef8-09723cf86f05.png)

- lf/hf
  - cppg : 1.1326673821740185
  - rppg : 0.5388986328578227
- lf보다 hf의 차이가 6.643878824492209 배 크다.

</div>
</details>

<details>
<summary>4_8.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113956142-fbdbe100-9857-11eb-8f1d-07f467761150.png)\
![image](https://user-images.githubusercontent.com/70633080/113956164-01d1c200-9858-11eb-8ca2-de54ca7b515a.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113956195-0b5b2a00-9858-11eb-9751-059726ddec9c.png)\
![image](https://user-images.githubusercontent.com/70633080/113956206-101fde00-9858-11eb-80e1-ab99c8ab89dd.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113956216-16ae5580-9858-11eb-8485-052db167ddcc.png)\
![image](https://user-images.githubusercontent.com/70633080/113956224-1b730980-9858-11eb-8a94-8040483c91b7.png)

- lf/hf
  - cppg : 0.8976963016149747
  - rppg : 0.4759708106425969
- lf보다 hf의 차이가 7.540021313517321 배 크다.

</div>
</details>

<details>
<summary>4_9.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113956324-40677c80-9858-11eb-97ae-242c26eb7ceb.png)\
![image](https://user-images.githubusercontent.com/70633080/113956339-45c4c700-9858-11eb-86ed-40271a4e1abd.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113956362-507f5c00-9858-11eb-9414-8d98ab3daca4.png)\
![image](https://user-images.githubusercontent.com/70633080/113956388-56753d00-9858-11eb-866b-b2a9828653d2.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113956410-5d9c4b00-9858-11eb-980d-a23d3f8cda1d.png)\
![image](https://user-images.githubusercontent.com/70633080/113956421-61c86880-9858-11eb-8151-88be5880ec19.png)

- lf/hf
  - cppg : 0.8766337178804039
  - rppg : 0.45590866145023895
- lf보다 hf의 차이가 8.760066261567298 배 크다.

</div>
</details>

<details>
<summary>4_10.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113956493-802e6400-9858-11eb-8784-fb839d765f86.png)\
![image](https://user-images.githubusercontent.com/70633080/113956507-88869f00-9858-11eb-8569-4aa10342b9fa.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113956541-92100700-9858-11eb-87a6-da3062b86711.png)\
![image](https://user-images.githubusercontent.com/70633080/113956561-976d5180-9858-11eb-9157-8b47160dec23.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113956580-9f2cf600-9858-11eb-84c6-56bcb8aee194.png)\
![image](https://user-images.githubusercontent.com/70633080/113956590-a3591380-9858-11eb-9e43-4711fbb3536b.png)

- lf/hf
  - cppg : 1.1051213377142866
  - rppg : 0.5106929569819503
- lf보다 hf의 차이가 12.924184354159136 배 크다.

</div>
</details>

</div>
</details>

<details>
<summary>6. 목지원(자세히)</summary>

 - After Shift **(파랑 : c, 주황 : r)**
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/120981674-debd8300-c7b2-11eb-8b05-130a99fb8e3c.png" weight="50%" height="50%">
</p>
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/120981754-f268e980-c7b2-11eb-9356-4f31bac7618b.png" weight="50%" height="50%">
</p>
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/120981805-feed4200-c7b2-11eb-805e-1cc3d24795b2.png" weight="50%" height="50%">
</p>


</div>
</details>

<details>
<summary>7. 유수경_2(자세히)</summary>


- Total : lf_hf_Ratio가 비슷하게 나왔음. **(2.4673490304430854 , 2.100023846724976)**
    - cppg data개수 모자람 168112개 
- After Shift **(파랑 : c, 주황 : r)**
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/114132479-661b8100-993f-11eb-9438-b51be55d06c1.png" weight="50%" height="50%">
</p>
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/114132495-6ddb2580-993f-11eb-9690-d43ec43d01a1.png" weight="50%" height="50%">
</p>
<p align="left">
    <img src="https://user-images.githubusercontent.com/70633080/114132515-759aca00-993f-11eb-8911-1fb4c0d0d0f4.png" weight="50%" height="50%">
</p>
 
<details>
<summary>Total(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113836997-5e859c00-97c8-11eb-8f28-002205e9f133.png)\
![image](https://user-images.githubusercontent.com/70633080/113837016-63e2e680-97c8-11eb-9201-c70c69ed677c.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113837054-6d6c4e80-97c8-11eb-83b0-336af1443196.png)\
![image](https://user-images.githubusercontent.com/70633080/113837076-72c99900-97c8-11eb-9b1b-36a40442da72.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113837114-7c530100-97c8-11eb-9582-2b8b7ba7e32e.png)\
![image](https://user-images.githubusercontent.com/70633080/113837139-8248e200-97c8-11eb-86d6-67fe77272bd4.png)

- lf/hf
  - cppg : 2.4673490304430854
  - rppg : 2.100023846724976
- lf보다 hf의 차이가 1.7005547198891278 배 크다.

</div>
</details>

<details>
<summary>7_0.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114129293-42553c80-9939-11eb-9749-ab3b23f29249.png)\
![image](https://user-images.githubusercontent.com/70633080/114129299-47b28700-9939-11eb-96b9-c87eb17a6200.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114129323-51d48580-9939-11eb-9242-93851ffa3e60.png)\
![image](https://user-images.githubusercontent.com/70633080/114129339-5731d000-9939-11eb-8723-a2b4f7988396.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114129355-6153ce80-9939-11eb-9192-13b22548aca0.png)\
![image](https://user-images.githubusercontent.com/70633080/114129364-657fec00-9939-11eb-9df2-669a2fc543be.png)

- lf/hf
  - cppg : 1.9084896964368139
  - rppg : 1.7162974365862924
- lf보다 hf의 차이가 1.8362665482477687 배 크다.

</div>
</details>

<details>
<summary>7_1.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114129471-98c27b00-9939-11eb-93d7-d126dfac7771.png)\
![image](https://user-images.githubusercontent.com/70633080/114129489-9d872f00-9939-11eb-8dac-80785e09b8e1.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114129521-aa0b8780-9939-11eb-8be3-bf4071e35037.png)\
![image](https://user-images.githubusercontent.com/70633080/114129533-aed03b80-9939-11eb-9a74-0d17f133b5a0.png)
- graph\
![image](https://user-imaes.githubusercontent.com/70633080/114129549-bb549400-9939-11eb-99b5-ed54d1b9872a.png)\
![image](https://user-images.githubusercontent.com/70633080/114129558-c0194800-9939-11eb-818a-836f05fade00.png)

- lf/hf
  - cppg : 1.5338333764226735
  - rppg : 1.3670932520305032
- lf보다 hf의 차이가 2.507082248313013 배 크다.

</div>
</details>

<details>
<summary>7_2.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114129621-e2ab6100-9939-11eb-9e5e-c968fc74b06b.png)\
![image](https://user-images.githubusercontent.com/70633080/114129627-e7701500-9939-11eb-99c7-90059ba0afc7.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114129639-efc85000-9939-11eb-93e0-17789b92d83c.png)\
![image](https://user-images.githubusercontent.com/70633080/114129646-f48d0400-9939-11eb-8166-32c3438c5822.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114129660-fbb41200-9939-11eb-96a6-1b0f792006d0.png)\
![image](https://user-images.githubusercontent.com/70633080/114129670-ffe02f80-9939-11eb-84d3-52c08dc7bc49.png)

- lf/hf
  - cppg : 1.773978603209888
  - rppg : 1.4984560398780322
- lf보다 hf의 차이가 3.2498582662619726 배 크다.

</div>
</details>

<details>
<summary>7_3.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114129712-1ab2a400-993a-11eb-95cf-8bd01678938e.png)\
![image](https://user-images.githubusercontent.com/70633080/114129725-200fee80-993a-11eb-9828-0581346db599.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114129740-29995680-993a-11eb-8b03-2945f0410680.png)\
![image](https://user-images.githubusercontent.com/70633080/114129754-2e5e0a80-993a-11eb-8d3d-b4ca9ac7db2f.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114129851-59485e80-993a-11eb-8584-c45ee0c2733b.png)\
![image](https://user-images.githubusercontent.com/70633080/114129857-5d747c00-993a-11eb-8133-31b1d3ce74b1.png)

- lf/hf
  - cppg : 1.7201904848931027
  - rppg : 1.582877936895584
- lf보다 hf의 차이가 1.574122033634668 배 크다.

</div>
</details>

<details>
<summary>7_4.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114130270-2357aa00-993b-11eb-814b-c71cf647b98b.png)\
![image](https://user-images.githubusercontent.com/70633080/114130279-28b4f480-993b-11eb-8fa4-aee4baca89f3.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114130309-3bc7c480-993b-11eb-9652-7a3ea7970849.png)\
![image](https://user-images.githubusercontent.com/70633080/114130292-32d6f300-993b-11eb-8aad-57ef3590c78d.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114130326-44b89600-993b-11eb-8553-428a94f1c14f.png)\
![image](https://user-images.githubusercontent.com/70633080/114130335-497d4a00-993b-11eb-84ef-82aa847c2c00.png)

- lf/hf
  - cppg : 1.7621079043113799
  - rppg : 1.544778546504284
- lf보다 hf의 차이가 2.2518905963217235 배 크다.

</div>
</details>

<details>
<summary>7_5.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114131299-5f8c0a00-993d-11eb-857e-e08b5143ab88.png)\
![image](https://user-images.githubusercontent.com/70633080/114131311-6581eb00-993d-11eb-81ae-58815de1bcf1.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114131350-73d00700-993d-11eb-9704-f064c9b489b2.png)\
![image](https://user-images.githubusercontent.com/70633080/114131362-77fc2480-993d-11eb-8c75-966b42f2d72a.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114131379-7e8a9c00-993d-11eb-9e82-4a517386bd41.png)\
![image](https://user-images.githubusercontent.com/70633080/114131399-85191380-993d-11eb-9e1c-fa51cc397ce3.png)

- lf/hf
  - cppg : 2.0047332234150446
  - rppg : 1.7566067268125525
- lf보다 hf의 차이가 2.0950425856866666 배 크다.

</div>
</details>

<details>
<summary>7_6.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114131468-a417a580-993d-11eb-9753-21d2353e271e.png)\
![image](https://user-images.githubusercontent.com/70633080/114131476-a8dc5980-993d-11eb-8e77-723263ddf26a.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114131508-b560b200-993d-11eb-9cef-ec1de869cd61.png)\
![image](https://user-images.githubusercontent.com/70633080/114131516-b98ccf80-993d-11eb-95e8-4c592f95638e.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114131548-c3aece00-993d-11eb-8551-10894e5e634c.png)\
![image](https://user-images.githubusercontent.com/70633080/114131562-c7daeb80-993d-11eb-8efb-3959cfa90044.png)

- lf/hf
  - cppg : 1.7915059941861924
  - rppg : 1.6669513030281722
- lf보다 hf의 차이가 1.386905385479064 배 크다.

</div>
</details>

<details>
<summary>7_7.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114131697-0a042d00-993e-11eb-9511-02d1132d8af4.png)\
![image](https://user-images.githubusercontent.com/70633080/114131706-0ec8e100-993e-11eb-8e2e-58ba9c00ee1f.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114131732-18eadf80-993e-11eb-87da-9d77e685f5d1.png)\
![image](https://user-images.githubusercontent.com/70633080/114131744-1ee0c080-993e-11eb-9a4f-562599f44c42.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114131759-2738fb80-993e-11eb-855e-8ca9ff68f0a4.png)\
![image](https://user-images.githubusercontent.com/70633080/114131769-2d2edc80-993e-11eb-8933-8ab0bebf0fa9.png)

- lf/hf
  - cppg : 2.15944190875116
  - rppg : 1.8872729620220297
- lf보다 hf의 차이가 1.393544390049671 배 크다.

</div>
</details>

<details>
<summary>7_8.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114131869-518ab900-993e-11eb-8dea-c0b7fc82d169.png)\
![image](https://user-images.githubusercontent.com/70633080/114131886-56e80380-993e-11eb-9beb-f4943d0e9809.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114131911-60716b80-993e-11eb-8f13-b3005df439db.png)\
![image](https://user-images.githubusercontent.com/70633080/114131924-65ceb600-993e-11eb-97af-a56a0c2e56cc.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114131941-6cf5c400-993e-11eb-8504-b43552ea4e5c.png)\
![image](https://user-images.githubusercontent.com/70633080/114131959-73843b80-993e-11eb-87af-c5d67c000c6d.png)

- lf/hf
  - cppg : 1.9315324720572378 
  - rppg : 1.694531005308966
- lf보다 hf의 차이가 1.93131345167256 배 크다.

</div>
</details>

<details>
<summary>7_9.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114132021-931b6400-993e-11eb-9851-f323c5e3a4ba.png)\
![image](https://user-images.githubusercontent.com/70633080/114132041-9878ae80-993e-11eb-9a8e-a30f5bc17206.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114132083-ac241500-993e-11eb-9de6-aa993be1e408.png)\
![image](https://user-images.githubusercontent.com/70633080/114132094-b1815f80-993e-11eb-8a7e-b01977ac55ad.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114132107-b80fd700-993e-11eb-97de-f98d3bd15a91.png)\
![image](https://user-images.githubusercontent.com/70633080/114132117-bcd48b00-993e-11eb-96ae-6e8d24f47081.png)

- lf/hf
  - cppg : 2.2880375311389938
  - rppg : 1.940798437221022
- lf보다 hf의 차이가 1.6416379265288568 배 크다.

</div>
</details>

<details>
<summary>7_10.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114132186-d83f9600-993e-11eb-90f6-b7157d30f25e.png)\
![image](https://user-images.githubusercontent.com/70633080/114132194-dd9ce080-993e-11eb-9d87-f4e4d364bf80.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114132219-e7bedf00-993e-11eb-9515-781d73d51202.png)\
![image](https://user-images.githubusercontent.com/70633080/114132225-ec839300-993e-11eb-8bba-3bbad38ac2e9.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114132241-f3120a80-993e-11eb-9de9-f1691ce1b341.png)\
![image](https://user-images.githubusercontent.com/70633080/114132252-f7d6be80-993e-11eb-9d44-e1379b8f2206.png)

- lf/hf
  - cppg : 3.129517695444601
  - rppg : 2.6689906896379134
- lf보다 hf의 차이가 1.0880060434915477 배 크다.

</div>
</details>

</div>
</details>

<details>
<summary>8. 유수경_3(자세히)</summary>

- Total : lf_hf_Ratio가 비슷하게 나왔음. **(1.722921074032543 , 1.4622911848470102)**
    - cppg data개수 모자람 168240개
- After Shift **(파랑 : c, 주황 : r)**
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/113863419-9bf82280-97e4-11eb-9d2d-62d434f20d97.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/113863498-b6ca9700-97e4-11eb-9c75-46906bfb955e.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/113863472-aaded500-97e4-11eb-98d0-6fde028900fa.png" weight="50%" height="50%">
    </p>
    
<details>
<summary>Total(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113836532-eb7c2580-97c7-11eb-8c43-a20fdc66d5a6.png)\
![image](https://user-images.githubusercontent.com/70633080/113836557-f20a9d00-97c7-11eb-800f-325712e5526a.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113836592-fb940500-97c7-11eb-9961-5e964e926cc9.png)\
![image](https://user-images.githubusercontent.com/70633080/113836612-00f14f80-97c8-11eb-8757-2992c403c112.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113836649-0a7ab780-97c8-11eb-9de2-f7825088d962.png)\
![image](https://user-images.githubusercontent.com/70633080/113836674-0f3f6b80-97c8-11eb-8e16-78ab9941ddca.png)

- lf/hf
  - cppg : 1.722921074032543
  - rppg : 1.4622911848470102
- lf보다 hf의 차이가 2.0438712349328543 배 크다.

</div>
</details>

<details>
<summary>8_0.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113856933-d78eee80-97dc-11eb-809e-43776af8a850.png)\
![image](https://user-images.githubusercontent.com/70633080/113856945-dcec3900-97dc-11eb-8dc4-dfb567b4b37c.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113856974-e7a6ce00-97dc-11eb-9192-ef7dc8d549a6.png)\
![image](https://user-images.githubusercontent.com/70633080/113856994-ed041880-97dc-11eb-9b0f-d226beff5167.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113857029-fb523480-97dc-11eb-935d-e11e03dd265f.png)\
![image](https://user-images.githubusercontent.com/70633080/113857052-0016e880-97dd-11eb-9197-e15d3210a312.png)

- lf/hf
  - cppg : 1.8588044938687627
  - rppg : 1.5645267109183345
- lf보다 hf의 차이가 1.4667556787248228 배 크다.

</div>
</details>

<details>
<summary>8_1.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113857173-263c8880-97dd-11eb-9b03-740427c30cee.png)\
![image](https://user-images.githubusercontent.com/70633080/113857198-2ccb0000-97dd-11eb-8521-82db4a101a66.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113857220-37859500-97dd-11eb-8dd2-78ac7d5c6f2f.png)\
![image](https://user-images.githubusercontent.com/70633080/113857232-3c4a4900-97dd-11eb-96eb-f7811eb47f70.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113857265-4409ed80-97dd-11eb-8edf-1e85e634b8eb.png)\
![image](https://user-images.githubusercontent.com/70633080/113857282-49673800-97dd-11eb-9b8e-11c065a5391c.png)

- lf/hf
  - cppg : 1.9179956876434612
  - rppg : 1.5882575432059682
- lf보다 hf의 차이가 1.9194647302013232 배 크다.

</div>
</details>

<details>
<summary>8_2.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113857361-6a2f8d80-97dd-11eb-9dd4-06a019d32257.png)\
![image](https://user-images.githubusercontent.com/70633080/113857384-6f8cd800-97dd-11eb-8a07-cacc83564e43.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113857424-79164000-97dd-11eb-93b8-96628b1568c0.png)\
![image](https://user-images.githubusercontent.com/70633080/113857442-7ddaf400-97dd-11eb-8bc0-bd60195a9157.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113857471-86332f00-97dd-11eb-80e3-da258e78b91b.png)\
![image](https://user-images.githubusercontent.com/70633080/113857484-8af7e300-97dd-11eb-89a0-1825d0a8de6d.png)

- lf/hf
  - cppg : 1.8274533426800845
  - rppg : 1.492761294835086
- lf보다 hf의 차이가 2.43775821776941 배 크다.

</div>
</details>

<details>
<summary>8_3.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113857603-ae229280-97dd-11eb-8a8b-c9ee20b7d2a4.png)\
![image](https://user-images.githubusercontent.com/70633080/113857628-b4b10a00-97dd-11eb-8d97-4d6e8ed30ff5.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113857661-bf6b9f00-97dd-11eb-990e-48d6d80ed2b9.png)\
![image](https://user-images.githubusercontent.com/70633080/113857677-c4c8e980-97dd-11eb-8dfe-12f4aa6236c3.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113857706-cbeff780-97dd-11eb-9cea-2f73da0dd792.png)\
![image](https://user-images.githubusercontent.com/70633080/113857718-d0b4ab80-97dd-11eb-995b-947cd760ed1c.png)

- lf/hf
  - cppg : 1.6283162979657182
  - rppg : 1.3796758236045208
- lf보다 hf의 차이가 2.357807685109653 배 크다.

</div>
</details>

<details>
<summary>8_4.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113857891-08bbee80-97de-11eb-830c-de369468215d.png)\
![image](https://user-images.githubusercontent.com/70633080/113857906-0e193900-97de-11eb-93bf-8ae7b0001ce0.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113857962-21c49f80-97de-11eb-8412-58e8d800e10e.png)\
![image](https://user-images.githubusercontent.com/70633080/113857920-15404700-97de-11eb-9893-77fb0cd461bc.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113858007-2be69e00-97de-11eb-911b-4f879de6d685.png)\
![image](https://user-images.githubusercontent.com/70633080/113858020-3012bb80-97de-11eb-9746-7b610fa0a1ac.png)

- lf/hf
  - cppg : 1.724029692184223
  - rppg : 1.4929719474898897
- lf보다 hf의 차이가 2.0379628959762344 배 크다.

</div>
</details>

<details>
<summary>8_5.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113858113-5173a780-97de-11eb-9702-957c0e77c035.png)\
![image](https://user-images.githubusercontent.com/70633080/113858134-58021f00-97de-11eb-8a27-ebf9feae4a75.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113858167-64867780-97de-11eb-8564-66c6167c2cff.png)\
![image](https://user-images.githubusercontent.com/70633080/113858186-694b2b80-97de-11eb-9a89-2b08f1b6c1ad.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113858235-710ad000-97de-11eb-9709-232d9f80898b.png)\
![image](https://user-images.githubusercontent.com/70633080/113858242-7536ed80-97de-11eb-8cf7-ed43b8d6ad02.png)

- lf/hf
  - cppg : 1.4656988386254508
  - rppg : 1.271016495695475
- lf보다 hf의 차이가 2.4275365519398844 배 크다.

</div>
</details>

<details>
<summary>8_6.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113858345-939ce900-97de-11eb-95bc-9ce58e783305.png)\
![image](https://user-images.githubusercontent.com/70633080/113858362-98fa3380-97de-11eb-99fe-66edea207e8e.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113858390-a31c3200-97de-11eb-9de0-d6179636d1d2.png)\
![image](https://user-images.githubusercontent.com/70633080/113858395-a7e0e600-97de-11eb-8f4f-bccd93347bf0.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113858424-afa08a80-97de-11eb-8c4a-a6bf1bf08eaf.png)\
![image](https://user-images.githubusercontent.com/70633080/113858445-b3cca800-97de-11eb-80bf-510eb972ea45.png)

- lf/hf
  - cppg : 1.4428584059040976
  - rppg : 1.1784277346528982
- lf보다 hf의 차이가 3.0698328622835156 배 크다.

</div>
</details>

<details>
<summary>8_7.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113858553-d363d080-97de-11eb-8ecc-32426d76985c.png)\
![image](https://user-images.githubusercontent.com/70633080/113858579-d8c11b00-97de-11eb-9b3f-db0254b7ac50.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113858611-e37bb000-97de-11eb-99cf-7f7a0e51055b.png)\
![image](https://user-images.githubusercontent.com/70633080/113858631-eaa2be00-97de-11eb-8b98-8ca95912e4b5.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113858659-f2626280-97de-11eb-80d1-b1dabbd7b843.png)\
![image](https://user-images.githubusercontent.com/70633080/113858674-f7271680-97de-11eb-8290-68fa9ac067ff.png)

- lf/hf
  - cppg : 1.5523752307637573
  - rppg : 1.312306396306448
- lf보다 hf의 차이가 2.9191441130499745 배 크다.

</div>
</details>

<details>
<summary>8_8.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113858764-13c34e80-97df-11eb-9baf-3219ca391c1d.png)\
![image](https://user-images.githubusercontent.com/70633080/113858785-19209900-97df-11eb-8704-93432f93fedf.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113858820-23db2e00-97df-11eb-89a4-e7cc840aa98a.png)\
![image](https://user-images.githubusercontent.com/70633080/113858854-2dfd2c80-97df-11eb-94c5-4f5293d3e4c9.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113858870-348ba400-97df-11eb-8d4e-0282d010cb4e.png)\
![image](https://user-images.githubusercontent.com/70633080/113858889-381f2b00-97df-11eb-9feb-ea66689a2374.png)

- lf/hf
  - cppg : 1.2930666907937858
  - rppg : 1.1302203309723164
- lf보다 hf의 차이가 2.39409982382708 배 크다.

</div>
</details>

<details>
<summary>8_9.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113858986-57b65380-97df-11eb-848f-ca9f755e0d4b.png)\
![image](https://user-images.githubusercontent.com/70633080/113859007-5dac3480-97df-11eb-95a8-8a198c562de7.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113859037-6a308d00-97df-11eb-8c7d-b1cf7e492fae.png)\
![image](https://user-images.githubusercontent.com/70633080/113859053-6ef54100-97df-11eb-9c56-24d6205897eb.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113859076-761c4f00-97df-11eb-8f6e-48e89913a131.png)\
![image](https://user-images.githubusercontent.com/70633080/113859089-79afd600-97df-11eb-9b22-915e85bfafdf.png)

- lf/hf
  - cppg : 1.3161139314749954
  - rppg : 1.117033011373932
- lf보다 hf의 차이가 5.27972853003578 배 크다.

</div>
</details>

<details>
<summary>8_10.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113859202-9b10c200-97df-11eb-9334-8b5fc44c65da.png)\
![image](https://user-images.githubusercontent.com/70633080/113859225-a106a300-97df-11eb-84d2-1c7c441ed56a.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113859306-b4b20980-97df-11eb-88fd-b754a1d3dedb.png)\
![image](https://user-images.githubusercontent.com/70633080/113859259-a95ede00-97df-11eb-8c63-eb0cf56d71ca.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113859327-bbd91780-97df-11eb-80b2-99a8a438dfb5.png)\
![image](https://user-images.githubusercontent.com/70633080/113859334-c0053500-97df-11eb-8d4a-d53a8b391759.png)

- lf/hf
  - cppg : 1.3477263145973282
  - rppg : 1.1545553372452964
- lf보다 hf의 차이가 2.8781831939589844 배 크다.

</div>
</details>

</div>
</details>

<details>
<summary>9. 이채원(자세히)</summary>

- Total : lf_hf_Ratio가 비슷하게 나왔음. **(0.8919346897922263 , 0.8264034869050073)**
    - rppg개수 40개 모자름(19760) (따라서 원래 index-40번부터 시작 : 860:sr * 630 -40)
        - group 15 -> 22
        - group 16 -> 1
        - group 17 -> 27
- After Shift **(파랑 : c, 주황 : r)**
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/113864426-d9a97b00-97e5-11eb-86e6-fb9e8186156a.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/113864319-baaae900-97e5-11eb-99e1-64d0141d6898.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/113864383-cd252280-97e5-11eb-923e-5be12e9549c6.png" weight="50%" height="50%">
    </p>

    

<details>
<summary>Total(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113835948-63961b80-97c7-11eb-8381-030fe0b6dd24.png)\
![image](https://user-images.githubusercontent.com/70633080/113835966-6abd2980-97c7-11eb-98e0-66807812dfee.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113836009-77da1880-97c7-11eb-96a5-d0fa7249d434.png)\
![image](https://user-images.githubusercontent.com/70633080/113836034-7e689000-97c7-11eb-97f0-d5f6b184568f.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113836080-89232500-97c7-11eb-91f4-7871cbb226b0.png)\
![image](https://user-images.githubusercontent.com/70633080/113836100-8de7d900-97c7-11eb-878c-e09f69289243.png)

- lf/hf
  - cppg : 0.8919346897922263
  - rppg : 0.8264034869050073
- lf보다 hf의 차이가 1.2712263266773152 배 크다.

</div>
</details>

<details>
<summary>9_0.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113848551-9219f380-97d3-11eb-8d04-bcaa14dd5a32.png)\
![image](https://user-images.githubusercontent.com/70633080/113848588-9d6d1f00-97d3-11eb-81bd-fdb759e849e0.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113848631-a65df080-97d3-11eb-8f7c-f3c0072f0894.png)\
![image](https://user-images.githubusercontent.com/70633080/113848667-abbb3b00-97d3-11eb-85f0-4bc87b66feda.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113848740-be357480-97d3-11eb-960b-26b403baeed9.png)\
![image](https://user-images.githubusercontent.com/70633080/113848761-c2619200-97d3-11eb-87bc-a32ca5894932.png)

- lf/hf
  - cppg : 0.5901466053456318
  - rppg : 0.6516871765911033
- lf보다 hf의 차이가 0.2019426138369514 배 크다.

</div>
</details>

<details>
<summary>9_1.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113849461-7bc06780-97d4-11eb-9ed5-a25c62070bbd.png)\
![image](https://user-images.githubusercontent.com/70633080/113849474-81b64880-97d4-11eb-824a-b64c2031d2f0.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113849502-8844c000-97d4-11eb-83ce-e7d56d143c33.png)\
![image](https://user-images.githubusercontent.com/70633080/113849518-8da20a80-97d4-11eb-872b-27cfc0e6452a.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113849562-9abef980-97d4-11eb-8813-fa48b9156565.png)\
![image](https://user-images.githubusercontent.com/70633080/113849596-a1e60780-97d4-11eb-9f9a-75c21408d0a1.png)

- lf/hf
  - cppg : 0.7382393902264306
  - rppg : 0.7089637234432726
- lf보다 hf의 차이가 0.11174444889393255 배 크다.

</div>
</details>

<details>
<summary>9_2.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113849838-d2c63c80-97d4-11eb-8055-3b63a8ed798b.png)\
![image](https://user-images.githubusercontent.com/70633080/113849873-d9ed4a80-97d4-11eb-9757-92a4d0629c19.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113849923-e5d90c80-97d4-11eb-9748-c4cc491a5805.png)\
![image](https://user-images.githubusercontent.com/70633080/113849943-ea9dc080-97d4-11eb-9f85-c93a95df445f.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113849974-f5585580-97d4-11eb-9363-b4691362d11e.png)\
![image](https://user-images.githubusercontent.com/70633080/113850011-fc7f6380-97d4-11eb-909b-498031dbe82e.png)

- lf/hf
  - cppg : 0.6612791025090395
  - rppg : 0.6179063177296421
- lf보다 hf의 차이가 5.717973701538685 배 크다.

</div>
</details>

<details>
<summary>9_3.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113850141-1f117c80-97d5-11eb-89c5-10e514145c5a.png)\
![image](https://user-images.githubusercontent.com/70633080/113850171-25075d80-97d5-11eb-9810-b1b49791857f.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113850212-2fc1f280-97d5-11eb-875c-610fc82bb351.png)\
![image](https://user-images.githubusercontent.com/70633080/113850235-36506a00-97d5-11eb-9fd9-7a71b5d88de1.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113850299-47997680-97d5-11eb-9a1d-f5d94f5a4d3a.png)\
![image](https://user-images.githubusercontent.com/70633080/113850317-4bc59400-97d5-11eb-954c-61fc7bd10e81.png)

- lf/hf
  - cppg : 0.7715687892849006
  - rppg : 0.6685235070740785
- lf보다 hf의 차이가 1.9376001266359186 배 크다.

</div>
</details>

<details>
<summary>9_4.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113850436-70ba0700-97d5-11eb-9db6-a9ebeddb169f.png)\
![image](https://user-images.githubusercontent.com/70633080/113850478-7a436f00-97d5-11eb-8bc1-8439ac4ace2b.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113850512-83ccd700-97d5-11eb-9fbb-d982eb378dfb.png)\
![image](https://user-images.githubusercontent.com/70633080/113850531-892a2180-97d5-11eb-9c39-7455627e0a54.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113850573-93e4b680-97d5-11eb-84f4-5de2d9961a3b.png)\
![image](https://user-images.githubusercontent.com/70633080/113850589-98a96a80-97d5-11eb-9d85-19785d798569.png)

- lf/hf
  - cppg : 1.0664385622034596
  - rppg : 0.8465225668870905
- lf보다 hf의 차이가 2.317754669937378 배 크다.

</div>
</details>

<details>
<summary>9_5.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113850715-b676cf80-97d5-11eb-805e-f790c6b94862.png)\
![image](https://user-images.githubusercontent.com/70633080/113850741-bd9ddd80-97d5-11eb-8d0a-02bc470985c6.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113850801-cd1d2680-97d5-11eb-8954-21c6e684047a.png)\
![image](https://user-images.githubusercontent.com/70633080/113850831-d4443480-97d5-11eb-80ba-da5dda4c2ab8.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113850870-de663300-97d5-11eb-847c-9548805fbd19.png)\
![image](https://user-images.githubusercontent.com/70633080/113850889-e32ae700-97d5-11eb-9cfc-bd2e77f060c8.png)

- lf/hf
  - cppg : 1.2410690503904542
  - rppg : 0.9775459807245811
- lf보다 hf의 차이가 7.1891234713079575 배 크다.

</div>
</details>

<details>
<summary>9_6.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113854080-6ac62500-97d9-11eb-951c-97d3d3c318da.png)\
![image](https://user-images.githubusercontent.com/70633080/113854097-71ed3300-97d9-11eb-92db-4e481ef6f896.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113854133-7c0f3180-97d9-11eb-9c52-7880b2f2e723.png)\
![image](https://user-images.githubusercontent.com/70633080/113854145-816c7c00-97d9-11eb-8552-173d6faf2d96.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113854179-8a5d4d80-97d9-11eb-88cf-b8f1509563a4.png)\
![image](https://user-images.githubusercontent.com/70633080/113854194-8e896b00-97d9-11eb-8654-bcd5b17e667b.png)

- lf/hf
  - cppg : 1.3287173414930786
  - rppg : 0.9981371391694405
- lf보다 hf의 차이가 3.641425590583698 배 크다.

</div>
</details>

<details>
<summary>9_7.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113854305-b2e54780-97d9-11eb-826c-a5116f425d32.png)\
![image](https://user-images.githubusercontent.com/70633080/113854325-b8429200-97d9-11eb-9a8b-e104ded12d84.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113854365-c1cbfa00-97d9-11eb-9eaa-25b35d7a5163.png)\
![image](https://user-images.githubusercontent.com/70633080/113854384-c7294480-97d9-11eb-811a-be84b2022fef.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113854407-d01a1600-97d9-11eb-8315-0978fad98866.png)\
![image](https://user-images.githubusercontent.com/70633080/113854423-d4deca00-97d9-11eb-9a9c-b2ec58eb8567.png)

- lf/hf
  - cppg : 1.1458854733379114
  - rppg : 0.855573145908229
- lf보다 hf의 차이가 5.007574982840265 배 크다.

</div>
</details>

<details>
<summary>9_8.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113854567-f63fb600-97d9-11eb-913b-2f69bbd20ce9.png)\
![image](https://user-images.githubusercontent.com/70633080/113854587-fb9d0080-97d9-11eb-9209-10abc3a0d949.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113854618-05beff00-97da-11eb-8f58-7e944b20c45e.png)\
![image](https://user-images.githubusercontent.com/70633080/113854629-0b1c4980-97da-11eb-99fd-c9bdf1443821.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113854656-13748480-97da-11eb-8885-46f271c0e2b4.png)\
![image](https://user-images.githubusercontent.com/70633080/113854666-17a0a200-97da-11eb-8937-48bd040560f5.png)

- lf/hf
  - cppg : 1.3264252888426804
  - rppg : 1.0461835843574063
- lf보다 hf의 차이가 16.217745626515168 배 크다.

</div>
</details>

<details>
<summary>9_9.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113854873-546c9900-97da-11eb-80b3-c27d0ee5176b.png)\
![image](https://user-images.githubusercontent.com/70633080/113854899-5f272e00-97da-11eb-8a47-7cb69e7bf38e.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113854935-69492c80-97da-11eb-99ae-bbda92725615.png)\
![image](https://user-images.githubusercontent.com/70633080/113854957-6ea67700-97da-11eb-9816-3546e0d16ee1.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113854985-75cd8500-97da-11eb-8894-e6a790cbf725.png)\
![image](https://user-images.githubusercontent.com/70633080/113854998-79f9a280-97da-11eb-93ea-f78661209d61.png)

- lf/hf
  - cppg : 1.465575363310893
  - rppg : 1.070597402306509
- lf보다 hf의 차이가 17.163128465709622 배 크다.

</div>
</details>

<details>
<summary>9_10.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113855095-9d245200-97da-11eb-9228-7dc912ff8b46.png)\
![image](https://user-images.githubusercontent.com/70633080/113855110-a2819c80-97da-11eb-8055-29dd37e1631d.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113855149-ac0b0480-97da-11eb-8915-7c2df3a1beaa.png)\
![image](https://user-images.githubusercontent.com/70633080/113855168-b1684f00-97da-11eb-8b62-1d5ccbb6e0b5.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113855194-b927f380-97da-11eb-9e85-4e139dbbebd1.png)\
![image](https://user-images.githubusercontent.com/70633080/113855211-bd541100-97da-11eb-983a-d14f6468699c.png)

- lf/hf
  - cppg : 1.3746336338822833
  - rppg : 0.9688355607695189
- lf보다 hf의 차이가 35.3826659772774 배 크다.

</div>
</details>

</div>
</details>

<details>
<summary>10. 한우정(자세히)</summary>

- Total : lf_hf_Ratio에 차이가 있음. **(0.5054755504352224 , 0.26475324894214664)**
    - rppg개수 70개 모자름(19760) (따라서 원래 index-72번부터 시작 : 828:sr * 630 -72)
        - group 8 -> 1
        - group 9 -> 1
        - group 10 -> 16
- After Shift **(파랑 : c, 주황 : r)**
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/114141666-ded50a00-994c-11eb-8712-beace96588f5.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/114141702-eb596280-994c-11eb-8408-270cef5d0b2b.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/114141725-f3b19d80-994c-11eb-96c2-9e464a7365fd.png" weight="50%" height="50%">
    </p>

    

<details>
<summary>Total(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/113983977-8b4bb900-9885-11eb-95d5-ede466a45fa6.png)\
![image](https://user-images.githubusercontent.com/70633080/113983996-90a90380-9885-11eb-8452-abf8e978802c.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/113984045-9e5e8900-9885-11eb-8553-4c7d368d3529.png)\
![image](https://user-images.githubusercontent.com/70633080/113984022-99013e80-9885-11eb-99e9-956f26704199.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/113984073-a5859700-9885-11eb-8603-11e71d017be9.png)\
![image](https://user-images.githubusercontent.com/70633080/113984082-a9b1b480-9885-11eb-80e2-66f060d7b100.png)

- lf/hf
  - cppg : 0.5054755504352224
  - rppg : 0.26475324894214664
- lf보다 hf의 차이가 6.7341302012603315 배 크다.

</div>
</details>

<details>
<summary>10_0.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114132881-20ab8380-9940-11eb-9580-0f84c80b7c71.png)\
![image](https://user-images.githubusercontent.com/70633080/114132890-25703780-9940-11eb-9ee6-1fa8591aadd0.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114132930-34ef8080-9940-11eb-886c-8a508bc98306.png)\
![image](https://user-images.githubusercontent.com/70633080/114132912-2dc87280-9940-11eb-920e-a68751481d18.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114132957-3caf2500-9940-11eb-85cb-f3b16d7fe0a6.png)\
![image](https://user-images.githubusercontent.com/70633080/114132966-4173d900-9940-11eb-8a25-605198634e98.png)

- lf/hf
  - cppg : 0.5014693697829238
  - rppg : 0.22091037928057478
- lf보다 hf의 차이가 7.275107539182831 배 크다.

</div>
</details>

<details>
<summary>10_1.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114134112-286c2780-9942-11eb-9dfd-9507f15540d3.png)\
![image](https://user-images.githubusercontent.com/70633080/114134122-2d30db80-9942-11eb-8af5-48f2512db0ba.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114134143-35891680-9942-11eb-9293-b03040c1c486.png)\
![image](https://user-images.githubusercontent.com/70633080/114134152-3a4dca80-9942-11eb-9d0f-9398f69c52a8.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114134170-420d6f00-9942-11eb-82df-9a2cd385c883.png)\
![image](https://user-images.githubusercontent.com/70633080/114134179-46d22300-9942-11eb-95b6-cba6844955fd.png)

- lf/hf
  - cppg : 0.2554406514631757
  - rppg : 0.1671540979595231
- lf보다 hf의 차이가 7.6207326092313545 배 크다.

</div>
</details>

<details>
<summary>10_2.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114134268-69643c00-9942-11eb-974c-7de8378e30c5.png)\
![image](https://user-images.githubusercontent.com/70633080/114134277-708b4a00-9942-11eb-81c6-09789503b6fc.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114134308-7b45df00-9942-11eb-82c9-5daccbdf65e6.png)\
![image](https://user-images.githubusercontent.com/70633080/114134318-800a9300-9942-11eb-9941-55c87032f5c9.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114134339-87ca3780-9942-11eb-979e-ac5d95f219df.png)\
![image](https://user-images.githubusercontent.com/70633080/114134346-8bf65500-9942-11eb-8607-a35e9bda2568.png)

- lf/hf
  - cppg : 0.3450738694810204
  - rppg : 0.17754097998390064
- lf보다 hf의 차이가 8.62132656848474 배 크다.

</div>
</details>

<details>
<summary>10_3.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114134401-a92b2380-9942-11eb-84ae-95b32a78bf7e.png)\
![image](https://user-images.githubusercontent.com/70633080/114134413-adefd780-9942-11eb-9daf-d41150cf2ff2.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114134550-e8f20b00-9942-11eb-9905-b7993ecb0ab3.png)\
![image](https://user-images.githubusercontent.com/70633080/114134440-b6481280-9942-11eb-9dc9-8fa13653d936.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114134572-f0b1af80-9942-11eb-96db-35c1b9e44346.png)\
![image](https://user-images.githubusercontent.com/70633080/114134587-f5766380-9942-11eb-9097-59060d901d8a.png)

- lf/hf
  - cppg : 0.4036978574602945
  - rppg : 0.20416128787067056
- lf보다 hf의 차이가 7.443991929740404 배 크다.

</div>
</details>

<details>
<summary>10_4.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114134664-12ab3200-9943-11eb-9e1c-52153827ca82.png)\
![image](https://user-images.githubusercontent.com/70633080/114134677-18087c80-9943-11eb-8522-9d7de0126ab2.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114134702-20f94e00-9943-11eb-8c2e-192d427c305e.png)\
![image](https://user-images.githubusercontent.com/70633080/114134728-28205c00-9943-11eb-8c4f-12f04314fb1b.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114134746-2f476a00-9943-11eb-8536-377040b6fb70.png)\
![image](https://user-images.githubusercontent.com/70633080/114134759-33738780-9943-11eb-9e10-d9a04d9b7bdf.png)

- lf/hf
  - cppg : 0.3843770755551231
  - rppg : 0.22585342884478585
- lf보다 hf의 차이가 6.3706333553736245 배 크다.

</div>
</details>

<details>
<summary>10_5.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114134820-4f772900-9943-11eb-892e-a3c15a89f577.png)\
![image](https://user-images.githubusercontent.com/70633080/114134830-543bdd00-9943-11eb-81c9-0b755d3f236b.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114134855-60279f00-9943-11eb-8033-88e27580d359.png)\
![image](https://user-images.githubusercontent.com/70633080/114134865-64ec5300-9943-11eb-9cdf-5ee5ab7266e3.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114134876-6cabf780-9943-11eb-97f9-7ed6aa80239e.png)\
![image](https://user-images.githubusercontent.com/70633080/114134898-703f7e80-9943-11eb-8ca4-af4d8a5fb2ee.png)

- lf/hf
  - cppg : 0.42236226196957743
  - rppg : 0.23331520853235502
- lf보다 hf의 차이가 6.717780047191996 배 크다.

</div>
</details>

<details>
<summary>10_6.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114135167-d4fad900-9943-11eb-880b-8325f6d46ae0.png)\
![image](https://user-images.githubusercontent.com/70633080/114135186-da582380-9943-11eb-9f5b-c6b08019475c.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114135217-e512b880-9943-11eb-9542-8841fafa1674.png)\
![image](https://user-images.githubusercontent.com/70633080/114135232-eb089980-9943-11eb-9a5e-9907a7530507.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114135448-3753d980-9944-11eb-8619-221154ef3ff4.png)\
![image](https://user-images.githubusercontent.com/70633080/114135464-3b7ff700-9944-11eb-9d43-f39740bd2db6.png)

- lf/hf
  - cppg : 0.409839634509373
  - rppg : 0.21035352051280015
- lf보다 hf의 차이가 7.565542891304801 배 크다.

</div>
</details>

<details>
<summary>10_7.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114135572-61a59700-9944-11eb-9b0c-5d501f7bb7fd.png)\
![image](https://user-images.githubusercontent.com/70633080/114135584-6702e180-9944-11eb-857a-9155feb62acd.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114137577-5f910780-9947-11eb-8b21-456fb06eea7e.png)\
![image](https://user-images.githubusercontent.com/70633080/114137586-6455bb80-9947-11eb-86a7-bf591b749708.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114137617-6cadf680-9947-11eb-8e8c-501c69b5a450.png)\
![image](https://user-images.githubusercontent.com/70633080/114137638-70da1400-9947-11eb-948e-aacdd681ade8.png)

- lf/hf
  - cppg : 0.450506793817796
  - rppg : 0.2915628908509832
- lf보다 hf의 차이가 4.814368022284787 배 크다.

</div>
</details>

<details>
<summary>10_8.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114140937-e647e380-994b-11eb-85f5-d5ff4fc440d6.png)\
![image](https://user-images.githubusercontent.com/70633080/114140955-eba52e00-994b-11eb-81f7-9d5a8da2e7ac.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114140974-f5c72c80-994b-11eb-82ee-1fbfc8024e3b.png)\
![image](https://user-images.githubusercontent.com/70633080/114140986-fb247700-994b-11eb-97ac-f1bf67347c4b.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114141008-01b2ee80-994c-11eb-9c69-7b17036a93d0.png)\
![image](https://user-images.githubusercontent.com/70633080/114141027-05467580-994c-11eb-8fd8-c51fbcf80305.png)

- lf/hf
  - cppg : 0.5369504702005459
  - rppg : 0.3813836851353919
- lf보다 hf의 차이가 4.487226434432397 배 크다.

</div>
</details>

<details>
<summary>10_9.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114141122-2018ea00-994c-11eb-8c6b-de1a9faae49e.png)\
![image](https://user-images.githubusercontent.com/70633080/114141135-24dd9e00-994c-11eb-850b-631c5aef5f4d.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114141151-2eff9c80-994c-11eb-83da-4dd81ae74c4a.png)\
![image](https://user-images.githubusercontent.com/70633080/114141171-33c45080-994c-11eb-8591-920bb87ba495.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114141199-3c1c8b80-994c-11eb-9b57-b3c2c28d81b4.png)\
![image](https://user-images.githubusercontent.com/70633080/114141208-40e13f80-994c-11eb-9dbe-7dbd0c868029.png)

- lf/hf
  - cppg : 0.4777327062062869
  - rppg : 0.3697405426563752
- lf보다 hf의 차이가 3.8362007715116953 배 크다.

</div>
</details>

<details>
<summary>10_10.csv(자세히)</summary>
  
- ppg\
![image](https://user-images.githubusercontent.com/70633080/114141272-5a828700-994c-11eb-8066-0fdc29e590c1.png)\
![image](https://user-images.githubusercontent.com/70633080/114141285-5fdfd180-994c-11eb-81bb-cf15659bb793.png)
- ppi\
![image](https://user-images.githubusercontent.com/70633080/114141327-68380c80-994c-11eb-911c-b5c5abdf90a7.png)\
![image](https://user-images.githubusercontent.com/70633080/114141342-6d955700-994c-11eb-8d0e-602327dfa10c.png)
- graph\
![image](https://user-images.githubusercontent.com/70633080/114141363-7554fb80-994c-11eb-84f2-d07c21bd1eaa.png)\
![image](https://user-images.githubusercontent.com/70633080/114141374-7ab24600-994c-11eb-8bc3-2b01699d12a7.png)

- lf/hf
  - cppg : 0.4761878668638144
  - rppg : 0.3433287513962649
- lf보다 hf의 차이가 4.712158552198214 배 크다.

</div>
</details>

</div>
</details>

## Error_MAE
- before interpolation

|Subject|LF|HF|LFnu|HFnu|LF/HF Ratio|
|------|---|---|---|---|---|
|0|67.02822727272724|165.14528418181823|1.7595707545454553|1.7595707545454546|0.07304521209090908|
|1|17.763888963636347|153.36126305454547|5.578847711818181|5.57884771181818|0.17657422518181812|
|2|60.90793082727276|345.34727730909094|10.314495493636365|10.314495493636365|0.40013056763636357|
|3|223.32611374545456|549.6352677909091|7.61666614909091|7.616666149090909|0.48722348899999995|
|4|65.2458429818182|565.2281617272727|20.880884476363633|20.880884476363633|0.8133197567272727|
|7|139.36207436363628|245.67209663636365|2.8652477836363626|2.8652477836363652|0.24351950463636368|

- after interpolation

|Subject|LF|HF|LFnu|HFnu|LF/HF Ratio|
|------|---|---|---|---|---|
|0|37.5957006363636|95.0709992727273|1.5156712972727286|1.5156712972727286|0.05113324772727271|
|1|9.62639466956522|35.450190582608684|1.8842518195652178|1.8842518195652163|0.04365169013043479|
|2|73.6376737727273|273.83267103636365|7.637345892727271|7.637345892727271|0.30699194036363636|
|3|226.39595815454547|460.2644792454546|6.086365021818182|6.086365021818182|0.4170258086363636|
|4|36.17263723636365|277.9736493|15.798977056363634|15.798977056363634|0.6337375194545454|
|6|144.3210095545455|299.7767645818182|3.3540070690909087|3.354007069090908|0.16222166972727273|
|8|150.85190054545458|250.67671154545454|2.861922651818182|2.861922651818182|0.17835126390909098|
|9|22.147028254545432|99.17271851818181|3.696911172727273|3.696911172727273|0.16042690618181818|

## 성능향상
1. Interpolation
- signal interpolation
    - rppg를 255sr로 interplolation
- RRI interpolation
    - cppg & rppg 모두 길이 * 2 로 interpolation
    - 성능 안좋음
2. RRI outlier remove


## 관련 모듈
### 1. pyserial
- serial port connection을 도와주는 모듈 
- python으로 usb직렬포트에 연결된 장치를 동작시킬 수 있도록 한다.
### 2. Heartpy
### 3. Scipy.signal.find_peaks
## 참고문헌
- http://www.vitalscan.kr/dt_hrv1_kr.htm
