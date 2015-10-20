import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu2PFJetSequence_PbPb_mc_cff import *

#PU jets with 15 GeV threshold for subtraction
akPu2PFmatch15 = akPu2PFmatch.clone(src = cms.InputTag("akPu2PFJets15"))
akPu2PFparton15 = akPu2PFparton.clone(src = cms.InputTag("akPu2PFJets15"))
akPu2PFcorr15 = akPu2PFcorr.clone(src = cms.InputTag("akPu2PFJets15"))
akPu2PFpatJets15 = akPu2PFpatJets.clone(jetSource = cms.InputTag("akPu2PFJets15"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2PFcorr15")),
                                        genJetMatch = cms.InputTag("akPu2PFmatch15"),
                                        genPartonMatch = cms.InputTag("akPu2PFparton15"),
)
akPu2PFJetAnalyzer15 = akPu2PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu2PFpatJets15"), doSubEvent = cms.untracked.bool(True) )
akPu2PFJetSequence15 = cms.Sequence(akPu2PFmatch15
                                    *
                                    akPu2PFparton15
                                    *
                                    akPu2PFcorr15
                                    *
                                    akPu2PFpatJets15
                                    *
                                    akPu2PFJetAnalyzer15
)
