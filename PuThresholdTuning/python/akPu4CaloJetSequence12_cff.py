import FWCore.ParameterSet.Config as cms

from HeavyIonsAnalysis.JetAnalysis.jets.akPu4CaloJetSequence_PbPb_mc_cff import *

#PU jets with 12 GeV threshold for subtraction
akPu4Calomatch12 = akPu4Calomatch.clone(src = cms.InputTag("akPu4CaloJets12"))
akPu4Caloparton12 = akPu4Caloparton.clone(src = cms.InputTag("akPu4CaloJets12"))
akPu4Calocorr12 = akPu4Calocorr.clone(src = cms.InputTag("akPu4CaloJets12"))
akPu4CalopatJets12 = akPu4CalopatJets.clone(jetSource = cms.InputTag("akPu4CaloJets12"),
                                        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu4Calocorr12")),
                                        genJetMatch = cms.InputTag("akPu4Calomatch12"),
                                        genPartonMatch = cms.InputTag("akPu4Caloparton12"),
)
akPu4CaloJetAnalyzer12 = akPu4CaloJetAnalyzer.clone(jetTag = cms.InputTag("akPu4CalopatJets12"), doSubEvent = cms.untracked.bool(True) )
akPu4CaloJetSequence12 = cms.Sequence(akPu4Calomatch12
                                     *
                                     akPu4Caloparton12
                                     *
                                     akPu4Calocorr12
                                     *
                                     akPu4CalopatJets12
                                     *
                                     akPu4CaloJetAnalyzer12
)
