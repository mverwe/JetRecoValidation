import FWCore.ParameterSet.Config as cms

## Default Parameter Sets
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *
from RecoHI.HiJetAlgos.HiPFJetParameters_cff import *

#pseudo towers for noise suppression background subtraction
PFTowers = cms.EDProducer("ParticleTowerProducer",
                          src = cms.InputTag("particleFlowTmp"),
                          useHF = cms.bool(False)
)

ak5PFJets = cms.EDProducer("FastjetJetProducer",
                           HiPFJetParameters,
                           AnomalousCellParameters,
                           MultipleAlgoIteratorBlock,
                           jetAlgorithm = cms.string("AntiKt"),
                           rParam       = cms.double(0.5)
)
ak5PFJets.src = cms.InputTag('particleFlowTmp')

akPu5PFJets = ak5PFJets.clone(jetType = cms.string('BasicJet'),
                              doPVCorrection = False,
                              doPUOffsetCorr = True,
                              subtractorName = cms.string("MultipleAlgoIterator"),    
                              src = cms.InputTag('PFTowers'),
                              doAreaFastjet = False
)

akPu5PFJets.puPtMin = cms.double(25)
akPu3PFJets10 = akPu5PFJets.clone(rParam       = cms.double(0.3), puPtMin = 10)
akPu3PFJets15 = akPu5PFJets.clone(rParam       = cms.double(0.3), puPtMin = 15) #default run 1
akPu3PFJets20 = akPu5PFJets.clone(rParam       = cms.double(0.3), puPtMin = 20)
akPu3PFJets25 = akPu5PFJets.clone(rParam       = cms.double(0.3), puPtMin = 25)
akPu3PFJets30 = akPu5PFJets.clone(rParam       = cms.double(0.3), puPtMin = 30)

hiRecoPFJets = cms.Sequence(
    PFTowers*
    akPu3PFJets10*akPu3PFJets15*akPu3PFJets20*akPu3PFJets25*akPu3PFJets30
    )

