import numpy as np
import dynalysis.basics as bcs
from dynalysis.gen_conf import exec_conf
from dynalysis.gen_pro import exec_pro
import subprocess


#=====parameters=====#
e1i1=30
e1i2=0
e2i1=0
e2i2=30
i1e1=60
i1e2=0
i1i2=30
i2e1=0
i2e2=60
i2i1=30
ee5=50
input3=45
input4=45
duration=1000

def deter_fire(train, thre=10):
    if np.mean(train) >= thre:
        return True
    return False


Out = []
n_std = 0
for be in np.arange(0,4,.15):
    inner = []
    for bi in np.arange(-2,4,0.2):
        b_exc = be
        b_inh = bi

        # exec_conf, exec_pro code here with different b_exc, b_inh, noise_std
        exec_conf([0,30,0,0], ID=4095, update_tar={\
                  'exc_1':[['inh_1','AMPA',e1i1,1,1], ['inh_2','AMPA',e1i2,1,1], ['exc_5','AMPA',ee5,1,1]],\
                  'exc_2':[['inh_1','AMPA',e2i1,1,1], ['inh_2','AMPA',e2i2,1,1], ['exc_5','AMPA',ee5,1,1]],\
                  'inh_1':[['exc_1','GABA',i1e1,1,1], ['exc_2','GABA',i1e2,1,1], ['inh_2','GABA',i1i2,1,1]],\
                  'inh_2':[['exc_1','GABA',i2e1,1,1], ['exc_2','GABA',i2e2,1,1], ['inh_1','GABA',i2i1,1,1]],\
                  'exc_3':[['exc_1','AMPA',input3,1,1], ['inh_1','AMPA',input3,1,1]],\
                  'exc_4':[['exc_2','AMPA',input4,1,1], ['inh_2','AMPA',input4,1,1]]},\
                  event_dic={'exc_1':{'Taum':20}, 'exc_2':{'Taum':20},\
                             'inh_1':{'Taum':20}, 'inh_2':{'Taum':20}},\
                  add_connections=[('exc_3','exc_1'),('exc_3', 'inh_1'),\
                                   ('exc_4','exc_2'),('exc_4', 'inh_2'),\
                                   ('exc_1','exc_5'),('exc_2','exc_5')])
#-.7
        exec_pro(ID=4095, trial_t=5600, output_Spike=False, gmean=0, gstd=0,\
                 event_dic={(100, 'exc_3'):['pulse',duration,1,0],\
                            (100, 'exc_4'):['pulse',duration,1,0],\
                            (1600, 'exc_3'):['pulse',duration,1,0],\
                            (1600, 'exc_4'):['pulse',duration,0.7,0],\
                            (3100, 'exc_3'):['pulse',duration,0.7,0],\
                            (3100, 'exc_4'):['pulse',duration,1,0],\
                            (2, 'exc_1'):['ramp',b_exc,n_std],\
                            (2, 'exc_2'):['ramp',b_exc,n_std],\
                            (2, 'inh_1'):['ramp',b_inh,n_std],\
                            (2, 'inh_2'):['ramp',b_inh,n_std],\
                            (2, 'exc_5'):['ramp',-0.4,0]},\
                output_MemPot=True)


        print ((b_exc,b_inh))
        subprocess.Popen("./flysim07_21_2.out -conf network.conf -pro network.pro -nmodel LIF -dt .1", shell = True).wait()

        cols = bcs.readcolumn('Frate.txt', to_float=True)[1:]
        # exc_1, ... exc_4, exc_5, inh_1, inh_2
        cond1 = deter_fire(cols[4][10:110]) #exc_1 (1,1)

        cond2 = deter_fire(cols[4][160:260]) #exc_1 (1,0)

        cond3 = deter_fire(cols[4][310:410]) #exc_1 (0,1)

        cond4 = deter_fire(cols[4][460:560]) #exc_1 (0,0)

        print((cond1,cond2,cond3,cond4))
        gate = 0 #'unclear'
        if cond1 and cond2 and cond3 and cond4: gate = 1 #'ON'
        if cond1 and cond2 and cond3 and (not cond4): gate = 2 #'OR'
        if (not cond1) and cond2 and cond3 and (not cond4): gate = 3 #'XOR'
        if cond1 and (not cond2) and (not cond3) and (not cond4): gate = 4 #'AND'
        #
        if (not cond1) and cond2 and cond3 and cond4: gate = 5 #'NAND'
        if cond1 and (not cond2) and (not cond3) and cond4: gate = 6 #'NXOR'
        if (not cond1) and (not cond2) and (not cond3) and cond4: gate = 7 #'NOR'
        if (not cond1) and (not cond2) and (not cond3) and (not cond4): gate = 8 #'OFF'
        inner.append(gate)
    Out.append(inner)

toExport = np.array(Out)

np.savetxt('graph.txt',toExport.astype(int),fmt='%i', delimiter=",")























        # subprocess('./flysim.out -pro network.pro...')
        # read Frate.txt file
        # find the output to (1,1), (1,0),...
        # if not
