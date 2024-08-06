import numpy as np
import pandas as pd
import h5py
import csv
import matplotlib.pyplot as plt
import matplotlib.colors
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

from matplotlib import cm 
import cv2



# Sigmoid Function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def F(x, a=1.6, theta=4):
    f = (1 + np.exp(-a * (x - theta)))**-1 - (1 + np.exp(a * theta))**-1
    return f

def dF(x, a=1.6, theta=4):
    dFdx = a * np.exp(-a * (x - theta)) * (1 + np.exp(-a * (x - theta)))**-2
    return dFdx


def default_pars(**kwargs):
    pars = {}

    ## set up
    ## Excitatory parameters
    pars['tau'] = 1       # Timescale of the E population [ms]
    pars['a']     = 1.6     # Gain
    pars['theta'] = 4       # Threshold

    # Connection strength
    pars['wEE'] = 5          # E to E 5
    pars['wEI'] = 14         # I to E 14
    pars['wIE'] = 7          # E to I 7
    pars['wII'] = 7          # I to I 7
    pars['wOE'] = 5.0        # E to OUT
    
    # External input
    pars['stim'] = 5.       # 內部 bias
    pars['Bias_E'] = 0.     # 內部 bias
    pars['Bias_I'] = 0.     # 內部 bias
    
    # Vector of discretized time points [ms]
    pars['T'] = 40         # Total duration of simulation [ms]
    pars['dt'] = 0.1         # Simulation time step [ms]
    pars['range_t'] = np.arange(0, pars['T']*4, pars['dt'])
    

    # External parameters if any
    for k in kwargs:
        pars[k] = kwargs[k]
        
    return pars


def plot_logic(data_temp, paras, e_bias, i_bias, Tit="title", figname="logic", path="phase/", plot_bool=False):
    '''
    plot single trial
    my_test_plot(t, data_temp)
    '''
    bo, wee, wei, wie, wii, wo, stim, T, a, theta, tau, bias, dif = paras
    fname = str(bo)+"_"+str(wee)+"_"+str(wei)+"_"+str(wie)+"_"+str(wii)+"_"+str(wo)+"_"+\
            str(stim)+"_"+str(T)+"_"+str(a)+ "_"+str(theta)+ "_"+str(tau)+ "_"+str(bias)+ "_"+str(dif)

    FZ = 16
    data_df = pd.DataFrame(data_temp, columns=["t", "E1", "E2", "I1", "I2", "EO", "Inp1", "Inp2"])

    fig, ax = plt.subplots(4, 1, figsize=(5, 5.5), sharex=True)
    plt.subplots_adjust(hspace=0.1, wspace=0.2, left=0.2)

    st = fig.suptitle(Tit, fontsize=FZ+2)

    ax[0].plot(data_df["t"], data_df["E1"], 'b', label='E1')
    ax[0].plot(data_df["t"], data_df["I1"], 'r', label='I1')
    ax[0].set_ylim([-0.1, 1.1])
    ax[0].set_title(fname)

    ax[1].plot(data_df["t"], data_df["E2"], 'b', label='E2')
    ax[1].plot(data_df["t"], data_df["I1"], 'r', label='I2')
    ax[1].set_ylim([-0.1, 1.1])

    ax[2].plot(data_df["t"], data_df["EO"], 'b', label='Eout')
    ax[2].axhline(y=0.5, xmin=0, xmax=T*4, color = 'k', linestyle = '--', alpha=0.3)
    ax[2].set_ylim([-0.1, 1.1])

    ax[3].plot(data_df["t"], data_df["Inp1"], 'g', label='Inp1')
    ax[3].plot(data_df["t"], data_df["Inp2"], 'm', linewidth=2, dashes=[6, 4], label='Inp2')
    ax[3].set_ylim([-0.1, 6])
    ax[3].set_xlabel('t (ms)', fontsize=FZ)

    cols = ['Node 1', 'Node 2', 'Eout', 'Stimulus']
    for i, col in enumerate(cols):
        ax[i].set_ylabel(col , fontsize=FZ)
        ax[i].legend(loc='center right', bbox_to_anchor=(1.3, 0.5))
    fig.tight_layout()
    plt.subplots_adjust(top=0.83)
    if plot_bool:
        plt.savefig(path + figname + ".png")
    plt.show()


def plot_logic_out(data_temp, paras, e_bias, i_bias, Tit="title", figname="logic", path="phase/", plot_bool=False):
    '''
    plot single trial
    my_test_plot(t, data_temp)
    '''
    bo, wee, wei, wie, wii, wo, stim, T, a, theta, tau, bias, dif = paras
    fname = str(bo)+"_"+str(wee)+"_"+str(wei)+"_"+str(wie)+"_"+str(wii)+"_"+str(wo)+"_"+\
            str(stim)+"_"+str(T)+"_"+str(a)+ "_"+str(theta)+ "_"+str(tau)+ "_"+str(bias)+ "_"+str(dif)

    FZ = 16
    data_df = pd.DataFrame(data_temp, columns=["t", "E1", "E2", "I1", "I2", "EO", "Inp1", "Inp2"])

    fig, ax = plt.subplots(2, 1, figsize=(5, 3), sharex=True)
    plt.subplots_adjust(hspace=0.1, wspace=0.2, left=0.2)

    st = fig.suptitle(Tit, fontsize=FZ)

    ax[0].plot(data_df["t"], data_df["EO"], 'b', label='Eout')
    ax[0].axhline(y=0.5, xmin=0, xmax=T*4, color = 'k', linestyle = '--', alpha=0.3)
    ax[0].set_ylim([-0.1, 1.1])

    ax[1].plot(data_df["t"], data_df["Inp1"], 'g', label='Inp1')
    ax[1].plot(data_df["t"], data_df["Inp2"], 'm', linewidth=2, dashes=[6, 4], label='Inp2')
    ax[1].set_ylim([-0.1, 6])
    ax[1].set_xlabel('t (ms)', fontsize=FZ)

    cols = ['Eout', 'Stimulus']
    for i, col in enumerate(cols):
        ax[i].set_ylabel(col , fontsize=FZ)
        ax[i].legend(loc='center right', bbox_to_anchor=(1.3, 0.5), fontsize=FZ-6)
        
    fig.tight_layout()
    plt.subplots_adjust(top=0.8)
    if plot_bool:
        plt.savefig(path + figname + ".png")
    plt.show()
    
def plot_logic_out_temp(data_temp, paras, e_bias, i_bias, Tit="title", figname="logic", path="phase/", plot_bool=False):
    '''
    plot single trial
    my_test_plot(t, data_temp)
    '''
    bo, wee, wei, wie, wii, wo, stim, T, a, theta, tau, bias, dif = paras
    fname = str(bo)+"_"+str(wee)+"_"+str(wei)+"_"+str(wie)+"_"+str(wii)+"_"+str(wo)+"_"+\
            str(stim)+"_"+str(T)+"_"+str(a)+ "_"+str(theta)+ "_"+str(tau)+ "_"+str(bias)+ "_"+str(dif)

    FZ = 16
    data_df = pd.DataFrame(data_temp, columns=["t", "E1", "E2", "I1", "I2", "EO", "Inp1", "Inp2"])

    fig, ax = plt.subplots(2, 1, figsize=(5, 3), sharex=True)
    plt.subplots_adjust(hspace=0.1, wspace=0.2, left=0.2)

    # st = fig.suptitle(Tit, fontsize=FZ)

    ax[0].plot(data_df["t"], data_df["EO"], 'b', label='Eout')
    ax[0].axhline(y=0.5, xmin=0, xmax=T*4, color = 'k', linestyle = '--', alpha=0.3)
    ax[0].set_ylim([-0.1, 1.1])
    ax[0].set_title(Tit, fontsize=FZ)

    ax[1].plot(data_df["t"], data_df["Inp1"], 'g', label='Input 1')
    ax[1].plot(data_df["t"], data_df["Inp2"], 'm', linewidth=2, dashes=[6, 4], label='Input 2')
    ax[1].set_ylim([-0.5, 6])
    ax[1].set_xlabel('t (ms)', fontsize=FZ)
    ax[1].axes.xaxis.set_ticks([])
    cols = ['Eout', 'Input']
    for i, col in enumerate(cols):
        ax[i].set_ylabel(col , fontsize=FZ)
        ax[i].legend(loc='center right', bbox_to_anchor=(1.4, 0.5), fontsize=FZ-6)
        
    fig.tight_layout()
    plt.subplots_adjust(top=0.8)
    if plot_bool:
        plt.savefig(path + figname + ".png")
    plt.show()
    

def plot_phase(fname, bias, dif, Z, path="phase/"):
    e_bias_list = np.arange(-bias, bias*1.5, dif)
    i_bias_list = np.arange(-bias, bias*1.5, dif)
    
    FZ = 16
    label_list = [0,  1,  2,  3,  4,  5,  6,  7,  8, 9, 10, 11]
    name_list = ["off","on","and","nand","or","nor","xor","xnor","imp","nimp", "other", "not consist"]
    
    fig, ax = plt.subplots(1, 1, figsize=(7,6))
    # left
    c = ax.pcolormesh(e_bias_list, i_bias_list, Z, 
                      cmap='Paired', 
                      vmin=-0.5, vmax=11.5,
                      edgecolors='k', 
                      linewidths=0.5)
    cbar = fig.colorbar(c, ticks=label_list)
    cbar.ax.set_yticklabels(name_list)  # vertically oriented colorbar
    
    # lim
    ax.set_title(fname, fontsize=FZ+4)
    ax.set_xlim(-bias-dif/2, bias*1.5-dif/2)
    ax.set_ylim(-bias-dif/2, bias*1.5-dif/2)
    ax.set_xlabel('e_bias', fontsize=FZ)
    ax.set_ylabel('i_bias', fontsize=FZ)
    
    plt.savefig(path+fname+".png")
    plt.show()
    # plt.close()
    

    
def plot_phase_16(Tit, figname, bias, dif, Z, path="phase/", plot_bool=False):
    
    FZ =16
    e_bias_list = np.arange(-bias, bias*1.5, dif)
    i_bias_list = np.arange(-bias, bias*1.5, dif)
    
    name_list = ["False", "AND", "A nimply B", "A", "B nimply A", "B", "XOR", "OR",
             "NOR", "XNOR", "Not B", "B imply A", "Not A", "A imply B", "NAND", "TRUE"]
    
    name_list = ["00- False", "01- AND", "02- A nimply B", "03- A", "04- B nimply A", "05- B", "06- XOR", "07- OR",
                 "08- NOR", "09- XNOR", "10- Not B", "11- B imply A", "12- Not A", "13- A imply B", "14- NAND", "15- TRUE"]

    cmap_list = ['#8fccff', '#a6ff9f', '#ffbd59', '#e6baff', '#b0796e', '#f0f0f0', '#ffff93', '#ffa6ff',
                 '#ff14e4', '#c6a300', '#adadad', '#672814', '#b123ff', '#ff7200', '#016835', '#0080b8']
    label_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    fig, ax = plt.subplots(1, 1, figsize=(7,6))
    # left
    new_inferno = cm.get_cmap('inferno', 16)
    custom_cmap = matplotlib.colors.LinearSegmentedColormap.from_list("custom", 
                                                                  ["red", "blue", "yellow"])

    cmap = ListedColormap(cmap_list)
    
    
    c = ax.pcolormesh(e_bias_list, i_bias_list, Z, 
                      cmap= cmap, 
                      vmin=-0.5, vmax=15.5,
                      # edgecolors='k', 
                      linewidths=0.5)
    cbar = fig.colorbar(c, ticks=label_list)
    cbar.ax.set_yticklabels(name_list)  # vertically oriented colorbar
    
    # lim
    ax.set_title(Tit, fontsize=FZ+4, pad=20)
    ax.set_xlim(-bias-dif/2, bias*1.5-dif/2)
    ax.set_ylim(-bias-dif/2, bias*1.5-dif/2)
    ax.set_xlabel('E1 bias', fontsize=FZ+2)
    ax.set_ylabel('I1 bias', fontsize=FZ+2)
#     ax.set_xlabel(r'$E bias_{E1}$', fontsize=FZ+2)
#     ax.set_ylabel(r'$I bias_{I1}$', fontsize=FZ+2)
    if plot_bool:
        plt.savefig(path + figname + ".png")
    plt.show()
    # plt.close()
    
def plot_phase_16_null(Tit, figname, bias, dif, Z, nullcline_all, path="phase/", plot_bool=False):
    
    FZ =16
    e_bias_list = np.arange(-bias, bias*1.5, dif)
    i_bias_list = np.arange(-bias, bias*1.5, dif)
    
    name_list = ["00-False", "01-AND", "02, A nimply B", "03, A", "04, B nimply A", "05, B", "06, XOR", "07, OR",
                 "08-NOR", "09-XNOR", "10-Not B", "11-B imply A", "12-Not A", "13-A imply B", "14-NAND", "15-TRUE"]

    cmap_list = ['#8fccff', '#a6ff9f', '#ffbd59', '#e6baff', '#b0796e', '#f0f0f0', '#ffff93', '#ffa6ff',
                 '#ff14e4', '#c6a300', '#adadad', '#672814', '#b123ff', '#ff7200', '#016835', '#0080b8']
    label_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    fig, ax = plt.subplots(1, 1, figsize=(7,6))
    # left
    cmap = ListedColormap(cmap_list)
    
    c = ax.pcolormesh(e_bias_list, i_bias_list, Z, 
                      cmap= cmap, 
                      vmin=-0.5, vmax=15.5,
                      # edgecolors='k', 
                      linewidths=0.5)
    cbar = fig.colorbar(c, ticks=label_list)
    cbar.ax.set_yticklabels(name_list)  # vertically oriented colorbar
    
    
    # nullcline_all
    nullcline_11_read, nullcline_10_read, nullcline_01_read, nullcline_00_read = nullcline_all
    plt.plot(nullcline_11_read[0], nullcline_11_read[1], lw=4, color="magenta")
    plt.plot(nullcline_10_read[0], nullcline_10_read[1], lw=4, color="coral")
    plt.plot(nullcline_01_read[0], nullcline_01_read[1], lw=4, color="lime")
    plt.plot(nullcline_00_read[0], nullcline_00_read[1], lw=4, color="cyan")
    
    
    
    # lim
    ax.set_title(Tit, fontsize=FZ+4, pad=20)
    ax.set_xlim(-bias-dif/2, bias*1.5-dif/2)
    ax.set_ylim(-bias-dif/2, bias*1.5-dif/2)
    ax.set_xlabel('e_bias', fontsize=FZ)
    ax.set_ylabel('i_bias', fontsize=FZ)
    if plot_bool:
        plt.savefig(path + figname + ".png")
    plt.show()
    # plt.close()

def plot_phase_16_null_temp(Tit, figname, bias, dif, Z, nullcline_all, path="phase/", plot_bool=False):
    
    FZ =16
    e_bias_list = np.arange(-bias, bias*1.5, dif)
    i_bias_list = np.arange(-bias, bias*1.5, dif)
    
    name_list = ["00- False", "01- AND", "02- A nimply B", "03- A", "04- B nimply A", "05- B", "06- XOR", "07- OR",
                 "08- NOR", "09- XNOR", "10- Not B", "11- B imply A", "12- Not A", "13- A imply B", "14- NAND", "15- TRUE"]

    cmap_list = ['#8fccff', '#a6ff9f', '#ffbd59', '#e6baff', '#b0796e', '#f0f0f0', '#ffff93', '#ffa6ff',
                 '#ff14e4', '#c6a300', '#adadad', '#672814', '#b123ff', '#ff7200', '#016835', '#0080b8']
    label_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    fig, ax = plt.subplots(1, 1, figsize=(7,6))
    # left
    cmap = ListedColormap(cmap_list)
    
    c = ax.pcolormesh(e_bias_list, i_bias_list, Z, 
                      cmap= cmap, 
                      vmin=-0.5, vmax=15.5,
                      # edgecolors='k', 
                      linewidths=0.5)
    cbar = fig.colorbar(c, ticks=label_list)
    cbar.ax.set_yticklabels(name_list)  # vertically oriented colorbar
    
    
    # nullcline_all
    nullcline_11_read, nullcline_10_read, nullcline_01_read, nullcline_00_read = nullcline_all
    plt.plot(nullcline_11_read[0], nullcline_11_read[1], lw=4, label="11", color="magenta")
    plt.plot(nullcline_10_read[0], nullcline_10_read[1], lw=4, label="10", color="coral")
    plt.plot(nullcline_01_read[0], nullcline_01_read[1], lw=4, label="01", color="lime")
    plt.plot(nullcline_00_read[0], nullcline_00_read[1], lw=4, label="00", color="cyan")
    plt.legend(fontsize=FZ)
    
    
    # lim
    ax.set_title(Tit, fontsize=FZ+4, pad=20)
    ax.set_xlim(-bias-dif/2, bias*1.5-dif/2)
    ax.set_ylim(-bias-dif/2, bias*1.5-dif/2)
    ax.set_xlabel('E bias', fontsize=FZ)
    ax.set_ylabel('I bias', fontsize=FZ)
    if plot_bool:
        plt.savefig(path + figname + ".png")
    plt.show()
    # plt.close()


def plot_loss_2d(Tit, figname, bias, dif, Z, tit, path="phase/", plot_bool=False):
    e_bias_list = np.arange(-bias, bias*1.5, dif)
    i_bias_list = np.arange(-bias, bias*1.5, dif)
    
    FZ = 14
    fig, ax = plt.subplots(1, 1, figsize=(5, 4))
    # left
    c = ax.pcolormesh(e_bias_list, i_bias_list, Z, 
                      cmap='hot', 
                      vmin=0, vmax=1,
                      #edgecolors='k', 
                      linewidths=0.5)
    cbar = fig.colorbar(c)
    
    # lim
    ax.set_title(Tit+'\n'+figname, fontsize=FZ)
    ax.set_xlim(-bias-dif/2, bias*1.5-dif/2)
    ax.set_ylim(-bias-dif/2, bias*1.5-dif/2)
    ax.set_xlabel('e_bias', fontsize=FZ)
    ax.set_ylabel('i_bias', fontsize=FZ)
    
    if plot_bool:
        plt.savefig(path+figname+"_2d_"+tit+".png")
    #plt.close()
    
def plot_loss_2d_null(Tit, figname, bias, dif, Z, nullcline, COLOR="red", path="phase/", plot_bool=False):
    e_bias_list = np.arange(-bias, bias*1.5, dif)
    i_bias_list = np.arange(-bias, bias*1.5, dif)
    
    FZ = 14
    fig, ax = plt.subplots(1, 1, figsize=(5, 4))
    # left
    c = ax.pcolormesh(e_bias_list, i_bias_list, Z, 
                      cmap='bwr', 
                      vmin=0, vmax=1,
                      #edgecolors='k', 
                      linewidths=0.5)
    cbar = fig.colorbar(c)
    cbar.set_label('Eout Firing Rate (Hz)', rotation=90)

    plt.plot(nullcline[0], nullcline[1], lw=4, color=COLOR, label="boundary")
    plt.legend(loc='upper left', fontsize=FZ)
    
    # lim
    ax.set_title(Tit+'\n'+figname, fontsize=FZ)
    ax.set_xlim(-bias-dif/2, bias*1.5-dif/2)
    ax.set_ylim(-bias-dif/2, bias*1.5-dif/2)
    ax.set_xlabel('E bias', fontsize=FZ)
    ax.set_ylabel('I bias', fontsize=FZ)
    
    if plot_bool:
        plt.savefig(path + figname + ".png")
    #plt.close()
    
    
def plot_loss_3d(FR_result, bias, dif, tit="tit", path="phase/"):
    
    e_bias_list = np.arange(-bias, bias*1.5, dif)
    i_bias_list = np.arange(-bias, bias*1.5, dif)
    X,Y = np.meshgrid(e_bias_list, i_bias_list)
    
    FZ = 14
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    c = ax.plot_surface(X, Y, Z , cmap='hot',vmin=0, vmax=1,)
    cbar = fig.colorbar(c,shrink=0.5)

    ax.set_title(tit+' landscape', fontsize=20)
    ax.set_xlabel('e_bias')
    ax.set_ylabel('i_bias')
    ax.set_zlabel('loss')

    ax.view_init(40, -125) # angle , azimuth
    
    plt.savefig(path+fname+"_3d_"+tit+".png")
    
    #plt.close()
    

def plot_3d():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # 產生 3D 座標資料
    z1 = np.random.randn(50)
    x1 = np.random.randn(50)
    y1 = np.random.randn(50)
    z2 = np.random.randn(50)
    x2 = np.random.randn(50)
    y2 = np.random.randn(50)

    # 繪製 3D 座標點
    ax.scatter(x1, y1, z1, c=z1, cmap='Reds', marker='^', label='My Points 1')
    ax.scatter(x2, y2, z2, c=z2, cmap='Blues', marker='o', label='My Points 2')

    # 顯示圖例
    ax.legend()

    # 顯示圖形
    plt.show()
    
def plot_eig(fname, bias, dif, Z, path="eig/"):
    e_bias_list = np.arange(-bias, bias*1.5, dif)
    i_bias_list = np.arange(-bias, bias*1.5, dif)
    
    FZ = 16
    name_list  = ["R0","R1","R2","R3","R4","imag","nan","nan","nan","nan", "nan", "nan"]
    label_list = [0,  1,  2,  3,  4,  5          ,  6,  7,  8, 9, 10, 11]
    
    fig, ax = plt.subplots(1, 1, figsize=(7,6))
    # left
    c = ax.pcolormesh(e_bias_list, i_bias_list, Z, 
                      cmap='Paired', 
                      vmin=-0.5, vmax=11.5,
                      edgecolors='k', 
                      linewidths=0.5)
    cbar = fig.colorbar(c, ticks=label_list)
    cbar.ax.set_yticklabels(name_list)  # vertically oriented colorbar
    
    # lim
    ax.set_title(fname, fontsize=FZ+4)
    ax.set_xlim(-bias-dif/2, bias*1.5-dif/2)
    ax.set_ylim(-bias-dif/2, bias*1.5-dif/2)
    ax.set_xlabel('e_bias', fontsize=FZ)
    ax.set_ylabel('i_bias', fontsize=FZ)
    
    plt.savefig(path+fname+".png")
    plt.show()
    plt.close()