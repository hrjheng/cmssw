#include "GeneratorInterface/GenFilters/interface/HDalitzEMEnrichingFilter.h"
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"

#include "TLorentzVector.h"

#include <iostream>

using namespace edm;
using namespace std;
using namespace HepMC;

HDalitzEMEnrichingFilter::HDalitzEMEnrichingFilter(const edm::ParameterSet &iConfig) : token_(consumes<edm::HepMCProduct>(edm::InputTag(iConfig.getUntrackedParameter("moduleLabel", std::string("generator")), "unsmeared"))),
                                                                                   maxEvents(iConfig.getUntrackedParameter<int>("maxEvents", 0)),
                                                                                   ptSeedThr(iConfig.getUntrackedParameter<double>("PtSeedThr")),
                                                                                   etaSeedThr(iConfig.getUntrackedParameter<double>("EtaSeedThr")),
                                                                                   ptGammaThr(iConfig.getUntrackedParameter<double>("PtGammaThr")),
                                                                                   etaGammaThr(iConfig.getUntrackedParameter<double>("EtaGammaThr")),
                                                                                   ptTkThr(iConfig.getUntrackedParameter<double>("PtTkThr")),
                                                                                   etaTkThr(iConfig.getUntrackedParameter<double>("EtaTkThr")),
                                                                                   ptElThr(iConfig.getUntrackedParameter<double>("PtElThr")),
                                                                                   etaElThr(iConfig.getUntrackedParameter<double>("EtaElThr")),
                                                                                   dRTkMax(iConfig.getUntrackedParameter<double>("dRTkMax")),
                                                                                   dRSeedMax(iConfig.getUntrackedParameter<double>("dRSeedMax")),
                                                                                   dPhiSeedMax(iConfig.getUntrackedParameter<double>("dPhiSeedMax")),
                                                                                   dEtaSeedMax(iConfig.getUntrackedParameter<double>("dEtaSeedMax")),
                                                                                   dRNarrowCone(iConfig.getUntrackedParameter<double>("dRNarrowCone")),
                                                                                   pTMinCandidate1(iConfig.getUntrackedParameter<double>("PtMinCandidate1")),
                                                                                   pTMinCandidate2(iConfig.getUntrackedParameter<double>("PtMinCandidate2")),
                                                                                   etaMaxCandidate(iConfig.getUntrackedParameter<double>("EtaMaxCandidate")),
                                                                                   invMassMin(iConfig.getUntrackedParameter<double>("InvMassMin")),
                                                                                   invMassMax(iConfig.getUntrackedParameter<double>("InvMassMax")),
                                                                                   energyCut(iConfig.getUntrackedParameter<double>("EnergyCut")),
                                                                                   nTkConeMax(iConfig.getUntrackedParameter<int>("NTkConeMax")),
                                                                                   nTkConeSum(iConfig.getUntrackedParameter<int>("NTkConeSum")),
                                                                                   acceptPrompts(iConfig.getUntrackedParameter<bool>("AcceptPrompts")),
                                                                                   promptPtThreshold(iConfig.getUntrackedParameter<double>("PromptPtThreshold"))