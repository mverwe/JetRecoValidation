import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_PbPb_mc_cff import *

#PU jets with 4 GeV threshold for subtraction
akPu4Calomatch4 = akPu4Calomatch.clone(src = cms.InputTag("akPu4CaloJets4"))
akPu4Caloparton4 = akPu4Caloparton.clone(src = cms.InputTag("akPu4CaloJets4"))
akPu4Calocorr4 = akPu4Calocorr.clone(src = cms.InputTag("akPu4CaloJets4"))
akPu4CalopatJets4 = akPu4CalopatJets.clone(jetSource = cms.InputTag("akPu4CaloJets4"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4Calocorr4")),
                                        genJetMatch = cms.InputTag("akPu4Calomatch4"),
                                        genPartonMatch = cms.InputTag("akPu4Caloparton4"),
)
akPu4CaloJetAnalyzer4 = akPu4CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu4CalopatJets4"), doSubEvent = cms.untracked.bool(True) )
akPu4CaloJetSequence4 = cms.Sequence(akPu4Calomatch4
                                     *
                                     akPu4Caloparton4
                                     *
                                     akPu4Calocorr4
                                     *
                                     akPu4CalopatJets4
                                     *
                                     akPu4CaloJetAnalyzer4
)
