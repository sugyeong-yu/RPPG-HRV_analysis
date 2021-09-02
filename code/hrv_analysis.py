from utils import *
import os
import heartpy as hp
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import signal
import csv
import math
from hrvanalysis import get_frequency_domain_features, get_time_domain_features
from utils import *
import pandas as pd
import sys
from scipy.interpolate import interp1d
import matplotlib as mlp
import time
from scipy.stats import zscore

def hrv_analysis(signal,sr,distance,th,rppg,windowsize):
    ppg_sig_=np.array(signal['ppg'],dtype='float32')
    ppg_time_= np.array(signal['time'],dtype='float32')
    # ================= preprocessing===================
    # 1. interpolation
    if rppg:
        print("interpolation")
        ppg_time = np.linspace(ppg_time_[0], ppg_time_[-1], 76500) # interpolation된 x
        i = interp1d(ppg_time_, ppg_sig_, kind='quadratic')
        ppg_sig = i(ppg_time) # interpolation된 y
        sr=255
    else :
        ppg_sig=ppg_sig_
        ppg_time=ppg_time_
    # 2. bandpass filtering
    filtered = preprocessing(ppg_sig, 2.0, 0.5, sr)
    # plt.figure(figsize=(20,7))
    # plt.plot(ppg_time,filtered)
    # plt.xlim([150000,200000])
    # plt.show()
    peaks_y, peaks_x = detect_peak(ppg_time, filtered, distance)

    # 3. extract PPI
    ppg_ppi = np.diff(peaks_x)
    # nni = ppg_ppi.copy()
    # nni[np.abs(zscore(ppg_ppi)) > th] = np.median(nni)
    nni=local_NNI(windowsize,th,peaks_x[1:],ppg_ppi)
    # ================ hrv analysis ======================
    #hrv_feature = get_frequency_domain_features(nni)  # rppg_ppi r_nni
    hrv_feature=get_time_domain_features(nni)
    return hrv_feature

if __name__ == "__main__":
    start_time=time.time()
    ppg_name='rppg'
    sr=30# 30
    distance=100#100
    window=300000
    th=2
    subject=7
    for num in range(11):
        path="D:\prlab\ysg\\rppg\RPPG-HRV_analysis\\data\\"+ppg_name+"\\shift\\%d\\"%(subject)+ppg_name+"%d_%d.csv"%(subject,num)
        print(path)
        ppg = pd.read_csv(path,header=None)
        ppg=ppg.transpose()
        ppg.columns = ['ppg', 'time', 'group']
        #ppg.columns=['ppg','realtime','time']
        hrv_feature=hrv_analysis(ppg,sr,distance,th,True,window)

        save_path = "D:\\prlab\\ysg\\rppg\\RPPG-HRV_analysis\\%d.csv" % subject
        with open(save_path, 'a', newline='') as f:
            wr = csv.writer(f)
            if num == 0:
                # 처음만 csv에 key 저장
                wr.writerow(hrv_feature.keys())
            wr.writerow(hrv_feature.values())
            f.close()

        stop_time=time.time()
        print(hrv_feature)
    #print("5분 데이터 1개 실행시간 : ",stop_time-start_time)


