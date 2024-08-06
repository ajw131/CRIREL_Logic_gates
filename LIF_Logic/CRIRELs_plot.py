import numpy as np
import pandas as pd
import h5py
import csv
import matplotlib.pyplot as plt
import cv2

def interval_logic_list(eo_list, time_stim=400, time_rest=400):
    '''
    interval_FR_time, logic_FR_time = interval_logic_list(f_df['time'], time_stim, time_rest)
    #input 
    eo_list              : array
    time_stim, time_rest : 間隔的時間 (預設400)
    
    # output
    interval_FR : 用來確認每個間隔是否相同
    logic_FR    : 用來判斷
    
    '''
    # =============== interval =============== 
    time_int = int(time_rest*0.75/10)         # interval start
    interval_FR = [ eo_list[time_int] ]
    for i in range(1, 6):                     # add rest term
        interval_FR.extend([ eo_list[time_int + (time_rest+time_stim)/10*i] ])
        
    # =============== logic ================== 
    time_log = int(time_rest/10 + time_stim*0.75/10)     # logic start
    logic_FR = [ eo_list[time_log] ]
    for i in range(1, 5):                     # add rest term
        logic_FR.extend([ eo_list[time_log + (time_rest+time_stim)/10*i] ])

    return(interval_FR, logic_FR)


def read_f_data(file_para, bias_str):
    '''
    m_df, f_df, neu_list = read_all_data(h5_path, fname, group_name, bias_str)
    路徑 檔名 組名 參數
    '''
    h5_path, fname, group_name = file_para
    
    f_h5py = h5py.File(h5_path+fname, 'r+')
    #print(list(f_h5py.keys()))
    group_para= f_h5py[group_name+"_group"]
    neu_list = list( group_para.attrs['neu_list'] )

    #m_data = np.array( group_para[bias_str+"_mem_dataset"] )
    f_data = np.array( group_para[bias_str+"_fra_dataset"] )


    #m_df = pd.DataFrame(m_data, columns = ['time']+neu_list)   # +['eo_1'] 
    f_df = pd.DataFrame(f_data, columns = ['time']+neu_list)   # +['eo_1'] 
    
    return(f_df, neu_list)

def read_all_data(file_para, bias_str):
    '''
    m_df, f_df, neu_list = read_all_data(h5_path, fname, group_name, bias_str)
    路徑 檔名 組名 參數
    '''
    h5_path, fname, group_name = file_para
    
    f_h5py = h5py.File(h5_path+fname, 'r+')
    #print(list(f_h5py.keys()))
    group_para= f_h5py[group_name+"_group"]
    neu_list = list( group_para.attrs['neu_list'] )

    m_data = np.array( group_para[bias_str+"_mem_dataset"] )
    f_data = np.array( group_para[bias_str+"_fra_dataset"] )


    m_df = pd.DataFrame(m_data, columns = ['time']+neu_list)   # +['eo_1'] 
    f_df = pd.DataFrame(f_data, columns = ['time']+neu_list)   # +['eo_1'] 
    
    return(m_df, f_df, neu_list)

def phase(file_para, bias_range, dif, Tick=False):
    
    h5_path, fname, group_name = file_para
    e_down, e_up, i_down, i_up = bias_range
    
    # score
    name_list = ["off","on","and","nand","or","nor","xor","xnor","imp","nimp", "other", "not consist"]
    score_list = [0, 62, 34, 28, 46, 16, 12, 50, 58, 4, 70, 80]
    label_list = [0,  1,  2,  3,  4,  5,  6,  7,  8, 9, 10, 11]


    x = np.arange( e_down, e_up, dif)     
    y = np.arange( i_down, i_up, dif)    
    Z = np.zeros([len(y), len(x)])


    f_h5py = h5py.File(h5_path+fname, 'r+')
    #print(list(f_h5py.keys()))
    group_para= f_h5py[group_name+"_group"]
    neu_list = list( group_para.attrs['neu_list'] )
    print(1)

    for e, e_bias in enumerate(x):
        for i, i_bias in enumerate(y):
            b_e1 = round(e_bias, 2)        # bias
            b_i1 = round(i_bias, 2)        # bias
            bias_str = "_" + str(b_e1) + "_" + str(b_i1) 
            f_df, _ = read_f_data(file_para, bias_str)             # read


            # 轉換成 truth table 和 分數
            interval_FR, logic_FR = interval_logic_list(f_df['buffer'])
            logic_score = sum( np.where(np.array(logic_FR)>0, [2,4,8,16,32], 0) )
            interval_score = sum( np.where(np.array(interval_FR)>0, [1,1,1,1,1,1], 0) ) # 有五個區間

            if interval_score>=1 and interval_score<=5: # 判斷區間是否相同
                # 1-4之間表示不是全有或全無
                logic_score = 80

            #================= classify ================= 
            n = 0
            for j, score in enumerate(score_list):
                if logic_score == score:
                    #print(name_list[i])
                    Z[i, e] = j           #要評儀
                    n+=1
            if n==0:
                Z[i, e] = 10          #沒有包含的也要等於 other 40, 10

    print('finish')

    ## plot
    FZ = 15
    fig, ax = plt.subplots(1, 2, figsize=(14,6))
    c = ax[0].pcolormesh(x, y, Z, 
                      cmap='Paired', 
                      vmin=-0.5, vmax=11.5,
                      #edgecolors='k', 
                      linewidths=0.5)

    ax[0].set_title(fname, fontsize=FZ+4)
    ax[0].set_xlabel('e_bias', fontsize=FZ)
    ax[0].set_ylabel('i_bias', fontsize=FZ)
    ax[1].set_title(fname, fontsize=FZ+4)
    ax[1].set_xlabel('e_bias', fontsize=FZ)
    ax[1].set_ylabel('i_bias', fontsize=FZ)
    
    # left
    c = ax[1].pcolormesh(x, y, Z, 
                      cmap='Paired', 
                      vmin=-0.5, vmax=11.5,
                      edgecolors='k', 
                      linewidths=0.5)
    cbar = fig.colorbar(c, ticks=label_list)
    cbar.ax.set_yticklabels(name_list)  # vertically oriented colorbar
    
    if Tick == True: # tick
        x_tick = [round(x_temp, 2) for x_temp in x]
        ax[0].set_xticks(x, x_tick)
        ax[1].set_xticks(x, x_tick)
        y_tick = [round(y_temp, 2) for y_temp in y]
        ax[0].set_yticks(y, y_tick)
        ax[1].set_xticks(x, x_tick)
    
    # lim
    ax[0].set_xlim(e_down-dif/2, e_up-dif/2)
    ax[0].set_ylim(i_down-dif/2, i_up-dif/2)
    ax[1].set_xlim(e_down-dif/2, e_up-dif/2)
    ax[1].set_ylim(i_down-dif/2, i_up-dif/2)
    plt.savefig("result/"+fname+".png")




def plot_single_FR(b_eo, f_df, fname, bias_str, tit):
    
    fig, ax = plt.subplots(4, 1, figsize=(5, 5), sharex=True)
    plt.subplots_adjust(hspace=0.2, wspace=0.2, left=0.2)

    FZ = 16
    st = fig.suptitle(tit+"\n"+fname, fontsize=FZ+4)

    
    ax[0].set_title(bias_str + "_FR", fontsize=FZ)


    ax[0].plot(f_df['time'], f_df['e1'], color='b', lw=0.5, label='e1')
    ax[0].plot(f_df['time'], f_df['i1'], color='r', lw=0.5, label='i1')
    ax[1].plot(f_df['time'], f_df['e2'], color='b', lw=0.5, label='e2')
    ax[1].plot(f_df['time'], f_df['i2'], color='r', lw=0.5, label='i2')
    ax[2].plot(f_df['time'], f_df['eo'], color='b', lw=0.5, label='eo')
    ax[2].plot(f_df['time'], f_df['buffer'], color='r', lw=0.5, label='buffer')
    
    ax[3].plot(f_df['time'], f_df['inp1'], color='g', lw=2, label='inp1')
    ax[3].plot(f_df['time'], f_df['inp2'], color='m', dashes=[6, 4], lw=2, label='inp2')
    ax[3].set_xlabel("time(s)" , fontsize=FZ)
        
    cols = ['node 1','node 2','eo', 'sti']
    for i, col in enumerate(cols):
        ax[i].set_ylabel(col , fontsize=FZ)
        
    # legend
    ax[0].legend(loc='center right', bbox_to_anchor=(1.3, 0.6))
    ax[1].legend(loc='center right', bbox_to_anchor=(1.3, 0.6))
    ax[2].legend(loc='center right', bbox_to_anchor=(1.35, 0.6))
    ax[3].legend(loc='center right', bbox_to_anchor=(1.35, 0.6))
    plt.subplots_adjust(top=0.8)
    plt.savefig("result/8logic_fr_fname/"+tit+".png", bbox_inches = 'tight')
    plt.show()
    
def plot_single_FR_nofname(b_eo, f_df, fname, bias_str, tit):
    
    fig, ax = plt.subplots(4, 1, figsize=(4, 5), sharex=True)
    plt.subplots_adjust(hspace=0.2, wspace=0.2, left=0.2)

    FZ = 16
    st = fig.suptitle(tit, fontsize=FZ+4)

    
    ax[0].set_title(bias_str + "_FR", fontsize=FZ)


    ax[0].plot(f_df['time'], f_df['e1'], color='b', lw=0.5, label='e1')
    ax[0].plot(f_df['time'], f_df['i1'], color='r', lw=0.5, label='i1')
    ax[1].plot(f_df['time'], f_df['e2'], color='b', lw=0.5, label='e2')
    ax[1].plot(f_df['time'], f_df['i2'], color='r', lw=0.5, label='i2')
    ax[2].plot(f_df['time'], f_df['eo'], color='b', lw=0.5, label='eo')
    ax[2].plot(f_df['time'], f_df['buffer'], color='r', lw=0.5, label='buffer')
    
    ax[3].plot(f_df['time'], f_df['inp1'], color='g', lw=2, label='inp1')
    ax[3].plot(f_df['time'], f_df['inp2'], color='m', dashes=[6, 4], lw=2, label='inp2')
    ax[3].set_xlabel("time(s)" , fontsize=FZ)
        
    cols = ['node 1','node 2','eo', 'sti']
    for i, col in enumerate(cols):
        ax[i].set_ylabel(col , fontsize=FZ)
        
    # legend
    ax[0].legend(loc='center right', bbox_to_anchor=(1.3, 0.6))
    ax[1].legend(loc='center right', bbox_to_anchor=(1.3, 0.6))
    ax[2].legend(loc='center right', bbox_to_anchor=(1.35, 0.6))
    ax[3].legend(loc='center right', bbox_to_anchor=(1.35, 0.6))
    plt.subplots_adjust(top=0.85)
    plt.savefig("result/8logic_fr/"+tit+".png", bbox_inches = 'tight')
    plt.show()

#plot mem fra 
def plot_single_Mem_FR(b_eo, m_df, f_df, fname, bias_str, tit):
    
    fig, ax = plt.subplots(4, 2, figsize=(8, 5), sharex=True)
    plt.subplots_adjust(hspace=0.2, wspace=0.2, left=0.2)

    FZ = 16
    st = fig.suptitle(tit+"\n"+fname, fontsize=FZ+4)

    
    ax[0][0].set_title(bias_str + "_Mem", fontsize=FZ)
    ax[0][1].set_title(bias_str + "_FR", fontsize=FZ)

    ax[0][0].plot(m_df['time'], m_df['e1'], color='b', lw=0.5)
    ax[0][0].plot(m_df['time'], m_df['i1'], color='r', lw=0.5)
    ax[1][0].plot(m_df['time'], m_df['e2'], color='b', lw=0.5)
    ax[1][0].plot(m_df['time'], m_df['i2'], color='r', lw=0.5)
    ax[2][0].plot(m_df['time'], m_df['eo'], color='b', lw=0.5)
    ax[2][0].plot(m_df['time'], m_df['buffer'], color='r', lw=0.5)

    ax[0][1].plot(f_df['time'], f_df['e1'], color='b', lw=0.5, label='e1')
    ax[0][1].plot(f_df['time'], f_df['i1'], color='r', lw=0.5, label='i1')
    ax[1][1].plot(f_df['time'], f_df['e2'], color='b', lw=0.5, label='e2')
    ax[1][1].plot(f_df['time'], f_df['i2'], color='r', lw=0.5, label='i2')
    ax[2][1].plot(f_df['time'], f_df['eo'], color='b', lw=0.5, label='eo')
    ax[2][1].plot(f_df['time'], f_df['buffer'], color='r', lw=0.5, label='buffer')
    
    for i in range(2):
        ax[3][i].plot(f_df['time'], f_df['inp1'], color='g', lw=2, label='inp1')
        ax[3][i].plot(f_df['time'], f_df['inp2'], color='m', dashes=[6, 4], lw=2, label='inp2')
        ax[3][i].set_xlabel("time(s)" , fontsize=FZ)
        
    cols = ['node 1','node 2','eo', 'sti']
    for i, col in enumerate(cols):
        ax[i][0].set_ylabel(col , fontsize=FZ)
        
    # legend
    ax[0][1].legend(loc='center right', bbox_to_anchor=(1.3, 0.6))
    ax[1][1].legend(loc='center right', bbox_to_anchor=(1.3, 0.6))
    ax[2][1].legend(loc='center right', bbox_to_anchor=(1.35, 0.6))
    ax[3][1].legend(loc='center right', bbox_to_anchor=(1.35, 0.6))
    plt.subplots_adjust(top=0.8)
    plt.savefig("result/8logic_fr_mem_fname/"+tit+".png", bbox_inches = 'tight')
    plt.show()




    
def phase_single(file_para, bias_range, dif, Tick=False):
    
    h5_path, fname, group_name = file_para
    e_down, e_up, i_down, i_up = bias_range
    
    # score
    name_list = ["off","on","and","nand","or","nor","xor","xnor","imp","nimp", "other", "not consist"]
    score_list = [0, 62, 34, 28, 46, 16, 12, 50, 58, 4, 70, 80]
    label_list = [0,  1,  2,  3,  4,  5,  6,  7,  8, 9, 10, 11]


    x = np.arange( e_down, e_up, dif)     
    y = np.arange( i_down, i_up, dif)    
    Z = np.zeros([len(y), len(x)])


    f_h5py = h5py.File(h5_path+fname, 'r')
    #print(list(f_h5py.keys()))
    group_para= f_h5py[group_name+"_group"]
    neu_list = list( group_para.attrs['neu_list'] )
    

    for e, e_bias in enumerate(x):
        for i, i_bias in enumerate(y):
            b_e1 = round(e_bias, 2)        # bias
            b_i1 = round(i_bias, 2)        # bias
            bias_str = "_" + str(b_e1) + "_" + str(b_i1) 
            _, f_df, _ = read_all_data([h5_path, fname, group_name], bias_str)


            # 轉換成 truth table 和 分數
            interval_FR, logic_FR = interval_logic_list(f_df['eo'])
            logic_score = sum( np.where(np.array(logic_FR)>0, [2,4,8,16,32], 0) )
            interval_score = sum( np.where(np.array(interval_FR)>0, [1,1,1,1,1,1], 0) ) # 有五個區間

            if interval_score>=1 and interval_score<=5: # 判斷區間是否相同
                # 1-4之間表示不是全有或全無
                logic_score = 80

            #================= classify ================= 
            n = 0
            for j, score in enumerate(score_list):
                if logic_score == score:
                    #print(name_list[i])
                    Z[i, e] = j           #要評儀
                    n+=1
            if n==0:
                Z[i, e] = 10          #沒有包含的也要等於 other 40, 10

    print('finish')

    ## plot
    FZ = 15
    fig, ax = plt.subplots(1, figsize=(7,6))
    c = ax.pcolormesh(x, y, Z, 
                      cmap='Paired', 
                      vmin=-0.5, vmax=11.5,
                      #edgecolors='k', 
                      linewidths=0.5)

    ax.set_title(group_name, fontsize=FZ)
    ax.set_xlabel('e_bias', fontsize=FZ)
    ax.set_ylabel('i_bias', fontsize=FZ)
    
    cbar = fig.colorbar(c, ticks=label_list)
    cbar.ax.set_yticklabels(name_list)  # vertically oriented colorbar
    
    if Tick == True: # tick
        x_tick = [round(x_temp, 2) for x_temp in x]
        ax.set_xticks(x, x_tick)
        y_tick = [round(y_temp, 2) for y_temp in y]
        ax.set_yticks(y, y_tick)
    
    # lim
    ax.set_xlim(e_down-dif/2, e_up-dif/2)
    ax.set_ylim(i_down-dif/2, i_up-dif/2)

