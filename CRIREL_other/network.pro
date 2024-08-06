EventTime 1
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 101.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1
Type=ChangeMembraneNoise
Label=#1#
Population:exc_2
GaussMean=2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 101.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_2
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1
Type=ChangeMembraneNoise
Label=#1#
Population:inh_1
GaussMean=1
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 101.0
Type=ChangeMembraneNoise
Label=#1#
Population:inh_1
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1000
Type=ChangeMembraneNoise
Label=#1#
Population:inh_2
GaussMean=1
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1100.0
Type=ChangeMembraneNoise
Label=#1#
Population:inh_2
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1500
Type=EndTrial
Label=End_of_the_trial
EndEvent

%--------------------------------------
DefineMacro
EndDefineMacro
%--------------------------------------
OutControl
FileName:Frate.txt
Type=FiringRate
FiringRateWindow=50
PrintStep=10
population:AllPopulation
EndOutputFile
%--------------------------------------
OutControl
FileName:MemPot.dat
Type=MemPot
population:AllPopulation
EndOutputFile
%--------------------------------------
EndOutControl
%--------------------------------------
