import subprocess
import dynalysis.basics as bcs
import dynalysis.classes as clss
from dynalysis.gen_conf import exec_conf
from dynalysis.gen_pro import exec_pro
from dynalysis.visualization import subplot, edplot

#dur must be 50 msec
# ibias must be from -.07 to 0 nA
#space is 500


space=500
bias = -.06
dur = 50
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

#exec_conf([0,50,4000,70], ID=2447, update_tar=ut, ev}
exec_conf([0,50,4000,70], ID=2447, update_tar=ut, event_dic=ed)
exec_pro(ID=2447,output_Spike=False, trial_t=2000, output_MemPot=True, event_dic=edp, MemPot='5-mag.dat',\
		output_Frate = False)


subprocess.Popen("./flysim07_21_2.out -conf network.conf -pro network.pro -nmodel LIF -dt .05", shell = True).wait()
subplot(fname='MemPot.dat', cols=[1,2,3,4])
