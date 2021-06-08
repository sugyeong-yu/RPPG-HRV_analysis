from utils import *
import os
import glob
import heartpy as hp
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import signal
import csv
import math
from hrvanalysis import get_frequency_domain_features
from utils import *
import pandas as pd
import sys
import natsort



# rppg데이터를 받아 전처리과정을 처리한 후 csv파일로 합친다.
# rppg의 경우 sr이 가변성을 가지기 때문에 sr별로 자른 데이터를 time축으로 변환 후 csv로 concat

def rppg_processing(path,subject:int):

    #경로 편집
    paths=glob.glob(os.path.join(path+str(subject), "*.csv")) # subject의 모든 csv파일 불러오기
    file_paths = natsort.natsorted(paths,reverse=False) # 0~661순으로 정렬

    for file_path in file_paths:
        print("file : ",file_path)
        order =int( file_path.split("\\")[-1].split("_")[1][:-4]) # 몇번째 그룹인지 0~661

        # pandas로 csv파일을 읽어옴
        rppg=pd.read_csv(file_path,header=None)
        sr = rppg.iloc[3][1] # sr 값 중 하나만 불러오기.
        rppg=rppg.iloc[0] # 0: hr, 1: time-stamp
        rppg=np.array(rppg).astype(np.float64)

        # bandpass filtering
        filtering_ppg=preprocessing(rppg,2.0,0.5,sr=sr)
        # plt.plot(filtering_ppg)
        # plt.show()

        # normalization
        norm_ppg=normalization(filtering_ppg)
        time = np.linspace(order, (len(norm_ppg) / sr)+order, len(norm_ppg) ) #len(norm_ppg) / sr > 몇 초까지 (start,stop,num)
        if order == 0:
            all_times=time
        else :
            all_times=np.concatenate((all_times,time),axis=None)

    print("all ~~ time !! :", all_times)
    return all_times,norm_ppg

def cppg_processing(path,subject)
    paths= glob.glob(os.path.join(path , "cppg"+str(subject)+".csv"))
    file_paths = natsort.natsorted(paths, reverse=False)  # 0~13순으로 정렬

    for file_path in file_paths:
        sr=255
        cppg=pd.read_csv(file_path,header=None)
        cppg=cppg.iloc[0]
        cppg = np.array(cppg).astype(np.float64)
        filtering_ppg = preprocessing(cppg, 2.0, 0.5, sr=sr)
        norm_ppg = normalization(filtering_ppg)
        time = np.linspace(0, (len(norm_ppg) / sr) , len(norm_ppg))
    return time,norm_ppg


if __name__ == "__main__":
    path="D:\prlab\ysg\\rppg\\rppg_HRV\data\ppg_data\\rppg(var_sr)\\before\\" # "D:\\prlab\\ysg\\rppg\\rppg_HRV\\data\\ppg_data\\cppg(soeui)"
    savePath="D:\prlab\ysg\\rppg\\rppg_HRV\data\ppg_data\\rppg(var_sr)\\after\\" # "D:\\prlab\\ysg\\rppg\\rppg_HRV\\data\\ppg_data\\cppg(soeui)\\after"
    label = path.split("\\")[-2][:4] # rppg or cppg
    if label=="rppg":
        for i in range(1,13):
            all_times,norm_ppg=rppg_processing(path,i+1)


    else :
        for i in range(1,13):
            all_times,norm_ppg=cppg_processing(path,i+1)

    # csv 저장
    f = open(savePath + label + str(i + 1) + ".csv", 'w', newline='')
    wr = csv.writer(f)

    wr.writerow(norm_ppg)
    wr.writerow(all_times)
    f.close()