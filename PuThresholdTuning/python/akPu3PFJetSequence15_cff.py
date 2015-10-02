import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_PbPb_mc_cff import *

#PU jets with 15 GeV threshold for subtraction
akPu3PFmatch15 = akPu3PFmatch.clone(src = cms.InputTag("akPu3PFJets15"))
akPu3PFparton15 = akPu3PFparton.clone(src = cms.InputTag("akPu3PFJets15"))
akPu3PFcorr15 = akPu3PFcorr.clone(src = cms.InputTag("akPu3PFJets15"))
akPu3PFpatJets15 = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu3PFJets15"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3PFcorr15")),
                                        genJetMatch = cms.InputTag("akPu3PFmatch15"),
                                        genPartonMatch = cms.InputTag("akPu3PFparton15"),
)
akPu3PFJetAnalyzer15 = akPu3PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu3PFpatJets15") )
akPu3PFJetSequence15 = cms.Sequence(akPu3PFmatch15
                                            *
                                            akPu3PFparton15
                                            *
                                            akPu3PFcorr15
                                            *
                                            akPu3PFpatJets15
                                            *
                                            akPu3PFJetAnalyzer15
)
