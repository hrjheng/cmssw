import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import * 
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import * 

### Process: Gamma+jets
### McM dataset name: QCD-Pt15-7000_TuneCP5_13TeV_pythia8_IsoTrackFilter (HCA-RunIIFall18GS-00004)
### McM link: https://cms-pdmv.cern.ch/mcm/requests?dataset_name=GJet_Pt-15To6000_TuneCP5-Flat_13TeV_pythia8&page=-1&shown=127&limit=100
generator = cms.EDFilter("Pythia8GeneratorFilter",
    crossSection = cms.untracked.double(365896),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    PythiaParameters = cms.PSet(
            pythia8CommonSettingsBlock, 
            pythia8CP5SettingsBlock, 
            processParameters = cms.vstring(
                    'PromptPhoton:gg2ggamma = on',
	                'PromptPhoton:qg2qgamma = on',
	                'PromptPhoton:qqbar2ggamma = on',
             	    'PhaseSpace:pTHatMin = 15.',
            	    'PhaseSpace:pTHatMax = 6000.',
                    'PhaseSpace:bias2Selection = on',
                    'PhaseSpace:bias2SelectionPow = 4.5',
                    'PhaseSpace:bias2SelectionRef = 15.',                    
	        ),
            parameterSets = cms.vstring('pythia8CommonSettings',
                                            'pythia8CP5Settings', 
                                            'processParameters', 
                                        )
    )
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/MCTunes2017/PythiaCP5Settings,v $'),
    annotation = cms.untracked.string('PYTHIA8 TuneCP5 at 13TeV- Prompt photon production, 15 =< pThat <= 6000 GeV')
)
