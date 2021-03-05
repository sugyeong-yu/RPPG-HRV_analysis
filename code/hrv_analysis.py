import os
import sys

import heartpy as hp
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import signal
import csv
import math
from hrvanalysis import get_frequency_domain_features
from utils import *


def hrv_analysis(cpath,rpath,save_path,c_sr,r_sr):

    #j=5 # 1~17 ( 5번부터가 새로운데이터) / 1~13
    # path 설정
    cppg_path= cpath

    rppg_path=rpath


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

    filtered= preprocessing(ppg_data,2.0,0.5,sr) #FIR_filter(ppg_data,200,40,0.032,True)

    ppg_scaled=normalization(filtered)
    plt.plot(ppg_scaled,label="after filtering and norm")
    plt.xlim([0, 3000])
    plt.show()

    peaks_y,peaks_x= detect_peak(ppg_scaled,c_distance)
    print("-------------------timedomain and find feak-------------------")
    time,time_peaks_x=Totimedomain(ppg_scaled,sr,peaks_x,peaks_y)

    print("total time(sec): ",time[-1])

    # 시각화 (peak와 wave)
    plt.scatter(time_peaks_x, peaks_y)
    plt.plot(time,ppg_scaled, label="find feak in time domain")
    plt.xlim([200, 210])
    plt.xlabel('time')
    plt.ylabel('signal')
    plt.show()
    #print("------------------------------------------------")


    cppg_ppi=cal_ppi(time_peaks_x)
    print("cppg_ppi shape: ", len(cppg_ppi))

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

    ppg_scaled=normalization(ppg_data)
    # plt.plot(ppg_scaled,label="after filtering and norm")
    # plt.xlim([0, 300])
    # plt.show()

    peaks_y,peaks_x= detect_peak(ppg_scaled,r_distance)
    print("-------------------timedomain and find feak-------------------")
    time,time_peaks_x=Totimedomain(ppg_scaled,sr,peaks_x,peaks_y)

    print("total time: ", time[-1])


    # 시각화 (peak와 wave)
    plt.scatter(time_peaks_x, peaks_y)
    plt.plot(time,ppg_scaled)
    plt.xlim([200, 210])
    plt.xlabel('time')
    plt.ylabel('signal')
    plt.show()
    #print("------------------------------------------------")
    rppg_ppi=cal_ppi(time_peaks_x)
    print("rppg_ppi shape: ",len(rppg_ppi))




    # ppi 비교
    # ppi 시각화
    if len(cppg_ppi)>len(rppg_ppi):
        cppg_ppi=cppg_ppi[:len(rppg_ppi)]
    elif len(cppg_ppi)<len(rppg_ppi):
        rppg_ppi=rppg_ppi[:len(cppg_ppi)]
    plt.scatter(rppg_ppi,cppg_ppi)
    plt.plot([0.25,1.5],[0.25,1.5],color='red',linestyle='--')
    plt.show()



    # hrv분석
    cppg_frequency_features = get_frequency_domain_features(cppg_ppi)
    rppg_frequency_features = get_frequency_domain_features(rppg_ppi)

    return cppg_frequency_features, rppg_frequency_features


if __name__ == "__main__":
    for i in range(17):
        for j in range(11):
            save_path ="E:\prlab\ysg\\rppg\\rppg_HRV\data\hrv_features\\final" + "\\" + str(i+1) + "_" + str(j) +'.csv'
            cppg_path="E:\prlab\ysg\\rppg\\rppg_HRV\data\ppg_signal\cut_cppg"+"\\cppg"+str(i+1)+"_"+str(j)+".csv"
            rppg_path="E:\prlab\ysg\\rppg\\rppg_HRV\data\ppg_signal\cut_rppg"+"\\rppg"+str(i+1)+"_"+str(j)+".csv"

            if os.path.isfile(cppg_path) == False or os.path.isfile(rppg_path) == False:
                continue

            if ((i+1) == 6 or (i+1) ==8 or (i+1) ==10 or (i+1) ==11):
                c_sr=60
                r_sr=30
            else:
                c_sr=200
                r_sr=30

            # hrv 분석
            cppg_frequency_features,rppg_frequency_features=hrv_analysis(cppg_path,rppg_path,save_path,c_sr,r_sr)

            #  csv로 결과 저장
            # 1. cppg
            cppg_frequency_features['num'] = str(i + 1)+"_"+str(j)
            rppg_frequency_features['num'] = str(i + 1)+"_"+str(j)
            f = open(save_path, 'w', newline='')
            wr = csv.writer(f)
            wr.writerow(cppg_frequency_features.keys())
            wr.writerow(cppg_frequency_features.values())
            wr.writerow(rppg_frequency_features.values())
            f.close()

## 개별실행

# if __name__ == "__main__":
#     i=15
#     j=0
#
#     save_path ="E:\prlab\ysg\\rppg\\rppg_HRV\data\hrv_features\\final" + "\\" + str(i+1) + "_" + str(j) +'.csv'
#     cppg_path="E:\prlab\ysg\\rppg\\rppg_HRV\data\ppg_signal\cut_cppg"+"\\cppg"+str(i+1)+"_"+str(j)+".csv"
#     rppg_path="E:\prlab\ysg\\rppg\\rppg_HRV\data\ppg_signal\cut_rppg"+"\\rppg"+str(i+1)+"_"+str(j)+".csv"
#
#     if os.path.isfile(cppg_path) == False or os.path.isfile(rppg_path) == False :
#         sys.exit()
#
#     if ((i+1) == 6 or (i+1) ==8 or (i+1) ==10 or (i+1) ==11):
#         c_sr=60
#         r_sr=30
#     else:
#         c_sr=200
#         r_sr=30
#
#     # hrv 분석
#     cppg_frequency_features,rppg_frequency_features=hrv_analysis(cppg_path,rppg_path,save_path,c_sr,r_sr)
#
#     # #  csv로 결과 저장
#     # # 1. cppg
#     # cppg_frequency_features['num'] = str(i + 1)+"_"+str(j)
#     # rppg_frequency_features['num'] = str(i + 1)+"_"+str(j)
#     # f = open(save_path, 'w', newline='')
#     # wr = csv.writer(f)
#     # wr.writerow(cppg_frequency_features.keys())
#     # wr.writerow(cppg_frequency_features.values())
#     # wr.writerow(rppg_frequency_features.values())
#     # f.close()