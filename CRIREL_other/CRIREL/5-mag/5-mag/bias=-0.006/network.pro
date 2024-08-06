EventTime 2
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=-0.0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2
Type=ChangeMembraneNoise
Label=#1#
Population:exc_2
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2
Type=ChangeMembraneNoise
Label=#1#
Population:inh_1
GaussMean=-0.006
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 400
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=1
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 500.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=-0.0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 800
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=1.5
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 900.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=-0.0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1200
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1300.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=-0.0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1600
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=2.5
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1700.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=-0.0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2000
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=3
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2100.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=-0.0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2400
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=3.5
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2500.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=-0.0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2800
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=4
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2900.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=-0.0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 3200
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=4.5
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 3300.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=-0.0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 3600
Type=EndTrial
Label=End_of_the_trial
EndEvent

%--------------------------------------
DefineMacro
EndDefineMacro
%--------------------------------------
OutControl
FileName:MemPot.dat
Type=MemPot
population:AllPopulation
EndOutputFile
%--------------------------------------
EndOutControl
%--------------------------------------
