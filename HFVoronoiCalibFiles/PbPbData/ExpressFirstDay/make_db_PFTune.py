import FWCore.ParameterSet.VarParsing as VarParsing

ivars = VarParsing.VarParsing('standard')

ivars.register ('outputTag',
                mult=ivars.multiplicity.singleton,
                mytype=ivars.varType.string,
                info="for testing")
ivars.outputTag="UETableCompatibilityFormat_PF_v00_express"

ivars.register ('inputFile',
                mult=ivars.multiplicity.singleton,
                mytype=ivars.varType.string,
                info="for testing")

ivars.register ('outputFile',
                mult=ivars.multiplicity.singleton,
                mytype=ivars.varType.string,
                info="for testing")

ivars.inputFile="ue_calibrations_pf_data.txt"
ivars.outputFile="./UETableCompatibilityFormat_PF_v00_express.db"

ivars.parseArguments()

import FWCore.ParameterSet.Config as cms

process = cms.Process('DUMMY')

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.source = cms.Source("EmptyIOVSource",
                            timetype = cms.string("runnumber"),
                            firstValue = cms.uint64(262314),
                            lastValue = cms.uint64(1),
                            interval = cms.uint64(1)
                            )

process.load("CondCore.DBCommon.CondDBCommon_cfi")
process.CondDBCommon.connect = "sqlite_file:" + ivars.outputFile

process.PoolDBOutputService = cms.Service("PoolDBOutputService",
                                          process.CondDBCommon,
                                          timetype = cms.untracked.string("runnumber"),
                                          toPut = cms.VPSet(cms.PSet(record = cms.string('JetCorrectionsRecord'),
                                                                     tag = cms.string(ivars.outputTag),
                                                                     label = cms.string("UETable_PF")
                                                                     )
                                                            )
                                          )

process.makeUETableDB = cms.EDAnalyzer('UETableProducer',
                                       txtFile = cms.string(ivars.inputFile),
				       jetCorrectorFormat = cms.untracked.bool(True)
                                       )

process.step  = cms.Path(process.makeUETableDB)
