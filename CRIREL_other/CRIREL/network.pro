EventTime 2
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=-0.2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2
Type=ChangeMembraneNoise
Label=#1#
Population:exc_2
GaussMean=-0.2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2
Type=ChangeMembraneNoise
Label=#1#
Population:exc_5
GaussMean=-0.835
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2
Type=ChangeMembraneNoise
Label=#1#
Population:inh_1
GaussMean=-0.5
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2
Type=ChangeMembraneNoise
Label=#1#
Population:inh_2
GaussMean=-0.5
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 100
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=1.8
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1100.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=-0.2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 100
Type=ChangeMembraneNoise
Label=#1#
Population:exc_2
GaussMean=1.8
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1100.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_2
GaussMean=-0.2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 100
Type=ChangeMembraneNoise
Label=#1#
Population:inh_1
GaussMean=1.5
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1100.0
Type=ChangeMembraneNoise
Label=#1#
Population:inh_1
GaussMean=-0.2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 100
Type=ChangeMembraneNoise
Label=#1#
Population:inh_2
GaussMean=1.5
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 1100.0
Type=ChangeMembraneNoise
Label=#1#
Population:inh_2
GaussMean=-0.2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2100
Type=ChangeMembraneNoise
Label=#1#
Population:exc_2
GaussMean=1.8
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 3100.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_2
GaussMean=-0.2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2100
Type=ChangeMembraneNoise
Label=#1#
Population:inh_2
GaussMean=1.5
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 3100.0
Type=ChangeMembraneNoise
Label=#1#
Population:inh_2
GaussMean=-0.2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2101
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=1.8
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 3101.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=-0.2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 2101
Type=ChangeMembraneNoise
Label=#1#
Population:inh_1
GaussMean=1.5
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 3101.0
Type=ChangeMembraneNoise
Label=#1#
Population:inh_1
GaussMean=-0.2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 4100
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=1.8
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 5100.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_1
GaussMean=-0.2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 4100
Type=ChangeMembraneNoise
Label=#1#
Population:inh_1
GaussMean=1.5
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 5100.0
Type=ChangeMembraneNoise
Label=#1#
Population:inh_1
GaussMean=-0.2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 4101
Type=ChangeMembraneNoise
Label=#1#
Population:exc_2
GaussMean=1.8
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 5101.0
Type=ChangeMembraneNoise
Label=#1#
Population:exc_2
GaussMean=-0.2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 4101
Type=ChangeMembraneNoise
Label=#1#
Population:inh_2
GaussMean=1.5
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 5101.0
Type=ChangeMembraneNoise
Label=#1#
Population:inh_2
GaussMean=-0.2
GaussSTD=0
EndEvent
%--------------------------------------

EventTime 5500
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
