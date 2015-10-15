import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_PbPb_mc_cff import *

#PU jets with 15 GeV threshold for subtraction
akPu4PFmatch15 = akPu4PFmatch.clone(src = cms.InputTag("akPu4PFJets15"))
akPu4PFparton15 = akPu4PFparton.clone(src = cms.InputTag("akPu4PFJets15"))
akPu4PFcorr15 = akPu4PFcorr.clone(src = cms.InputTag("akPu4PFJets15"))
akPu4PFpatJets15 = akPu4PFpatJets.clone(jetSource = cms.InputTag("akPu4PFJets15"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4PFcorr15")),
                                        genJetMatch = cms.InputTag("akPu4PFmatch15"),
                                        genPartonMatch = cms.InputTag("akPu4PFparton15"),
)
akPu4PFJetAnalyzer15 = akPu4PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu4PFpatJets15"), doSubEvent = cms.untracked.bool(True) )
akPu4PFJetSequence15 = cms.Sequence(akPu4PFmatch15
                                            *
                                            akPu4PFparton15
                                            *
                                            akPu4PFcorr15
                                            *
                                            akPu4PFpatJets15
                                            *
                                            akPu4PFJetAnalyzer15
)
