import FWCore.ParameterSet.Config as cms

from RecoJets.Configuration.CaloTowersRec_cff import *

## Default Parameter Sets
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *
from RecoHI.HiJetAlgos.HiCaloJetParameters_cff import *

## Calo Towers
CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz')
)

caloTowers = cms.EDProducer("CaloTowerCandidateCreator",
                            src = cms.InputTag("towerMaker"),
                            e = cms.double(0.0),
                            verbose = cms.untracked.int32(0),
                            pt = cms.double(0.0),
                            minimumE = cms.double(0.0),
                            minimumEt = cms.double(0.0),
                            et = cms.double(0.0)
)

## Noise reducing PU subtraction algos

## anti-kT
akPu5CaloJets = cms.EDProducer(
    "FastjetJetProducer",
    HiCaloJetParameters,
    AnomalousCellParameters,
    MultipleAlgoIteratorBlock,
    jetAlgorithm = cms.string("AntiKt"),
    rParam       = cms.double(0.5)
)
akPu5CaloJets.puPtMin = cms.double(10)
akPu5CaloJets.radiusPU = cms.double(0.5)

#R=0.2
akPu2CaloJets05 = akPu5CaloJets.clone(rParam       = cms.double(0.2), puPtMin = 4, nSigmaPU = 0.5)
akPu2CaloJets10 = akPu5CaloJets.clone(rParam       = cms.double(0.2), puPtMin = 4, nSigmaPU = 1)   #default run 1
akPu2CaloJets15 = akPu5CaloJets.clone(rParam       = cms.double(0.2), puPtMin = 4, nSigmaPU = 1.5)
akPu2CaloJets05.radiusPU = 0.5
akPu2CaloJets10.radiusPU = 0.5
akPu2CaloJets15.radiusPU = 0.5

#R=0.3
akPu3CaloJets05 = akPu5CaloJets.clone(rParam       = cms.double(0.3), puPtMin = 6, nSigmaPU = 0.5)
akPu3CaloJets10 = akPu5CaloJets.clone(rParam       = cms.double(0.3), puPtMin = 6, nSigmaPU = 1)   #default run 1
akPu3CaloJets15 = akPu5CaloJets.clone(rParam       = cms.double(0.3), puPtMin = 6, nSigmaPU = 1.5)
akPu3CaloJets05.radiusPU = 0.5
akPu3CaloJets10.radiusPU = 0.5
akPu3CaloJets15.radiusPU = 0.5

#R=0.4
akPu4CaloJets05 = akPu5CaloJets.clone(rParam       = cms.double(0.4), puPtMin = 8, nSigmaPU = 0.5)
akPu4CaloJets10 = akPu5CaloJets.clone(rParam       = cms.double(0.4), puPtMin = 8, nSigmaPU = 1)   #default run 1
akPu4CaloJets15 = akPu5CaloJets.clone(rParam       = cms.double(0.4), puPtMin = 8, nSigmaPU = 1.5)
akPu4CaloJets05.radiusPU = 0.5
akPu4CaloJets10.radiusPU = 0.5
akPu4CaloJets15.radiusPU = 0.5


## Sequences
hiRecoCaloJets = cms.Sequence(
    akPu2CaloJets05*akPu2CaloJets10*akPu2CaloJets15
    *akPu3CaloJets05*akPu3CaloJets10*akPu3CaloJets15
    *akPu4CaloJets05*akPu4CaloJets10*akPu4CaloJets15
)

hiRecoCaloJets2 = cms.Sequence(
    akPu2CaloJets05*akPu2CaloJets10*akPu2CaloJets15
)

hiRecoCaloJets3 = cms.Sequence(
    akPu3CaloJets05*akPu3CaloJets10*akPu3CaloJets15
)

hiRecoCaloJets4 = cms.Sequence(
    akPu4CaloJets05*akPu4CaloJets10*akPu4CaloJets15
)


