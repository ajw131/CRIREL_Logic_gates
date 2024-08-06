import subprocess
import dynalysis.basics as bcs
import dynalysis.classes as clss
from dynalysis.gen_conf import exec_conf
from dynalysis.gen_pro import exec_pro
from dynalysis.visualization import subplot, edplot

'''
Show:
add one plot to show how interval between I1 spikes
and number of E1 spikes in each burst are affected by input strength or other parameters.
'''

e1b=0.5
e2b=0.5

ut={}
ed={(0, 'exc_1'):['ramp',e1b+3,0],\
    (0, 'exc_2'):['ramp',e2b+3,0],\
    (0, 'inh_1'):['ramp',-0.5,0],\
    (0, 'inh_2'):['ramp',-0.5,0]}
exec_conf([30,65,200,5], ID=3435, update_tar=ut)
exec_pro(ID=3435,output_Spike=False, trial_t=1000, output_MemPot=True, event_dic=ed, MemPot='2-sCPG.dat',\
		output_Frate = False)


subprocess.Popen("./flysim07_21_2.out -conf network.conf -pro network.pro -nmodel LIF -dt .05", shell = True).wait()
subplot(fname='MemPot.dat', cols=[1,2,3,4])
