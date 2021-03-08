# rppg_HRV
:heartpulse: 비접촉식 rppg를 이용한 HRV분석
# DATA
- Data
  - 1.lf
  - 2.hf	
  - 3.lf_hf_ratio	
  - 4.lfnu	
  - 5.hfnu	
  - 6.total_power	
  - 7.vlf	
  - 8.num
- 전처리를 거친 rppg data와 cppg data를 사용
  - bandpass filtering은 CPPG만 거친다. ( rppg는 bandwidth filtering을 이미 거친 데이터)
  - 총 9분30초의 data를 5분씩 자름\
![rppg](https://user-images.githubusercontent.com/70633080/110286439-49321c00-8028-11eb-9c35-be82c612153d.png)
![cppg](https://user-images.githubusercontent.com/70633080/110286466-56e7a180-8028-11eb-8283-61b70f7bb34b.png)

# Protocol
1. 실험
  - rppg와 cppg를 동시에 측정한다.
  - 피험자 수 : 13명
  - 실험시간 : 11분 ( 앞의 30초 자르고 뒤의 1분 자르기)
  - 사용된 기기 : 총2개 (P400과 SPO2)
    - 사람 별로 둘중 잘나온 data
2. 데이터 분석
    1. Data load : csv file을 불러와 심박신호를 불러옴
    2. Data cutting : 데이터의 노이즈를 감안하여 앞의 30초, 뒤의 1분을 잘라 9분30초의 데이터로 만듬
    3. Filtering : 데이터에 노이즈가 섞여있으므로 cppg의 경우 bandfass filter를 이용해 노이즈를 제거함.
    4. Normalization : cppg와 rppg 그리고 피험자마다 데이터의 범위가 다를 수 있기 때문에 0 ~ 1 사이값으로 정규화해줌
    5. find peak : peak를 찾음
    6. time domain : 현재 데이터의 가로축은 시간이 아닌 데이터의 순서인덱스로 구성되어 있기 때문에 시간축으로 바꿔움 (peak도 함께)
    7. ppi 계산 : hrv분석에서 필요한 것은 ppi(peak간의 간격) 데이터이기 때문에 찾은 peak를 통해 ppi를 계산한다.
    8. hrv feature extract : hrv 특징을 추출해주는 모듈을 사용하여 각 특징들을 뽑는다.
    9. Cppg vs Rppg : 각 특징 값을 비교한다.
# 발전
- rppg 전처리해보고 결과비교하기
# Result

- [Data shift 적용 전](https://github.com/sugyeong-yu/rppg_HRV/blob/main/README.md#before-data-shift)
- [Data shift 적용 후](https://github.com/sugyeong-yu/rppg_HRV/blob/main/README.md#after-data-shift)
  - Data를 cutting & shift하여 데이터의 수를 늘린다.
- [RPPG 전처리 적용 전 결과](https://github.com/sugyeong-yu/rppg_HRV/blob/main/README.md#rppg-filtering-%EA%B3%BC%EC%A0%95-%EC%A0%84)
- [RPPG 전처리 적용 후 결과 비교](https://github.com/sugyeong-yu/rppg_HRV/blob/main/README.md#rppg-filtering-%EA%B3%BC%EC%A0%95-%ED%9B%84)
  - bandwidth filtering을 거쳤지만 안정적이지 못한 rppg신호로 인해 결과가 잘 나오지 않는 경우가 있다.
  - 이를 대비하여 bandpass filter를 추가로 적용해본다.

## Before Data shift
### 1. P400
- 계열1(파란) : Cppg(p400)
- 계열2(주황) : Rppg(web-cam)
1. 김나혜
<img src="https://user-images.githubusercontent.com/70633080/109270154-f9e23380-7850-11eb-9fd4-1f5b2b1363da.png" width=80% height=80%>
2. 김소의
<img src="https://user-images.githubusercontent.com/70633080/110065786-55fa0a00-7db3-11eb-902a-c4829c4d04f1.png" width=80% height=80%>
3.김나혜
<img src="https://user-images.githubusercontent.com/70633080/110065911-a709fe00-7db3-11eb-8cec-23976163e55c.png" width=80% height=80%>
4.김소의
<img src="https://user-images.githubusercontent.com/70633080/110065971-c56ff980-7db3-11eb-80b1-03a91e4fb802.png" width=80% height=80%>
5. 김나혜
<img src="https://user-images.githubusercontent.com/70633080/109270068-d7e8b100-7850-11eb-98a8-5b9622cf601f.png" width=80% height=80%>
6. 유수경
<img src="https://user-images.githubusercontent.com/70633080/109270833-f9966800-7851-11eb-9dfc-da5b5b45021e.png" width=80% height=80%>
7. 김소의
<img src="https://user-images.githubusercontent.com/70633080/109271081-598d0e80-7852-11eb-82d2-e1c248e5b585.png" width=80% height=80%>
8. 이승건
<img src="https://user-images.githubusercontent.com/70633080/109271352-bc7ea580-7852-11eb-970d-6b4533d42bc3.png" width=80% height=80%>
9. 목지원
<img src="https://user-images.githubusercontent.com/70633080/109271524-fcde2380-7852-11eb-9278-3138fa5ee6a0.png" width=80% height=80%>
10. 한나연
<img src="https://user-images.githubusercontent.com/70633080/109271732-44fd4600-7853-11eb-9b8b-fa41610ae90e.png" width=80% height=80%>
11. 성시원
<img src="https://user-images.githubusercontent.com/70633080/109271993-9f96a200-7853-11eb-8dae-e7afe79adbad.png" width=80% height=80%>
12. 장우혁
<img src="https://user-images.githubusercontent.com/70633080/109272215-e5ec0100-7853-11eb-8b1f-252bdd737ca3.png" width=80% height=80%>
13. 이미경
<img src="https://user-images.githubusercontent.com/70633080/109272488-467b3e00-7854-11eb-8c2b-e60e2da5e96a.png" width=80% height=80%>
14. 황현상
<img src="https://user-images.githubusercontent.com/70633080/109272660-88a47f80-7854-11eb-9863-561d260d2b77.png" width=80% height=80%>
15. 이건영
<img src="https://user-images.githubusercontent.com/70633080/109272796-b5589700-7854-11eb-86f0-12d1cec3aed6.png" width=80% height=80%>
16. 진경원
<img src="https://user-images.githubusercontent.com/70633080/109272938-e3d67200-7854-11eb-8c20-43da30702356.png" width=80% height=80%>
17. 서건하
<img src="https://user-images.githubusercontent.com/70633080/109273140-24ce8680-7855-11eb-8650-ba4ec3a6ba08.png" width=80% height=80%>

- Total (lf_hf_ratio)\
![image](https://user-images.githubusercontent.com/70633080/110065472-87260a80-7db2-11eb-8669-c6a32104f5e6.png)

### 2. SpO2_ppg
- 계열1(파란) : Cppg(SpO2)
- 계열2(주황) : Rppg(web-cam)
1. 김나혜
2. 유수경
<img src="https://user-images.githubusercontent.com/70633080/109286776-0d4bc980-7866-11eb-93da-6a47b93b3413.png" width=80% height=80%>
3. 김소의
4. 이승건
<img src="https://user-images.githubusercontent.com/70633080/109287024-61ef4480-7866-11eb-8783-c27f8457ed5e.png" width=80% height=80%>
5. 목지원
6. 한나연
<img src="https://user-images.githubusercontent.com/70633080/109287746-594b3e00-7867-11eb-9840-5e22ae8cbea6.png" width=80% height=80%>
7. 성시원
<img src="https://user-images.githubusercontent.com/70633080/109289018-f2c71f80-7868-11eb-9f5e-6210147085e6.png" width=80% height=80%>
8. 장우혁
<img src="https://user-images.githubusercontent.com/70633080/109289164-2a35cc00-7869-11eb-9ccd-2085b8d68954.png" width=80% height=80%> 

- Total (lf_hf_ratio)\
![image](https://user-images.githubusercontent.com/70633080/109295516-396d4780-7872-11eb-844d-222c8bc51a9f.png)



## After Data shift
1. 김나혜 (P400)\
  ![image](https://user-images.githubusercontent.com/70633080/110087300-cfefba80-7dd6-11eb-9853-e5d7dfcdf376.png)
    1. 1_0.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110082923-5b664d00-7dd1-11eb-885b-961366d5aef1.png)
    2. 1_1.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110083078-91a3cc80-7dd1-11eb-9b91-edaf70610bb0.png)
    3. 1_2.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110083285-e0e9fd00-7dd1-11eb-9a6d-c8bae9b266a7.png)
    4. 1_3.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110083393-fd863500-7dd1-11eb-95a0-03fa66ee7a30.png)
    5. 1_4.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110083467-11ca3200-7dd2-11eb-8b32-b9f7e7b4d054.png)
    6. 1_5.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110083532-27d7f280-7dd2-11eb-881f-dec335ebfdc8.png)
    7. 1_6.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110087770-6b812b00-7dd7-11eb-873e-b19ff2f5df46.png)
    8. 1_7.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110087833-80f65500-7dd7-11eb-9d89-763027d203b5.png)
    9. 1_8.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110087909-966b7f00-7dd7-11eb-9793-ed7744bd2139.png)
    10. 1_9.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110087994-ab481280-7dd7-11eb-86a7-88b2d340f14f.png)
    11. 1_10.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110088104-c74bb400-7dd7-11eb-8d0d-c797627a511d.png)


2. 김소의(p400)\
![image](https://user-images.githubusercontent.com/70633080/110274487-475d5e00-8012-11eb-886c-619621fb7902.png)
    1. 2_0.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110273858-d9fcfd80-8010-11eb-9aa3-5f71da0582a7.png)
    2. 2_1.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110273905-f4cf7200-8010-11eb-82f8-19ea0f14f9df.png)
    3. 2_2.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110273963-14669a80-8011-11eb-8268-e76f30c4ebfe.png)
    4. 2_3.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110274003-2ea07880-8011-11eb-9920-2a3136bea23a.png)
    5. 2_4.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110274050-4546cf80-8011-11eb-8c8b-671d63b9b0ef.png)
    6. 2_5.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110274193-98b91d80-8011-11eb-9c95-b3547b3dff5d.png)
    7. 2_6.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110274237-b4242880-8011-11eb-94f3-0c83e4c31705.png)
    8. 2_7.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110274291-d0c06080-8011-11eb-827c-b4d978192af5.png)
    9. 2_8.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110274327-e9c91180-8011-11eb-9511-14a7770a40cb.png)
    10. 2_9.csv\
  ![image](https://user-images.githubusercontent.com/70633080/110274360-02392c00-8012-11eb-97f1-6fa1546e8208.png)
    11. 2_10.csv\ 
  ![image](https://user-images.githubusercontent.com/70633080/110274424-23018180-8012-11eb-8318-0dae8df7e2c3.png)

### rppg filtering 과정 전
- PPI비교
  - 잘 나온 예시\
  ![image](https://user-images.githubusercontent.com/70633080/110275093-b7b8af00-8013-11eb-9d54-3d2bd271d1d6.png)
  ![image](https://user-images.githubusercontent.com/70633080/110275100-c010ea00-8013-11eb-8ec6-e5f1f7e42964.png)
  - 잘못나온 예시\
  ![image](https://user-images.githubusercontent.com/70633080/110275053-a40d4880-8013-11eb-89ee-84269ad57e57.png)
  ![image](https://user-images.githubusercontent.com/70633080/110275066-aa9bc000-8013-11eb-8ea5-0c6db012df2a.png)
### rppg filtering 과정 후 
- 1_2.csv
  - rppg\
  ![image](https://user-images.githubusercontent.com/70633080/110288521-7c29df00-802b-11eb-889f-0d6b3ae10055.png)
  ![image](https://user-images.githubusercontent.com/70633080/110288527-7fbd6600-802b-11eb-9433-648d9ff1dfa9.png)
  - ppi\
  ![image](https://user-images.githubusercontent.com/70633080/110288542-864bdd80-802b-11eb-941d-244746171e75.png)
  ![image](https://user-images.githubusercontent.com/70633080/110288548-88ae3780-802b-11eb-9607-f2873b69fabd.png)
  - graph\
  ![image](https://user-images.githubusercontent.com/70633080/110288559-8f3caf00-802b-11eb-8afe-f8fe4e2540b9.png)
  - ppi는 확연히 좋아졌지만 graph에서의 차이는 더 커짐,,
- 2_2.csv
  - rppg\
  ![before](https://user-images.githubusercontent.com/70633080/110287498-f9eceb00-8029-11eb-9108-8e86884ea82b.png)
  ![after](https://user-images.githubusercontent.com/70633080/110287527-05401680-802a-11eb-9ff0-aaad2d5f4681.png)
  - ppi\
  ![before](https://user-images.githubusercontent.com/70633080/110287619-2d2f7a00-802a-11eb-850d-e74af12a3152.png)
  ![after](https://user-images.githubusercontent.com/70633080/110287462-ea6da200-8029-11eb-9626-97bc6a8326e9.png)
  - graph\
  ![image](https://user-images.githubusercontent.com/70633080/110288459-61576a80-802b-11eb-88bf-67abb99039bb.png)
  - ppi는 더 좋아졌고 그래프상으로는 유사함

- 6_1.csv
  - rppg\
  ![image](https://user-images.githubusercontent.com/70633080/110289335-9dd79600-802c-11eb-85bf-d7c1379fb95e.png)
  ![image](https://user-images.githubusercontent.com/70633080/110289351-a4fea400-802c-11eb-8ab6-216375e43374.png)
  - ppi\
  ![image](https://user-images.githubusercontent.com/70633080/110289147-5c46eb00-802c-11eb-9966-c49da92354c5.png)
  ![image](https://user-images.githubusercontent.com/70633080/110289137-57823700-802c-11eb-8f40-3985f72cc9fe.png)
  - graph\
  ![image](https://user-images.githubusercontent.com/70633080/110289562-f149e400-802c-11eb-9578-82cf0e7c840a.png)
  ![image](https://user-images.githubusercontent.com/70633080/110289542-e98a3f80-802c-11eb-950f-988b79ea8521.png)
  - ppi는 약간 좋아졌고 그래프는 훨씬 좋아짐

- 6_2.csv
  - rppg\
  ![image](https://user-images.githubusercontent.com/70633080/110290113-bac09900-802d-11eb-8c39-0ee12dcc5ffe.png)
  ![image](https://user-images.githubusercontent.com/70633080/110290127-be542000-802d-11eb-85ad-0eaaddd6b047.png)
  - ppi\
  ![image](https://user-images.githubusercontent.com/70633080/110290153-c613c480-802d-11eb-9c8c-672457252155.png)
  ![image](https://user-images.githubusercontent.com/70633080/110290156-c90eb500-802d-11eb-89dd-f15c6dcecb85.png)
  - graph\
  ![image](https://user-images.githubusercontent.com/70633080/110290307-fce9da80-802d-11eb-980f-2fe80e1d5f72.png)
  ![image](https://user-images.githubusercontent.com/70633080/110290226-dfb50c00-802d-11eb-9cda-88493cc14add.png)
  - ppi엔 약간  그래프에선 나빠짐
