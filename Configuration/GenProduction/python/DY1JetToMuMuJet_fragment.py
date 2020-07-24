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
                                 'WeakBosonAndParton:qqbar2gmZg = on',
                                 'WeakBosonAndParton:qg2gmZq = on',
                                 'WeakBosonAndParton:fgm2gmZf = on',
                                 '23:mMin = 0.211316751',
                                 '23:mMax = 60.0',
                                 '23:onMode = off',
                                 '23:OnIfMatch = 13 -13',
                                 'PhaseSpace:pTHatMin = 25.',
                                 'PhaseSpace:mHatMin = 0.211316751'),
                             parameterSets = cms.vstring('processParameters')
                         )
)

# https://github.com/cms-sw/cmssw/blob/master/GeneratorInterface/Core/src/PythiaHepMCFilterGammaGamma.cc
# gj_filter = cms.EDFilter("PythiaFilterGammaGamma",
#     PtSeedThr = cms.untracked.double(5.0),
#     EtaSeedThr = cms.untracked.double(2.8),
#     PtGammaThr = cms.untracked.double(0.0),
#     EtaGammaThr = cms.untracked.double(2.8),
#     PtElThr = cms.untracked.double(2.0),
#     EtaElThr = cms.untracked.double(2.8),
#     dRSeedMax = cms.untracked.double(0.0),
#     dPhiSeedMax = cms.untracked.double(0.2),
#     dEtaSeedMax = cms.untracked.double(0.12),
#     dRNarrowCone = cms.untracked.double(0.02),
#     PtTkThr = cms.untracked.double(1.6),
#     EtaTkThr = cms.untracked.double(2.2),
#     dRTkMax = cms.untracked.double(0.2),
#     PtMinCandidate1 = cms.untracked.double(15.),
#     PtMinCandidate2 = cms.untracked.double(15.),
#     EtaMaxCandidate = cms.untracked.double(3.0),
#     NTkConeMax = cms.untracked.int32(2),
#     NTkConeSum = cms.untracked.int32(4),
#     InvMassMin = cms.untracked.double(40.0),
#     InvMassMax = cms.untracked.double(14000.0),
#     EnergyCut = cms.untracked.double(1.0),
#     AcceptPrompts = cms.untracked.bool(True),
#     PromptPtThreshold = cms.untracked.double(15.0)   
    
# )

# ProductionFilterSequence = cms.Sequence(generator*gj_filter)

genParticlesForFilter = cms.EDProducer("GenParticleProducer",
    saveBarCodes = cms.untracked.bool(True),
    src = cms.InputTag("generator", "unsmeared"),
    abortOnUnknownPDGCode = cms.untracked.bool(False)
)

emenrichingfilter = cms.EDFilter("EMEnrichingFilter",
                                 filterAlgoPSet = cms.PSet(isoGenParETMin=cms.double(20.),
                                                           isoGenParConeSize=cms.double(0.1),
                                                           clusterThreshold=cms.double(20.),
                                                           isoConeSize=cms.double(0.2),
                                                           hOverEMax=cms.double(0.5),
                                                           tkIsoMax=cms.double(5.),
                                                           caloIsoMax=cms.double(10.),
                                                           requireTrackMatch=cms.bool(False),
                                                           genParSource = cms.InputTag("genParticlesForFilter")
                                                           )
                                 )
    

# add your filters to this sequence
ProductionFilterSequence = cms.Sequence(generator * (genParticlesForFilter + emenrichingfilter))