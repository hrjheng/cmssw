import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity=cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.0),
                         crossSection = cms.untracked.double(0.0),
                         maxEventsToPrint = cms.untracked.int32(0),
                         PythiaParameters = cms.PSet(
                             processParameters = cms.vstring(
                                 'Main:timesAllowErrors = 10000',
                                 'WeakBosonAndParton:ffbar2gmZgm = on',
                                 '23:mMin = 0.211316751',
                                 '23:mMax = 60.0',
                                 '23:onMode = off',
                                 '23:OnIfMatch = 13 -13',
                                 'PhaseSpace:pTHatMin = 15.',
                                 'PhaseSpace:mHatMin = 0.211316751'),
                             parameterSets = cms.vstring('processParameters')
                         )
)
