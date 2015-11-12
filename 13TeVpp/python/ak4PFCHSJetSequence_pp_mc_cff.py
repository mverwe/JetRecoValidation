

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *

ak4PFCHSmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("ak4PFJetsCHS"),
    matched = cms.InputTag("ak4GenJetsNoNu"),
    maxDeltaR = 0.4
    )

ak4PFCHSparton = patJetPartonMatch.clone(src = cms.InputTag("ak4PFJetsCHS"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

ak4PFCHScorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L1FastJet','L2Relative','L3Absolute','L2L3Residual'),
    src = cms.InputTag("ak4PFJetsCHS"),
    payload = "AK4PFchs"
    )

ak4PFCHSpatJets = patJets.clone(jetSource = cms.InputTag("ak4PFJetsCHS"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("ak4PFCHScorr")),
                                               genJetMatch = cms.InputTag("ak4PFCHSmatch"),
                                               genPartonMatch = cms.InputTag("ak4PFCHSparton"),
                                               jetIDMap = cms.InputTag("ak4PFCHSJetID"),
                                               addBTagInfo         = False,
                                               addTagInfos         = False,
                                               addDiscriminators   = False,
                                               addAssociatedTracks = False,
                                               addJetCharge        = False,
                                               addJetID            = False,
                                               getJetMCFlavour     = False,
                                               addGenPartonMatch   = True,
                                               addGenJetMatch      = True,
                                               embedGenJetMatch    = True,
                                               embedGenPartonMatch = True,
                                               # embedCaloTowers     = False,
                                               # embedPFCandidates = False
				            )

ak4PFCHSJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("ak4PFCHSpatJets"),
                                                             genjetTag = 'ak4GenJetsNoNu',
                                                             rParam = 0.4,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'patJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("generalTracks"),
                                                             fillGenJets = True,
                                                             isMC = True,
                                                             genParticles = cms.untracked.InputTag("genParticles"),
							     eventInfoTag = cms.InputTag("generator"),
                                                             jetPtMin = cms.untracked.double(1)
                                                             )

ak4PFCHSJetSequence_mc = cms.Sequence(
						  ak4PFCHSmatch
                                                  *
                                                  ak4PFCHSparton
                                                  *
                                                  ak4PFCHScorr
                                                  *
                                                  ak4PFCHSpatJets
                                                  *
                                                  ak4PFCHSJetAnalyzer
                                                  )

ak4PFCHSJetSequence_data = cms.Sequence(ak4PFCHScorr
                                                    *
                                                    ak4PFCHSpatJets
                                                    *
                                                    ak4PFCHSJetAnalyzer
                                                    )

ak4PFCHSJetSequence_jec = cms.Sequence(ak4PFCHSJetSequence_mc)
ak4PFCHSJetSequence_mix = cms.Sequence(ak4PFCHSJetSequence_mc)

ak4PFCHSJetSequence = cms.Sequence(ak4PFCHSJetSequence_mc)
