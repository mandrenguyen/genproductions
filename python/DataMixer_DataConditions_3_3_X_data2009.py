import FWCore.ParameterSet.Config as cms
def customise(process):

# placeholder !!!!!! replace with the actual run number of
# the real run to be overlaid

    process.source.firstRun = cms.untracked.uint32(122314)

    process.ecalConditions1 = cms.ESSource("PoolDBESSource",                                          
         process.CondDBSetup,                                                                                 
         timetype = cms.string('runnumber'),                                                          
         toGet = cms.VPSet(                                                                           
             cms.PSet(                                                                                
        record = cms.string('EcalPedestalsRcd'),                                                      
        tag = cms.string('EcalPedestals_2009runs_hlt')                                                
        ),                                                                                            
             cms.PSet(                                                                                
        record = cms.string('EcalADCToGeVConstantRcd'),                                               
        tag = cms.string('EcalADCToGeVConstant_coll09_v3_offline')                                    
        ),                                                                                            
             cms.PSet(                                                                                
        record = cms.string('EcalChannelStatusRcd'),                                                  
        tag = cms.string('EcalChannelStatus_coll09_v1_offline')                                       
        ),                                                                                            
             cms.PSet(                                                                                
        record = cms.string('EcalGainRatiosRcd'),                                                     
        tag = cms.string('EcalGainRatios_TestPulse2009_offline')                                      
        ),                                                                                            
             cms.PSet(                                                                                
        record = cms.string('EcalIntercalibConstantsRcd'),                                            
        tag = cms.string('EcalIntercalibConstants_coll09_v3_offline')                                 
        ),                                                                                            
             cms.PSet(                                                                                
        record = cms.string('EcalIntercalibErrorsRcd'),                                               
        tag = cms.string('EcalIntercalibErrors_mc')                                                   
        ),                                                                                            
             cms.PSet(                                                                                
        record = cms.string('EcalWeightXtalGroupsRcd'),                                               
        tag = cms.string('EcalWeightXtalGroups_mc')                                                   
        ),                                                                                            
             cms.PSet(                                                                                
        record = cms.string('EcalTBWeightsRcd'),                                                      
        tag = cms.string('EcalTBWeights_EBEE_BeamComm09_offline')                                     
        ),                                                                                            
             cms.PSet(                                                                                
        record = cms.string('EcalMappingElectronicsRcd'),                                             
        tag = cms.string('EcalMappingElectronics_EEMap')                                              
        ),                                                                                            
             cms.PSet(                                                                                
        record = cms.string('EcalTimeCalibConstantsRcd'),                                             
        tag = cms.string('EcalTimeCalibConstants_2009runs_offline')                                   
        ),                                                                                            
             ),                                                                                       
        connect = cms.string('frontier://FrontierProd/CMS_COND_31X_ECAL'),                            
              authenticationMethod = cms.untracked.uint32(0)                                          
    )                                                                                                 
                                                                                                      
    process.ecalConditions2 = cms.ESSource("PoolDBESSource",                                          
                                           process.CondDBSetup,                                               
                                           timetype = cms.string('runnumber'),                        
                                           toGet = cms.VPSet(                                         
        cms.PSet(                                                                                     
        record = cms.string('EcalLaserAPDPNRatiosRcd'),                                               
        tag = cms.string('EcalLaserAPDPNRatios_prompt')                                               
          ),                                                                                          
        ),                                                                                            
        connect = cms.string('frontier://FrontierProd/CMS_COND_31X_FROM21X'),                         
              authenticationMethod = cms.untracked.uint32(0)                                          
    )                                                                                                 
                                                                                                      
    process.es_prefer_ecal1 = cms.ESPrefer("PoolDBESSource","ecalConditions1")                        
    process.es_prefer_ecal2 = cms.ESPrefer("PoolDBESSource","ecalConditions2")                        
                                                                                                      
    process.hcalConditions = cms.ESSource("PoolDBESSource",                                           
                                          process.CondDBSetup,                                                
                                          timetype = cms.string('runnumber'),                         
                                          toGet = cms.VPSet(                                          
        cms.PSet(                                                                                     
        record = cms.string('HcalPedestalsRcd'),                                                      
        tag = cms.string('HcalPedestals_ADC_v7.03_hlt')                                               
        ),                                                                                            
        cms.PSet(                                                                                     
        record = cms.string('HcalPedestalWidthsRcd'),                                                 
        tag = cms.string('HcalPedestalWidths_ADC_v7.01_hlt')                                          
        ),                                                                                            
        cms.PSet(                                                                                     
        record = cms.string('HcalElectronicsMapRcd'),                                                 
        tag = cms.string('HcalElectronicsMap_v7.03_hlt')                                              
        ),                                                                                            
        cms.PSet(                                                                                     
        record = cms.string('HcalGainsRcd'),                                                          
        tag = cms.string('HcalGains_v2.08_express')                                                   
        ),                                                                                            
        cms.PSet(                                                                                     
        record = cms.string('HcalQIEDataRcd'),                                                        
        tag = cms.string('HcalQIEData_NormalMode_v7.00_hlt')                                          
        ),                                                                                            
        cms.PSet(                                                                                     
        record = cms.string('HcalRespCorrsRcd'),                                                      
        tag = cms.string('HcalRespCorrs_v1.02_express')                                               
        ),                                                                                            
        cms.PSet(                                                                                     
        record = cms.string('HcalChannelQualityRcd'),                                                 
        tag = cms.string('HcalChannelQuality_v1.09_offline')                                          
        ),                                                                                            
        cms.PSet(                                                                                     
        record = cms.string('HcalL1TriggerObjectsRcd'),                                               
        tag = cms.string('HcalL1TriggerObjects_v1.00_hlt')                                            
        ),                                                                                            
        cms.PSet(                                                                                     
        record = cms.string('HcalPFCorrsRcd'),                                                        
        tag = cms.string('HcalPFCorrs_v2.00_express')                                                 
        ),                                                                                            
        cms.PSet(                                                                                     
        record = cms.string('HcalTimeCorrsRcd'),                                                      
        tag = cms.string('HcalTimeCorrs_v1.00_express')                                               
        ),                                                                                            
        cms.PSet(                                                                                     
        record = cms.string('HcalLUTCorrsRcd'),                                                       
        tag = cms.string('HcalLUTCorrs_v1.01_hlt')                                                    
        ),                                                                                            
        cms.PSet(                                                                                     
        record = cms.string('HcalZSThresholdsRcd'),                                                   
        tag = cms.string('HcalZSThresholds_v1.01_hlt')                                                
        ),                                                                                            
        ),                                                                                            
             connect = cms.string('frontier://FrontierProd/CMS_COND_31X_HCAL'),                       
                      authenticationMethod = cms.untracked.uint32(0)                                  
    )                                                                                                 
                                                                                                      
    process.es_prefer_hcal = cms.ESPrefer("PoolDBESSource","hcalConditions")                          
                                                                                                      
    try: 
        process.ecalRecHit.ChannelStatusToBeExcluded = [ 1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 78, 142 ]  
    except:
        print "ecalRecHit not loaded"
 
    return(process)