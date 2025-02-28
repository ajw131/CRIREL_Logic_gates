import subprocess
import dynalysis.classes as clss
from dynalysis.gen_conf import exec_conf
from dynalysis.gen_pro import exec_pro
from dynalysis.visualization import subplot, edplot
import numpy as np
import matplotlib.pyplot as plt

ID = 4095 #4095 3513, 3579

ed_conf={'exc_1':{'GABA':['GABA','5','-90','0','0','0']},\
        'exc_2':{'GABA':['GABA','5','-90','0','0','0']},\
        'inh_1':{'AMPA':['AMPA','2','0','0','10.5','1']},\
        'inh_2':{'AMPA':['AMPA','2','0','0','10.5','1']}}

ebias = 1
ed_pro={(1,'exc_1'):['pulse',100,2,0],\
(1,'exc_2'):['pulse',100,2,0],\
(1,'inh_1'):['pulse', 100, 1, 0],\
(1000,'inh_2'):['pulse', 100, 1, 0]}


exec_conf([50,140,10,70], ID=ID,\
          event_dic=ed_conf)
exec_pro(ID=ID, trial_t = 1500, output_Spike=False,
         event_dic=ed_pro, output_MemPot=True, baseline=False)

subprocess.Popen("./flysim07_21_2.out -conf network.conf -pro network.pro -nmodel LIF -dt 0.01", shell = True).wait()

edplot(ed_pro)
subplot(fname='MemPot.dat')
