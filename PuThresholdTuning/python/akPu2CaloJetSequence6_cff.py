import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu2CaloJetSequence_PbPb_mc_cff import *

#PU jets with 6 GeV threshold for subtraction
akPu2Calomatch6 = akPu4Calomatch.clone(src = cms.InputTag("akPu2CaloJets6"))
akPu2Caloparton6 = akPu4Caloparton.clone(src = cms.InputTag("akPu2CaloJets6"))
akPu2Calocorr6 = akPu4Calocorr.clone(src = cms.InputTag("akPu2CaloJets6"))
akPu2CalopatJets6 = akPu4CalopatJets.clone(jetSource = cms.InputTag("akPu2CaloJets6"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2Calocorr6")),
                                        genJetMatch = cms.InputTag("akPu2Calomatch6"),
                                        genPartonMatch = cms.InputTag("akPu2Caloparton6"),
)
akPu2CaloJetAnalyzer6 = akPu4CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu2CalopatJets6"), doSubEvent = cms.untracked.bool(True) )
akPu2CaloJetSequence6 = cms.Sequence(akPu2Calomatch6
                                     *
                                     akPu2Caloparton6
                                     *
                                     akPu2Calocorr6
                                     *
                                     akPu2CalopatJets6
                                     *
                                     akPu2CaloJetAnalyzer6
)
