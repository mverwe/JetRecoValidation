import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu2CaloJetSequence_PbPb_mc_cff import *

#PU jets with 8 GeV threshold for subtraction
akPu2Calomatch8 = akPu4Calomatch.clone(src = cms.InputTag("akPu2CaloJets8"))
akPu2Caloparton8 = akPu4Caloparton.clone(src = cms.InputTag("akPu2CaloJets8"))
akPu2Calocorr8 = akPu4Calocorr.clone(src = cms.InputTag("akPu2CaloJets8"))
akPu2CalopatJets8 = akPu4CalopatJets.clone(jetSource = cms.InputTag("akPu2CaloJets8"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2Calocorr8")),
                                        genJetMatch = cms.InputTag("akPu2Calomatch8"),
                                        genPartonMatch = cms.InputTag("akPu2Caloparton8"),
)
akPu2CaloJetAnalyzer8 = akPu4CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu2CalopatJets8"), doSubEvent = cms.untracked.bool(True) )
akPu2CaloJetSequence8 = cms.Sequence(akPu2Calomatch8
                                     *
                                     akPu2Caloparton8
                                     *
                                     akPu2Calocorr8
                                     *
                                     akPu2CalopatJets8
                                     *
                                     akPu2CaloJetAnalyzer8
)
