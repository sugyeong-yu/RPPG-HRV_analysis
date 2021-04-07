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
<summary>0. 유수경_1(자세히)</summary>

 - Total : lf_hf_Ratio가 유사함. **(0.8577113522342822 , 00.8144823574325695)**
 
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

</div>
</details>

<details>
<summary>1. 김나혜(자세히)</summary>
    
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

<details>
<summary>4. 이승건(자세히)</summary>

- cppg data개수 모자람 168199개
- rppg data개수 모자람 19793개
 - Total : lf_hf_Ratio가 차이가 있음. **(1.4807216224170776 , 0.6178131036269046)**
    - lf는 거의 유사하지만 hf에서 큰 차이를 보임
 
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

</div>
</details>

<details>
<summary>7. 유수경_2(자세히)</summary>

- cppg data개수 모자람 168112개
- Total : lf_hf_Ratio가 비슷하게 나왔음. **(2.4673490304430854 , 2.100023846724976)**
 
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

</div>
</details>

<details>
<summary>8. 유수경_3(자세히)</summary>

- cppg data개수 모자람 168240개
- Total : lf_hf_Ratio가 비슷하게 나왔음. **(1.722921074032543 , 1.4622911848470102)**
 
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

- rppg개수 40개 모자름(19760) (따라서 원래 index-40번부터 시작 : 860:sr * 630 -40)
    - group 15 -> 22
    - group 16 -> 1
    - group 17 -> 27
- Total : lf_hf_Ratio가 비슷하게 나왔음. **(0.8919346897922263 , 0.8264034869050073)**
- Shift

    

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

## 관련 공부
### 1. pyserial
- serial port connection을 도와주는 모듈 
- python으로 usb직렬포트에 연결된 장치를 동작시킬 수 있도록 한다.
