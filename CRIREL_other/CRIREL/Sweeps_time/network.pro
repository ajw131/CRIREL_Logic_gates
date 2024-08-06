EventTime 2
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=4.9500000000000055
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2
Type=ChangeMembraneNoise
Label=#1#
Population:exc_2
GaussMean=4.9500000000000055
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2
Type=ChangeMembraneNoise
Label=#1#
Population:exc_5
GaussMean=-0.1
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2
Type=ChangeMembraneNoise
Label=#1#
Population:inh_1
GaussMean=4.949999999999972
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2
Type=ChangeMembraneNoise
Label=#1#
Population:inh_2
GaussMean=4.949999999999972
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 100
Type=ChangeMembraneNoise
Label=#1#
Population:exc_3
GaussMean=1
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1100.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_3
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 100
Type=ChangeMembraneNoise
Label=#1#
Population:exc_4
GaussMean=1
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1100.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_4
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1600
Type=ChangeMembraneNoise
Label=#1#
Population:exc_4
GaussMean=1
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2600.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_4
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1605
Type=ChangeMembraneNoise
Label=#1#
Population:exc_3
GaussMean=1
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2605.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_3
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 3100
Type=ChangeMembraneNoise
Label=#1#
Population:exc_3
GaussMean=1
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 4100.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_3
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 3105
Type=ChangeMembraneNoise
Label=#1#
Population:exc_4
GaussMean=1
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 4105.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_4
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 5600
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
