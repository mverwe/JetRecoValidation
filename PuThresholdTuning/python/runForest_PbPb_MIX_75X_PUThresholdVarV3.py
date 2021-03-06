import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')
process.options = cms.untracked.PSet(
    # wantSummary = cms.untracked.bool(True)
    #SkipEvent = cms.untracked.vstring('ProductNotFound')
)

#####################################################################################
# HiForest labelling info
#####################################################################################

process.load("HeavyIonsAnalysis.JetAnalysis.HiForest_cff")
process.HiForest.inputLines = cms.vstring("HiForest V3",)
import subprocess
version = subprocess.Popen(["(cd $CMSSW_BASE/src && git describe --tags)"], stdout=subprocess.PIPE, shell=True).stdout.read()
if version == '':
    version = 'no git info'
process.HiForest.HiForestVersion = cms.untracked.string(version)

#####################################################################################
# Input source
#####################################################################################

process.source = cms.Source("PoolSource",
                            duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
                            fileNames = cms.untracked.vstring(
"/store/user/twang/Pyquen_DiJet_pt40_5020GeV_GEN_SIM_PU_20150813/Pyquen_DiJet_pt40_5020GeV_step3_RECODEBUG_20150813/3179e0200600a67eea51209589c07fdd/step3_RECODEBUG_RAW2DIGI_L1Reco_RECO_PU_100_1_ppt.root"
                                #"/store/relval/CMSSW_7_5_0_pre5/RelValPhotonJets_Pt_10_13_HI/GEN-SIM-RECO/MCHI2_75_V2-v2/00000/BAA0D4EC-AF0B-E511-95A6-02163E011865.root"

    ))
#root://cmsxrootd.fnal.gov//

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10))


#####################################################################################
# Load Global Tag, Geometry, etc.
#####################################################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
#process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

# PbPb 53X MC

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '75X_mcRun2_HeavyIon_v5', '')

#process.GlobalTag.toGet.extend([
#    cms.PSet(record = cms.string("HeavyIonRcd"),
#             tag = cms.string("CentralityTable_HFtowers200_HydjetDrum5_v750x02_mc"),
#             connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS"),
#             label = cms.untracked.string("HFtowersHydjetDrum5")
#    ),
#])

from HeavyIonsAnalysis.Configuration.CommonFunctions_cff import *
#overrideGT_PbPb2760(process)
overrideJEC_PbPb2760(process)

process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")
process.centralityBin.Centrality = cms.InputTag("hiCentrality")
process.centralityBin.centralityVariable = cms.string("HFtowers")
process.centralityBin.nonDefaultGlauberModel = cms.string("HydjetDrum5")

#####################################################################################
# Define tree output
#####################################################################################

process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string("HiForest.root"))

################################################################################
# Additional Reconstruction and Analysis: Main Body
################################################################################

#begin: MV edits

## PF jets
process.load('HiRecoPFJets_PuThreshold_cff') ##creates sequence hiRecoPFJets

process.load('akPu4PFJetSequence10_cff')
process.load('akPu4PFJetSequence15_cff')
process.load('akPu4PFJetSequence20_cff')
process.load('akPu4PFJetSequence25_cff')
process.load('akPu4PFJetSequence30_cff')

process.jetSequencesPF = cms.Sequence(process.hiRecoPFJets4
                                      +process.akPu4PFJetSequence10
                                      +process.akPu4PFJetSequence15
                                      +process.akPu4PFJetSequence20
                                      +process.akPu4PFJetSequence25
                                      +process.akPu4PFJetSequence30
)

## Calo jets
process.load('HiRecoCaloJets_PuThreshold_cff') ##creates sequence hiRecoPFJets

process.load('akPu4CaloJetSequence4_cff')
process.load('akPu4CaloJetSequence6_cff')
process.load('akPu4CaloJetSequence8_cff')
process.load('akPu4CaloJetSequence10_cff')
process.load('akPu4CaloJetSequence12_cff')

process.jetSequencesCalo = cms.Sequence(process.hiRecoCaloJets4
                                        +process.akPu4CaloJetSequence4
                                        +process.akPu4CaloJetSequence6
                                        +process.akPu4CaloJetSequence8
                                        +process.akPu4CaloJetSequence10
                                        +process.akPu4CaloJetSequence12
)

#end: MV edits

process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_mc_cfi')
process.hiEvtAnalyzer.doMC = cms.bool(False) #the gen info dataformat has changed in 73X, we need to update hiEvtAnalyzer code
process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi')

#####################################################################################
# To be cleaned

process.load('HeavyIonsAnalysis.JetAnalysis.ExtraTrackReco_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.TrkAnalyzers_MC_cff')
process.load("HeavyIonsAnalysis.TrackAnalysis.METAnalyzer_cff")
process.load("HeavyIonsAnalysis.JetAnalysis.pfcandAnalyzer_cfi")
process.load('HeavyIonsAnalysis.JetAnalysis.rechitanalyzer_cfi')
process.rechitAna = cms.Sequence(process.rechitanalyzer+process.pfTowers)
process.pfcandAnalyzer.skipCharged = False
process.pfcandAnalyzer.pfPtMin = 0

#####################################################################################

#########################
# Track Analyzer
#########################
process.anaTrack.qualityStrings = cms.untracked.vstring(['highPurity','tight','loose'])

process.pixelTrack.qualityStrings = cms.untracked.vstring('highPurity')
process.hiTracks.cut = cms.string('quality("highPurity")')

# set track collection to iterative tracking
process.anaTrack.trackSrc = cms.InputTag("hiGeneralTracks")

# clusters missing in recodebug - to be resolved
process.anaTrack.doPFMatching = False
process.pixelTrack.doPFMatching = False

process.anaTrack.doSimVertex = True
process.anaTrack.doSimTrack = True
# process.ppTrack.fillSimTrack = True

process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cff")
process.tpRecoAssocGeneralTracks = process.trackingParticleRecoTrackAsssociation.clone()
process.tpRecoAssocGeneralTracks.label_tr = cms.InputTag("hiGeneralTracks")
process.quickTrackAssociatorByHits.ComponentName = cms.string('quickTrackAssociatorByHits')


#####################
# Photons
#####################

process.load('HeavyIonsAnalysis.PhotonAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.genParticleSrc = cms.InputTag("genParticles")

#####################
# muons
######################
#process.load("HeavyIonsAnalysis.MuonAnalysis.hltMuTree_cfi")
#process.hltMuTree.doGen = cms.untracked.bool(True)
#process.load("RecoHI.HiMuonAlgos.HiRecoMuon_cff")
#process.muons.JetExtractorPSet.JetCollectionLabel = cms.InputTag("akVs3PFJets")
#process.globalMuons.TrackerCollectionLabel = "hiGeneralTracks"
#process.muons.TrackExtractorPSet.inputTrackCollection = "hiGeneralTracks"
#process.muons.inputCollectionLabels = ["hiGeneralTracks", "globalMuons", "standAloneMuons:UpdatedAtVtx", "tevMuons:firstHit", "tevMuons:picky", "tevMuons:dyt"]

# HYDJET RECO file didn't have ak2GenJets and ak6GenJets as input, so removed them
# and ran our own hiGenJets sequence
from RecoHI.HiJetAlgos.HiGenJets_cff import ak3HiGenJets, ak4HiGenJets
from RecoJets.Configuration.GenJetParticles_cff import genParticlesForJets
genParticlesForJets.ignoreParticleIDs += cms.vuint32( 12,14,16)

process.hiSelectGenJets = cms.Sequence(
    genParticlesForJets +
    ak3HiGenJets +
    ak4HiGenJets
)

process.anaTrack.doSimTrack = cms.untracked.bool(False)

process.HiGenParticleAna.genParticleSrc = cms.untracked.InputTag("genParticles")

process.load("GeneratorInterface.HiGenCommon.HeavyIon_cff")


process.ana_step = cms.Path(process.heavyIon*
                            process.hltanalysis *
#temp                            process.hltobject *
                            process.centralityBin *
                            process.hiEvtAnalyzer*
                            process.HiGenParticleAna*
                            #process.hiGenJetsCleaned*
                            process.quickTrackAssociatorByHits*
                            #process.tpRecoAssocGeneralTracks + #used in HiPFJetAnalyzer
                            process.hiSelectGenJets +
                            process.jetSequencesPF +
                            process.jetSequencesCalo +
                            process.ggHiNtuplizer +
                            process.pfcandAnalyzer +
                            process.rechitAna +
#temp                            process.hltMuTree +
                            process.HiForest +
                            # process.cutsTPForFak +
                            # process.cutsTPForEff +
                            process.anaTrack
                            #process.pixelTrack
                            )

process.load('HeavyIonsAnalysis.JetAnalysis.EventSelection_cff')
process.phltJetHI = cms.Path( process.hltJetHI )
#process.pcollisionEventSelection = cms.Path(process.collisionEventSelection)
# process.pHBHENoiseFilter = cms.Path( process.HBHENoiseFilter ) #should be put back in later
#process.pHBHENoiseFilterResultProducer = cms.Path( process.HBHENoiseFilterResultProducer )
process.phfCoincFilter = cms.Path(process.hfCoincFilter )
process.phfCoincFilter3 = cms.Path(process.hfCoincFilter3 )
process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter )
#process.phltPixelClusterShapeFilter = cms.Path(process.siPixelRecHits*process.hltPixelClusterShapeFilter )
process.phiEcalRecHitSpikeFilter = cms.Path(process.hiEcalRecHitSpikeFilter )

process.pAna = cms.EndPath(process.skimanalysis)

# Customization
