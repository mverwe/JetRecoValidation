import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu2CaloJetSequence_PbPb_mc_cff import *

#PU jets: type 15
akPu2Calomatch15 = akPu2Calomatch.clone(src = cms.InputTag("akPu2CaloJets15"))
akPu2Caloparton15 = akPu2Caloparton.clone(src = cms.InputTag("akPu2CaloJets15"))
akPu2Calocorr15 = akPu2Calocorr.clone(src = cms.InputTag("akPu2CaloJets15"))
akPu2CalopatJets15 = akPu2CalopatJets.clone(jetSource = cms.InputTag("akPu2CaloJets15"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu2Calocorr15")),
                                        genJetMatch = cms.InputTag("akPu2Calomatch15"),
                                        genPartonMatch = cms.InputTag("akPu2Caloparton15"),
)
akPu2CaloJetAnalyzer15 = akPu2CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu2CalopatJets15"), doSubEvent = cms.untracked.bool(True) )
akPu2CaloJetSequence15 = cms.Sequence(akPu2Calomatch15
                                    *
                                    akPu2Caloparton15
                                    *
                                    akPu2Calocorr15
                                    *
                                    akPu2CalopatJets15
                                    *
                                    akPu2CaloJetAnalyzer15
)
