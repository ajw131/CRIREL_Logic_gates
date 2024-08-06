import os
import subprocess
import dynalysis.basics as bcs
import dynalysis.classes as clss
from dynalysis.gen_conf import exec_conf
from dynalysis.gen_pro import exec_pro
from dynalysis.visualization import subplot, edplot

mother = os.getcwd(); b = clss.branch('5-mag', mother)

#low has bias i_1 and i_2 = 0
e=-.0
ed={'inh_2':{'Taum':80, 'C':1}, 'inh_1':{}}
ut={'exc_1':[['inh_2','AMPA',1,25,1],['inh_1','AMPA',1,20,1]],\
    'inh_2':[['inh_1','GABA',1,30,1]]}
edp={
     (2, 'exc_1'):['ramp',e,0],\
     (2, 'exc_2'):['ramp',0,0],\
     (2, 'inh_1'):['ramp',-.00751,0],\
     (100,'exc_1'):['pulse_b',50,1,0,e],\
     (300,'exc_1'):['pulse_b',50,1.5,0,e],\
     (500,'exc_1'):['pulse_b',50,2,0,e],\
     (700,'exc_1'):['pulse_b',50,2.5,0,e],\
     (900,'exc_1'):['pulse_b',50,3,0,e],\
     (1100,'exc_1'):['pulse_b',50,3.5,0,e],\
     (1300,'exc_1'):['pulse_b',50,4,0,e],\
     (1500,'exc_1'):['pulse_b',50,4.5,0,e]}
exec_conf([0,50,4000,70], ID=2447, update_tar=ut, event_dic=ed)
exec_pro(ID=2447,output_Spike=False, trial_t=1600, output_MemPot=True, event_dic=edp,\
		output_Frate = False)


