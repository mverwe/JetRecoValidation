import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_PbPb_mc_cff import *

#PU jets: type 05
akPu4Calomatch05 = akPu4Calomatch.clone(src = cms.InputTag("akPu4CaloJets05"))
akPu4Caloparton05 = akPu4Caloparton.clone(src = cms.InputTag("akPu4CaloJets05"))
akPu4Calocorr05 = akPu4Calocorr.clone(src = cms.InputTag("akPu4CaloJets05"))
akPu4CalopatJets05 = akPu4CalopatJets.clone(jetSource = cms.InputTag("akPu4CaloJets05"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4Calocorr05")),
                                        genJetMatch = cms.InputTag("akPu4Calomatch05"),
                                        genPartonMatch = cms.InputTag("akPu4Caloparton05"),
)
akPu4CaloJetAnalyzer05 = akPu4CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu4CalopatJets05"), doSubEvent = cms.untracked.bool(True) )
akPu4CaloJetSequence05 = cms.Sequence(akPu4Calomatch05
                                     *
                                     akPu4Caloparton05
                                     *
                                     akPu4Calocorr05
                                     *
                                     akPu4CalopatJets05
                                     *
                                     akPu4CaloJetAnalyzer05
)
