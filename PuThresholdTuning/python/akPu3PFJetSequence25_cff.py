import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_PbPb_mc_cff import *

#PU jets with 25 GeV threshold for subtraction
akPu3PFmatch25 = akPu3PFmatch.clone(src = cms.InputTag("akPu3PFJets25"))
akPu3PFparton25 = akPu3PFparton.clone(src = cms.InputTag("akPu3PFJets25"))
akPu3PFcorr25 = akPu3PFcorr.clone(src = cms.InputTag("akPu3PFJets25"))
akPu3PFpatJets25 = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu3PFJets25"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3PFcorr25")),
                                        genJetMatch = cms.InputTag("akPu3PFmatch25"),
                                        genPartonMatch = cms.InputTag("akPu3PFparton25"),
)
akPu3PFJetAnalyzer25 = akPu3PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu3PFpatJets25"), doSubEvent = cms.untracked.bool(True) )
akPu3PFJetSequence25 = cms.Sequence(akPu3PFmatch25
                                            *
                                            akPu3PFparton25
                                            *
                                            akPu3PFcorr25
                                            *
                                            akPu3PFpatJets25
                                            *
                                            akPu3PFJetAnalyzer25
)
