import os
from utils import *
# data shift
def Data_processing(c, path, sr):
    ppg_path = path
    ppg_list = os.listdir(ppg_path)
    print("file_list : ", ppg_list)

    for i in range(len(ppg_list)):
        # path 설정
        ppg_path_ = ppg_path + '\\' + ppg_list[i]

        # ppg
        print(" file name : ", ppg_list[i])
        #print(ppg_path_)

        ppg_data = load_data(ppg_path_)
        ppg_data = np.array(ppg_data)
        print("before: ", len(ppg_data))
        #         if(len(ppg_data)< (630*sr)) : # 만약 데이터가 10분30초보다 적다면
        #             cut_ppg=ppg_data[-18000:] # 뒤에서부터 18000개 가져오기
        #         else:
        cut_ppg = ppg_data[sr * 30:sr * 630]  # 앞에 30초 부터 10분 자르기, 12000~132001 > 120000개 데이터    900~19801 > 18000개데이터
        print("after: ", len(cut_ppg))
        # 5분크기로 30초씩 sift해서 데이터 늘리기
        t1 = 0
        t2 = sr * 300  # 5분 -> 300초
        #len(cut_ppg)
        # for j in range(len(cut_ppg)):
        #     new_ppg=ppg_data[t1:t2]
        #     f = open('E:\\prlab\\ysg\\rppg\\rppg_HRV\\data\\ppg_signal\\cut_'+c+'\\'+str(ppg_list[i][:-4])+'_'+str(j)+'.csv','w', newline='')
        #
        #     wr = csv.writer(f)
        #     wr.writerow(new_ppg)
        #     f.close()
        #     print(len(new_ppg))
        #     t1 = t1+(30*sr)
        #     t2 = t2+(30*sr)
        #     print(t1, t2)
        #     if t2>len(cut_ppg) :
        #         break;
        #     print('slicing ppg 저장: ', str(i)+'_'+str(j))

# p400만
#path = "E:\\prlab\\ysg\\rppg\\rppg_HRV\\data\\ppg_signal\\cppg(p400)" # 200
#path="E:\\prlab\\ysg\\rppg\\rppg_HRV\\data\\ppg_signal\\rppg(p400)" #30

# spo2만
#path = "E:\\prlab\\ysg\\rppg\\rppg_HRV\\data\\ppg_signal\\cppg(spo2)" #60
path="E:\\prlab\\ysg\\rppg\\rppg_HRV\\data\\ppg_signal\\3.rppg(spo2)" #30

# p400+spo2
#path = "E:\\prlab\\ysg\\rppg\\rppg_HRV\\data\\ppg_signal\\cppg(p400+spo2)" # 200
#path="E:\\prlab\\ysg\\rppg\\rppg_HRV\\data\\ppg_signal\\rppg(p400+spo2)" #30
Data_processing("rppg(spo2)", path, 30)