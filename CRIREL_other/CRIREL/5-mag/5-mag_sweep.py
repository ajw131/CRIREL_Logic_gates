import os
import numpy as np
import subprocess
import dynalysis.basics as bcs
import dynalysis.classes as clss
from dynalysis.gen_conf import exec_conf
from dynalysis.gen_pro import exec_pro
from dynalysis.visualization import subplot, edplot

space = 400
dur = 100
mother = os.getcwd()
b = clss.branch('5-mag', mother)
for bias in list(np.arange(0,-0.00751,-0.001))+[-.00751]:
	b2 = clss.branch('bias='+str(bias), b.pathlink); b2.mkdir(); os.chdir(b2.pathlink)
	e=-.0
	ed={'inh_2':{'Taum':80, 'C':1}, 'inh_1':{}}
	ut={'exc_1':[['inh_2','AMPA',1,25,1],['inh_1','AMPA',1,20,1]],\
		'inh_2':[['inh_1','GABA',1,30,1]]}
	edp={
		 (2, 'exc_1'):['ramp',e,0],\
		 (2, 'exc_2'):['ramp',0,0],\
		 (2, 'inh_1'):['ramp',bias,0],\
		 (space,'exc_1'):['pulse_b',dur,1,0,e],\
		 (space*2,'exc_1'):['pulse_b',dur,1.5,0,e],\
		 (space*3,'exc_1'):['pulse_b',dur,2,0,e],\
		 (space*4,'exc_1'):['pulse_b',dur,2.5,0,e],\
		 (space*5,'exc_1'):['pulse_b',dur,3,0,e],\
		 (space*6,'exc_1'):['pulse_b',dur,3.5,0,e],\
		 (space*7,'exc_1'):['pulse_b',dur,4,0,e],\
		 (space*8,'exc_1'):['pulse_b',dur,4.5,0,e]}
	exec_conf([0,50,4000,70], ID=2447, update_tar=ut, event_dic=ed)
	exec_pro(ID=2447,output_Spike=False, trial_t=space*9, output_MemPot=True, event_dic=edp,\
			output_Frate = False)
	clss.copy_flysim(destination=b2.pathlink)

