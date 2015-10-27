import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu2CaloJetSequence_PbPb_mc_cff import *

#PU jets with 10 GeV threshold for subtraction
akPu2Calomatch10 = akPu2Calomatch.clone(src = cms.InputTag("akPu2CaloJets10"))
akPu2Caloparton10 = akPu2Caloparton.clone(src = cms.InputTag("akPu2CaloJets10"))
akPu2Calocorr10 = akPu2Calocorr.clone(src = cms.InputTag("akPu2CaloJets10"))
akPu2CalopatJets10 = akPu2CalopatJets.clone(jetSource = cms.InputTag("akPu2CaloJets10"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2Calocorr10")),
                                        genJetMatch = cms.InputTag("akPu2Calomatch10"),
                                        genPartonMatch = cms.InputTag("akPu2Caloparton10"),
)
akPu2CaloJetAnalyzer10 = akPu2CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu2CalopatJets10"), doSubEvent = cms.untracked.bool(True) )
akPu2CaloJetSequence10 = cms.Sequence(akPu2Calomatch10
                                     *
                                     akPu2Caloparton10
                                     *
                                     akPu2Calocorr10
                                     *
                                     akPu2CalopatJets10
                                     *
                                     akPu2CaloJetAnalyzer10
)
