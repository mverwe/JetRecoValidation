import FWCore.ParameterSet.Config as cms
process = cms.Process("jectxt")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
# define your favorite global tag
process.GlobalTag.globaltag = '74X_dataRun2_HLT_ppAt5TeV_v0'#Prompt_v4'#auto:run2_data'

process.GlobalTag.toGet.extend([
    cms.PSet(record = cms.string("JetCorrectionsRecord"),
             tag = cms.string("UETableCompatibilityFormat_Calo_v02_offline"),
             label = cms.untracked.string("UETable_Calo")
    )
])

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))
process.source = cms.Source("EmptySource")
process.readAK4PF = cms.EDAnalyzer('JetCorrectorDBReader',  
                                   # below is the communication to the database 
                                   payloadName    = cms.untracked.string('UETable_Calo'),
                                   # this is used ONLY for the name of the printed txt files. You can use any name that you like, 
                                   # but it is recommended to use the GT name that you retrieved the files from.
                                   globalTag = cms.untracked.string('74X_dataRun2_HLT_ppAt5TeV_v0'),
                                   printScreen    = cms.untracked.bool(False),
                                   createTextFile = cms.untracked.bool(True)
                                  )

process.readAK4PFoff = process.readAK4PF.clone(payloadName = 'UETable_Calo')
process.p = cms.Path(process.readAK4PFoff)
