import os
import sys

import heartpy as hp
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import scipy
from scipy import signal
import csv
import math
from hrvanalysis import get_frequency_domain_features
from hrvanalysis import plot_psd
import seaborn as sns
from utils import *

# matplotlib.use('Qt5Agg')

def hrv_analysis(cpath,rpath,save_path,c_sr,r_sr):

    #j=5 # 1~17 ( 5번부터가 새로운데이터) / 1~13
    # path 설정
    cppg_path = cpath

    rppg_path = rpath


    print("=======================================START CPPG============================================")
    #cppg

    sr= c_sr # 200, 60
    c_distance=12
    print(" cppg file name : ", cppg_path)
    ppg_data=load_data(cppg_path)
    #print(ppg_data)
    ppg_data=np.array(ppg_data) # list를 numpy array로
    #cut_ppg=ppg_data[sr*30:sr*630]
    ppg_data=ppg_data.astype(np.float64)
    #print("cutting ppg: ",len(cut_ppg)) # cppg1: 120000 / cppg2: 36000
    print('ppg_length: ',len(ppg_data))

    plt.plot(ppg_data,label="cutting_ppg")
    plt.xlim([0, 3000])
    plt.show()

    # 주파수스펙트럼 시각화.
    f, psd = scipy.signal.periodogram(ppg_data, fs=sr, window='hann')

    plt.plot(f, psd, 'k', linewidth=2,label="frequency_spectrum")
    plt.xlim([0, 4])
    plt.show()

    filtered=preprocessing(ppg_data,2.0,0.5,sr) # FIR_filter(ppg_data,sr,40,0.032,True)

    ppg_scaled=normalization(filtered)
    #ppg_scaled=filtered

    peaks_y,peaks_x= detect_peak(ppg_scaled,c_distance)
    print("-------------------timedomain and find feak-------------------")
    time,ctime_peaks_x=Totimedomain(ppg_scaled,sr,peaks_x,peaks_y)

    time=time*1000
    ctime_peaks_x=ctime_peaks_x*1000

    print("total time(sec): ",time[-1])

    # 시각화 (peak와 wave)
    plt.scatter(ctime_peaks_x, peaks_y)
    plt.plot(time,ppg_scaled, label="find feak in time domain")
    plt.xlim([0, 10000])
    plt.xlabel('time')
    plt.ylabel('signal')
    plt.show()
    #print("------------------------------------------------")
    print("peaks_x: ", ctime_peaks_x)

    cppg_ppi,cppg_ppi_x=cal_ppi(ctime_peaks_x)
    print("cppg_ppi shape: ", len(cppg_ppi))
    print("cppg_ppi : ", cppg_ppi)
    plt.plot(cppg_ppi, label="cppg ppi")
    plt.xlim([0, 100])
    plt.show()

    print("=========================================finish===============================================")

    print("======================================START RPPG==============================================")
    # rppg
    print(" rppg file name : ", rppg_path)

    sr=r_sr
    r_distance=15

    ppg_data=load_data(rppg_path)
    #print(ppg_data)
    ppg_data=np.array(ppg_data) # list를 numpy array로
    #cut_ppg=ppg_data[sr*30:sr*630] # 18000개
    ppg_data=ppg_data.astype(np.float64)
    #print("cutting ppg: ",len(cut_ppg))
    print("ppg_length: ", len(ppg_data))

    plt.plot(ppg_data,label="after cutting")
    plt.xlim([0, 300])
    plt.show()

    # 주파수스펙트럼 시각화.
    f, psd = scipy.signal.periodogram(ppg_data, fs=sr, window='hann')

    plt.plot(f, psd, 'k', linewidth=2, label="frequency_spectrum")
    plt.xlim([0, 4])
    plt.show()

    ppg_data = preprocessing(ppg_data, 2.0, 0.5, sr) # FIR_filter(ppg_data,sr,20,0.032,True)


    ppg_scaled=normalization(ppg_data)
    #ppg_scaled=ppg_data

    peaks_y,peaks_x= detect_peak(ppg_scaled,r_distance)
    print("-------------------timedomain and find feak-------------------")
    time,rtime_peaks_x=Totimedomain(ppg_scaled,sr,peaks_x,peaks_y)

    time=time*1000
    rtime_peaks_x=rtime_peaks_x*1000
    print("total time: ", time[-1])


    # 시각화 (peak와 wave)
    plt.scatter(rtime_peaks_x, peaks_y)
    plt.plot(time,ppg_scaled)
    plt.xlim([0, 10000])
    plt.xlabel('time')
    plt.ylabel('signal')
    plt.show()
    #print("------------------------------------------------")
    print("peaks_x: ",rtime_peaks_x)

    rppg_ppi,rppg_ppi_x=cal_ppi(rtime_peaks_x)
    print("rppg_ppi shape: ",len(rppg_ppi))
    print(len(rppg_ppi_x))
    print("rppg_ppi: ",rppg_ppi)

    plt.plot(rppg_ppi)
    plt.xlim([0, 100])
    plt.show()


    #
    # hrv분석
    cppg_frequency_features = get_frequency_domain_features(cppg_ppi)
    rppg_frequency_features = get_frequency_domain_features(rppg_ppi)
    #
    #
    # ppi 비교
    # ppi 시각화

    plot_psd(cppg_ppi, method="welch")
    plot_psd(rppg_ppi, method="welch")

    plt.scatter(rppg_ppi_x,rppg_ppi)
    plt.scatter(cppg_ppi_x,cppg_ppi)
    plt.xlim(0,50)
    plt.show()
    #
    # if len(cppg_ppi)>len(rppg_ppi):
    #     cppg_ppi=cppg_ppi[:len(rppg_ppi)]
    # elif len(cppg_ppi)<len(rppg_ppi):
    #     rppg_ppi=rppg_ppi[:len(cppg_ppi)]


    return cppg_frequency_features, rppg_frequency_features


if __name__ == "__main__":
    # save path, ppg path, sr 설정확인할것
    save_path="D:\prlab\ysg\\rppg\\rppg_HRV\data\\new_data\\"

    #for i in range(13):
    i = 3 # p400: 0~16  / spo2,soeui: 0~12
    cf = open(save_path + str(i + 1) + "_cppg.csv", 'w', newline='')
    cwr = csv.writer(cf)
    rf = open(save_path + str(i + 1) + "_rppg.csv", 'w', newline='')
    rwr = csv.writer(rf)

    for j in range(11):
        print("J: ", j)
        cppg_path="D:\prlab\ysg\\rppg\\rppg_HRV\data\ppg_signal\\3-1.cut_cppg(soeui)"+"\\cppg"+str(i+1)+"_"+str(j)+".csv"
        rppg_path="D:\prlab\ysg\\rppg\\rppg_HRV\data\ppg_signal\\2-1.cut_rppg(spo2)"+"\\rppg"+str(i+1)+"_"+str(j)+".csv"

        if os.path.isfile(cppg_path) == False or os.path.isfile(rppg_path) == False:
            print("!!!!!error!!!!!")
            continue

        c_sr=255 # 200, 60, 255
        r_sr=30

        # hrv 분석
        cppg_frequency_features, rppg_frequency_features = hrv_analysis(cppg_path, rppg_path, save_path, c_sr, r_sr)
        # if ((i+1) == 6 or (i+1) ==8 or (i+1) ==10 or (i+1) ==11):
        #     c_sr=60
        #     r_sr=30
        # else:
        #     c_sr=200
        #     r_sr=30



        #  csv로 결과 저장
        cppg_frequency_features['num'] = str(i+1) + "_" + str(j)
        rppg_frequency_features['num'] = str(i+1) + "_" + str(j)

        if j==0:
            # 처음만 csv에 key 저장
            cwr.writerow(cppg_frequency_features.keys())
            rwr.writerow(rppg_frequency_features.keys())
        cwr.writerow(cppg_frequency_features.values())
        rwr.writerow(rppg_frequency_features.values())

    cf.close()
    rf.close()


# # 개별실행
#
# if __name__ == "__main__":
#     i=5
#     j=0
#
#     save_path ="E:\prlab\ysg\\rppg\\rppg_HRV\data\hrv_features\\4.shift(rppg_filtering)" + "\\" + str(i) + "_" + str(j) +'.csv'
#     cppg_path="E:\prlab\ysg\\rppg\\rppg_HRV\data\ppg_signal\\2-1.cut_cppg(p400+spo2)"+"\\cppg"+str(i)+"_"+str(j)+".csv"
#     rppg_path="E:\prlab\ysg\\rppg\\rppg_HRV\data\ppg_signal\\2-1.cut_rppg(p400+spo2)"+"\\rppg"+str(i)+"_"+str(j)+".csv"
#
#     if os.path.isfile(cppg_path) == False or os.path.isfile(rppg_path) == False :
#         sys.exit()
#
#     # p400 + spo2인 경우
#     if ((i) == 6 or (i) ==8 or (i) ==10 or (i) ==11):
#         c_sr=60
#         r_sr=30
#     else:
#         c_sr=200
#         r_sr=30
#     print("a")
#     # hrv 분석
#     cppg_frequency_features,rppg_frequency_features=hrv_analysis(cppg_path,rppg_path,save_path,c_sr,r_sr)
#
#     #  csv로 결과 저장
#     # 1. cppg
#     cppg_frequency_features['num'] = str(i)+"_"+str(j)
#     rppg_frequency_features['num'] = str(i)+"_"+str(j)
#     cf = open(save_path, 'w', newline='')
#     cwr = csv.writer(cf)
#     cwr.writerow(cppg_frequency_features.keys())
#     cwr.writerow(cppg_frequency_features.values())
#     cf.close()
#
#     rf = open(save_path, 'w', newline='')
#     rwr = csv.writer(rf)
#     rwr.writerow(rppg_frequency_features.keys())
#     rwr.writerow(rppg_frequency_features.values())
#     rf.close()