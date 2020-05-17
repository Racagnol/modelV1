import sciunit

#==============================================================================

class SheetFiringRate(sciunit.Capability):
    """Get the average firing rate of the sheet"""

    def sheet_firing_rate(self, sheet):
        """Model should implement this method such as to retrieve the average firing rate of its sheet of neurons passed in input 
	   sheet should be a string specifying the name of the sheet
        """
        raise NotImplementedError()


class StatsSheetFiringRate(SheetFiringRate):
    """ Get descriptibe statistics about the distribution of the average firing rates of the sheet """

    def stats_sheet_firing_rate(self, sheet):
        """Model should implement this method such as to retrieve descriptive statistics about the distribution of 
	the average firing rates of its sheet of neurons passed in input 
	   sheet should be a string specifying the name of the sheet
	"""
	raise NotImplementedError()

class SheetsMembranePotential(sciunit.Capability):
    """Get the average resting membrane potential of the sheets"""

    def sheets_membrane_potential(self, sheets):
        """Model should implement this method such as to retrieve the resting membrane potential 
	   of its sheets of neurons passed in input 
	   sheets should be a string or a list of strings specifying the name of the sheets
        """
        raise NotImplementedError()

class SheetsExcitatorySynapticConductance(sciunit.Capability):
    """Get the average excitatory synaptic conductance of the sheet"""

    def sheets_excitatory_synaptic_conductance(self, sheets):
        """Model should implement this method such as to retrieve the excitatory synaptic conductance 
	   of its sheets of neurons passed in input 
	   sheets should be a string or a list of strings specifying the name of the sheets
        """
        raise NotImplementedError()

class SheetsInhibitorySynapticConductance(sciunit.Capability):
    """Get the average inhibitory synaptic conductance of the sheets"""

    def sheets_inhibitory_synaptic_conductance(self, sheets):
        """Model should implement this method such as to retrieve the inhibitory synaptic conductance
	   of its sheets of neurons passed in input 
	   sheets should be a string or a list of strings specifying the name of the sheet
        """
        raise NotImplementedError()

class SheetCorrelationCoefficient(sciunit.Capability):
    """Get the correlation coefficient between the PSTH of all pair of neurons of the sheet"""

    def sheet_correlation_coefficient(self, sheets):
	""" Model should implement this method such as to retrieve the correlation coefficient
	    of its sheets of neurons passed in input
	    sheet should be a string specifying the name of the sheet
	"""
	raise NotImplementedError()

class SheetCVISI(sciunit.Capability):
    """Get the squared value coefficient variation of the interspike interval of the neurons of the sheet"""

    def sheet_CV_ISI(self, sheets):
        """ Model should implement this method such as to retrieve the coefficient variation of the interspike interval 
            of its sheets of neurons passed in input
            sheet should be a string specifying the name of the sheet
        """
        raise NotImplementedError()


class SheetHWHH(sciunit.Capability):
    """Get the Half-Width at Half-Height of the orientation tuning curve of the neurons of the sheet"""

    def sheets_HWHH(self, sheets):
        """ Model should implement this method such as to retrieve the Half-Width at Half-Height
            of its sheets of neurons passed in input
            sheet should be a string specifying the name of the sheet
            contrast should be an int or a float specifying the value of contrast of the stimulus
        """
        raise NotImplementedError()

class SheetRURA(sciunit.Capability):
    """Get the Relative Unselective Response Amplitude  of the neurons of the sheet"""

    def sheets_RURA(self, sheets):
        """ Model should implement this method such as to retrieve the Relative Unselective Response Amplitude 
            of its sheets of neurons passed in input
            sheet should be a string specifying the name of the sheet
            contrast should be an int or a float specifying the value of contrast of the stimulus
	"""
        raise NotImplementedError()

class SheetF0Vm(sciunit.Capability):
    """Get the F0 component of the membrane potential of the neurons of the sheet"""

    def sheets_F0_Vm(self, sheets):
        """ Model should implement this method such as to retrieve the F0 component of the membrane potential 
            of its sheets of neurons passed in input
            sheet should be a string specifying the name of the sheet
            contrast should be an int or a float specifying the value of contrast of the stimulus
        """
        raise NotImplementedError()

class SheetF1Vm(sciunit.Capability):
    """Get the F1 component of the membrane potential of the neurons of the sheet"""

    def sheets_F1_Vm(self, sheets):
        """ Model should implement this method such as to retrieve the F1 component of the membrane potential
            of its sheets of neurons passed in input
            sheet should be a string specifying the name of the sheet
            contrast should be an int or a float specifying the value of contrast of the stimulus
        """
        raise NotImplementedError()

class SheetModulationRatioVm(sciunit.Capability):
    """Get the modulation ratio of the membrane potential of the neurons of the sheet"""

    def sheets_modulation_ratio_Vm(self, sheets):
        """ Model should implement this method such as to retrieve the modulation ratio of the membrane potential
            of its sheets of neurons passed in input
            sheet should be a string specifying the name of the sheet
            contrast should be an int or a float specifying the value of contrast of the stimulus
        """
        raise NotImplementedError()


class SheetModulationRatio(sciunit.Capability):
    """Get the modulation ratio computed from the PSTH of the neurons of the sheet"""

    def sheets_modulation_ratio(self, sheets):
        """ Model should implement this method such as to retrieve the modulation ratio 
            of its sheets of neurons passed in input
            sheet should be a string specifying the name of the sheet
            contrast should be an int or a float specifying the value of contrast of the stimulus
        """
        raise NotImplementedError()
