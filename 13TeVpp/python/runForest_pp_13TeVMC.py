import FWCore.ParameterSet.Config as cms
process = cms.Process('HiForest')

#parse command line arguments
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('analysis')
options.parseArguments()


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
                            fileNames = cms.untracked.vstring('file:/afs/cern.ch/user/m/mverweij/work/jetsPbPb/mc/pp13TeV/RunIISpring15DR74-AsymptFlat0to50bx25Reco_MCRUN2_74_V9-v3/data/0009D30B-0207-E511-B581-0026182FD753.root')
                                #options.inputFiles[0])
)

# Number of events we want to process, -1 = all events
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)


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
process.load('Configuration.StandardSequences.ReconstructionHeavyIons_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

#https://twiki.cern.ch/twiki/bin/viewauth/CMS/JECDataMC#Recommended_for_MC
#Summer15_25nsV6_MC.db -> cannot find global tag name. Using earlier one
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '74X_mcRun2_asymptotic_v2', '')

#####################################################################################
# Define tree output
#####################################################################################
process.TFileService = cms.Service("TFileService",
                                   fileName=cms.string(options.outputFile))

#####################################################################################
# Additional Reconstruction and Analysis: Main Body
#####################################################################################

process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak4PFJetSequence_pp_mc_cff')
process.ak4PFmatch.matched = cms.InputTag("ak4GenJetsNoNu")
process.ak4PFcorr.levels   = cms.vstring('L1FastJet','L2Relative','L3Absolute','L2L3Residual')
process.ak4PFcorr.payload="AK4PF";
process.ak4PFJetAnalyzer.jetPtMin = cms.untracked.double(1)
process.ak4PFJetAnalyzer.genjetTag = 'ak4GenJetsNoNu'

process.load('ak4PFCHSJetSequence_pp_mc_cff')

process.load('HeavyIonsAnalysis.JetAnalysis.jets.ak4CaloJetSequence_pp_mc_cff')
process.ak4Calomatch.matched = cms.InputTag("ak4GenJetsNoNu")
process.ak4Calocorr.payload="AK4Calo";
process.ak4CaloJetAnalyzer.jetPtMin = cms.untracked.double(1)
process.ak4CaloJetAnalyzer.genjetTag = 'ak4GenJetsNoNu'

#turn off jec for calo jets
process.ak4CalopatJets.jetCorrFactorsSource = cms.VInputTag(cms.InputTag(""))
process.ak4CalopatJets.addJetCorrFactors=False
process.ak4CaloJetAnalyzer.useJEC=cms.untracked.bool(False)
process.ak4CaloJetSequence_nocorr = cms.Sequence(process.ak4Calomatch
                                                 *
                                                 process.ak4Caloparton
                                                 *
                                                 process.ak4CalopatJets
                                                 *
                                                 process.ak4CaloJetAnalyzer
)

process.jetSequences = cms.Sequence(process.ak4PFJetSequence
                                    + process.ak4PFCHSJetSequence
                                    + process.ak4CaloJetSequence_nocorr
                                    )

process.load('HeavyIonsAnalysis.EventAnalysis.hievtanalyzer_mc_cfi')
process.hiEvtAnalyzer.doMC = cms.bool(True) #the gen info dataformat has changed in 73X, we need to update hiEvtAnalyzer code
process.hiEvtAnalyzer.useHepMC = cms.bool(False) 

process.hiEvtAnalyzer.doCentrality     = cms.bool(False)
process.hiEvtAnalyzer.doEvtPlane       = cms.bool(False)
process.hiEvtAnalyzer.doEvtPlaneFlat   = cms.bool(False)

process.load('HeavyIonsAnalysis.EventAnalysis.hltanalysis_cff')
process.load('HeavyIonsAnalysis.JetAnalysis.HiGenAnalyzer_cfi') #HiGenParticleana

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
process.pfcandAnalyzer.pfCandidateLabel = cms.InputTag("particleFlow")
process.pfcandAnalyzer.doVS = cms.untracked.bool(False)
process.pfcandAnalyzer.bkg = cms.InputTag("")
process.pfcandAnalyzer.genLabel = cms.InputTag("genParticles")

#####################################################################################

#########################
# Track Analyzer
#########################
process.anaTrack.qualityStrings = cms.untracked.vstring(['highPurity','tight','loose'])

process.pixelTrack.qualityStrings = cms.untracked.vstring('highPurity')
process.hiTracks.cut = cms.string('quality("highPurity")')

# set track collection to iterative tracking
process.anaTrack.trackSrc = cms.InputTag("generalTracks")

# clusters missing in recodebug - to be resolved
process.anaTrack.doPFMatching = True#False
process.pixelTrack.doPFMatching = False

process.anaTrack.doSimVertex = True
process.anaTrack.doSimTrack = True
#process.anaTrack.doSimTrack = cms.untracked.bool(False)
# process.ppTrack.fillSimTrack = True

process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cff")
process.tpRecoAssocGeneralTracks = process.trackingParticleRecoTrackAsssociation.clone()
process.tpRecoAssocGeneralTracks.label_tr = cms.InputTag("generalTracks")
process.quickTrackAssociatorByHits.ComponentName = cms.string('quickTrackAssociatorByHits')


#####################
# Photons
#####################

process.load('HeavyIonsAnalysis.PhotonAnalysis.ggHiNtuplizer_cfi')
process.ggHiNtuplizer.genParticleSrc         = cms.InputTag("genParticles")
process.ggHiNtuplizer.gsfElectronLabel       = cms.InputTag("gedGsfElectrons")
process.ggHiNtuplizer.useValMapIso           = cms.bool(False)
process.ggHiNtuplizer.VtxLabel               = cms.InputTag("offlinePrimaryVerticesWithBS")
process.ggHiNtuplizer.particleFlowCollection = cms.InputTag("particleFlow")
process.ggHiNtuplizer.doVsIso                 = cms.bool(False)
#process.ggHiNtuplizerGED = process.ggHiNtuplizer.clone(recoPhotonSrc = cms.InputTag('gedPhotons'))
process.ggHiNtuplizerGED = process.ggHiNtuplizer.clone(recoPhotonSrc = cms.InputTag('gedPhotons'),
                                                       recoPhotonHiIsolationMap = cms.InputTag('photonIsolationHIProducerGED')
)

#####################
process.HiGenParticleAna.genParticleSrc = cms.untracked.InputTag("genParticles")
process.HiGenParticleAna.doVertex = cms.untracked.bool(True)

process.load("GeneratorInterface.HiGenCommon.HeavyIon_cff")

#pileup vertices
process.load("Validation.RecoVertex.mcverticesanalyzer_cfi")

#process.pileup = cms.EDAnalyzer(
#    "MCVerticesAnalyzer",
#    verbose                      = cms.untracked.int32(0),
#    dumpAllEvents                = cms.untracked.int32(0),
#    vertexCollLabel              = cms.untracked.InputTag('offlinePrimaryVertices')
#)

process.load('HeavyIonsAnalysis.VertexAnalysis.MCVerticesAnalyzer_cff')

process.ana_step = cms.Path(process.heavyIon*
                            process.hltanalysis *
                            #temp                            process.hltobject *
                            process.hiEvtAnalyzer*
                            process.HiGenParticleAna*
                            process.quickTrackAssociatorByHits*
                            process.jetSequences +
                            process.ggHiNtuplizer +
                            process.ggHiNtuplizerGED +
                            process.pfcandAnalyzer +
                            #process.rechitAna +
                            process.HiForest #+
                            #+ process.mcverticesanalyzer
                            + process.pileup
                            #process.ppTrack 
                            #process.anaTrack 
)

process.load('HeavyIonsAnalysis.JetAnalysis.EventSelection_cff')
process.phltJetHI = cms.Path( process.hltJetHI )

process.collisionEventSelectionCus = cms.Sequence(process.noBSChalo *
                                          process.hfCoincFilter3 *
                                          process.primaryVertexFilter)
process.pcollisionEventSelection = cms.Path(process.collisionEventSelectionCus)
process.load('CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi')
process.pHBHENoiseFilterResultProducer = cms.Path( process.HBHENoiseFilterResultProducer )
process.phfCoincFilter = cms.Path(process.hfCoincFilter )
process.phfCoincFilter3 = cms.Path(process.hfCoincFilter3 )
process.pprimaryVertexFilter = cms.Path(process.primaryVertexFilter )
#process.phltPixelClusterShapeFilter = cms.Path(process.siPixelRecHits*process.hltPixelClusterShapeFilter )
process.phiEcalRecHitSpikeFilter = cms.Path(process.hiEcalRecHitSpikeFilter )

#process.load("HeavyIonsAnalysis.VertexAnalysis.PAPileUpVertexFilter_cff")

process.pVertexFilterCutG = cms.Path(process.pileupVertexFilterCutG)
process.pVertexFilterCutGloose = cms.Path(process.pileupVertexFilterCutGloose)
process.pVertexFilterCutGtight = cms.Path(process.pileupVertexFilterCutGtight)
process.pVertexFilterCutGplus = cms.Path(process.pileupVertexFilterCutGplus)
process.pVertexFilterCutE = cms.Path(process.pileupVertexFilterCutE)
process.pVertexFilterCutEandG = cms.Path(process.pileupVertexFilterCutEandG)


process.pAna = cms.EndPath(process.skimanalysis)

# Customization
oldGenParticleTag=cms.InputTag("hiGenParticles")
newGenParticleTag=cms.InputTag("genParticles")
oldProcLabelTag=cms.InputTag("hiSignal")
newProcLabelTag=cms.InputTag("generator")
oldVtxLabelTag=cms.InputTag("hiSelectedVertex")
newVtxLabelTag=cms.InputTag("offlinePrimaryVerticesWithBS")


from PhysicsTools.PatAlgos.tools.helpers import massSearchReplaceAnyInputTag
for s in process.paths_().keys():
    massSearchReplaceAnyInputTag(getattr(process,s),oldGenParticleTag,newGenParticleTag)
    #massSearchReplaceAnyInputTag(getattr(process,s),newGenParticleTag,oldGenParticleTag)  // go back to hiGenParticles
    massSearchReplaceAnyInputTag(getattr(process,s),oldVtxLabelTag,newVtxLabelTag)
   
