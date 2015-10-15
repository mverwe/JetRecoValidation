import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu3PFJetSequence_PbPb_mc_cff import *

#PU jets with 20 GeV threshold for subtraction
akPu3PFmatch20 = akPu3PFmatch.clone(src = cms.InputTag("akPu3PFJets20"))
akPu3PFparton20 = akPu3PFparton.clone(src = cms.InputTag("akPu3PFJets20"))
akPu3PFcorr20 = akPu3PFcorr.clone(src = cms.InputTag("akPu3PFJets20"))
akPu3PFpatJets20 = akPu3PFpatJets.clone(jetSource = cms.InputTag("akPu3PFJets20"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3PFcorr20")),
                                        genJetMatch = cms.InputTag("akPu3PFmatch20"),
                                        genPartonMatch = cms.InputTag("akPu3PFparton20"),
)
akPu3PFJetAnalyzer20 = akPu3PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu3PFpatJets20"), doSubEvent = cms.untracked.bool(True) )
akPu3PFJetSequence20 = cms.Sequence(akPu3PFmatch20
                                            *
                                            akPu3PFparton20
                                            *
                                            akPu3PFcorr20
                                            *
                                            akPu3PFpatJets20
                                            *
                                            akPu3PFJetAnalyzer20
)
