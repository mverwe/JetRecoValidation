import FWCore.ParameterSet.Config as cms

#Creates sequences with various nSigmaPU for PU jet algorithm

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

#R=0.2
akPu2PFJets05 = akPu5PFJets.clone(rParam       = cms.double(0.2), puPtMin = 10, nSigmaPU = 0.5)
akPu2PFJets10 = akPu5PFJets.clone(rParam       = cms.double(0.2), puPtMin = 10, nSigmaPU = 1)   #default run 1
akPu2PFJets15 = akPu5PFJets.clone(rParam       = cms.double(0.2), puPtMin = 10, nSigmaPU = 1.5)
akPu2PFJets05.radiusPU = 0.5
akPu2PFJets10.radiusPU = 0.5
akPu2PFJets15.radiusPU = 0.5


#R=0.3
akPu3PFJets05 = akPu5PFJets.clone(rParam       = cms.double(0.3), puPtMin = 15, nSigmaPU = 0.5)
akPu3PFJets10 = akPu5PFJets.clone(rParam       = cms.double(0.3), puPtMin = 15, nSigmaPU = 1)   #default run 1
akPu3PFJets15 = akPu5PFJets.clone(rParam       = cms.double(0.3), puPtMin = 15, nSigmaPU = 1.5)
akPu3PFJets05.radiusPU = 0.5
akPu3PFJets10.radiusPU = 0.5
akPu3PFJets15.radiusPU = 0.5

#R=0.4
akPu4PFJets05 = akPu5PFJets.clone(rParam       = cms.double(0.4), puPtMin = 20, nSigmaPU = 0.5)
akPu4PFJets10 = akPu5PFJets.clone(rParam       = cms.double(0.4), puPtMin = 20, nSigmaPU = 1)   #default run 1
akPu4PFJets15 = akPu5PFJets.clone(rParam       = cms.double(0.4), puPtMin = 20, nSigmaPU = 1.5)
akPu4PFJets05.radiusPU = 0.5
akPu4PFJets10.radiusPU = 0.5
akPu4PFJets15.radiusPU = 0.5

hiRecoPFJets = cms.Sequence(
    PFTowers
    *akPu2PFJets05*akPu2PFJets10*akPu2PFJets15
    *akPu3PFJets05*akPu3PFJets10*akPu3PFJets15
    *akPu4PFJets05*akPu4PFJets10*akPu4PFJets15
)

hiRecoPFJets2 = cms.Sequence(
    PFTowers
    *akPu2PFJets05*akPu2PFJets10*akPu2PFJets15
)

hiRecoPFJets3 = cms.Sequence(
    PFTowers
    *akPu3PFJets05*akPu3PFJets10*akPu3PFJets15
)

hiRecoPFJets4 = cms.Sequence(
    PFTowers
    *akPu4PFJets05*akPu4PFJets10*akPu4PFJets15
)



