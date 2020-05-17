from models import *
from tests import *
from helper_functions import *
import sys


#newModel=ModelV1Spont(sys.argv[1])
newModel=ModelV1DriftingGratings(sys.argv[1])

newTest=ModulationRatio(1,"V1_Exc_L4", 100)
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=ModulationRatio(1,"V1_Exc_L2/3", 100)
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=ModulationRatio(newModel.sheets_modulation_ratio( "V1_Exc_L2/3",100),"V1_Exc_L4", 100)
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=ModulationRatioVm(1,"V1_Exc_L4", 100)
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=ModulationRatioVm(1,"V1_Exc_L2/3", 100)
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=ModulationRatioVm(newModel.sheets_modulation_ratio_Vm( "V1_Exc_L2/3",100),"V1_Exc_L4", 100)
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=HWHH({"mean": 23.4, "std": besselCorrection(9.2,58), "n": 58},["V1_Exc_L4", "V1_Exc_L2/3"], 100)
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=HWHH({"mean": 31.8, "std": besselCorrection(11.3,19), "n": 19},["V1_Inh_L4", "V1_Inh_L2/3"], 100)
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=HWHH(newModel.sheets_HWHH(["V1_Exc_L4", "V1_Exc_L2/3"], 30),["V1_Exc_L4", "V1_Exc_L2/3"], 100)
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=HWHH(newModel.sheets_HWHH(["V1_Inh_L4", "V1_Inh_L2/3"], 30),["V1_Inh_L4", "V1_Inh_L2/3"], 100)
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=RURA({"mean": 2.5, "std": besselCorrection(8.5,58), "n": 58},["V1_Exc_L4", "V1_Exc_L2/3"],100)
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=RURA({"mean": 18.1, "std": besselCorrection(25.7,19), "n": 19},["V1_Inh_L4", "V1_Inh_L2/3"],100)
score= newTest.judge(newModel, deep_error=True)
score.summarize()


newTest=ExcitatoryAverageFiringRate(2,"V1_Exc_L4")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=InhibitoryAverageFiringRate(newModel.stats_sheet_firing_rate("V1_Exc_L4"),"V1_Inh_L4")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=ExcitatoryAverageFiringRate(2,"V1_Exc_L2/3")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=InhibitoryAverageFiringRate(newModel.stats_sheet_firing_rate("V1_Exc_L2/3"),"V1_Inh_L2/3")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=DistributionAverageFiringRate("lognormal","V1_Exc_L4")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=DistributionAverageFiringRate("lognormal","V1_Inh_L4")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=DistributionAverageFiringRate("lognormal","V1_Exc_L2/3")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=DistributionAverageFiringRate("lognormal","V1_Inh_L2/3")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=CorrelationCoefficient(newModel.sheet_correlation_coefficient("V1_Exc_L4"),"V1_Inh_L4")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=CorrelationCoefficient(newModel.sheet_correlation_coefficient("V1_Exc_L2/3"),"V1_Inh_L2/3")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=CV_ISI(0.8,"V1_Exc_L4")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=CV_ISI(0.8,"V1_Inh_L4")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=CV_ISI(0.8,"V1_Exc_L2/3")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=CV_ISI(0.8,"V1_Inh_L2/3")
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=RestingPotential({"mean": -72.8, "std": besselCorrection(5,119), "n": 119},["V1_Exc_L4", "V1_Inh_L4", "V1_Exc_L2/3", "V1_Inh_L2/3"])
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=ExcitatorySynapticConductance({"mean": 0.001, "std": besselCorrection(0.0009,22), "n": 22},["V1_Exc_L4", "V1_Inh_L4", "V1_Exc_L2/3", "V1_Inh_L2/3"])
score= newTest.judge(newModel, deep_error=True)
score.summarize()

newTest=InhibitorySynapticConductance({"mean": 0.0049, "std": besselCorrection(0.0036,22), "n": 22},["V1_Exc_L4", "V1_Inh_L4", "V1_Exc_L2/3", "V1_Inh_L2/3"])
score= newTest.judge(newModel, deep_error=True)
score.summarize()
