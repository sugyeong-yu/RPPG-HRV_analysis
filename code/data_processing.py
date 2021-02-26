def Data_processing(c, path, sr):
    ppg_path = path
    ppg_list = os.listdir(ppg_path)
    print("file_list : ", ppg_list)

    for i in range(len(ppg_list)):
        # path 설정
        ppg_path_ = ppg_path + '\\' + ppg_list[i]

        # ppg
        print(" file name : ", ppg_list[i])
        print(ppg_path_)

        ppg_data = load_data(ppg_path_)
        ppg_data = np.array(ppg_data)
        print(len(ppg_data))
        cut_ppg = ppg_data[sr * 60:sr * 660 + 1]  # 앞에 1분 짜르기, 12000~132001 > 120001개 데이터    900~19801 > 18001개데이터
        print(len(cut_ppg))
        # 5분크기로 30초씩 sift해서 데이터 늘리기
        t1 = 0
        t2 = sr * 300  # 5분 -> 300초
        for j in range(len(cut_ppg)):
            new_ppg = ppg_data[t1:t2]
            f = open(
                'E:\\prlab\\ysg\\rppg\\rppg_HRV\\data\\ppg_signal\\cut_' + c + '\\' + str(ppg_list[i][:5]) + '_' + str(
                    j) + '.csv', 'w', newline='')
            wr = csv.writer(f)
            wr.writerow(new_ppg)
            f.close()
            t1 = t1 + (30 * sr)
            t2 = t2 + (30 * sr)
            if t2 > len(cut_ppg):
                break;
            print('slicing ppg 저장: ', str(i) + '_' + str(j))


#
# path="E:\\prlab\\ysg\\rppg\\rppg_HRV\\data\\ppg_signal\\new_cppg"
# # path="E:\\prlab\\ysg\\rppg\\rppg_HRV\\data\\ppg_signal\\new_rppg"
# Data_processing("cppg",path,sr)