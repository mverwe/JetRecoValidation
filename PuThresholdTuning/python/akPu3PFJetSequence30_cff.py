import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_PbPb_mc_cff import *

#PU jets with 30 GeV threshold for subtraction
akPu3PFmatch30 = akPu3PFmatch.clone(src = cms.InputTag("akPu3PFJets30"))
akPu3PFparton30 = akPu3PFparton.clone(src = cms.InputTag("akPu3PFJets30"))
akPu3PFcorr30 = akPu3PFcorr.clone(src = cms.InputTag("akPu3PFJets30"))
akPu3PFpatJets30 = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu3PFJets30"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3PFcorr30")),
                                        genJetMatch = cms.InputTag("akPu3PFmatch30"),
                                        genPartonMatch = cms.InputTag("akPu3PFparton30"),
)
akPu3PFJetAnalyzer30 = akPu3PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu3PFpatJets30") )
akPu3PFJetSequence30 = cms.Sequence(akPu3PFmatch30
                                            *
                                            akPu3PFparton30
                                            *
                                            akPu3PFcorr30
                                            *
                                            akPu3PFpatJets30
                                            *
                                            akPu3PFJetAnalyzer30
)
