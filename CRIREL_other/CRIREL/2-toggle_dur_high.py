import subprocess
import dynalysis.basics as bcs
import dynalysis.classes as clss
from dynalysis.gen_conf import exec_conf
from dynalysis.gen_pro import exec_pro
from dynalysis.visualization import subplot, edplot

'''
Show:
what is the minimum strength and duration to turn on and off the toggle?
'''
#max dur is 20, after that there is bursting.
#Note longer duration will cause a 2-burst toggle
#this will generalize to an n-burst toggle

e1b=0.5
e2b=0.5
p = 0
dur= 5

ut={}
ed={(100,'exc_1'):['pulse_b',15+dur,3+p,0,e1b],\
    (100,'exc_2'):['pulse_b',15+dur,3+p,0,e2b],\
    (400,'exc_1'):['pulse_b',15+dur,3+p,0,e1b],\
    (400,'exc_2'):['pulse_b',15+dur,3+p,0,e2b],\
    (0, 'exc_1'):['ramp',e1b,0],\
    (0, 'exc_2'):['ramp',e2b,0],\
    (0, 'inh_1'):['ramp',-0.5,0],\
    (0, 'inh_2'):['ramp',-0.5,0]}
exec_conf([30,65,200,5], ID=3435, update_tar=ut)
exec_pro(ID=3435,output_Spike=False, trial_t=1000, output_MemPot=True, event_dic=ed, MemPot='2-toggle.dat',\
		output_Frate = False)

subprocess.Popen("./flysim07_21_2.out -conf network.conf -pro network.pro -nmodel LIF -dt .05", shell = True).wait()
subplot(fname='MemPot.dat', cols=[1,2,3,4])
