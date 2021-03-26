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
  - cppg와 rppg의 시간 맞춰주기
2. 신호 전처리
  - bandfass filtering
  - normalization(0~1)
3. Peak detection
4. rr interval 계산
5. hrv feature extract


### 1. pyserial
- serial port connection을 도와주는 모듈 
- python으로 usb직렬포트에 연결된 장치를 동작시킬 수 있도록 한다.
