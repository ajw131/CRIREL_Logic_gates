import subprocess
import dynalysis.basics as bcs
import dynalysis.classes as clss
from dynalysis.gen_conf import exec_conf
from dynalysis.gen_pro import exec_pro
from dynalysis.visualization import subplot, edplot

#low has bias i_1 and i_2 = 0

ed={'inh_2':{'Taum':80, 'C':1}, 'inh_1':{}}
ut={'exc_1':[['inh_2','AMPA',1,25,1],['inh_1','AMPA',1,20,1]],\
    'inh_2':[['inh_1','GABA',1,30,1]]}
edp={(100,'exc_1'):['pulse',50,1,0],\
     (300,'exc_1'):['pulse',50,1.5,0],\
     (500,'exc_1'):['pulse',50,2,0],\
     (700,'exc_1'):['pulse',50,2.5,0],\
     (900,'exc_1'):['pulse',50,3,0],\
     (1100,'exc_1'):['pulse',50,3.5,0],\
     (1300,'exc_1'):['pulse',50,4,0],\
     (1500,'exc_1'):['pulse',50,4.5,0]}
exec_conf([0,50,4000,70], ID=2447, update_tar=ut, event_dic=ed)
exec_pro(ID=2447,output_Spike=False, trial_t=2000, output_MemPot=True, event_dic=edp, MemPot='5-mag.dat',\
		output_Frate = False)


subprocess.Popen("./flysim07_21_2.out -conf network.conf -pro network.pro -nmodel LIF -dt .05", shell = True).wait()
subplot(fname='MemPot.dat', cols=[1,2,3,4])
