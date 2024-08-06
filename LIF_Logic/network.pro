%(2, 'ChangeMembraneNoise', 'buffer', 0.1, 0)
%(2, 'ChangeMembraneNoise', 'eo', 0.5, 0)
%(2, 'ChangeMembraneNoise', 'e1', 2.75, 0)
%(2, 'ChangeMembraneNoise', 'e2', 2.75, 0)
%(2, 'ChangeMembraneNoise', 'i1', 4.75, 0)
%(2, 'ChangeMembraneNoise', 'i2', 4.75, 0)
%(800, 'ChangeMembraneNoise', 'inp1', 1.2, 1)
%(800, 'ChangeMembraneNoise', 'inp2', 1.2, 1)
%(1600, 'ChangeMembraneNoise', 'inp1', 0, 0)
%(1600, 'ChangeMembraneNoise', 'inp2', 0, 0)
%(2400, 'ChangeMembraneNoise', 'inp1', 1.2, 1)
%(2410.0, 'ChangeMembraneNoise', 'inp2', 1.2, 1)
%(3200, 'ChangeMembraneNoise', 'inp1', 0, 0)
%(3200, 'ChangeMembraneNoise', 'inp2', 0, 0)
%(4010.0, 'ChangeMembraneNoise', 'inp1', 1.2, 1)
%(4000, 'ChangeMembraneNoise', 'inp2', 1.2, 1)
%(4800, 'ChangeMembraneNoise', 'inp1', 0, 0)
%(4800, 'ChangeMembraneNoise', 'inp2', 0, 0)
%(5600, 'ChangeMembraneNoise', 'inp1', 0, 0)
%(5610.0, 'ChangeMembraneNoise', 'inp2', 0, 0)
%(6400, 'ChangeMembraneNoise', 'inp1', 0, 0)
%(6400, 'ChangeMembraneNoise', 'inp2', 0, 0)
%(6500, 'EndTrial')

%--------------------------------

EventTime 2
Type=ChangeMembraneNoise
Population: buffer
GaussMean=0.1
GaussSTD=0
EndEvent

EventTime 2
Type=ChangeMembraneNoise
Population: eo
GaussMean=0.5
GaussSTD=0
EndEvent

EventTime 2
Type=ChangeMembraneNoise
Population: e1
GaussMean=2.75
GaussSTD=0
EndEvent

EventTime 2
Type=ChangeMembraneNoise
Population: e2
GaussMean=2.75
GaussSTD=0
EndEvent

EventTime 2
Type=ChangeMembraneNoise
Population: i1
GaussMean=4.75
GaussSTD=0
EndEvent

EventTime 2
Type=ChangeMembraneNoise
Population: i2
GaussMean=4.75
GaussSTD=0
EndEvent

EventTime 800
Type=ChangeMembraneNoise
Population: inp1
GaussMean=1.2
GaussSTD=1
EndEvent

EventTime 800
Type=ChangeMembraneNoise
Population: inp2
GaussMean=1.2
GaussSTD=1
EndEvent

EventTime 1600
Type=ChangeMembraneNoise
Population: inp1
GaussMean=0
GaussSTD=0
EndEvent

EventTime 1600
Type=ChangeMembraneNoise
Population: inp2
GaussMean=0
GaussSTD=0
EndEvent

EventTime 2400
Type=ChangeMembraneNoise
Population: inp1
GaussMean=1.2
GaussSTD=1
EndEvent

EventTime 2410.0
Type=ChangeMembraneNoise
Population: inp2
GaussMean=1.2
GaussSTD=1
EndEvent

EventTime 3200
Type=ChangeMembraneNoise
Population: inp1
GaussMean=0
GaussSTD=0
EndEvent

EventTime 3200
Type=ChangeMembraneNoise
Population: inp2
GaussMean=0
GaussSTD=0
EndEvent

EventTime 4010.0
Type=ChangeMembraneNoise
Population: inp1
GaussMean=1.2
GaussSTD=1
EndEvent

EventTime 4000
Type=ChangeMembraneNoise
Population: inp2
GaussMean=1.2
GaussSTD=1
EndEvent

EventTime 4800
Type=ChangeMembraneNoise
Population: inp1
GaussMean=0
GaussSTD=0
EndEvent

EventTime 4800
Type=ChangeMembraneNoise
Population: inp2
GaussMean=0
GaussSTD=0
EndEvent

EventTime 5600
Type=ChangeMembraneNoise
Population: inp1
GaussMean=0
GaussSTD=0
EndEvent

EventTime 5610.0
Type=ChangeMembraneNoise
Population: inp2
GaussMean=0
GaussSTD=0
EndEvent

EventTime 6400
Type=ChangeMembraneNoise
Population: inp1
GaussMean=0
GaussSTD=0
EndEvent

EventTime 6400
Type=ChangeMembraneNoise
Population: inp2
GaussMean=0
GaussSTD=0
EndEvent

EventTime 6500
Type=EndTrial
EndEvent


%--------------------------------

OutControl

FileName: MemPot.dat
Type=MemPot
population=AllPopulation
EndOutputFile

FileName: SpikeALL.dat
Type=Spike
population=AllPopulation
EndOutputFile

FileName: FiringRateALL.dat
Type=FiringRate
population=AllPopulation
FiringRateWindow=50
PrintStep=10
EndOutputFile

EndOutControl
