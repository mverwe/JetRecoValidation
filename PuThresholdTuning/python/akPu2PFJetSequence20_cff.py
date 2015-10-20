import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu2PFJetSequence_PbPb_mc_cff import *

#PU jets with 20 GeV threshold for subtraction
akPu2PFmatch20 = akPu2PFmatch.clone(src = cms.InputTag("akPu2PFJets20"))
akPu2PFparton20 = akPu2PFparton.clone(src = cms.InputTag("akPu2PFJets20"))
akPu2PFcorr20 = akPu2PFcorr.clone(src = cms.InputTag("akPu2PFJets20"))
akPu2PFpatJets20 = akPu2PFpatJets.clone(jetSource = cms.InputTag("akPu2PFJets20"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2PFcorr20")),
                                        genJetMatch = cms.InputTag("akPu2PFmatch20"),
                                        genPartonMatch = cms.InputTag("akPu2PFparton20"),
)
akPu2PFJetAnalyzer20 = akPu2PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu2PFpatJets20"), doSubEvent = cms.untracked.bool(True) )
akPu2PFJetSequence20 = cms.Sequence(akPu2PFmatch20
                                    *
                                    akPu2PFparton20
                                    *
                                    akPu2PFcorr20
                                    *
                                    akPu2PFpatJets20
                                    *
                                    akPu2PFJetAnalyzer20
)
