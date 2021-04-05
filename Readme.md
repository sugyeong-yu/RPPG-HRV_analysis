# rppg_hrv
- 비접촉식 ppg(rppg)로도 hrv분석이 가능함을 증명한다.


## Code inform
- utils.py : 데이터 전처리 및 ppi 계산 등 필요한 함수를 구현해놓은 python file
- video.ipynb : 실시간 웹캠으로 얼굴 image를 촬영하는 동시에 접촉식ppg data를 실시간 시간과 함께 기록한다.
- rppg.ipynb : 캡처된 얼굴 image들을 불러와 ppg신호를 추출하여 시간과 함께 기록하는 rppg추출
- variable_sampling_rate.ipynb : sr이 가변적인 rppg의 신호를 불러와 시간정보에 맞추어 초당 sr을 추출하여 그룹화한다.
- hrv_analysis.ipynb : 추출한 hrv신호들을 불러와 rppg와 cppg의 결과를 비교한다.

## Protocol
1. 실험
    - 얼굴 이미지와 cppg를 동시에 추출.
    - 얼굴 이미지로 rppg를 추출
    - cppg와 rppg의 시간 기록 및 맞춰주기
    - data shift
2. 신호 전처리
    - bandfass filtering
    - normalization(0~1)
3. Peak detection
4. rr interval 계산
    - 이상값 제거
5. hrv feature extract

## Process
### 새로운 데이터
- 본인의 데이터를 사용
- data shift없이 앞,뒤 30초 자른 데이터 사용했음.
- bandpass filtering 사용함
- 그 결과, lf/hf 가 유사했고 lf에서 큰차이가 나지 않음. 
- 비교적 hf에서 더 큰차이를 보임.
- 2번 : lf는 완전유사, hf에서 큰차이
- 3번 : lf도 차이가 좀나긴하지만 hf에서 차이가 2
- 4번 : lf 유사, hf에서 큰차이 근데 데이터수가 모자름 
### 데이터 shift
- 수경(0) : 모두다 유사.
- 미경(2) : 모두다 r의 hf가 더 높고 차이가 컸으며 lf에서는 차이가 그리 크지않았음.

## Result
<details>
<summary>3. 복진영(자세히)</summary>

- lf/hf에 차이가 있음.
- lf에도 약간의 차이가 있음
- 그러나 lf에 비해 hf가 더 차이가 있었음.

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

## 관련 공부
### 1. pyserial
- serial port connection을 도와주는 모듈 
- python으로 usb직렬포트에 연결된 장치를 동작시킬 수 있도록 한다.
