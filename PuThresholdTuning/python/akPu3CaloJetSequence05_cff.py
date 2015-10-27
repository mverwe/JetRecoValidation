import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu3CaloJetSequence_PbPb_mc_cff import *

#PU jets: type 05
akPu3Calomatch05 = akPu3Calomatch.clone(src = cms.InputTag("akPu3CaloJets05"))
akPu3Caloparton05 = akPu3Caloparton.clone(src = cms.InputTag("akPu3CaloJets05"))
akPu3Calocorr05 = akPu3Calocorr.clone(src = cms.InputTag("akPu3CaloJets05"))
akPu3CalopatJets05 = akPu3CalopatJets.clone(jetSource = cms.InputTag("akPu3CaloJets05"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3Calocorr05")),
                                        genJetMatch = cms.InputTag("akPu3Calomatch05"),
                                        genPartonMatch = cms.InputTag("akPu3Caloparton05"),
)
akPu3CaloJetAnalyzer05 = akPu3CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu3CalopatJets05"), doSubEvent = cms.untracked.bool(True) )
akPu3CaloJetSequence05 = cms.Sequence(akPu3Calomatch05
                                    *
                                    akPu3Caloparton05
                                    *
                                    akPu3Calocorr05
                                    *
                                    akPu3CalopatJets05
                                    *
                                    akPu3CaloJetAnalyzer05
)
