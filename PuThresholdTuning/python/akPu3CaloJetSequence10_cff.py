import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu3CaloJetSequence_PbPb_mc_cff import *

#PU jets: type 10
akPu3Calomatch10 = akPu3Calomatch.clone(src = cms.InputTag("akPu3CaloJets10"))
akPu3Caloparton10 = akPu3Caloparton.clone(src = cms.InputTag("akPu3CaloJets10"))
akPu3Calocorr10 = akPu3Calocorr.clone(src = cms.InputTag("akPu3CaloJets10"))
akPu3CalopatJets10 = akPu3CalopatJets.clone(jetSource = cms.InputTag("akPu3CaloJets10"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3Calocorr10")),
                                        genJetMatch = cms.InputTag("akPu3Calomatch10"),
                                        genPartonMatch = cms.InputTag("akPu3Caloparton10"),
)
akPu3CaloJetAnalyzer10 = akPu3CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu3CalopatJets10"), doSubEvent = cms.untracked.bool(True) )
akPu3CaloJetSequence10 = cms.Sequence(akPu3Calomatch10
                                    *
                                    akPu3Caloparton10
                                    *
                                    akPu3Calocorr10
                                    *
                                    akPu3CalopatJets10
                                    *
                                    akPu3CaloJetAnalyzer10
)
