import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_PbPb_mc_cff import *

#PU jets with 10 GeV threshold for subtraction
akPu4Calomatch10 = akPu4Calomatch.clone(src = cms.InputTag("akPu4CaloJets10"))
akPu4Caloparton10 = akPu4Caloparton.clone(src = cms.InputTag("akPu4CaloJets10"))
akPu4Calocorr10 = akPu4Calocorr.clone(src = cms.InputTag("akPu4CaloJets10"))
akPu4CalopatJets10 = akPu4CalopatJets.clone(jetSource = cms.InputTag("akPu4CaloJets10"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4Calocorr10")),
                                        genJetMatch = cms.InputTag("akPu4Calomatch10"),
                                        genPartonMatch = cms.InputTag("akPu4Caloparton10"),
)
akPu4CaloJetAnalyzer10 = akPu4CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu4CalopatJets10"), doSubEvent = cms.untracked.bool(True) )
akPu4CaloJetSequence10 = cms.Sequence(akPu4Calomatch10
                                     *
                                     akPu4Caloparton10
                                     *
                                     akPu4Calocorr10
                                     *
                                     akPu4CalopatJets10
                                     *
                                     akPu4CaloJetAnalyzer10
)
