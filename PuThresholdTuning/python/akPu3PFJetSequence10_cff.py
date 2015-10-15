import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_PbPb_mc_cff import *

#PU jets with 10 GeV threshold for subtraction
akPu3PFmatch10 = akPu3PFmatch.clone(src = cms.InputTag("akPu3PFJets10"))
akPu3PFparton10 = akPu3PFparton.clone(src = cms.InputTag("akPu3PFJets10"))
akPu3PFcorr10 = akPu3PFcorr.clone(src = cms.InputTag("akPu3PFJets10"))
akPu3PFpatJets10 = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu3PFJets10"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3PFcorr10")),
                                        genJetMatch = cms.InputTag("akPu3PFmatch10"),
                                        genPartonMatch = cms.InputTag("akPu3PFparton10"),
)
akPu3PFJetAnalyzer10 = akPu3PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu3PFpatJets10"), doSubEvent = cms.untracked.bool(True) )
akPu3PFJetSequence10 = cms.Sequence(akPu3PFmatch10
                                            *
                                            akPu3PFparton10
                                            *
                                            akPu3PFcorr10
                                            *
                                            akPu3PFpatJets10
                                            *
                                            akPu3PFJetAnalyzer10
)
