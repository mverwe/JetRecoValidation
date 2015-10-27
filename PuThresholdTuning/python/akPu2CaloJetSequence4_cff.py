import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu2CaloJetSequence_PbPb_mc_cff import *

#PU jets with 4 GeV threshold for subtraction
akPu2Calomatch4 = akPu4Calomatch.clone(src = cms.InputTag("akPu2CaloJets4"))
akPu2Caloparton4 = akPu4Caloparton.clone(src = cms.InputTag("akPu2CaloJets4"))
akPu2Calocorr4 = akPu4Calocorr.clone(src = cms.InputTag("akPu2CaloJets4"))
akPu2CalopatJets4 = akPu4CalopatJets.clone(jetSource = cms.InputTag("akPu2CaloJets4"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2Calocorr4")),
                                        genJetMatch = cms.InputTag("akPu2Calomatch4"),
                                        genPartonMatch = cms.InputTag("akPu2Caloparton4"),
)
akPu2CaloJetAnalyzer4 = akPu4CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu2CalopatJets4"), doSubEvent = cms.untracked.bool(True) )
akPu2CaloJetSequence4 = cms.Sequence(akPu2Calomatch4
                                     *
                                     akPu2Caloparton4
                                     *
                                     akPu2Calocorr4
                                     *
                                     akPu2CalopatJets4
                                     *
                                     akPu2CaloJetAnalyzer4
)
