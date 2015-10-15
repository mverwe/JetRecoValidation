import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu4PFJetSequence_PbPb_mc_cff import *

#PU jets with 20 GeV threshold for subtraction
akPu4PFmatch20 = akPu4PFmatch.clone(src = cms.InputTag("akPu4PFJets20"))
akPu4PFparton20 = akPu4PFparton.clone(src = cms.InputTag("akPu4PFJets20"))
akPu4PFcorr20 = akPu4PFcorr.clone(src = cms.InputTag("akPu4PFJets20"))
akPu4PFpatJets20 = akPu4PFpatJets.clone(jetSource = cms.InputTag("akPu4PFJets20"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4PFcorr20")),
                                        genJetMatch = cms.InputTag("akPu4PFmatch20"),
                                        genPartonMatch = cms.InputTag("akPu4PFparton20"),
)
akPu4PFJetAnalyzer20 = akPu4PFJetAnalyzer.clone(jetTag = cms.InputTag("akPu4PFpatJets20"), doSubEvent = cms.untracked.bool(True) )
akPu4PFJetSequence20 = cms.Sequence(akPu4PFmatch20
                                            *
                                            akPu4PFparton20
                                            *
                                            akPu4PFcorr20
                                            *
                                            akPu4PFpatJets20
                                            *
                                            akPu4PFJetAnalyzer20
)
