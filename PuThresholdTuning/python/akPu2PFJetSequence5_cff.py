import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu2PFJetSequence_PbPb_mc_cff import *

#PU jets with 5 GeV threshold for subtraction
akPu2PFmatch5 = akPu2PFmatch.clone(src = cms.InputTag("akPu2PFJets5"))
akPu2PFparton5 = akPu2PFparton.clone(src = cms.InputTag("akPu2PFJets5"))
akPu2PFcorr5 = akPu2PFcorr.clone(src = cms.InputTag("akPu2PFJets5"))
akPu2PFpatJets5 = akPu2PFpatJets.clone(jetSource = cms.InputTag("akPu2PFJets5"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2PFcorr5")),
                                        genJetMatch = cms.InputTag("akPu2PFmatch5"),
                                        genPartonMatch = cms.InputTag("akPu2PFparton5"),
)
akPu2PFJetAnalyzer5 = akPu2PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu2PFpatJets5"), doSubEvent = cms.untracked.bool(True) )
akPu2PFJetSequence5 = cms.Sequence(akPu2PFmatch5
                                    *
                                    akPu2PFparton5
                                    *
                                    akPu2PFcorr5
                                    *
                                    akPu2PFpatJets5
                                    *
                                    akPu2PFJetAnalyzer5
)
