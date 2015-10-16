import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_PbPb_mc_cff import *

#PU jets with 8 GeV threshold for subtraction
akPu4Calomatch8 = akPu4Calomatch.clone(src = cms.InputTag("akPu4CaloJets8"))
akPu4Caloparton8 = akPu4Caloparton.clone(src = cms.InputTag("akPu4CaloJets8"))
akPu4Calocorr8 = akPu4Calocorr.clone(src = cms.InputTag("akPu4CaloJets8"))
akPu4CalopatJets8 = akPu4CalopatJets.clone(jetSource = cms.InputTag("akPu4CaloJets8"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4Calocorr8")),
                                        genJetMatch = cms.InputTag("akPu4Calomatch8"),
                                        genPartonMatch = cms.InputTag("akPu4Caloparton8"),
)
akPu4CaloJetAnalyzer8 = akPu4CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu4CalopatJets8"), doSubEvent = cms.untracked.bool(True) )
akPu4CaloJetSequence8 = cms.Sequence(akPu4Calomatch8
                                     *
                                     akPu4Caloparton8
                                     *
                                     akPu4Calocorr8
                                     *
                                     akPu4CalopatJets8
                                     *
                                     akPu4CaloJetAnalyzer8
)
