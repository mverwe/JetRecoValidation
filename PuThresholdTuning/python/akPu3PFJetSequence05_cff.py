import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_PbPb_mc_cff import *

#PU jets: type 05
akPu3PFmatch05 = akPu3PFmatch.clone(src = cms.InputTag("akPu3PFJets05"))
akPu3PFparton05 = akPu3PFparton.clone(src = cms.InputTag("akPu3PFJets05"))
akPu3PFcorr05 = akPu3PFcorr.clone(src = cms.InputTag("akPu3PFJets05"))
akPu3PFpatJets05 = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu3PFJets05"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3PFcorr05")),
                                        genJetMatch = cms.InputTag("akPu3PFmatch05"),
                                        genPartonMatch = cms.InputTag("akPu3PFparton05"),
)
akPu3PFJetAnalyzer05 = akPu3PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu3PFpatJets05"), doSubEvent = cms.untracked.bool(True) )
akPu3PFJetSequence05 = cms.Sequence(akPu3PFmatch05
                                  *
                                  akPu3PFparton05
                                  *
                                  akPu3PFcorr05
                                  *
                                  akPu3PFpatJets05
                                  *
                                  akPu3PFJetAnalyzer05
)
