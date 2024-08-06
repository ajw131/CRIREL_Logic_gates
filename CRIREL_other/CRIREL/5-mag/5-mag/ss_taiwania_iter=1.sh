#!/bin/bash

##################################
for d in ./*/ ; do
	
	#enter file
	cp flysim.out $d
	cd $d
	echo File: $d

	#run flysim
	./flysim.out -pro network.pro -conf network.conf -t 4 -s moderate -nmodel LIF
	rm ConfsInfo.log
	rm network.log
	rm flysim.out
	#leave param_file
	cd ..

done
##################################
