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
  - 총 9분30초의 data를 5분씩 자름
  - 예시 ( rppg , cppg)\
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
# 실험 경우의 수
- 기기 3개 ( P400, SPO2, 소의PPG)
- filtering ( cppg&rppg or only cppg )
- norm ( O or X )
# Result

- [0.Data shift 적용 전](https://github.com/sugyeong-yu/rppg_HRV/blob/main/README.md#before-data-shift)
- [0.Data shift 적용 후](https://github.com/sugyeong-yu/rppg_HRV/blob/main/README.md#after-data-shift)
  - Data를 cutting & shift하여 데이터의 수를 늘린다.
  - [1.기기 별](https://github.com/sugyeong-yu/rppg_HRV/blob/main/README.md#device--with-or-without-filtering)
  - [2.rppg_filtering 유무](https://github.com/sugyeong-yu/rppg_HRV/blob/main/README.md#device--with-or-without-filtering)
    - [RPPG 전처리 적용 전 PPI](https://github.com/sugyeong-yu/rppg_HRV/blob/main/README.md#rppg-filtering-%EA%B3%BC%EC%A0%95-%EC%A0%84)
    - [RPPG 전처리 적용 후 PPI 비교](https://github.com/sugyeong-yu/rppg_HRV/blob/main/README.md#rppg-filtering-%EA%B3%BC%EC%A0%95-%ED%9B%84)
      - bandwidth filtering을 거쳤지만 안정적이지 못한 rppg신호로 인해 결과가 잘 나오지 않는 경우가 있다.
      - 이를 대비하여 bandpass filter를 추가로 적용해본다.
  - [3.normalization 유무]
  

## Before Data shift
### 1. P400
- 계열1(파란) : Cppg(p400)
- 계열2(주황) : Rppg(web-cam)

- Total (lf_hf_ratio)\
![image](https://user-images.githubusercontent.com/70633080/110065472-87260a80-7db2-11eb-8669-c6a32104f5e6.png)

<details>
<summary>hrv feature graph(자세히)</summary>

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

</div>
</details>


### 2. SpO2_ppg
- 계열1(파란) : Cppg(SpO2)
- 계열2(주황) : Rppg(web-cam)
- Total (lf_hf_ratio)
<img src="https://user-images.githubusercontent.com/70633080/109295516-396d4780-7872-11eb-844d-222c8bc51a9f.png" width=80% height=80%>

<details>
<summary>hrv feature graph(자세히)</summary>
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

</div>
</details>




## After Data shift

### device & With or Without filtering
|기기|filtering O|filtering X|
|------|---|---|
|P400|O|X|
|SPO2|O|X|
|soeui|O|X|

<details>
<summary>1.김나혜(P400)(자세히)</summary>

|기기|filtering O|filtering X|
|------|---|---|
|P400|8|7|
|SPO2|8|7|
|soeui|**9**|7|

![O](https://user-images.githubusercontent.com/70633080/110915695-50746500-835b-11eb-92bf-8cd154344479.png)
![X](https://user-images.githubusercontent.com/70633080/110915712-54a08280-835b-11eb-89bc-018afd560268.png)

![O](https://user-images.githubusercontent.com/70633080/110915803-7568d800-835b-11eb-82bd-c7031cf8e99f.png)
![X](https://user-images.githubusercontent.com/70633080/110915822-7c8fe600-835b-11eb-90e3-3830f5d65ee6.png)

![O](https://user-images.githubusercontent.com/70633080/110915998-aba65780-835b-11eb-8854-a5375a35e8a8.png)
![X](https://user-images.githubusercontent.com/70633080/110916020-b19c3880-835b-11eb-973d-a6bcdc798262.png)

</div>
</details>

<details>
<summary>2. 유수경(SPO2)(자세히)</summary>

|기기|filtering O|filtering X|
|------|---|---|
|P400|9|9|
|SPO2|8|**10**|
|soeui|8|6|

![O](https://user-images.githubusercontent.com/70633080/110916562-4868f500-835c-11eb-9d9e-bc4affb90d75.png)
![X](https://user-images.githubusercontent.com/70633080/110916571-4acb4f00-835c-11eb-9799-e98b8184ede7.png)

![O](https://user-images.githubusercontent.com/70633080/110916654-60d90f80-835c-11eb-93b4-3b3aee2fa42e.png)
![X](https://user-images.githubusercontent.com/70633080/110916667-65052d00-835c-11eb-8200-2fc17ea633b9.png)

![O](https://user-images.githubusercontent.com/70633080/110916733-74847600-835c-11eb-8f6a-2fb7dc1f0854.png)
![X](https://user-images.githubusercontent.com/70633080/110916754-7817fd00-835c-11eb-90c6-04956336b31b.png)

</div>
</details>

<details>
<summary>3. 김소의(P400)(자세히)</summary>

|기기|filtering O|filtering X|
|------|---|---|
|P400|6|9|
|SPO2|**9**|**9**|
|soeui|8|6|

![O](https://user-images.githubusercontent.com/70633080/110917198-fc6a8000-835c-11eb-83dd-4e3f0076bf0e.png)
![X](https://user-images.githubusercontent.com/70633080/110917221-02f8f780-835d-11eb-8438-42d6e21dd181.png)

![O](https://user-images.githubusercontent.com/70633080/110917304-1c9a3f00-835d-11eb-8625-83b729a68ece.png)
![X](https://user-images.githubusercontent.com/70633080/110917308-1efc9900-835d-11eb-86e6-5525cbc6834c.png)

![O](https://user-images.githubusercontent.com/70633080/110917375-2fad0f00-835d-11eb-9c09-d1e8bb8c84c8.png)
![X](https://user-images.githubusercontent.com/70633080/110917382-3176d280-835d-11eb-9dba-23353c0694f8.png)

</div>
</details>

</div>
</details>

<details>
<summary>4. 이승건(SPO2)(자세히)</summary>

|기기|filtering O|filtering X|
|------|---|---|
|P400|7|**10**|
|SPO2|8|9|
|soeui|7|**10**|

![O](https://user-images.githubusercontent.com/70633080/110917963-e1e4d680-835d-11eb-92cf-44a09101ead0.png)
![X](https://user-images.githubusercontent.com/70633080/110917979-e6a98a80-835d-11eb-8d7e-b884ef630fdb.png)

![O](https://user-images.githubusercontent.com/70633080/110918020-f45f1000-835d-11eb-8d6a-73b13455f713.png)
![X](https://user-images.githubusercontent.com/70633080/110918023-f5903d00-835d-11eb-846c-80f1e42da5db.png)

![O](https://user-images.githubusercontent.com/70633080/110918045-fde87800-835d-11eb-91a2-796b38475bdb.png)
![X](https://user-images.githubusercontent.com/70633080/110918050-ffb23b80-835d-11eb-875e-52a3fda4e257.png)


</div>
</details>

<details>
<summary>5. 목지원(P400)(자세히)</summary>

|기기|filtering O|filtering X|
|------|---|---|
|P400|6|6|
|SPO2|8|8|
|soeui|**9**|8|

![O](https://user-images.githubusercontent.com/70633080/110918535-a0a0f680-835e-11eb-8248-0c834ee96641.png)
![X](https://user-images.githubusercontent.com/70633080/110918550-a26aba00-835e-11eb-80d9-c2fe6a337b8e.png)

![O](https://user-images.githubusercontent.com/70633080/110918689-ca5a1d80-835e-11eb-84cb-c430baaf954f.png)
![X](https://user-images.githubusercontent.com/70633080/110918697-cc23e100-835e-11eb-8817-8248843cebaa.png)

![O](https://user-images.githubusercontent.com/70633080/110918830-f07fbd80-835e-11eb-83e8-81d0b415e171.png)
![X](https://user-images.githubusercontent.com/70633080/110918839-f2e21780-835e-11eb-91e2-830fc1e3a437.png)

</div>
</details>

<details>
<summary>6. 한나연(spo2)(자세히)</summary>

|기기|filtering O|filtering X|
|------|---|---|
|P400|6|6|
|SPO2|**9**|8|
|soeui|8|6|

![O](https://user-images.githubusercontent.com/70633080/110919068-2fae0e80-835f-11eb-855d-d3fefbe1cf79.png)
![X](https://user-images.githubusercontent.com/70633080/110919081-33419580-835f-11eb-8889-a9ce2bf26724.png)

![O](https://user-images.githubusercontent.com/70633080/110919165-4b191980-835f-11eb-9e73-5a7054b7c990.png)
![X](https://user-images.githubusercontent.com/70633080/110919169-4ce2dd00-835f-11eb-8c29-2d959b597f5e.png)

![O](https://user-images.githubusercontent.com/70633080/110919337-7c91e500-835f-11eb-962c-a0705c4f518f.png)
![X](https://user-images.githubusercontent.com/70633080/110919347-7e5ba880-835f-11eb-9fa3-d2b10044e3fa.png)

</div>
</details>


<details>
<summary>11. 성시원(spo2)(자세히)</summary>



</div>
</details>

<details>
<summary>12. 장우혁(P400)(자세히)</summary>



</div>
</details>

<details>
<summary>13. 이미경(P400)(자세히)</summary>



</div>
</details>

<details>
<summary>14. 황현상(P400)(자세히)</summary>



</div>
</details>

<details>
<summary>15. 이건영(P400)(자세히)</summary>



</div>
</details>

<details>
<summary>16. 진경원(P400)(자세히)</summary>



</div>
</details>

<details>
<summary>17. 서건하(P400)(자세히)</summary>



</div>
</details>

#### rppg filtering 과정 전
- PPI비교
  - 잘 나온 예시\
  ![image](https://user-images.githubusercontent.com/70633080/110275093-b7b8af00-8013-11eb-9d54-3d2bd271d1d6.png)
  ![image](https://user-images.githubusercontent.com/70633080/110275100-c010ea00-8013-11eb-8ec6-e5f1f7e42964.png)
  - 잘못나온 예시\
  ![image](https://user-images.githubusercontent.com/70633080/110275053-a40d4880-8013-11eb-89ee-84269ad57e57.png)
  ![image](https://user-images.githubusercontent.com/70633080/110275066-aa9bc000-8013-11eb-8ea5-0c6db012df2a.png)
#### rppg filtering 과정 후 
- PPI
  - (왼: before -> 오: after)\
  ![image](https://user-images.githubusercontent.com/70633080/110288542-864bdd80-802b-11eb-941d-244746171e75.png)
  ![image](https://user-images.githubusercontent.com/70633080/110288548-88ae3780-802b-11eb-9607-f2873b69fabd.png)
  ![before](https://user-images.githubusercontent.com/70633080/110287619-2d2f7a00-802a-11eb-850d-e74af12a3152.png)
  ![after](https://user-images.githubusercontent.com/70633080/110287462-ea6da200-8029-11eb-9626-97bc6a8326e9.png)
  ![image](https://user-images.githubusercontent.com/70633080/110290153-c613c480-802d-11eb-9c8c-672457252155.png)
  ![image](https://user-images.githubusercontent.com/70633080/110290156-c90eb500-802d-11eb-89dd-f15c6dcecb85.png)
- PPI 그래프는 향상됨을 볼 수 있음
- 그러나 hrv feature graph에서는 성능이 좋아지거나 안좋아지거나 비슷하거나 하는 다양한 경우가 발생
- 하나 안하나 거기서 거기,,?

###  With or Without Normalization

|기기|Norm O|Norm X|
|------|---|---|
|SPO2(filtering)|||


<details>
<summary>11. 성시원(spo2)(자세히)</summary>



</div>
</details>
