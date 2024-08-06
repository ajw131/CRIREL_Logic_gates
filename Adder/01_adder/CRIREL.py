import numpy as np
import pandas as pd
import h5py
import csv
import matplotlib.pyplot as plt
import cv2

def interval_logic_list(logic_score):
    name_list = ["off","on","and","nand","or","nor","xor","xnor","imp","nimp", "other", "not consist"]
    score_list = [0, 30,  2, 28, 14, 16, 12, 18, 26, 4, 70, 80]
    label_list = [0,  1,  2,  3,  4,  5,  6,  7,  8, 9, 10, 11]
    label = 10
    for j, score in enumerate(score_list):
        if logic_score == score:
            label = j
    return(label)

def interval_logic_list_16(logic_score):
    name_list = ["False", "A nimply B", "A", "B nimply A", "B", "XOR", "OR",
                 "NOR", "XNOR", "Not B", "B imply A", "Not A", "A imply B", "NAND", "TRUE", "other"]
    label_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    label = 16
    for j, score in enumerate(label_list):
        if logic_score == score:
            label = j
    return(label)

def F(x, a=1.6, theta=4):
    f = (1 + np.exp(-a * (x - theta)))**-1 - (1 + np.exp(a * theta))**-1
    return f

def simulation_logic_data(paras, e_bias, i_bias, W1, W2, B1, B2, **other_pars):
    '''
    use (0, 0) stimulus to find real initial condition
    input : parameters
    output : a_in, a_out, data_temp
    parameters
    '''
    bo, wee, wei, wie, wii, wo, stim, T, a, theta, tau, bias, dif = paras
    
    dt = 0.1
    # data space
    range_t = np.arange(0, 4*T, dt)           # 4倍
    Lt = range_t.size                        
    data_temp = np.zeros([Lt, 8])
    
    # 刺激
    I0 = np.array([[   0,    0,    0,    0],
                   [stim,    0, stim,    0],     # current (1, 0) stimulus
                   [0   , stim,    0, stim],     # current (0, 1) stimulus
                   [stim, stim, stim, stim]])    # current (1, 1) stimulus
    
    # initial condiction
    a_in = np.zeros(4)       # initial FR  [r_E1, r_E2, r_I1, r_I2]
    a_out = np.zeros(1)      # out FR      [r_EO] 
    
    time_df = 0.2       # 刺激的前後休息時間
    for k, t in enumerate( np.delete(range_t, -1) ):
        if t>T*(0+time_df) and t<T*(1-time_df) :          # (1,1)
            I = I0[3]
        elif t>T*(1+time_df) and t<T*(2-time_df) :        # (1,0)
            I = I0[1]
        elif t>T*(2+time_df) and t<T*(3-time_df) :        # (0,1)
            I = I0[2]
        else :                                            # (0,0)
            I = I0[0]
        
        
        Z1 = np.dot(W1, a_in) + B1 + I
        da_in = (F(Z1, a, theta) - a_in)*dt/tau

        Z2 = np.dot(W2, a_in[0:2]) + B2
        da_out = (F(Z2, a, theta) - a_out)*dt/tau
        
        a_in += da_in
        a_out += da_out
        data_temp[k+1, 1:5] = a_in
        data_temp[k+1, 5] = a_out
        data_temp[k+1, 6:8] = I[0:2]
    
    #模擬結束
    # 加入時間
    data_temp[:, 0] = range_t
    
    # 取出四個時段的FR   (0.25-0.75)
    time_stamp = ( np.arange(0,4)*T+ T*0.7 )*10
    logic_FR = np.zeros(4)
    for t, time in enumerate(time_stamp):                     # add rest term
        logic_FR[t]=data_temp[int(time), 5]               # logic_FR
    
    # 四個時段的FR算出 logic type
    logic_score = sum( np.where(np.array(logic_FR)>0.5, [2**i for i in range(0,4)], 0) )
    logic_label = interval_logic_list_16(logic_score)

    return data_temp, logic_FR, logic_label


def simulation_crirel_data(paras, e_bias, i_bias, W1, W2, B1, B2, **other_pars):
    '''
    use (0, 0) stimulus to find real initial condition
    input : parameters
    output : a_in, a_out, data_temp
    parameters
    '''
    bo, wee, wei, wie, wii, wo, stim, T, a, theta, tau, bias, dif = paras
    
    dt = 0.1
    # data space
    range_t = np.arange(0, 8*T, dt)           # 8倍
    Lt = range_t.size                        
    data_temp = np.zeros([Lt, 9])
    
    # 刺激
    I0 = np.array([[0, stim, stim, stim, stim],     # current (0, 1, 1) stimulus
                   [0, stim,    0, stim,    0],     # current (0, 1, 0) stimulus
                   [0, 0   , stim,    0, stim],     # current (0, 0, 1) stimulus
                   [0,    0,    0,    0,    0],     # current (0, 0, 0) stimulus
                   [9, stim, stim, stim, stim],     # current (1, 1, 1) stimulus
                   [9, stim,    0, stim,    0],     # current (1, 1, 0) stimulus
                   [9, 0   , stim,    0, stim],     # current (1, 0, 1) stimulus
                   [9,    0,    0,    0,    0]      # current (1, 0, 0) stimulus
                   ])
    
    # initial condiction
    a_in = np.zeros(5)       # initial FR  [r_E1, r_E2, r_I1, r_I2]
    a_out = np.zeros(1)      # out FR      [r_EO] 
    
    time_df = 0.2       # 刺激的前後休息時間
    for k, t in enumerate( np.delete(range_t, -1) ):
        if t>T*(0+time_df) and t<T*(1-time_df) :          # (0,1,1)
            I = I0[0]
        elif t>T*(1+time_df) and t<T*(2-time_df) :        # (0,1,0)
            I = I0[1]
        elif t>T*(2+time_df) and t<T*(3-time_df) :        # (0,0,1)
            I = I0[2]
        elif t>T*(3+time_df) and t<T*(4-time_df) :        # (0,0,0)
            I = I0[3]
        elif t>T*(4+time_df) and t<T*(5-time_df) :        # (1,1,1)
            I = I0[4]
        elif t>T*(5+time_df) and t<T*(6-time_df) :        # (1,1,0)
            I = I0[5]
        elif t>T*(6+time_df) and t<T*(7-time_df) :        # (1,0,1)
            I = I0[6]
        elif t>T*(7+time_df) and t<T*(8-time_df) :        # (1,0,0)
            I = I0[7]
        else :                                            # (0,0)
            if t<T*4:
                I = I0[3]
            else:
                I = I0[7]
            
        
        Z1 = np.dot(W1, a_in) + B1 + I
        da_in = (F(Z1, a, theta) - a_in)*dt/tau

        Z2 = np.dot(W2, a_in[1:3]) + B2
        da_out = (F(Z2, a, theta) - a_out)*dt/tau
        
        a_in += da_in
        a_out += da_out
        data_temp[k+1, 1:6] = a_in
        data_temp[k+1, 6] = a_out
        data_temp[k+1, 7:9] = I[1:3]
    
    #模擬結束
    # 加入時間
    data_temp[:, 0] = range_t
    
    # 取出四個時段的FR   (0.25-0.75)
    time_stamp = ( np.arange(0,4)*T+ T*0.7 )*10
    logic_FR = np.zeros(4)
    for t, time in enumerate(time_stamp):                     # add rest term
        logic_FR[t]=data_temp[int(time), 6]               # logic_FR
    
    # 四個時段的FR算出 logic type
    logic_score = sum( np.where(np.array(logic_FR)>0.5, [2**i for i in range(0,4)], 0) )
    logic_label = interval_logic_list_16(logic_score)

    return data_temp , logic_FR, logic_label


# def simulation_logic(paras, e_bias, i_bias, W1, W2, B1, B2, **other_pars):
#     # only return label
#     '''
#     use (0, 0) stimulus to find real initial condition
#     input : parameters
#     output : a_in, a_out, data_temp
#     parameters
#     '''
#     bo, wee, wei, wie, wii, wo, stim, T, a, theta, tau, bias, dif = paras
    
#     dt = 0.1
#     # data space
#     range_t = np.arange(0, 4*T, dt)           # 4倍
#     Lt = range_t.size                        
#     data_temp = np.zeros([Lt])
    
#     # 刺激
#     I0 = np.array([[   0,    0,    0,    0],
#                    [stim,    0, stim,    0],     # current (1, 0) stimulus
#                    [0   , stim,    0, stim],     # current (0, 1) stimulus
#                    [stim, stim, stim, stim]])    # current (1, 1) stimulus
    
#     # initial condiction
#     a_in = np.zeros(4)       # initial FR  [r_E1, r_E2, r_I1, r_I2]
#     a_out = np.zeros(1)      # out FR      [r_EO] 
    
#     tt = 1/10
#     for k, t in enumerate( np.delete(range_t, -1) ):
#         if t>T*(0+tt) and t<T*(1-tt) :     # (1,1)
#             I = I0[3]
#         elif t>T*(1+tt) and t<T*(2-tt) :         # (1,0)
#             I = I0[1]
#         elif t>T*(2+tt) and t<T*(3-tt) :        # (0,1)
#             I = I0[2]
#         else :
#             I = I0[0]
        
        
#         Z1 = np.dot(W1, a_in) + B1 + I
#         da_in = (fplot.F(Z1, a, theta) - a_in)*dt/tau

#         Z2 = np.dot(W2, a_in[0:2]) + B2
#         da_out = (fplot.F(Z2, a, theta) - a_out)*dt/tau
        
#         a_in += da_in
#         a_out += da_out
#         data_temp[k+1] = a_out
    
#     # get logic data
#     time_stamp = ( np.arange(0,4)*T+ T*0.7 )*10
#     logic_FR = np.zeros(4)
#     for t, time in enumerate(time_stamp):                     # add rest term
#         logic_FR[t]=data_temp[int(time)]               # logic_FR
    
#     # get logic label 
#     logic_score = sum( np.where(np.array(logic_FR)>0.5, [2**i for i in range(1,5)], 0) )
#     label = interval_logic_list(logic_score)

#     return label