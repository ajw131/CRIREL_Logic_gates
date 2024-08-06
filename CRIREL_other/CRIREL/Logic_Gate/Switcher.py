import subprocess
import os
import dynalysis.basics as bcs
import dynalysis.classes as clss
from dynalysis.gen_conf import exec_conf
from dynalysis.gen_pro import exec_pro
from dynalysis.visualization import subplot, edplot


AND  = [0,0 ,-.2,-.2, 0]
IMP  = [1,.7, .8, 1, 0]
NAND = [.7,.7,1.7, 1.7, .5]
NIMP = [.2,0,.85,.85,.3]
NOR  = [.75,.75,2.1,2.1,.3]
NXOR = [.9,.9,.5,.5,-.7]#[1.25,1.25,1.15,1.15,0]
OR   = [0.3,0.3,-.75,-.75,0]
XOR   = [0.2,0.2,1.5,1.5,.25]
bias= [AND,IMP,NAND,NIMP,NOR,NXOR,OR,XOR]
gate = 5
gate2 =6
biasNAME = ['AND','IMP','NAND','NIMP','NOR','NXOR','OR','XOR']
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
duration=2000
bias_current=0
dur2 = 500


for gate in xrange(0,8):
    for gate2 in xrange(0,8):

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

        exec_pro(ID=4095, trial_t=15000, output_Spike=False, gmean=0, gstd=0,\
                 event_dic={(8100, 'exc_3'):['pulse',duration,1,0],\
                            (8100, 'exc_4'):['pulse',duration,1,0],\
                            (4100, 'exc_3'):['pulse',duration,1,0],\
                            (4100, 'exc_4'):['pulse',duration,0.7,0],\
                            (100, 'exc_3'):['pulse',duration,0.7,0],\
                            (100, 'exc_4'):['pulse',duration,1,0],\
                            ##
                            (1100, 'exc_1'):['pulse_b',dur2,bias[gate2][0],0,bias[gate][0]],\
                            (1100, 'exc_2'):['pulse_b',dur2,bias[gate2][1],0,bias[gate][1]],\
                            (1100, 'inh_1'):['pulse_b',dur2,bias[gate2][2],0,bias[gate][2]],\
                            (1100, 'inh_2'):['pulse_b',dur2,bias[gate2][3],0,bias[gate][3]],\
                            (1100, 'exc_5'):['pulse_b',dur2,bias[gate2][4],0,bias[gate][4]],\
                            ##
                            ##
                            (5100, 'exc_1'):['pulse_b',dur2,bias[gate2][0],0,bias[gate][0]],\
                            (5100, 'exc_2'):['pulse_b',dur2,bias[gate2][1],0,bias[gate][1]],\
                            (5100, 'inh_1'):['pulse_b',dur2,bias[gate2][2],0,bias[gate][2]],\
                            (5100, 'inh_2'):['pulse_b',dur2,bias[gate2][3],0,bias[gate][3]],\
                            (5100, 'exc_5'):['pulse_b',dur2,bias[gate2][4],0,bias[gate][4]],\
                            ##
                            ##
                            (9100, 'exc_1'):['pulse_b',dur2,bias[gate2][0],0,bias[gate][0]],\
                            (9100, 'exc_2'):['pulse_b',dur2,bias[gate2][1],0,bias[gate][1]],\
                            (9100, 'inh_1'):['pulse_b',dur2,bias[gate2][2],0,bias[gate][2]],\
                            (9100, 'inh_2'):['pulse_b',dur2,bias[gate2][3],0,bias[gate][3]],\
                            (9100, 'exc_5'):['pulse_b',dur2,bias[gate2][4],0,bias[gate][4]],\
                            ##
                            ##
                            (13100, 'exc_1'):['pulse_b',dur2,bias[gate2][0],0,bias[gate][0]],\
                            (13100, 'exc_2'):['pulse_b',dur2,bias[gate2][1],0,bias[gate][1]],\
                            (13100, 'inh_1'):['pulse_b',dur2,bias[gate2][2],0,bias[gate][2]],\
                            (13100, 'inh_2'):['pulse_b',dur2,bias[gate2][3],0,bias[gate][3]],\
                            (13100, 'exc_5'):['pulse_b',dur2,bias[gate2][4],0,bias[gate][4]],\
                            ##
                            (2, 'exc_1'):['ramp',bias[gate][0],0],\
                            (2, 'exc_2'):['ramp',bias[gate][1],0],\
                            (2, 'inh_1'):['ramp',bias[gate][2],0],\
                            (2, 'inh_2'):['ramp',bias[gate][3],0],\
                            (2, 'exc_5'):['ramp',bias[gate][4],0]},\
                output_MemPot=True)


        subprocess.Popen("./flysim07_21_2.out -conf network.conf -pro network.pro -nmodel LIF -dt .05", shell = True).wait()
        subplot(fname='MemPot.dat', cols=[1,5,5,5])
        os.rename("Frate.png",'MemPot_'+biasNAME[gate]+'_switch_'+biasNAME[gate2]+'.png')
