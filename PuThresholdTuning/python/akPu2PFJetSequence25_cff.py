import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu2PFJetSequence_PbPb_mc_cff import *

#PU jets with 25 GeV threshold for subtraction
akPu2PFmatch25 = akPu2PFmatch.clone(src = cms.InputTag("akPu2PFJets25"))
akPu2PFparton25 = akPu2PFparton.clone(src = cms.InputTag("akPu2PFJets25"))
akPu2PFcorr25 = akPu2PFcorr.clone(src = cms.InputTag("akPu2PFJets25"))
akPu2PFpatJets25 = akPu2PFpatJets.clone(jetSource = cms.InputTag("akPu2PFJets25"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2PFcorr25")),
                                        genJetMatch = cms.InputTag("akPu2PFmatch25"),
                                        genPartonMatch = cms.InputTag("akPu2PFparton25"),
)
akPu2PFJetAnalyzer25 = akPu2PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu2PFpatJets25"), doSubEvent = cms.untracked.bool(True) )
akPu2PFJetSequence25 = cms.Sequence(akPu2PFmatch25
                                    *
                                    akPu2PFparton25
                                    *
                                    akPu2PFcorr25
                                    *
                                    akPu2PFpatJets25
                                    *
                                    akPu2PFJetAnalyzer25
)
