import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_PbPb_mc_cff import *

#PU jets with 6 GeV threshold for subtraction
akPu4Calomatch6 = akPu4Calomatch.clone(src = cms.InputTag("akPu4CaloJets6"))
akPu4Caloparton6 = akPu4Caloparton.clone(src = cms.InputTag("akPu4CaloJets6"))
akPu4Calocorr6 = akPu4Calocorr.clone(src = cms.InputTag("akPu4CaloJets6"))
akPu4CalopatJets6 = akPu4CalopatJets.clone(jetSource = cms.InputTag("akPu4CaloJets6"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4Calocorr6")),
                                        genJetMatch = cms.InputTag("akPu4Calomatch6"),
                                        genPartonMatch = cms.InputTag("akPu4Caloparton6"),
)
akPu4CaloJetAnalyzer6 = akPu4CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu4CalopatJets6"), doSubEvent = cms.untracked.bool(True) )
akPu4CaloJetSequence6 = cms.Sequence(akPu4Calomatch6
                                     *
                                     akPu4Caloparton6
                                     *
                                     akPu4Calocorr6
                                     *
                                     akPu4CalopatJets6
                                     *
                                     akPu4CaloJetAnalyzer6
)
