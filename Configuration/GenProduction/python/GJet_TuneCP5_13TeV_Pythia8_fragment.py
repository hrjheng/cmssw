import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

source = cms.Source("EmptySource")
generator = cms.EDFilter('Pythia8GeneratorFilter',
        comEnergy = cms.double(13000.0),
        crossSection = cms.untracked.double(1.0),
        filterEfficiency = cms.untracked.double(1.0),
        maxEventsToPrint = cms.untracked.int32(0),
        pythiaHepMCVerbosity = cms.untracked.bool(False),
        pythiaPylistVerbosity = cms.untracked.int32(0),

        PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
            processParameters = cms.vstring(
            'PromptPhoton:qg2qgamma = on       ! prompt photon production',
            'PromptPhoton:qqbar2ggamma = on    ! prompt photon production',
            'PromptPhoton:gg2ggamma = on       ! prompt photon production',
            'PhaseSpace:pTHatMin = 20.         ! minimum pt hat for hard interactions', 
            'PhaseSpace:pTHatMax = -1          ! maximum pt hat for hard interactions'),
            parameterSets = cms.vstring('pythia8CommonSettings',
                                        'pythia8CP5Settings',
                                        'processParameters')
            )
)

gj_filter = cms.EDFilter("PythiaFilterGammaGamma",
    PtSeedThr = cms.untracked.double(5.0),
    EtaSeedThr = cms.untracked.double(2.8),
    PtGammaThr = cms.untracked.double(0.0),
    EtaGammaThr = cms.untracked.double(2.8),
    PtElThr = cms.untracked.double(2.0),
    EtaElThr = cms.untracked.double(2.8),
    dRSeedMax = cms.untracked.double(0.0),
    dPhiSeedMax = cms.untracked.double(0.2),
    dEtaSeedMax = cms.untracked.double(0.12),
    dRNarrowCone = cms.untracked.double(0.02),
    PtTkThr = cms.untracked.double(1.6),
    EtaTkThr = cms.untracked.double(2.2),
    dRTkMax = cms.untracked.double(0.2),
    PtMinCandidate1 = cms.untracked.double(25.),
    PtMinCandidate2 = cms.untracked.double(25.),
    EtaMaxCandidate = cms.untracked.double(3.0),
    NTkConeMax = cms.untracked.int32(2),
    NTkConeSum = cms.untracked.int32(4),
    InvMassMin = cms.untracked.double(0.211316),
    InvMassMax = cms.untracked.double(1000.0),
    EnergyCut = cms.untracked.double(1.0),
    AcceptPrompts = cms.untracked.bool(True),
    PromptPtThreshold = cms.untracked.double(15.0)   
    
)

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

# HDalitzmmgFilter = cms.EDFilter('HDalitzMuMuGammaFilter',

#   HepMCProduct             = cms.InputTag("generator","unmeared"),
#   minPhotonPt              = cms.double(25.),
#   minLeptonPt              = cms.double(2.),
#   minPhotonEta             = cms.double(-3),
#   minLeptonEta             = cms.double(-3),
#   maxPhotonEta             = cms.double(3),
#   maxLeptonEta             = cms.double(3),
#   minDimuMass              = cms.double(0.211316),
#   minMMGMass               = cms.double(60)
#  )

 
ProductionFilterSequence = cms.Sequence(generator*gj_filter)