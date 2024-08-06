import subprocess
import dynalysis.basics as bcs
import dynalysis.classes as clss
from dynalysis.gen_conf import exec_conf
from dynalysis.gen_pro import exec_pro
from dynalysis.visualization import subplot, edplot

'''
How does the frequency of this CPG depend on the input?
'''

p = 2  #-2 (or 2)

dur= 10 #


#PLOT this
#anti toggle
# i =  2#2
# e=-1.5 #-1

#PLOT this
#anti toggle 2 (p=2)
# i = 0
# e = -1.5

#cpg (heh?)
#i = 2 #2
#e=-0#-1

#semi-sync (?)
#i = -1.16 #2
#e=- 1.7#-1

#PLOT this
#anti-sync 1
i = -1.16 #2
e=- 1.8#-1

#antisync 2
# i = -1.0 #2
# e=- 1.75#-1


#semi-sync cpg ee=50
# q= -.5
# i = 0+q #.7
# e= -1+q


# #PLOT this
# # #toggle p =2
# q= -.5
# i = 0+q -1. #.7
# e= -1.4+q +0

ut={}
 #15,15

#
# ed={(0, 'inh_1'):['pulse_b',1.5,7,0,i],\
#     (200,'inh_1'):['pulse_b',+dur,i+p,0,+i],\
#     (200,'inh_2'):['pulse_b',+dur,i+p,0,i],\
#     (500,'inh_1'):['pulse_b',+dur,i+p,0,+i],\
#     (500,'inh_2'):['pulse_b',+dur,i+p,0,i],\
#     (800,'inh_2'):['pulse_b',+dur,i+p,0,+i],\
#     (800,'inh_1'):['pulse_b',+dur,i+p,0,i],\
#     (2, 'exc_1'):['ramp',2.4+e,0],\
#     (2, 'exc_2'):['ramp',2.4+e,0],\
#     (2, 'inh_1'):['ramp',i,0],\
#     (2, 'inh_2'):['ramp',i,0]}

#for toggle and synchronized

# ed={(200,'exc_1'):['pulse_b',+dur,2.4+e+p,0,2.4+e],\
#     (200,'exc_2'):['pulse_b',+dur,2.4+e+p,0,2.4+e],\
#     (500,'exc_1'):['pulse_b',+dur,2.4+e+p,0,2.4+e],\
#     (500,'exc_2'):['pulse_b',+dur,2.4+e+p,0,2.4+e],\
#     (800,'exc_2'):['pulse_b',+dur,2.4+e+p,0,2.4+e],\
#     (800,'exc_1'):['pulse_b',+dur,2.4+e+p,0,2.4+e],\
#     (2, 'exc_1'):['ramp',2.4+e,0],\
#     (2, 'exc_2'):['ramp',2.4+e,0],\
#     (2, 'inh_1'):['ramp',i,0],\
#     (2, 'inh_2'):['ramp',i,0]}

#for magnitude
# e=-5
# i =-2
#
# ed={(100,'exc_1'):['pulse_b',75,.5,0,2.4+e],\
#      (300,'exc_1'):['pulse_b',75,1.,0,2.4+e],\
#      (500,'exc_1'):['pulse_b',75,1.5,0,2.4+e],\
#      (700,'exc_1'):['pulse_b',75,2.5,0,2.4+e],\
#      (900,'exc_1'):['pulse_b',75,3,0,2.4+e],\
#      (1100,'exc_1'):['pulse_b',75,3.5,0,2.4+e],\
#      (1300,'exc_1'):['pulse_b',75,4,0,2.4+e],\
#      (1500,'exc_1'):['pulse_b',75,6,0,2.4+e],\
#      (2, 'exc_1'):['ramp',2.4+e,0],\
#      (2, 'exc_2'):['ramp',2.4+e+2,0],\
#      (2, 'inh_1'):['ramp',i,0],\
#      (2, 'inh_2'):['ramp',i-1,0]}
#





print p
exec_conf([70,70,70 ,70], ID=3435)
exec_pro(ID=3435,output_Spike=False, trial_t=2000, output_MemPot=True, event_dic=ed, MemPot='3-aCPG.dat',\
		output_Frate = False)


print 'hi'
subprocess.Popen("./flysim07_21_2.out -conf network.conf -pro network.pro -nmodel LIF -dt .05", shell = True).wait()
subplot(fname='MemPot.dat', cols=[1,2,3,4])

print 'done'
7
