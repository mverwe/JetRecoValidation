import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu2CaloJetSequence_PbPb_mc_cff import *

#PU jets with 2 GeV threshold for subtraction
akPu2Calomatch2 = akPu4Calomatch.clone(src = cms.InputTag("akPu2CaloJets2"))
akPu2Caloparton2 = akPu4Caloparton.clone(src = cms.InputTag("akPu2CaloJets2"))
akPu2Calocorr2 = akPu4Calocorr.clone(src = cms.InputTag("akPu2CaloJets2"))
akPu2CalopatJets2 = akPu4CalopatJets.clone(jetSource = cms.InputTag("akPu2CaloJets2"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2Calocorr2")),
                                        genJetMatch = cms.InputTag("akPu2Calomatch2"),
                                        genPartonMatch = cms.InputTag("akPu2Caloparton2"),
)
akPu2CaloJetAnalyzer2 = akPu4CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu2CalopatJets2"), doSubEvent = cms.untracked.bool(True) )
akPu2CaloJetSequence2 = cms.Sequence(akPu2Calomatch2
                                     *
                                     akPu2Caloparton2
                                     *
                                     akPu2Calocorr2
                                     *
                                     akPu2CalopatJets2
                                     *
                                     akPu2CaloJetAnalyzer2
)
