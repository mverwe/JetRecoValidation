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
akPu2CaloJets2 = akPu5CaloJets.clone(rParam       = cms.double(0.2), puPtMin = 2)
akPu2CaloJets4 = akPu5CaloJets.clone(rParam       = cms.double(0.2), puPtMin = 4)#default run1
akPu2CaloJets6 = akPu5CaloJets.clone(rParam       = cms.double(0.2), puPtMin = 6)
akPu2CaloJets8 = akPu5CaloJets.clone(rParam       = cms.double(0.2), puPtMin = 8)
akPu2CaloJets10 = akPu5CaloJets.clone(rParam      = cms.double(0.2), puPtMin = 10)
akPu2CaloJets2.radiusPU = 0.5
akPu2CaloJets4.radiusPU = 0.5
akPu2CaloJets6.radiusPU = 0.5
akPu2CaloJets8.radiusPU = 0.5
akPu2CaloJets10.radiusPU = 0.5

#R=0.4
akPu4CaloJets4 = akPu5CaloJets.clone(rParam       = cms.double(0.4), puPtMin = 4)
akPu4CaloJets6 = akPu5CaloJets.clone(rParam       = cms.double(0.4), puPtMin = 6)
akPu4CaloJets8 = akPu5CaloJets.clone(rParam       = cms.double(0.4), puPtMin = 8) #default run 1
akPu4CaloJets10 = akPu5CaloJets.clone(rParam      = cms.double(0.4), puPtMin = 10)
akPu4CaloJets12 = akPu5CaloJets.clone(rParam      = cms.double(0.4), puPtMin = 12)
akPu4CaloJets4.radiusPU = 0.5
akPu4CaloJets6.radiusPU = 0.5
akPu4CaloJets8.radiusPU = 0.5
akPu4CaloJets10.radiusPU = 0.5
akPu4CaloJets12.radiusPU = 0.5

## Sequences
hiRecoCaloJets2 = cms.Sequence(
    akPu2CaloJets2*akPu2CaloJets4*akPu2CaloJets6*akPu2CaloJets8*akPu2CaloJets10
)

hiRecoCaloJets4 = cms.Sequence(
    akPu4CaloJets4*akPu4CaloJets6*akPu4CaloJets8*akPu4CaloJets10*akPu4CaloJets12
)

