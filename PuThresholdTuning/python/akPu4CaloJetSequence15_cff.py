import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_PbPb_mc_cff import *

#PU jets: type 15
akPu4Calomatch15 = akPu4Calomatch.clone(src = cms.InputTag("akPu4CaloJets15"))
akPu4Caloparton15 = akPu4Caloparton.clone(src = cms.InputTag("akPu4CaloJets15"))
akPu4Calocorr15 = akPu4Calocorr.clone(src = cms.InputTag("akPu4CaloJets15"))
akPu4CalopatJets15 = akPu4CalopatJets.clone(jetSource = cms.InputTag("akPu4CaloJets15"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4Calocorr15")),
                                        genJetMatch = cms.InputTag("akPu4Calomatch15"),
                                        genPartonMatch = cms.InputTag("akPu4Caloparton15"),
)
akPu4CaloJetAnalyzer15 = akPu4CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu4CalopatJets15"), doSubEvent = cms.untracked.bool(True) )
akPu4CaloJetSequence15 = cms.Sequence(akPu4Calomatch15
                                     *
                                     akPu4Caloparton15
                                     *
                                     akPu4Calocorr15
                                     *
                                     akPu4CalopatJets15
                                     *
                                     akPu4CaloJetAnalyzer15
)
