import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu2CaloJetSequence_PbPb_mc_cff import *

#PU jets: type 05
akPu2Calomatch05 = akPu2Calomatch.clone(src = cms.InputTag("akPu2CaloJets05"))
akPu2Caloparton05 = akPu2Caloparton.clone(src = cms.InputTag("akPu2CaloJets05"))
akPu2Calocorr05 = akPu2Calocorr.clone(src = cms.InputTag("akPu2CaloJets05"))
akPu2CalopatJets05 = akPu2CalopatJets.clone(jetSource = cms.InputTag("akPu2CaloJets05"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2Calocorr05")),
                                        genJetMatch = cms.InputTag("akPu2Calomatch05"),
                                        genPartonMatch = cms.InputTag("akPu2Caloparton05"),
)
akPu2CaloJetAnalyzer05 = akPu2CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu2CalopatJets05"), doSubEvent = cms.untracked.bool(True) )
akPu2CaloJetSequence05 = cms.Sequence(akPu2Calomatch05
                                    *
                                    akPu2Caloparton05
                                    *
                                    akPu2Calocorr05
                                    *
                                    akPu2CalopatJets05
                                    *
                                    akPu2CaloJetAnalyzer05
)
