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

## 관련 공부
### 1. pyserial
- serial port connection을 도와주는 모듈 
- python으로 usb직렬포트에 연결된 장치를 동작시킬 수 있도록 한다.
