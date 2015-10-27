import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu3CaloJetSequence_PbPb_mc_cff import *

#PU jets: type 15
akPu3Calomatch15 = akPu3Calomatch.clone(src = cms.InputTag("akPu3CaloJets15"))
akPu3Caloparton15 = akPu3Caloparton.clone(src = cms.InputTag("akPu3CaloJets15"))
akPu3Calocorr15 = akPu3Calocorr.clone(src = cms.InputTag("akPu3CaloJets15"))
akPu3CalopatJets15 = akPu3CalopatJets.clone(jetSource = cms.InputTag("akPu3CaloJets15"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3Calocorr15")),
                                        genJetMatch = cms.InputTag("akPu3Calomatch15"),
                                        genPartonMatch = cms.InputTag("akPu3Caloparton15"),
)
akPu3CaloJetAnalyzer15 = akPu3CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu3CalopatJets15"), doSubEvent = cms.untracked.bool(True) )
akPu3CaloJetSequence15 = cms.Sequence(akPu3Calomatch15
                                    *
                                    akPu3Caloparton15
                                    *
                                    akPu3Calocorr15
                                    *
                                    akPu3CalopatJets15
                                    *
                                    akPu3CaloJetAnalyzer15
)
