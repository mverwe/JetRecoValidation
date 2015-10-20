import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu2PFJetSequence_PbPb_mc_cff import *

#PU jets with 10 GeV threshold for subtraction
akPu2PFmatch10 = akPu2PFmatch.clone(src = cms.InputTag("akPu2PFJets10"))
akPu2PFparton10 = akPu2PFparton.clone(src = cms.InputTag("akPu2PFJets10"))
akPu2PFcorr10 = akPu2PFcorr.clone(src = cms.InputTag("akPu2PFJets10"))
akPu2PFpatJets10 = akPu2PFpatJets.clone(jetSource = cms.InputTag("akPu2PFJets10"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2PFcorr10")),
                                        genJetMatch = cms.InputTag("akPu2PFmatch10"),
                                        genPartonMatch = cms.InputTag("akPu2PFparton10"),
)
akPu2PFJetAnalyzer10 = akPu2PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu2PFpatJets10"), doSubEvent = cms.untracked.bool(True) )
akPu2PFJetSequence10 = cms.Sequence(akPu2PFmatch10
                                    *
                                    akPu2PFparton10
                                    *
                                    akPu2PFcorr10
                                    *
                                    akPu2PFpatJets10
                                    *
                                    akPu2PFJetAnalyzer10
)
