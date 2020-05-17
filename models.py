import sciunit
from capabilities import * # One of many potential model capabilities.
from mozaik.analysis.analysis import *
from mozaik.analysis.vision import *
from mozaik.storage.queries import *
from mozaik.storage.datastore import PickledDataStore


class ModelV1Spont(sciunit.Model, StatsSheetFiringRate, SheetsMembranePotential, SheetsExcitatorySynapticConductance, SheetsInhibitorySynapticConductance, SheetCorrelationCoefficient, SheetCVISI):
	"""A model of spontaneous activity of V1."""

	def __init__(self, path, name="Spontaneous activity of V1", **params):
		""" path should be a string containing  the path of the files containing the results of the simulation of the model
		"""
		self.data_store = param_filter_query(PickledDataStore(load=True,parameters=ParameterSet({'root_directory': path,'store_stimuli' : False}),replace=True),st_direct_stimulation_name=None,st_name="InternalStimulus")
		super(ModelV1Spont, self).__init__(name=name, data_store=self.data_store)


	def sheet_firing_rate(self, sheet):
		"""Get the average firing rates of the sheet
                sheet should be a string containing the name of the sheet
                """
		try:
                        assert (isinstance(sheet, str))
                except Exception:
                        raise sciunit.errors.Error("Parameter sheet must be a string")

                return param_filter_query(self.data_store, value_name='Firing rate', identifier='PerNeuronValue', sheet_name=sheet, analysis_algorithm='TrialAveragedFiringRate').get_analysis_result()[0].values

	

	def stats_sheet_firing_rate(self, sheet):
		"""Get descriptive statistics about the average firing rates of the sheet
		sheet should be a string containing the name of the sheet
		"""	
                AVF= self.sheet_firing_rate(sheet)
		mean_AVF=numpy.mean(AVF)
                std_AVF=numpy.std(AVF,ddof=1)
                n=len(AVF)
                return {"mean": mean_AVF, "std": std_AVF, "n": n}


	def sheet_correlation_coefficient(self, sheet):
		"""Get the correlation coefficient of the sheet
		sheet should be a string containing the name of the sheet
		"""	

                try:
                	assert (isinstance(sheet, str))
                except Exception:
                	raise sciunit.errors.Error("Parameter sheet must be a string")
		
		CC=param_filter_query(self.data_store, value_name='Correlation coefficient(psth (bin=10.0))', identifier='PerNeuronValue', sheet_name=sheet, analysis_algorithm='NeuronToNeuronAnalogSignalCorrelations').get_analysis_result()[0].values
		mean_CC=numpy.mean(CC)
		std_CC=numpy.std(CC,ddof=1)
		n=len(CC)	
		
		return {"mean": mean_CC, "std": std_CC, "n": n}


	def sheet_CV_ISI(self, sheet):
                """Get the squared value coefficient variation of the interspike interval of the sheet
                sheet should be a string containing the name of the sheet
                """

                try:
                        assert (isinstance(sheet, str))
                except Exception:
                        raise sciunit.errors.Error("Parameter sheet must be a string")

                CV_ISI=param_filter_query(self.data_store, value_name='CV of ISI squared', identifier='PerNeuronValue', sheet_name=sheet, analysis_algorithm='Irregularity').get_analysis_result()[0].values
                mean_CV_ISI=numpy.mean(CV_ISI)
                std_CV_ISI=numpy.std(CV_ISI,ddof=1)
                n=len(CV_ISI)

                return {"mean": mean_CV_ISI, "std": std_CV_ISI, "n": n}


	def sheets_membrane_potential(self, sheets):
		"""Get the average resting membrane potential of the sheets"""
	
		ms = lambda a: (numpy.mean(a),numpy.std(a, ddof=1))
		population=[]
		mean=[]
		std=[]

		if type(sheets)== str:
			mean_VM, std_VM = ms(param_filter_query(self.data_store,sheet_name=sheets,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(VM)').get_analysis_result()[0].values)
			n=len(param_filter_query(self.data_store, sheet_name=s).get_segments()[0].get_stored_vm_ids())
	
		else:
			try:
		                assert (isinstance(sheets, list))
        		except Exception:
            			raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

			for s in sheets:
				try: 
	                                assert (isinstance(s, str))
	                        except Exception:
	                                raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")
				population.append(len(param_filter_query(self.data_store, sheet_name=s).get_segments()[0].get_stored_vm_ids()))
				mean.append(numpy.mean(param_filter_query(self.data_store,sheet_name=s,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(VM)').get_analysis_result()[0].values))
				std.append(numpy.std(param_filter_query(self.data_store,sheet_name=s,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(VM)').get_analysis_result()[0].values, ddof=1))
	
			mean_VM, std_VM = ms(param_filter_query(self.data_store,sheet_name=sheets,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(VM)').get_analysis_result()[0].values)
			mean_VM=numpy.mean(mean)
			std_VM=(sum([(p-1)*st**2 for (st,p) in zip(std,population)])/(sum(population)-len(population)))**0.5
			n=sum(population)

		return {"mean": mean_VM, "std": std_VM, "n": n}




	def sheets_excitatory_synaptic_conductance(self, sheets):
		"""Get the average excitatory synaptic conductance of the sheets"""
               
		ms = lambda a: (numpy.mean(a),numpy.std(a,ddof=1))
                population=[]
                mean=[]
                std=[]

                if type(sheets)== str:
                        mean_ECond, std_ECond = ms(param_filter_query(self.data_store,sheet_name=sheets,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ECond)').get_analysis_result()[0].values)
                        n=len(param_filter_query(self.data_store, sheet_name=s).get_segments()[0].get_stored_esyn_ids())
                        
                else:
                        try:
                                assert (isinstance(sheets, list))
                        except Exception:
                                raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

                        for s in sheets:
                                try:
                                        assert (isinstance(s, str))
                                except Exception:
                                        raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")
                                population.append(len(param_filter_query(self.data_store, sheet_name=s).get_segments()[0].get_stored_vm_ids()))
                                mean.append(numpy.mean(param_filter_query(self.data_store,sheet_name=s,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ECond)').get_analysis_result()[0].values))
                                std.append(numpy.std(param_filter_query(self.data_store,sheet_name=s,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ECond)').get_analysis_result()[0].values, ddof=1))
                        
			mean_ECond, std_ECond = ms(param_filter_query(self.data_store,sheet_name=sheets,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ECond)').get_analysis_result()[0].values)
                        mean_ECond=numpy.mean(mean)
                        std_ECond=(sum([(p-1)*st**2 for (st,p) in zip(std,population)])/(sum(population)-len(population)))**0.5
                        n=sum(population)

		return {"mean": mean_ECond, "std": std_ECond, "n": n}
	



	def sheets_inhibitory_synaptic_conductance(self, sheets):
		"""Get the average inhibitory synaptic conductance of the sheets"""
	
                ms = lambda a: (numpy.mean(a),numpy.std(a,ddof=1))
                population=[]
                mean=[]
                std=[]

                if type(sheets)== str:
                        mean_ICond, std_ICond = ms(param_filter_query(self.data_store,sheet_name=sheets,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ICond)').get_analysis_result()[0].values)
                        n=len(param_filter_query(self.data_store, sheet_name=s).get_segments()[0].get_stored_isyn_ids())
                        
                else:
                        try:
                                assert (isinstance(sheets, list))
                        except Exception:
                                raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

                        for s in sheets:
                                try:
                                        assert (isinstance(s, str))
                                except Exception:
                                        raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")
                                population.append(len(param_filter_query(self.data_store, sheet_name=s).get_segments()[0].get_stored_vm_ids()))
                                mean.append(numpy.mean(param_filter_query(self.data_store,sheet_name=s,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ICond)').get_analysis_result()[0].values))
                                std.append(numpy.std(param_filter_query(self.data_store,sheet_name=s,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ICond)').get_analysis_result()[0].values, ddof=1))
                        
                        mean_ICond, std_ICond = ms(param_filter_query(self.data_store,sheet_name=sheets,analysis_algorithm='Analog_MeanSTDAndFanoFactor',value_name='Mean(ICond)').get_analysis_result()[0].values)
                        mean_ICond=numpy.mean(mean)
                        std_ICond=(sum([(p-1)*st**2 for (st,p) in zip(std,population)])/(sum(population)-len(population)))**0.5
                        n=sum(population)

		return {"mean": mean_ICond, "std": std_ICond, "n": n}




class ModelV1DriftingGratings(ModelV1Spont, SheetHWHH, SheetRURA, SheetModulationRatioVm, SheetModulationRatio):
        """A model of activity of V1 in response to drifting sinusoidal gratings."""

        def __init__(self, path, name="Model of V1 for drifting gratings"):

                self.data_store_drift = param_filter_query(PickledDataStore(load=True,parameters=ParameterSet({'root_directory': path,'store_stimuli' : False}),replace=True),st_name="FullfieldDriftingSinusoidalGrating")
                super(ModelV1DriftingGratings, self).__init__(name=name, path=path, data_store_drift=self.data_store_drift)


	def sheets_HWHH(self, sheets, contrast):
		"""Get the Half-Width at Half-Height of the sheets"""
	
                population=[]
                mean=[]
                std=[]

		try:
                	assert (isinstance(contrast, int) or isinstance(contrast, float))
        	except Exception:
			raise sciunit.errors.Error("Parameter contrast must be a float or an int")

                if type(sheets)== str:
			HWHH=param_filter_query(self.data_store_drift, value_name='orientation HWHH of Firing rate', identifier='PerNeuronValue', sheet_name=sheets, st_contrast=contrast).get_analysis_result()[0].values
                	mean_HWHH=numpy.mean(HWHH)
                	std_HWHH=numpy.std(HWHH,ddof=1)
                	n=len(HWHH)

                else:
                        try:
                                assert (isinstance(sheets, list))
                        except Exception:
                                raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

                        for s in sheets:
                                try:
                                        assert (isinstance(s, str))
                                except Exception:
                                        raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

                                HWHH=param_filter_query(self.data_store_drift, value_name='orientation HWHH of Firing rate', identifier='PerNeuronValue', sheet_name=sheets, st_contrast=contrast).get_analysis_result()[0].values
				population.append(len(HWHH))
                                mean.append(numpy.mean(HWHH))
                                std.append(numpy.std(HWHH, ddof=1))

                        mean_HWHH=numpy.mean(mean)
                        std_HWHH=(sum([(p-1)*st**2 for (st,p) in zip(std,population)])/(sum(population)-len(population)))**0.5
                        n=sum(population)

                return {"mean": mean_HWHH, "std": std_HWHH, "n": n}

	def sheets_RURA(self, sheets, contrast):
		"""Get the Relative Unselective Response AMplitude"""
	
                population=[]
                mean=[]
                std=[]

		try:
                	assert (isinstance(contrast, int) or isinstance(contrast, float))
        	except Exception:
			raise sciunit.errors.Error("Parameter contrast must be a float or an int")


                if type(sheets)== str:
			RURA=param_filter_query(self.data_store_drift, value_name=['orientation CV(Firing rate)'], identifier='PerNeuronValue', sheet_name=sheets, st_contrast=contrast).get_analysis_result()[0].values
                	mean_RURA=numpy.mean(RURA)
                	std_RURA=numpy.std(RURA,ddof=1)
                	n=len(RURA)

                else:
                        try:
                                assert (isinstance(sheets, list))
                        except Exception:
                                raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

                        for s in sheets:
                                try:
                                        assert (isinstance(s, str))
                                except Exception:
                                        raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

                                RURA=param_filter_query(self.data_store_drift, value_name=['orientation CV(Firing rate)'], identifier='PerNeuronValue', sheet_name=sheets, st_contrast=contrast).get_analysis_result()[0].values

				population.append(len(RURA))
                                mean.append(numpy.mean(RURA))
                                std.append(numpy.std(RURA, ddof=1))

                        mean_RURA=numpy.mean(mean)
                        std_RURA=(sum([(p-1)*st**2 for (st,p) in zip(std,population)])/(sum(population)-len(population)))**0.5
                        n=sum(population)

                return {"mean": mean_RURA, "std": std_RURA, "n": n}

        def sheets_F0_Vm(self, sheets, contrast):
                """Get the F0 component of the membrane potential"""

                population=[]
                mean=[]
                std=[]

                try:
                        assert (isinstance(contrast, int) or isinstance(contrast, float))
                except Exception:
                        raise sciunit.errors.Error("Parameter contrast must be a float or an int")


                if type(sheets)== str:
                        F0=param_filter_query(self.data_store_drift, value_name='F0_Vm', identifier='PerNeuronValue', sheet_name=sheets, st_contrast=contrast).get_analysis_result()[0].values
                        mean_F0=numpy.mean(F0)
                        std_F0=numpy.std(F0,ddof=1)
                        n=len(F0)

                else:
                        try:
                                assert (isinstance(sheets, list))
                        except Exception:
                                raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

                        for s in sheets:
                                try:
                                        assert (isinstance(s, str))
                                except Exception:
                                        raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

                                F0=param_filter_query(self.data_store_drift, value_name='F0_Vm', identifier='PerNeuronValue', sheet_name=sheets, st_contrast=contrast).get_analysis_result()[0].values

                                population.append(len(F0))
                                mean.append(numpy.mean(F0))
                                std.append(numpy.std(F0, ddof=1))

                        mean_F0=numpy.mean(mean)
                        std_F0=(sum([(p-1)*st**2 for (st,p) in zip(std,population)])/(sum(population)-len(population)))**0.5
                        n=sum(population)

                return {"mean": mean_F0, "std": std_F0, "n": n}

        def sheets_modulation_ratio_Vm(self, sheets, contrast):
                """Get the modulation ratio of the membrane potential"""

                population=[]
                mean=[]
                std=[]

                try:
                        assert (isinstance(contrast, int) or isinstance(contrast, float))
                except Exception:
                        raise sciunit.errors.Error("Parameter contrast must be a float or an int")


                if type(sheets)== str:
                        F0=param_filter_query(self.data_store_drift, value_name='-(x+y)(F0_Vm,Mean(VM))', identifier='PerNeuronValue', sheet_name=sheets, st_contrast=contrast).get_analysis_result()[0].values
                        F1=param_filter_query(self.data_store_drift, value_name='F1_Vm', identifier='PerNeuronValue', sheet_name=sheets, st_contrast=contrast).get_analysis_result()[0].values
			MR=numpy.array(F0)/numpy.array(F1)
                        mean_MR=numpy.mean(MR)
                        std_MR=numpy.std(MR,ddof=1)
                        n=len(MR)

                else:
                        try:
                                assert (isinstance(sheets, list))
                        except Exception:
                                raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

                        for s in sheets:
                                try:
                                        assert (isinstance(s, str))
                                except Exception:
                                        raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

                        	F0=param_filter_query(self.data_store_drift, value_name='-(x+y)(F0_Vm,Mean(VM))', identifier='PerNeuronValue', sheet_name=s, st_contrast=contrast).get_analysis_result()[0].values
                        	F1=param_filter_query(self.data_store_drift, value_name='F1_Vm', identifier='PerNeuronValue', sheet_name=s, st_contrast=contrast).get_analysis_result()[0].values
				MR=numpy.array(F0)/numpy.array(F1)

                                population.append(len(MR))
                                mean.append(numpy.mean(MR))
                                std.append(numpy.std(MR, ddof=1))

                        mean_MR=numpy.mean(mean)
                        std_MR=(sum([(p-1)*st**2 for (st,p) in zip(std,population)])/(sum(population)-len(population)))**0.5
                        n=sum(population)

                return {"mean": mean_MR, "std": std_MR, "n": n}

        def sheets_modulation_ratio(self, sheets, contrast):
                """Get the modulation ratio of the PSTH"""

                population=[]
                mean=[]
                std=[]

                try:
                        assert (isinstance(contrast, int) or isinstance(contrast, float))
                except Exception:
                        raise sciunit.errors.Error("Parameter contrast must be a float or an int")


                if type(sheets)== str:
                        MR=param_filter_query(self.data_store_drift, value_name='Modulation ratio(time)', identifier='PerNeuronValue', sheet_name=sheets, st_contrast=contrast).get_analysis_result()[0].values
                        mean_MR=numpy.mean(MR)
                        std_MR=numpy.std(MR,ddof=1)
                        n=len(MR)

                else:
                        try:
                                assert (isinstance(sheets, list))
                        except Exception:
                                raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

                        for s in sheets:
                                try:
                                        assert (isinstance(s, str))
                                except Exception:
                                        raise sciunit.errors.Error("Parameter sheets must be a string or a list of string")

                                MR=param_filter_query(self.data_store_drift, value_name='Modulation ratio(time)', identifier='PerNeuronValue', sheet_name=sheets, st_contrast=contrast).get_analysis_result()[0].values

                                population.append(len(MR))
                                mean.append(numpy.mean(MR))
                                std.append(numpy.std(MR, ddof=1))

                        mean_MR=numpy.mean(mean)
                        std_MR=(sum([(p-1)*st**2 for (st,p) in zip(std,population)])/(sum(population)-len(population)))**0.5
                        n=sum(population)

                return {"mean": mean_MR, "std": std_MR, "n": n}

