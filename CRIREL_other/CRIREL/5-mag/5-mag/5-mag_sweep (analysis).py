import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import dynalysis.basics as bcs
import dynalysis.classes as clss
from dynalysis.visualization import subplot

mother = os.getcwd(); b_graph = clss.branch('graphs', mother); b_graph.mkdir()
for bias in list(np.arange(0,-0.00751,-0.001))+[-0.00751]:
	b2 = clss.branch('bias='+str(bias), mother)
	subplot(fname=os.path.join(b2.pathlink, 'MemPot.dat'),\
			outputfigname=os.path.join(b_graph.pathlink, 'bias='+str(bias)+'.png'))

if False:
	fig, ax2 = plt.subplots()
	color = 'k'
	ax2.set_xlabel('time (s)')
	ax2.set_ylabel('ISI of $I_1$ (ms)', color=color)  # we already handled the x-label with ax1
	ax2.plot(np.arange(-0.25, 0.75+0.1, 0.1), np.array(I_meanISI)*1000, color=color, linewidth=2.5, marker='o')
	ax2.tick_params(axis='y', labelcolor=color)
	ax2.spines['top'].set_visible(False)
	ax2.spines['right'].set_visible(False)

	fig.tight_layout()  # otherwise the right y-label is slightly clipped
	plt.savefig('2-sCPG.png', dpi=600)




			