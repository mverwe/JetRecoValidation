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

#R=0.3
akPu3PFJets10 = akPu5PFJets.clone(rParam       = cms.double(0.3), puPtMin = 10)
akPu3PFJets15 = akPu5PFJets.clone(rParam       = cms.double(0.3), puPtMin = 15) #default run 1
akPu3PFJets20 = akPu5PFJets.clone(rParam       = cms.double(0.3), puPtMin = 20)
akPu3PFJets25 = akPu5PFJets.clone(rParam       = cms.double(0.3), puPtMin = 25)
akPu3PFJets30 = akPu5PFJets.clone(rParam       = cms.double(0.3), puPtMin = 30)
akPu3PFJets10.radiusPU = 0.5
akPu3PFJets15.radiusPU = 0.5
akPu3PFJets20.radiusPU = 0.5
akPu3PFJets25.radiusPU = 0.5
akPu3PFJets30.radiusPU = 0.5

#R=0.4
akPu4PFJets10 = akPu5PFJets.clone(rParam       = cms.double(0.4), puPtMin = 10)
akPu4PFJets15 = akPu5PFJets.clone(rParam       = cms.double(0.4), puPtMin = 15) 
akPu4PFJets20 = akPu5PFJets.clone(rParam       = cms.double(0.4), puPtMin = 20) #default run 1
akPu4PFJets25 = akPu5PFJets.clone(rParam       = cms.double(0.4), puPtMin = 25)
akPu4PFJets30 = akPu5PFJets.clone(rParam       = cms.double(0.4), puPtMin = 30)
akPu4PFJets10.radiusPU = 0.5
akPu4PFJets15.radiusPU = 0.5
akPu4PFJets20.radiusPU = 0.5
akPu4PFJets25.radiusPU = 0.5
akPu4PFJets30.radiusPU = 0.5


hiRecoPFJets3 = cms.Sequence(
    PFTowers*
    akPu3PFJets10*akPu3PFJets15*akPu3PFJets20*akPu3PFJets25*akPu3PFJets30
)

hiRecoPFJets4 = cms.Sequence(
    PFTowers*
    akPu4PFJets10*akPu4PFJets15*akPu4PFJets20*akPu4PFJets25*akPu4PFJets30
)



