import sciunit
import capabilities as cap
import scores 
#===============================================================================


class Test(sciunit.Test):
    """ Extension of sciunit.nest by adding the parameter sheet """


    def __init__(self,
                 observation = None,
                 sheet = None,
                 contrast = 100,
		 name = "Test1"):

        self.sheet=sheet
	self.contrast=contrast
        sciunit.Test.__init__(self, observation, name)


class ExcitatoryAverageFiringRate(Test):
    """Test the if the distribution of the sheet average firing rates is significatively lesser than a predefined value"""

    score_type = scores.StudentsTestScore
    """specifies the type of score returned by the test"""

    description = "Test  if the sheet average firing rate is lesser than a predifined value"

    def __init__(self,
                 observation = None,
		 sheet = None,
                 name = "Excitatory Average Firing Rate Test"):
	
	self.required_capabilities += (cap.StatsSheetFiringRate,)
        Test.__init__(self,observation, sheet, name=name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
        
	try:
        	assert (isinstance(observation, int) or isinstance(observation, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a float or an integer"))
        	
    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction=model.stats_sheet_firing_rate(self.sheet)
        if type(prediction).__module__=="numpy":
		prediction=prediction.item()
        return prediction

    #----------------------------------------------------------------------
    def compute_score(self, observation, prediction):
	score = scores.StudentsTestScore.compute(observation, prediction)
     	return score



class InhibitoryAverageFiringRate(Test):
    """Test the if the sheet average firing rates is significantly greater than the average firing rates 
	of a predefined distribution"""

    score_type = scores.StudentsTestScore
    """specifies the type of score returned by the test"""

    description = "Test if the sheet average firing rate is greater than a predefined value"

    def __init__(self,
                 observation = None,
		 sheet = None,
                 name = "Inhibitory Average Firing Rate Test"):

        self.required_capabilities += (cap.StatsSheetFiringRate,)
        Test.__init__(self, observation, sheet, name=name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
	try:
            assert len(observation.keys()) == 3
            for key, val in observation.items():
                assert key in ["mean", "std","n"]
                if key =="n":
                        assert (isinstance(val, int))
                else:
                        assert (isinstance(val, int) or isinstance(val, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a dictionary of the form:"
                 "{'mean': NUM1, 'std': NUM2, 'n' : NUM3}"))
    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction=model.stats_sheet_firing_rate(self.sheet)
	if type(prediction).__module__=="numpy":
        	prediction=prediction.item()
        return prediction

    #----------------------------------------------------------------------
    def compute_score(self, observation, prediction):
        score = scores.StudentsTestScore.compute(observation, prediction)
	return score


class DistributionAverageFiringRate(Test):
    """Test the if the sheet average firing rates distributions is significatively different 
    than a specific distribution"""

    score_type = scores.ShapiroTestScore
    """specifies the type of score returned by the test"""

    description = """Test if the sheet average firing rates distributions is significatively different 
    than a specific distribution""" 

    def __init__(self,
                 observation = None,
                 sheet = None,
                 name = "Distribution Average Firing Rate Test"):

        self.required_capabilities += (cap.SheetFiringRate,)
        Test.__init__(self, observation, sheet, name=name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
        try:
            assert isinstance(observation, str)
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation should be a string containing the name of the distribution the average firing rates should be compared to, either: 'normal' or 'lognormal'"))
    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction=model.sheet_firing_rate(self.sheet)
        return prediction

    #----------------------------------------------------------------------
    def compute_score(self, observation, prediction):
        score = scores.ShapiroTestScore.compute(observation, prediction)
        return score


class CorrelationCoefficient(Test):
    """Test the if the sheet distribution correlation coefficient is significatively greater than a predefined distribution"""

    score_type = scores.StudentsTestScore
    """specifies the type of score returned by the test"""

    description = "Test if the sheet correlation coefficient is greater than a predefined value"

    def __init__(self,
                 observation = None,
                 sheet = None,
                 name = "Correlation Coefficient Test"):

        if type(observation).__module__=="numpy":
                observation=observation.item()

        self.required_capabilities += (cap.SheetCorrelationCoefficient,)
        Test.__init__(self, observation, sheet, name=name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
        try:
            assert len(observation.keys()) == 3 
            for key, val in observation.items():
		assert key in ["mean", "std","n"]
		if key =="n":
                	assert (isinstance(val, int))
		else:
                	assert (isinstance(val, int) or isinstance(val, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a dictionary of the form:"
                 "{'mean': NUM1, 'std': NUM2, 'n' : NUM3}"))
    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction=model.sheet_correlation_coefficient(self.sheet)
        if type(prediction).__module__=="numpy":
                prediction=prediction.item()
        return prediction

    #----------------------------------------------------------------------
    def compute_score(self, observation, prediction):
        score = scores.StudentsTestScore.compute(observation, prediction)
        return score



class CV_ISI(Test):
    """Test the if the sheet distribution of its coefficient of variation
	 is significatively greater than a predefined distribution"""

    score_type = scores.StudentsTestScore
    """specifies the type of score returned by the test"""

    description = "Test if the sheet coefficient of variation of its interspike intervals is greater than a predefined value"

    def __init__(self,
                 observation = None,
                 sheet = None,
                 name = "Coefficient of Variation of Interspike Intervals Test"):

        if type(observation).__module__=="numpy":
                observation=observation.item()

        self.required_capabilities += (cap.SheetCVISI,)
        Test.__init__(self, observation, sheet, name=name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
        try:
                assert (isinstance(observation, int) or isinstance(observation, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a float or an integer"))

    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction=model.sheet_CV_ISI(self.sheet)
        if type(prediction).__module__=="numpy":
                prediction=prediction.item()
        return prediction

    #----------------------------------------------------------------------
    def compute_score(self, observation, prediction):
        score = scores.StudentsTestScore.compute(observation, prediction)
        return score





class RestingPotential(Test):
    """Test the sheets' average resting membrane potential"""

    #score_type = sciunit.scores.CohenDScore
    score_type = scores.StudentsTestScore
    """specifies the type of score returned by the test"""

    description = ("Test the sheets' average resting membrane potential")

    def __init__(self,
                 observation,
		 sheet, 
                 name ="Sheets Resting Membrane Potential Test"):
        self.required_capabilities += (cap.SheetsMembranePotential,)
	Test.__init__(self, observation, sheet, name=name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
        try:
            assert len(observation.keys()) == 3 
            for key, val in observation.items():
		assert key in ["mean", "std","n"]
		if key =="n":
                	assert (isinstance(val, int))
		else:
                	assert (isinstance(val, int) or isinstance(val, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a dictionary of the form:"
                 "{'mean': NUM1, 'std': NUM2, 'n' : NUM3}"))

    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction = model.sheets_membrane_potential(self.sheet)
        return prediction

    #----------------------------------------------------------------------

    def compute_score(self, observation, prediction):
	score = scores.StudentsTestScore.compute(observation, prediction)
        return score

class ExcitatorySynapticConductance(Test):
    """Test the sheets' average excitatory synaptic conductance"""

    score_type = scores.StudentsTestScore 
    """specifies the type of score returned by the test"""

    description = ("Test the sheets' average excitatory synaptic conductance")

    def __init__(self,
                 observation,
                 sheet,
                 name ="Sheets Excitatory Synaptic Conductance Test"):
        self.required_capabilities += (cap.SheetsExcitatorySynapticConductance,)
        Test.__init__(self, observation, sheet, name=name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
        try:
            assert len(observation.keys()) == 3
            for key, val in observation.items():
                assert key in ["mean", "std","n"]
                if key =="n":
                        assert (isinstance(val, int))
                else:
                        assert (isinstance(val, int) or isinstance(val, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a dictionary of the form:"
                 "{'mean': NUM1, 'std': NUM2, 'n' : NUM3}"))

    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction = model.sheets_excitatory_synaptic_conductance(self.sheet)
        return prediction

    #----------------------------------------------------------------------

    def compute_score(self, observation, prediction):
	score = scores.StudentsTestScore.compute(observation, prediction)
        return score

class InhibitorySynapticConductance(Test):
    """Test the sheet' average inhibitory synaptic conductance"""

    score_type = scores.StudentsTestScore
    """specifies the type of score returned by the test"""

    description = ("Test the sheet' average inhibitory synaptic conductance")

    def __init__(self,
                 observation,
                 sheet,
                 name ="Sheets Inhibitory Synaptic Conductance Test"):
        self.required_capabilities += (cap.SheetsInhibitorySynapticConductance,)
        Test.__init__(self, observation, sheet, name=name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
        try:
            assert len(observation.keys()) == 3
            for key, val in observation.items():
                assert key in ["mean", "std","n"]
                if key =="n":
                        assert (isinstance(val, int))
                else:
                        assert (isinstance(val, int) or isinstance(val, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a dictionary of the form:"
                 "{'mean': NUM1, 'std': NUM2, 'n' : NUM3}"))

    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction = model.sheets_inhibitory_synaptic_conductance(self.sheet)
        return prediction

    #----------------------------------------------------------------------

    def compute_score(self, observation, prediction):
        score = scores.StudentsTestScore.compute(observation, prediction)
        return score



class HWHH(Test):
    """Test the if the sheet Half-Width at Half-Weight is significantly different than a predefined distribution"""

    score_type = scores.StudentsTestScore
    """specifies the type of score returned by the test"""

    description = "Test if the sheet Half-Width at Half-Height is significantly different than a predefined value"

    def __init__(self,
                 observation = None,
		 sheet = None,
		 contrast = None,
                 name = "Half-Width at Half-Height Test"):

        self.required_capabilities += (cap.SheetHWHH,)
        Test.__init__(self, observation, sheet, contrast, name=name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
	try:
            assert len(observation.keys()) == 3
            for key, val in observation.items():
                assert key in ["mean", "std","n"]
                if key =="n":
                        assert (isinstance(val, int))
                else:
                        assert (isinstance(val, int) or isinstance(val, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a dictionary of the form:"
                 "{'mean': NUM1, 'std': NUM2, 'n' : NUM3}"))
    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction=model.sheets_HWHH(self.sheet, self.contrast)
	if type(prediction).__module__=="numpy":
        	prediction=prediction.item()
        return prediction

    #----------------------------------------------------------------------
    def compute_score(self, observation, prediction):
        score = scores.StudentsTestScore.compute(observation, prediction)
	return score

class RURA(Test):
    """Test the if the sheet Relative Unselective Response Amplitude is significantly different than a predefined distribution"""

    score_type = scores.StudentsTestScore
    """specifies the type of score returned by the test"""

    description = "Test if the sheet Relative Unselective Response Amplitude is significantly different than a predefined value"

    def __init__(self,
                 observation = None,
		 sheet = None,
		 contrast = None,
                 name = "Relative Unselective Response Amplitude Test"):

        self.required_capabilities += (cap.SheetRURA,)
        Test.__init__(self, observation, sheet, contrast, name=name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
	try:
            assert len(observation.keys()) == 3
            for key, val in observation.items():
                assert key in ["mean", "std","n"]
                if key =="n":
                        assert (isinstance(val, int))
                else:
                        assert (isinstance(val, int) or isinstance(val, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a dictionary of the form:"
                 "{'mean': NUM1, 'std': NUM2, 'n' : NUM3}"))
    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction=model.sheets_RURA(self.sheet, self.contrast)
	if type(prediction).__module__=="numpy":
        	prediction=prediction.item()
        return prediction

    #----------------------------------------------------------------------
    def compute_score(self, observation, prediction):
        score = scores.StudentsTestScore.compute(observation, prediction)
	return score

class F0Vm(Test):
    """Test the if the sheets F0 component of the membrane potential is significantly different than a predefined distribution"""

    score_type = scores.StudentsTestScore
    """specifies the type of score returned by the test"""

    description = "Test if the sheets F0 component of the membrane potential is significantly different than a predefined value"

    def __init__(self,
                 observation = None,
		 sheet = None,
		 contrast = None,
                 name = "F0 Vm Test"):

        self.required_capabilities += (cap.SheetF0Vm,)

        Test.__init__(self, observation, sheet, contrast, name=name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
	try:
            assert len(observation.keys()) == 3
            for key, val in observation.items():
                assert key in ["mean", "std","n"]
                if key =="n":
                        assert (isinstance(val, int))
                else:
                        assert (isinstance(val, int) or isinstance(val, float))
        except Exception:
            raise sciunit.errors.ObservationError(
                ("Observation must return a dictionary of the form:"
                 "{'mean': NUM1, 'std': NUM2, 'n' : NUM3}"))
    #----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction=model.sheets_F0Vm(self.sheet, self.contrast)
	if type(prediction).__module__=="numpy":
        	prediction=prediction.item()
        return prediction

    #----------------------------------------------------------------------
    def compute_score(self, observation, prediction):
        score = scores.StudentsTestScore.compute(observation, prediction)
	return score



class ModulationRatioVm(Test):
    """Test the if the sheets modulation ratio computed from the membrane potential is significantly different than a predefined distribution"""

    score_type = scores.StudentsTestScore
    """specifies the type of score returned by the test"""

    description = "Test if the sheets modulation ratio computed from the membrane potential is significantly different than a predefined value"

    def __init__(self,
                 observation = None,
                 sheet = None,
                 contrast = None,
                 name = "Modulation ratio membrane potential Test"):

        self.required_capabilities += (cap.SheetModulationRatioVm,)

        Test.__init__(self, observation, sheet, contrast, name=name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
        if not (isinstance(observation, int) or isinstance(observation, float)):
                try:
                    assert len(observation.keys()) == 3
                    for key, val in observation.items():
                        assert key in ["mean", "std","n"]
                        if key =="n":
                                assert (isinstance(val, int))
                        else:
                                assert (isinstance(val, int) or isinstance(val, float))
                except Exception:
                    raise sciunit.errors.ObservationError(
                        ("Observation must return a float, an integern or a dictionary of the form:"
                         "{'mean': NUM1, 'std': NUM2, 'n' : NUM3}"))
#----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction=model.sheets_modulation_ratio_Vm(self.sheet, self.contrast)
        if type(prediction).__module__=="numpy":
                prediction=prediction.item()
        return prediction

    #----------------------------------------------------------------------
    def compute_score(self, observation, prediction):
        score = scores.StudentsTestScore.compute(observation, prediction)
        return score




class ModulationRatio(Test):
    """Test the if the sheets modulation ratio computed from the PSTH is significantly different than a predefined distribution"""

    score_type = scores.StudentsTestScore
    """specifies the type of score returned by the test"""

    description = "Test if the sheets modulation ratio computed from the PSTH is significantly different than a predefined value"

    def __init__(self,
                 observation = None,
                 sheet = None,
                 contrast = None,
		 name = "Modulation ratio PSTH Test"):

        self.required_capabilities += (cap.SheetModulationRatio,)

        Test.__init__(self, observation, sheet, contrast, name=name)

    #----------------------------------------------------------------------

    def validate_observation(self, observation):
        if not (isinstance(observation, int) or isinstance(observation, float)):
		try:
	            assert len(observation.keys()) == 3
	            for key, val in observation.items():
	                assert key in ["mean", "std","n"]
	                if key =="n":
	                        assert (isinstance(val, int))
	                else:
	                        assert (isinstance(val, int) or isinstance(val, float))
	        except Exception:
	            raise sciunit.errors.ObservationError(
	                ("Observation must return a float, an integern or a dictionary of the form:"
	                 "{'mean': NUM1, 'std': NUM2, 'n' : NUM3}"))
#----------------------------------------------------------------------

    def generate_prediction(self, model):
        prediction=model.sheets_modulation_ratio(self.sheet, self.contrast)
        if type(prediction).__module__=="numpy":
                prediction=prediction.item()
        return prediction

    #----------------------------------------------------------------------
    def compute_score(self, observation, prediction):
        score = scores.StudentsTestScore.compute(observation, prediction)
        return score
