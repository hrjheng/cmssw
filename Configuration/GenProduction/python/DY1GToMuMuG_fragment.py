import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter(
    "Pythia8GeneratorFilter",
    pythiaPylistVerbosity=cms.untracked.int32(1),
    filterEfficiency=cms.untracked.double(1.0),
    pythiaHepMCVerbosity=cms.untracked.bool(False),
    comEnergy=cms.double(13000.0),
    crossSection=cms.untracked.double(0.0),
    maxEventsToPrint=cms.untracked.int32(0),
    PythiaParameters=cms.PSet(
        processParameters=cms.vstring(
            "Main:timesAllowErrors = 10000",
            "WeakBosonAndParton:ffbar2gmZgm = on",
            "23:mMin = 0.211316751",
            "23:mMax = 60.0",
            "23:onMode = off",
            "23:OnIfMatch = 13 -13",
            "PhaseSpace:pTHatMin = 15.",
            "PhaseSpace:mHatMin = 0.211316751",
        ),
        parameterSets=cms.vstring("processParameters"),
    ),
)

genParticlesForFilter = cms.EDProducer(
    "GenParticleProducer",
    saveBarCodes=cms.untracked.bool(True),
    src=cms.InputTag("generator", "unsmeared"),
    abortOnUnknownPDGCode=cms.untracked.bool(False),
)

emenrichingfilter = cms.EDFilter(
    "EMEnrichingFilter",
    filterAlgoPSet=cms.PSet(
        isoGenParETMin=cms.double(20.0),
        isoGenParConeSize=cms.double(0.1),
        clusterThreshold=cms.double(20.0),
        isoConeSize=cms.double(0.2),
        hOverEMax=cms.double(0.5),
        tkIsoMax=cms.double(5.0),
        caloIsoMax=cms.double(10.0),
        requireTrackMatch=cms.bool(False),
        genParSource=cms.InputTag("genParticlesForFilter"),
    ),
)

HDalitzmmgFilter = cms.EDFilter(
    "HDalitzMuMuGammaFilter",
    HepMCProduct=cms.InputTag("generator", "unsmeared"),
    minPhotonPt=cms.double(25.0),
    minLeptonPt=cms.double(3.0),
    minPhotonEta=cms.double(-3.0),
    minLeptonEta=cms.double(-3.0),
    maxPhotonEta=cms.double(3.0),
    maxLeptonEta=cms.double(3.0),
    minDimuMass=cms.double(0.211316),
    maxDimuMass=cms.double(60.0),
    minMMGMass=cms.double(60.0),
)


# add your filters to this sequence
ProductionFilterSequence = cms.Sequence(
    generator * (genParticlesForFilter + emenrichingfilter + HDalitzmmgFilter)
)
