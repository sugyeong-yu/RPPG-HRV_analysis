import os
import heartpy as hp
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import signal
import csv
import math
from hrvanalysis import get_frequency_domain_features
from sklearn.preprocessing import MinMaxScaler



# csv파일 불러와서 ppg_data로 반환
def load_data(path):

    f = open(path, 'r', encoding='utf-8-sig')
    rdr = csv.reader(f)
    ppg_data=[]
    for line in rdr:
        ppg_data.extend(line)
    f.close()
    return ppg_data

def normalization(ppg_data):
    ppg_data=np.array(ppg_data)
    # MinMaxScaler객체 생성
    scaler = MinMaxScaler()
    # MinMaxScaler 로 데이터 셋 변환. fit() 과 transform() 호출.
    scaler.fit(ppg_data.reshape(len(ppg_data),1))
    ppg_scaled = scaler.transform(ppg_data.reshape(len(ppg_data),1))
    #print(type(ppg_scaled))
    #print(ppg_scaled.shape) > len(ppg_data),1
#     plt.plot(ppg_scaled)
#     plt.show()
    return ppg_scaled.reshape(len(ppg_data))

# peak 찾는 함수(amplitude)
def detect_peak(ppg_time,ppg_data,distance):
    point = scipy.signal.find_peaks(ppg_data, distance=distance)
    peak = np.zeros(len(point[0]))
    peak_x = np.zeros(len(point[0]))
    for i in range(len(point[0])):
        peak_x[i] = ppg_time[point[0][i]]
        peak[i] = (ppg_data[point[0][i]])
# peak = peak 값 (y축값), point[0] = peak의 x위치
    return peak, peak_x


# time은 sec
def Totimedomain(time, peaks_x):
    # peak->timedomain
    time_peaks_x = np.zeros_like(peaks_x, dtype=float)
    for i in range(len(peaks_x)):
        time_peaks_x[i] = time[peaks_x[i]]

    return time_peaks_x


def preprocessing(ppg_data, cut_l, cut_h, sr):
    filtered = hp.filter_signal(ppg_data, cutoff=cut_l, sample_rate=sr, order=3, filtertype='lowpass')
    filtered = hp.filter_signal(filtered, cutoff=cut_h, sample_rate=sr, order=3, filtertype='highpass')
    return filtered


def FIR_filter(data, sr, taps, cutoff, pass_zero):
    x = [0 for _ in range(taps)]
    f_data = []

    # 필터 계수
    h = signal.firwin(taps, cutoff=cutoff, pass_zero=pass_zero, fs=sr)
    for n in range(len(data)):
        for k in range(taps - 1, 0, -1):
            x[k] = x[k - 1]

        new_input = int(data[n])
        x[0] = new_input

        out_value = 0

        for k in range(taps):
            out_value = out_value + (h[k] * x[k])

        f_data.insert(n, out_value)
    return f_data

## R-R interval구하기
def length(x1,x2):
    return x2-x1

def cal_ppi(peak_x):
    ppi=np.zeros(len(peak_x)-1)
    ppi_x=np.zeros(len(peak_x)-1)
    for i in range (len(peak_x)-1):
        peak_dist= length(peak_x[i],peak_x[i+1]) #x축사이의 거리만 (시간차 를 보는 것)
        ppi[i]=peak_dist
        ppi_x[i]= peak_x[i]
    #print(hrv)
    return ppi,ppi_x