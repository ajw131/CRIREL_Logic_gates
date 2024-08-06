EventTime 100
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=1
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 150.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 300
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=1.5
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 350.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 500
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 550.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 700
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=2.5
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 750.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 900
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=3
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 950.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1100
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=3.5
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1150.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1300
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=4
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1350.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1500
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=4.5
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1550.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=0
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1600
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
