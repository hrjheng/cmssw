#ifndef HDalitzMuMuGammaFilter_h
#define HDalitzMuMuGammaFilter_h

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

/* 

 Description: Modified from deprecated filter ZgammaMassFilter
     
*/

namespace edm
{
class HepMCProduct;
}

class HDalitzMuMuGammaFilter : public edm::EDFilter
{
public:
    explicit HDalitzMuMuGammaFilter(const edm::ParameterSet &);
    ~HDalitzMuMuGammaFilter();

    virtual bool filter(edm::Event &, const edm::EventSetup &);

private:
    // ----------memeber function----------------------
    int charge(const int &Id);

    // ----------member data ---------------------------

    edm::EDGetTokenT<edm::HepMCProduct> token_;

    double minPhotonPt;
    double minLeptonPt;

    double minPhotonEta;
    double minLeptonEta;

    double maxPhotonEta;
    double maxLeptonEta;

    double minDimuMass;
    double maxDimuMass;
    double minMMGMass;
};
#endif
