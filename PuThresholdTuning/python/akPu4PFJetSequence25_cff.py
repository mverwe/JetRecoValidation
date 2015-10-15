import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_PbPb_mc_cff import *

#PU jets with 25 GeV threshold for subtraction
akPu4PFmatch25 = akPu4PFmatch.clone(src = cms.InputTag("akPu4PFJets25"))
akPu4PFparton25 = akPu4PFparton.clone(src = cms.InputTag("akPu4PFJets25"))
akPu4PFcorr25 = akPu4PFcorr.clone(src = cms.InputTag("akPu4PFJets25"))
akPu4PFpatJets25 = akPu4PFpatJets.clone(jetSource = cms.InputTag("akPu4PFJets25"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4PFcorr25")),
                                        genJetMatch = cms.InputTag("akPu4PFmatch25"),
                                        genPartonMatch = cms.InputTag("akPu4PFparton25"),
)
akPu4PFJetAnalyzer25 = akPu4PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu4PFpatJets25"), doSubEvent = cms.untracked.bool(True) )
akPu4PFJetSequence25 = cms.Sequence(akPu4PFmatch25
                                            *
                                            akPu4PFparton25
                                            *
                                            akPu4PFcorr25
                                            *
                                            akPu4PFpatJets25
                                            *
                                            akPu4PFJetAnalyzer25
)
