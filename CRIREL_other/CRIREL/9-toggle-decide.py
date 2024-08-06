import subprocess
import dynalysis.basics as bcs
import dynalysis.classes as clss
from dynalysis.gen_conf import exec_conf
from dynalysis.gen_pro import exec_pro
from dynalysis.visualization import subplot, edplot

'''
How does the frequency of this CPG depend on the input?
'''
p =-2 #lowest 1.5 on 95, higest seems unbounded.
#start sweep from -1

dur= 05 #sweep from 75(onset) to as high as you want. Steps in 5 ms
#prolly want to start the sweep lower than 60. Prolly 0?
i = 2
e=-1
ut={}
ed={(0, 'inh_1'):['pulse_b',15,5,0,i],\
    (200,'inh_1'):['pulse_b',+dur,i+p,0,+i],\
    (200,'inh_2'):['pulse_b',+dur,i+p,0,i],\
    (500,'inh_1'):['pulse_b',+dur,i+p,0,+i],\
    (500,'inh_2'):['pulse_b',+dur,i+p,0,i],\
    (800,'inh_2'):['pulse_b',+dur,i+p,0,+i],\
    (800,'inh_1'):['pulse_b',+dur,i+p,0,i],\
    (2, 'exc_1'):['ramp',2.4+e,0],\
    (2, 'exc_2'):['ramp',2.4+e,0],\
    (2, 'inh_1'):['ramp',i,0],\
    (2, 'inh_2'):['ramp',i,0]}
exec_conf([70,10,70,70], ID=3435)
exec_pro(ID=3435,output_Spike=False, trial_t=1100, output_MemPot=True, event_dic=ed, MemPot='3-aCPG.dat',\
		output_Frate = False)


print 'hi'
subprocess.Popen("./flysim07_21_2.out -conf network.conf -pro network.pro -nmodel LIF -dt .05", shell = True).wait()
subplot(fname='MemPot.dat', cols=[1,2,3,4])

print 'done'
7
