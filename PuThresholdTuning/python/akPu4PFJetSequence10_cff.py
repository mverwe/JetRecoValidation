import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_PbPb_mc_cff import *

#PU jets with 10 GeV threshold for subtraction
akPu4PFmatch10 = akPu4PFmatch.clone(src = cms.InputTag("akPu4PFJets10"))
akPu4PFparton10 = akPu4PFparton.clone(src = cms.InputTag("akPu4PFJets10"))
akPu4PFcorr10 = akPu4PFcorr.clone(src = cms.InputTag("akPu4PFJets10"))
akPu4PFpatJets10 = akPu4PFpatJets.clone(jetSource = cms.InputTag("akPu4PFJets10"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4PFcorr10")),
                                        genJetMatch = cms.InputTag("akPu4PFmatch10"),
                                        genPartonMatch = cms.InputTag("akPu4PFparton10"),
)
akPu4PFJetAnalyzer10 = akPu4PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu4PFpatJets10"), doSubEvent = cms.untracked.bool(True) )
akPu4PFJetSequence10 = cms.Sequence(akPu4PFmatch10
                                    *
                                    akPu4PFparton10
                                    *
                                    akPu4PFcorr10
                                    *
                                    akPu4PFpatJets10
                                    *
                                    akPu4PFJetAnalyzer10
)
