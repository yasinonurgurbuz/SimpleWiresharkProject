parsedContent = {}

messageTypeDict = {
                    '00':'Unknown',
                    '06':'Address Complete',
                    '09':'Answer',        
                    '41':'Application transport',
                    '13':'Blocking 39',
                    '15':'Blocking acknowledgement',
                    '2c':'Call progress',
                    '18':'Circuit group blocking',
                    '1a':'Circuit group blocking acknowledgement',
                    '2a':'Circuit group query (national use)',
                    '2b':'Circuit group query response (national use)',
                    '17':'Circuit group reset',
                    '29':'Circuit group reset acknowledgement',
                    '19':'Circuit group unblocking',
                    '1b':'Circuit group unblocking acknowledgement',
                    '31':'Charge information (national use)',
                    '2f':'Confusion',
                    '07':'Connect',
                    '05':'Continuity',
                    '11':'Continuity check request',
                    '33':'Facility',
                    '20':'Facility accepted',
                    '21':'Facility reject',
                    '1f':'Facility request', 
                    '08':'Forward transfer',
                    '36':'Identification request',
                    '37':'Identification response',
                    '04':'Information (national use)',
                    '03':'Information request (national use)',
                    '01':'Initial address',
                    '24':'Loop back acknowledgement (national use)',
                    '40':'Loop prevention',
                    '32':'Network resource management',
                    '30':' Overload (national use)',
                    '28':' Pass-along (national use)',
                    '42':' Pre-release information',
                    '0c':' Release',
                    '10':' Release complete',
                    '12':' Reset circuit',
                    '0e':' Resume',
                    '38':' Segmentation',
                    '02':' Subsequent address',
                    '43':' Subsequent Directory Number (national use)',
                    '0d':' Suspend Message',
                    '14':' Unblocking',
                    '16':' Unblocking acknowledgement',
                    '2e':' Unequipped CIC (national use)',
                    '35':' User Part available',
                    '34':' User Part test',
                    '2d':' User-to-user information',
                    '0a':' Reserved (used in 1984 version)',
                    '0b':' Reserved (used in 1984 version)',
                    '0f':' Reserved (used in 1984 version)',
                    '22':' Reserved (used in 1984 version)',
                    '23':' Reserved (used in 1984 version)',
                    '25':' Reserved (used in 1984 version)',
                    '26':' Reserved (used in 1984 version)',
                    '1d':' Reserved (used in 1988 version)',
                    '1c':' Reserved (used in 1988 version)',
                    '1e':' Reserved (used in 1988 version)',
                    '27':' Reserved (used in 1988 version)', 
                    '39':' Reserved (used in B-ISUP)',
                    '3a':' Reserved (used in B-ISUP)',
                    '3b':' Reserved (used in B-ISUP)', 
                    '3c':' Reserved (used in B-ISUP)', 
                    '3d':' Reserved (used in B-ISUP)', 
                    '3e':' Reserved (used in B-ISUP)',
                    '3f':' Reserved (used in B-ISUP)', 
                    '80':' Reserved for future extension'
                    }
indicatorTypeDict ={}



indicatorTypeDict = { 
                    '00':'Unknown',
                    '2e':'Access delivery information',                  
                    '03':'Access transport',
                    '78':'Application transport', 
                    '27':'Automatic congestion level', 
                    '11':'Backward call indicators', 
                    '4d':'Backward GVNS', 
                    '36':'Call diversion information', 
                    '6e':'Call diversion treatment indicators', 
                    '2d':'Call history information', 
                    '70':'Call offering treatment indicators', 
                    '01':'Call reference (national use)', 
                    '45':'Call transfer number', 
                    '43':'Call transfer reference', 
                    '6f':'Called IN number', 
                    '7d':'Called directory number (national use)', 
                    '04':'Called party number', 
                    '81':'Calling geodetic location', 
                    '0a':'Calling party number', 
                    '09':'Calling party''s category', 
                    '12':'Cause indicators', 
                    '7a':'CCNR possible indicator', 
                    '4b':'CCSS Parameter', 
                    '71':'Charged party identification (national use)',
                    '25':'Circuit assignment map',
                    '15':'Circuit group supervision message type', 
                    '26':'Circuit state indicator (national use)',
                    '1a':'Closed user group interlock code',
                    '79':'Collect call request', 
                    '72':'Conference treatment indicators',
                    '21':'Connected number',
                    '0d':'Connection request',
                    '10':'Continuity indicators', 
                    '65':'Correlation id',
                    '73':'Display information',
                    '37':'Echo control information',
                    '00':'End of optional parameters', 
                    '24':'Event information',
                    '18':'Facility indicator',  
                    '07':'Forward call indicators',  
                    '4c':'Forward GVNS Parameter', 
                    'c1':'Generic digits (national use)', 
                    '2c':'Generic notification indicator',
                    'c0':'Generic number', 
                    '82':'HTR information',  
                    '3d':'Hop counter',  
                    '0f':'Information indicators (national use)',  
                    '0e':'Information request indicators (national use)',  
                    '3f':'Location number',  
                    '44':'Loop prevention indicators',  
                    '3b':'MCID request indicators',  
                    '3c':'MCID response indicators',  
                    '38':'Message compatibility information',  
                    '3a':'MLPP precedence', 
                    '06':'Nature of connection indicators',  
                    '5b':'Network management controls',  
                    '84':'Network routing number (national use)', 
                    '2f':'Network specific facility (national use)',  
                    '8d':'Number portability forward information (network option)',  
                    '29':'Optional backward call indicators', 
                    '08':'Optional forward call indicators',  
                    '28':'Original called number', 
                    '7f':'Original called IN number',  
                    '2b':'Origination ISC point code',  
                    '39':'Parameter compatibility information', 
                    '7b':'Pivot capability', 
                    '87':'Pivot counter',  
                    '89':'Pivot routing backward information',  
                    '88':'Pivot routing forward information',  
                    '7c':'Pivot routing indicators', 
                    '86':'Pivot status (national use)',  
                    '31':'Propagation delay counter',  
                    '85':'Query on release capability (network option)',  
                    '16':'Range and status', 
                    '8c':'Redirect backward information (national use)',  
                    '4e':'Redirect capability (national use)', 
                    '77':'Redirect counter (national use)',  
                    '8b':'Redirect forward information (national use)', 
                    '8a':'Redirect status (national use)', 
                    '0b':'Redirecting number', 
                    '13':'Redirection information', 
                    '0c':'Redirection number', 
                    '40':'Redirection number restriction',
                    '32':'Remote operations (national use)',
                    '66':'SCF id','33':'Service activation', 
                    '33':'Service activation',
                    '1e':'Signalling point code (national use)',
                    '05':'Subsequent number',
                    '22':'Suspend/Resume indicators',
                    '23':'Transit network selection (national use)',
                    '02':'Transmission medium requirement',
                    '3e':'Transmission medium requirement prime', 
                    '35':'Transmission medium used',
                    '74':'UID action indicators',
                    '75':'UID capability indicators',
                    '1d':'User service information', 
                    '30':'User service information prime',
                    '34':'User teleservice information',
                    '2a':'User-to-user indicators',
                    '20':'User-to-user information',
                    '14':'Reserved (used in 1984 version, Red Book)',
                    '19':'Reserved (used in 1984 version, Red Book)',
                    '1b':'Reserved (used in 1984 version, Red Book)',
                    '1c':'Reserved (used in 1984 version, Red Book)',
                    '1f':'Reserved (used in 1984 version, Red Book)',
                    '17':'Reserved (used in 1988 version, Blue Book)',
                    '41':'Reserved (used in 1992 version) Parameter',
                    '42':'Reserved (used in 1992 version) Parameter',
                    '80':'Reserved for future extension Parameter'              
                    }

for i in range (0,256):
    if indicatorTypeDict.get("%0.2x"%i) == None:
        indicatorTypeDict["%0.2x"%i]='Unknown'

    

SatelliteIndicator                    = {                 
                                        '00':' Satellite Indicator: No satellite circuit in the connection',
                                        '01':' Satellite Indicator: One satellite circuit in the connection',
                                        '10':' Satellite Indicator: Two satellite circuits in the connection',
                                        '11':' Satellite Indicator: Spare' 
                                        }
    
ContinuityCheckIndicator              = {                 
                                        '00':' Continuity Check Indicator: Continuity check not required ',
                                        '01':' Continuity Check Indicator: Continuity check required on this circuit',
                                        '10':' Continuity Check Indicator: Continuity check performed on a previous circuit',
                                        '11':' Continuity Check Indicator: Spare' 
                                        }

EchoControlDeviceIndicator            = {                 
                                         '0':' Echo Control Device Indicator: Outgoing echo control device not included',
                                         '1':' Echo Control Device Indicator: Outgoing echo control device included'
                                        }


NationalInternationalCallIndicator    = {                 
                                         '0':' National/international call indicator: Call to be treated as a national call',
                                         '1':' National/international call indicator: Call to be treated as an international call'
                                        }

EndToEndMethodIndicator               = {
                                        '00':' End-to-end method indicator: No end-to-end method available (only link-by-link method available)',
                                        '01':' End-to-end method indicator: Pass-along method available (national use)',
                                        '10':' End-to-end method indicator: SCCP method available ',
                                        '11':' End-to-end method indicator: Pass-along and SCCP methods available (national use)' 
                                        }

InterworkingIndicator                 = {
                                         '0':' Interworking indicator: No interworking encountered (No. 7 signalling all the way)',
                                         '1':' Interworking indicator: Interworking encountered  '
                                        }

EndToEndInformationIndicator          = {
                                         '0':' End-to-end information indicator (national use): No end-to-end information available',
                                         '1':' End-to-end information indicator (national use): End-to-end information available'
                                        }

ISDNuserPartIndicator                 = {
                                         '0':' ISDN user part indicator : ISDN user part not used all the way',
                                         '1':' ISDN user part indicator  : ISDN user part used all the way'
                                        }

ISDNuserPartPreferenceIndicator       = {
                                        '00':' ISDN user part preference indicator: ISDN user part preferred all the way',
                                        '01':' ISDN user part preference indicator: ISDN user part not required all the way',
                                        '10':' ISDN user part preference indicator: ISDN user part required all the way',
                                        '11':' ISDN user part preference indicator: Spare' 
                                        }

ISDNAccessIndicator                   = {
                                         '0':' ISDN access indicator: Originating access non-ISDN',
                                         '1':' ISDN access indicator: Originating access ISD '
                                        }
SCCPmethodIndicator                   = {
                                         '00':' SCCP method indicator: No indication',
                                         '01':' SCCP method indicator: Connectionless method available (national use)',
                                         '10':' SCCP method indicator: Connection oriented method available',
                                         '11':' SCCP method indicator: Connectionless and connection oriented methods available (national use)' 
                                        }

PortedNumberTranslationIndicator      = {
                                         '0':' Ported number translation indicator: Number not translated',
                                        }

QueryOnReleaseAttemptIndicator       =  {
                                         '0':' Query on Release attepmt indicator: No QoR routing attempt in progress',
                                        }

CallingPartysCategoryParameterField  = {
                                        '00':' Calling party''s category unknown at this time (national use) ',
                                        '01':' Operator, language French ',
                                        '02':' Operator, language English',
                                        '03':' Operator, language German',
                                        '04':' Operator, language Russian  ',
                                        '05':' Operator, language Spanish ',
                                        '06':' (available to Administrations for selection a particular language by mutual agreement)',
                                        '07':' (available to Administrations for selection a particular language by mutual agreement)',
                                        '08':' (available to Administrations for selection a particular language by mutual agreement)',
                                        '09':' Reserved (see ITU-T Recommendation Q.104) (Note) (national use)  ',
                                        '0a':' Ordinary calling subscriber ',
                                        '0b':' Calling subscriber with priority ',
                                        '0c':' Data call (voice band data)   ',
                                        '0d':' Test call  ',
                                        '0e':' Spare',
                                        '0f':' Payphone ',
                                        }
OddEvenIndicator = {
                     '0':' Odd Even Indicator: Even number of address signals ',
                     '1':' Odd Even Indicator: Odd number of address signals'
                   }

NatureOfAddressIndicator = {
                            '0000000':' Spare',
                            '0000001':' Subscriber number (national use)',
                            '0000010':' Unknown (national use)',
                            '0000011':' National (significant) number ',
                            '0000100':' International number',
                            '0000101':' Network-specific number (national use)',
                            '0000110':' Network routing number in national (significant) number format (nationaluse)',
                            '0000111':' Network routing number in network-specific number format (national use)',
                            '0001000':' Network routing number concatenated with Called Directory Number (national use)',
                            '1111111':' Operator, language Spanish',
                            }

InternalNetworkNumberIndicator = {
                                  '0':' Internal network number indicator: Routing to internal network number allowed  ',
                                  '1':' Internal network number indicator: Routing to internal network number not allowed '
                                  }

NumberPlanIndicator = {
                       '000':' Number plan indicator: spare  ',
                       '001':' Number plan indicator: ISDN (Telephony) numbering plan (ITU-T Recommendation E.164) ',
                       '010':' Number plan indicator: Spare  ',
                       '011':' Number plan indicator: Data numbering plan (ITU-T Recommendation X.121) (national use)  ',
                       '100':' Number plan indicator: Telex numbering plan (ITU-T Recommendation F.69) (national use)   ',
                       '101':' Number plan indicator: Reserved for national use  ',
                       '110':' Number plan indicator: Reserved for national use   ',
                       '111':' Number plan indicator: Spare '
                      }


AddresSignal = {
     '0000':' Address signal digit: 0 (0)',
     '0001':' Address signal digit: 1 (1)',
     '0010':' Address signal digit: 2 (2)',
     '0011':' Address signal digit: 3 (3)',
     '0100':' Address signal digit: 4 (4)',
     '0101':' Address signal digit: 5 (5)',
     '0110':' Address signal digit: 6 (6)',
     '0111':' Address signal digit: 7 (7)',
     '1000':' Address signal digit: 8 (8)',
     '1001':' Address signal digit: 9 (9)',
     '1010':' Address signal digit: a (10)',
     '1011':' Address signal digit: b (11)',
     '1100':' Address signal digit: c (12)',
     '1101':' Address signal digit: d (13)',
     '1110':' Address signal digit: e (14)',
     '1111':' Address signal digit: f (15)',
     }
