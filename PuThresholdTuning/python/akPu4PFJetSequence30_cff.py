import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_PbPb_mc_cff import *

#PU jets with 30 GeV threshold for subtraction
akPu4PFmatch30 = akPu4PFmatch.clone(src = cms.InputTag("akPu4PFJets30"))
akPu4PFparton30 = akPu4PFparton.clone(src = cms.InputTag("akPu4PFJets30"))
akPu4PFcorr30 = akPu4PFcorr.clone(src = cms.InputTag("akPu4PFJets30"))
akPu4PFpatJets30 = akPu4PFpatJets.clone(jetSource = cms.InputTag("akPu4PFJets30"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4PFcorr30")),
                                        genJetMatch = cms.InputTag("akPu4PFmatch30"),
                                        genPartonMatch = cms.InputTag("akPu4PFparton30"),
)
akPu4PFJetAnalyzer30 = akPu4PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu4PFpatJets30"), doSubEvent = cms.untracked.bool(True) )
akPu4PFJetSequence30 = cms.Sequence(akPu4PFmatch30
                                            *
                                            akPu4PFparton30
                                            *
                                            akPu4PFcorr30
                                            *
                                            akPu4PFpatJets30
                                            *
                                            akPu4PFJetAnalyzer30
)
