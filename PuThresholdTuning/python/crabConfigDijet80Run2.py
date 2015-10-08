from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
#from WMCore.Configuration import Configuration
#config = Configuration()

#config.section_("General")
config.General.requestName   = 'HiForestDijet80Run2Fullv2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

#config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName    = 'runForest_PbPb_MIX_75X_PUThresholdVarV2.py'

#config.section_("Data")
config.Data.inputDataset = '/PyquenUnquenched_Dijet_NcollFilt_pthat80_740pre8_MCHI1_74_V4_GEN-SIM_v3/dgulhan-HydjetNcoll_Pyquen_DiJet_pt80to9999_5020GeV_cfi_RECODEBUG_750_run2_mc_HIon_BS-d4e92c99eed5ed00c983ef409e3f7a2f/USER'
#config.Data.inputDataset = '/Pyquen_DiJet_pt40_5020GeV_GEN_SIM_PU_20150813/twang-Pyquen_DiJet_pt40_5020GeV_step3_RECODEBUG_20150813-3179e0200600a67eea51209589c07fdd/USER'
#config.Data.inputDataset = '/Pyquen_DiJet_Pt120_TuneZ2_Unquenched_Hydjet1p8_2760GeV/HiFall13DR53X-NoPileUp_STARTHI53_LV1-v3/GEN-SIM-RECO'
config.Data.inputDBS = 'phys03' #'global'
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 2
#config.Data.totalUnits = 100 #process small amount first
#config.Data.lumiMask = 'lumi_JSON.txt'
#config.Data.runRange = '247324'
#config.Data.outLFNDirBase = '/store/user/mverweij/pp2015/MC/Monash13_0T'
config.Data.outLFNDirBase = '/store/group/cmst3/user/mverweij/jetsPbPb/Run2Prep/Dijet80CMSSW753p1/v3'
config.Data.publication = False #True
config.Data.publishDataName = ''

#config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist = ['T2_CH_CERN']

