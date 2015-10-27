import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_PbPb_mc_cff import *

#PU jets: type 05
akPu4PFmatch05 = akPu4PFmatch.clone(src = cms.InputTag("akPu4PFJets05"))
akPu4PFparton05 = akPu4PFparton.clone(src = cms.InputTag("akPu4PFJets05"))
akPu4PFcorr05 = akPu4PFcorr.clone(src = cms.InputTag("akPu4PFJets05"))
akPu4PFpatJets05 = akPu4PFpatJets.clone(jetSource = cms.InputTag("akPu4PFJets05"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4PFcorr05")),
                                        genJetMatch = cms.InputTag("akPu4PFmatch05"),
                                        genPartonMatch = cms.InputTag("akPu4PFparton05"),
)
akPu4PFJetAnalyzer05 = akPu4PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu4PFpatJets05"), doSubEvent = cms.untracked.bool(True) )
akPu4PFJetSequence05 = cms.Sequence(akPu4PFmatch05
                                  *
                                  akPu4PFparton05
                                  *
                                  akPu4PFcorr05
                                  *
                                  akPu4PFpatJets05
                                  *
                                  akPu4PFJetAnalyzer05
)
