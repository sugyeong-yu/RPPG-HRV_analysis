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
- hrv_analysis.ipynb : 추출한 PPG신호들을 불러와 전처리과정 수행, HRV계산 , rppg와 cppg의 결과를 비교하는 main파일이다.
- error_rate.ipynb : MAPE를 구하는 과정
## Protocol
1. Matching Time
    - cppg와 rppg의 시간 기록 및 맞춰주기
2. Data shift
    - Data 수 늘리기
3. 신호 전처리(동잡음 제거)
    - bandfass filtering
    - **interpolation**
4. **Peak detection**
5. rr interval 계산
    - 이상값 제거
    - **rri interpolation** : zscore 2이상 > median값으로 대체
6. hrv feature extract
    - 주파수 변환(FFT)
    - 각 지표값 계산

## Result
### after interpolation

<details>
<summary>0. 유수경(자세히)</summary>

- After Shift **(파랑 : c, 주황 : r)**
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121157664-b7cf8180-c884-11eb-8811-ae4d1cc987a2.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121157535-9d95a380-c884-11eb-83f0-76e130ccdd36.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121157605-ad14ec80-c884-11eb-86c6-9c26511a4912.png" weight="50%" height="50%">
    </p>


</div>
</details>

<details>
<summary>1. 김나혜(자세히)</summary>

- After Shift **(파랑 : c, 주황 : r)**
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121158023-00873a80-c885-11eb-948a-4ddc1a902586.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121157899-e9484d00-c884-11eb-9d8d-6c750d67a33f.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121157962-f402e200-c884-11eb-9b54-77b36f697159.png" weight="50%" height="50%">
    </p>

</div>
</details>

<details>
<summary>2. 이미경(자세히)</summary>

- After Shift **(파랑 : c, 주황 : r)**
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121298988-b909b880-c92f-11eb-9923-a4e46ba930a2.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121298865-8495fc80-c92f-11eb-886b-b63021acf13d.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121298953-a7281580-c92f-11eb-87e9-7145ecd68e89.png" weight="50%" height="50%">
    </p>

</div>
</details>

<details>
<summary>3. 복진영(자세히)</summary>

- After Shift **(파랑 : c, 주황 : r)**
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121299637-b065b200-c930-11eb-92a0-6c29207fd5a3.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121299663-bb204700-c930-11eb-9ee1-327af4514fef.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121299688-c4a9af00-c930-11eb-9ddc-9cd829548c7a.png" weight="50%" height="50%">
    </p>

</div>
</details>

<details>
<summary>4. 이승건(자세히)</summary>

- After Shift **(파랑 : c, 주황 : r)**
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121299897-063a5a00-c931-11eb-8468-c3ded9e076a3.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121299773-e145e700-c930-11eb-9120-5325f3b4b358.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121299835-f4f14d80-c930-11eb-9567-ec5eb6105d05.png" weight="50%" height="50%">
    </p>

</div>
</details>

<details>
<summary>6. 목지원(자세히)</summary>

- After Shift **(파랑 : c, 주황 : r)**
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121300033-3d107000-c931-11eb-96c5-f43d163505d5.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121300062-47cb0500-c931-11eb-880a-b895094e0ee8.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121300085-50bbd680-c931-11eb-84c3-9349c02f6f78.png" weight="50%" height="50%">
    </p>

</div>
</details>

<details>
<summary>7. 유수경(자세히)</summary>

- After Shift **(파랑 : c, 주황 : r)**
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121300270-94164500-c931-11eb-9127-5cc468baea15.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121300214-81037500-c931-11eb-956e-302f77229a76.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121300245-8a8cdd00-c931-11eb-849f-ac71d7c66bb1.png" weight="50%" height="50%">
    </p>

</div>
</details>

<details>
<summary>8. 유수경(자세히)</summary>

- After Shift **(파랑 : c, 주황 : r)**
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121300407-c45de380-c931-11eb-8c19-eef7dbe795f0.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121300449-cfb10f00-c931-11eb-8fc8-1bfff88335a5.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121300474-d9d30d80-c931-11eb-96df-2106137c3232.png" weight="50%" height="50%">
    </p>

</div>
</details>

<details>
<summary>9. 이채원(자세히)</summary>

- After Shift **(파랑 : c, 주황 : r)**
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121301469-37b42500-c933-11eb-9e08-7aa0d3b06d0c.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121301497-43075080-c933-11eb-8eca-dbff68d0198b.png" weight="50%" height="50%">
    </p>
    <p align="left">
        <img src="https://user-images.githubusercontent.com/70633080/121301520-4bf82200-c933-11eb-82a2-c9bc9beaafc7.png" weight="50%" height="50%">
    </p>

</div>
</details>

## Error_MAPE
- MAE를 percentage로 나타낸 오류

|Subject|LF|HF|LFnu|HFnu|LF/HF Ratio|
|------|---|---|---|---|---|
|0|2.8872087544547393|5.861178684017609|3.350985072013366|2.8109087600953595|6.038429821194515|
|1|6.417701990876125|13.429052407903647|11.11510278792065|6.192950985967|16.18713528362225|
|2|13.225598377711108|54.8460506544275|14.625953833604626|16.436452243256326|26.609694501825466|
|3|13.822062628582088|51.23745428470032|9.618777774258897|17.899117742700206|21.83058127682691|
|4|8.607210684208018|90.65756689071944|35.886858460223586|50.01491570039429|46.42828015789942|
|6|14.33750709789632|30.811411874400505|6.373582692918397|7.602173921916772|12.544127794962371|
|7|6.005514752653282|17.129279303668273|3.3815341932955536|6.73766560623688|9.449196919322652|
|8|8.381996054357625|22.146049975544425|4.707205797806904|7.386282518489523|11.242315299918836|
|9|3.180680456622452|14.026737728930842|7.123159746938428|8.00036896731856|13.948012329409012|
|10|66.68657929365014|75.56412545135001|7.834356028702107|2.9159734301814377|10.538612092910158|
|11|48.131596542831225|75.99573236679021|12.477667125525825|4.074904604367801|15.762645448191199|

- good / bad case
    - good : 0,1,6,7,8,9
    - bad : 2,3,4

- NNI

|Subject|LF|HF|LFnu|HFnu|LF/HF Ratio|
|------|---|---|---|---|---|
|0|2.8872087544547393|5.861178684017609|3.350985072013366|2.8109087600953595|6.038429821194515|
|1(C2,R3)|53.00984872246723|36.93029903267332|7.891524099163043|4.656104302050855|13.379275367257252|
|**2**|35.65433405928819|35.000949411566936|3.4140408960970245|2.5643061953456305|5.940796334550791|
|**3**|15.619992334316255|34.147513451235454|5.708730860874415|8.898387080396326|12.44515528501262|
|**4**|51.54845908793105|70.63511809153465|7.967425539827687|6.535685936100638|12.89686467116794|
|6(유지)|14.33750709789632|30.811411874400505|6.373582692918397|7.602173921916772|12.544127794962371|
|**7(C2.0 R2.5)**|15.349812391035009|13.666160723342664|2.2093815569167874|3.403207884496201|5.7101652060297425|
|**8**|3.4086357241056318|12.412729637485551|3.867001891918643|5.836600278060514|9.022814301782613|
|9(유지)|3.180680456622452|14.026737728930842|7.123159746938428|8.00036896731856|13.948012329409012|
|10(유지C3,R2)|66.68657929365014|75.56412545135001|7.834356028702107|2.9159734301814377|10.538612092910158|
|**11(Cx R2)**|38.78701369457467|30.288710694497663|10.165037708442274|2.6645133116930007|13.2895068723929|

## 관련 모듈
### 1. pyserial
- serial port connection을 도와주는 모듈 
- python으로 usb직렬포트에 연결된 장치를 동작시킬 수 있도록 한다.
### 2. Heartpy
### 3. Scipy.signal.find_peaks
## 참고문헌
- http://www.vitalscan.kr/dt_hrv1_kr.htm
- https://blog.orikami.nl/exploring-heart-rate-variability-using-python-483a7037c64d
