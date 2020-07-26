#include "GeneratorInterface/GenFilters/interface/HDalitzMuMuGammaFilter.h"
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"

#include "TLorentzVector.h"

#include <iostream>

// order std::vector of TLorentzVector elements
class orderByPt
{
public:
    bool operator()(TLorentzVector const &a, TLorentzVector const &b)
    {
        if (a.Pt() == b.Pt())
        {
            return a.Pt() < b.Pt();
        }
        else
        {
            return a.Pt() > b.Pt();
        }
    }
};

using namespace edm;
using namespace std;
using namespace HepMC;

HDalitzMuMuGammaFilter::HDalitzMuMuGammaFilter(const edm::ParameterSet &iConfig) : token_(consumes<edm::HepMCProduct>(edm::InputTag(iConfig.getUntrackedParameter("moduleLabel", std::string("generator")), "unsmeared"))),
                                                                                   minPhotonPt(iConfig.getParameter<double>("minPhotonPt")),
                                                                                   minLeptonPt(iConfig.getParameter<double>("minLeptonPt")),
                                                                                   minPhotonEta(iConfig.getParameter<double>("minPhotonEta")),
                                                                                   minLeptonEta(iConfig.getParameter<double>("minLeptonEta")),
                                                                                   maxPhotonEta(iConfig.getParameter<double>("maxPhotonEta")),
                                                                                   maxLeptonEta(iConfig.getParameter<double>("maxLeptonEta")),
                                                                                   minDimuMass(iConfig.getParameter<double>("minDimuMass")),
                                                                                   maxDimuMass(iConfig.getParameter<double>("maxDimuMass")),
                                                                                   minMMGMass(iConfig.getParameter<double>("minMMGMass"))
{
}

HDalitzMuMuGammaFilter::~HDalitzMuMuGammaFilter()
{
}

// ------------ method called to skim the data  ------------
bool HDalitzMuMuGammaFilter::filter(edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    using namespace edm;

    bool accepted = false;
    Handle<HepMCProduct> evt;
    iEvent.getByToken(token_, evt);
    const HepMC::GenEvent *myGenEvent = evt->GetEvent();

    vector<TLorentzVector> Muon;
    Muon.clear();
    vector<TLorentzVector> Photon;
    Photon.clear();
    vector<float> Charge;
    Charge.clear();

    for (HepMC::GenEvent::particle_const_iterator p = myGenEvent->particles_begin(); p != myGenEvent->particles_end(); ++p)
    {
        if ((*p)->status() == 1 && abs((*p)->pdg_id()) == 13)
        {
            TLorentzVector LeptP((*p)->momentum().px(), (*p)->momentum().py(), (*p)->momentum().pz(), (*p)->momentum().e());
            if (LeptP.Pt() > minLeptonPt)
            {
                Muon.push_back(LeptP);
            } // if pt
        }     // if lepton

        if ((*p)->status() == 1 && abs((*p)->pdg_id()) == 22)
        {
            TLorentzVector PhotP((*p)->momentum().px(), (*p)->momentum().py(), (*p)->momentum().pz(), (*p)->momentum().e());
            if (PhotP.Pt() > minPhotonPt)
            {
                Photon.push_back(PhotP);
            } // if pt
        }     // if photon

    } // loop over particles

    // std::cout << "\n" << "Photon size: " << Photon.size() << std::endl;
    // for (unsigned int u=0; u<Photon.size(); u++){
    //   std::cout << "BEF photon PT: " << Photon[u].Pt() << std::endl;
    // }
    // std::cout << "\n" << "Muon size: " << Muon.size() << std::endl;
    // for (unsigned int u=0; u<Muon.size(); u++){
    //   std::cout << "BEF lepton PT: " << Muon[u].Pt() << std::endl;
    // }

    // order Muon and Photon according to Pt
    std::stable_sort(Photon.begin(), Photon.end(), orderByPt());
    std::stable_sort(Muon.begin(), Muon.end(), orderByPt());

    //  std::cout << "\n" << std::endl;
    //  std::cout << "\n" << "Photon size: " << Photon.size() << std::endl;
    //  for (unsigned int u=0; u<Photon.size(); u++){
    //    std::cout << "AFT photon PT: " << Photon[u].Pt() << std::endl;
    //  }
    //  std::cout << "\n" << "Muon size: " << Muon.size() << std::endl;
    //  for (unsigned int u=0; u<Muon.size(); u++){
    //    std::cout << "AFT lepton PT: " << Muon[u].Pt() << std::endl;
    //  }
    //  std::cout << "\n" << std::endl;

    if (!Photon.empty() &&
        Muon.size() > 1 &&
        Photon[0].Pt() >= minPhotonPt &&
        Muon[0].Pt() >= minLeptonPt &&
        Muon[1].Pt() >= minLeptonPt &&
        Photon[0].Eta() >= minPhotonEta &&
        Muon[0].Eta() >= minLeptonEta &&
        Muon[1].Eta() >= minLeptonEta &&
        Photon[0].Eta() <= maxPhotonEta &&
        Muon[0].Eta() <= maxLeptonEta &&
        Muon[1].Eta() <= maxLeptonEta &&
        (Muon[0] + Muon[1]).M() >= minDimuMass &&
        (Muon[0] + Muon[1]).M() <= maxDimuMass &&
        (Muon[0] + Muon[1] + Photon[0]).M() > minMMGMass)
    { // satisfy molteplicity, kinematics, and ll llg minimum mass
        accepted = true;
    }

    //  std::cout << "++ returning: " << accepted << "\n" << std::endl;

    return accepted;
}