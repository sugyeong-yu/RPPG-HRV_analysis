from utils import *
import os
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
from scipy.interpolate import interp1d
import matplotlib as mlp
import time


# 그래프 확인하기
subject=11
num=10

cppg_frequency_features=[]
rppg_frequency_features=[]

def hrv_analysis(signal,sr=30,distance=100):
    rppg_sig_=np.array(signal['rppg'],dtype='float32')
    rppg_time_= np.array(signal['time'],dtype='float32')
    # ================= preprocessing===================
    # 1. interpolation
    rppg_time = np.linspace(rppg_time_[0], rppg_time_[-1], len(rppg_time_)*8) # interpolation된 x
    i = interp1d(rppg_time_, rppg_sig_, kind='quadratic')
    rppg_sig = i(rppg_time) # interpolation된 y
    # 2. bandpass filtering
    filterd = preprocessing(rppg_sig, 2.0, 0.5, sr)
    r_peaks_y, r_peaks_x = detect_peak(rppg_time, filterd, distance)

    # 3. extract PPI
    rppg_ppi = np.diff(r_peaks_x)

    # ================ hrv analysis ======================
    hrv_feature = get_frequency_domain_features(rppg_ppi)  # rppg_ppi r_nni
    return hrv_feature

if __name__ == "__main__":
    start_time=time.time()
    subject=0
    num=0
    path="D:\prlab\ysg\\rppg\RPPG-HRV_analysis\\data\\rppg\\shift\\%d\\rppg%d_%d.csv"%(subject,subject,num)
    rppg = pd.read_csv(path,header=None)
    rppg=rppg.loc[:,0:150]
    rppg=rppg.transpose()
    rppg.columns=['rppg','time','group']
    hrv_feature=hrv_analysis(rppg)
    stop_time=time.time()
    print(hrv_feature)
    print("5분 데이터 1개 실행시간 : ",stop_time-start_time)


