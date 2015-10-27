import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu2PFJetSequence_PbPb_mc_cff import *

#PU jets: type 05
akPu2PFmatch05 = akPu2PFmatch.clone(src = cms.InputTag("akPu2PFJets05"))
akPu2PFparton05 = akPu2PFparton.clone(src = cms.InputTag("akPu2PFJets05"))
akPu2PFcorr05 = akPu2PFcorr.clone(src = cms.InputTag("akPu2PFJets05"))
akPu2PFpatJets05 = akPu2PFpatJets.clone(jetSource = cms.InputTag("akPu2PFJets05"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2PFcorr05")),
                                        genJetMatch = cms.InputTag("akPu2PFmatch05"),
                                        genPartonMatch = cms.InputTag("akPu2PFparton05"),
)
akPu2PFJetAnalyzer05 = akPu2PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu2PFpatJets05"), doSubEvent = cms.untracked.bool(True) )
akPu2PFJetSequence05 = cms.Sequence(akPu2PFmatch05
                                  *
                                  akPu2PFparton05
                                  *
                                  akPu2PFcorr05
                                  *
                                  akPu2PFpatJets05
                                  *
                                  akPu2PFJetAnalyzer05
)
