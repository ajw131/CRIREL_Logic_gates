import dynalysis.classes as clss
from dynalysis.iA2B import tpe_ut_dic, tpe_bias_dic, synwgt_dic

tpe_ut_dic={'Logic':[30,30,30,30,60,30,60,30]}
tpe_bias_dic={'AND':[0,0,-0.2,-0.2],\
              'OR':[]}

def update_ut_by_motif(motif, synwgt, ut, gate):
    #e1e2,e1i1,e2e1,e2i2,i1e1,i1i2,i2e2,i2i1
    c, reclist=0, ['AMPA','AMPA','AMPA','AMPA','GABA','GABA','GABA','GABA']
    for pair in motif.pairlist:
        pre, post = clss.convert_neuname(pair[0], motif.name), clss.convert_neuname(pair[1], motif.name)
        if pre not in ut.keys(): ut[pre]=[]
        ut[pre].append([post,reclist[c],1,synwgt[gate][c],1])
        c+=1
    return ut

def update_bias_by_motif(motif, tpe_bias_dic, bias, gate):
    #e1,e2,i1,i2
    c=0
    for neu in motif.neulist:
        neuron = clss.convert_neuname(neu, motif.name)
        if (0, neuron) in bias.keys():
            print('Repeated bias current detected!') 
            print(bias.keys())
        bias[(0,neuron)]=['ramp',tpe_bias_dic[gate][c],0]
        c+=1
    return bias

ut = {}; bias = {}
mot = clss.motif(3435)
ut = update_ut_by_motif(mot, tpe_ut_dic, ut, 'Logic')
bias = update_bias_by_motif(mot, tpe_bias_dic, bias, 'AND')

