from dictionaryModule import *
from dictionaryModule import messageTypeDict
from dictionaryModule import parsedContent

def DetectMessageType(messageTypeValue):
    if messageTypeValue in messageTypeDict:
        return messageTypeDict[messageTypeValue]
    elif messageTypeValue not in messageTypeDict:
        print("!!! Undefined Message Type")
        return 'ERR'

def ParseNOC(NOCIE):
    print(".... .." + NOCIE[6:] + SatelliteIndicator[NOCIE[6:]])
    print(".... " + NOCIE[4:6] + ".." + ContinuityCheckIndicator[NOCIE[4:6]])
    print("..." + NOCIE[3] + " ...." + EchoControlDeviceIndicator[NOCIE[3]])

def ParseFCI(FCI):
    print('.... ...' + FCI[0][7]   + ' .... .... ='       + NationalInternationalCallIndicator[FCI[0][7]])
    print('.... .'   + FCI[0][5:7] + '. .... .... ='      + EndToEndMethodIndicator[FCI[0][5:7]])
    print('.... '    + FCI[0][4]   + '... .... .... ='    + InterworkingIndicator[FCI[0][4]])
    print('...'      + FCI[0][3]   + ' .... .... .... ='  + EndToEndInformationIndicator[FCI[0][3]])
    print('..'       + FCI[0][2]   + '. .... .... .... =' + ISDNuserPartIndicator[FCI[0][2]])
    print(FCI[0][0:2]  +           '.. .... .... .... ='  + ISDNuserPartPreferenceIndicator[FCI[0][0:2]])
    print('.... .... .... ...' + FCI[1][7]    + ' ='        + ISDNAccessIndicator[FCI[1][7]])
    print('.... .... .... .'   + FCI[1][5:7]  + '. ='       + SCCPmethodIndicator[FCI[1][5:7]])
    print('.... .... ...'      + FCI[1][3]    + ' .... ='   + PortedNumberTranslationIndicator[FCI[1][3]])
    print('.... .... ..'       + FCI[1][2]    + '. .... ='  + QueryOnReleaseAttemptIndicator[FCI[1][2]])

def ParsePartyNumber(ParameterContent):
    print(ParameterContent[0][0] + '........ ='         + OddEvenIndicator[ParameterContent[0][0]])
    if ParameterContent[0][1:8] in NatureOfAddressIndicator:
        print("."    + ParameterContent[0][1:8] + '  ='      + NatureOfAddressIndicator[ParameterContent[0][1:8]])
    else:
        print("."    + ParameterContent[0][1:8] + '  ='      + 'Spare')
    print(ParameterContent[1][0] + '........ ='         + InternalNetworkNumberIndicator[ParameterContent[1][0]])
    print("."    + ParameterContent[1][1:4] + '....  ='  + NumberPlanIndicator[ParameterContent[1][1:4]])
    print("...."    + ParameterContent[1][4:8] + '  ='      + ' Spare')
    for binOct in ParameterContent[2:-1]:
        print("...." + binOct[4:9] + AddresSignal[binOct[4:9]])
        print(binOct[0:4] + "...." + AddresSignal[binOct[0:4]])
    if ParameterContent[0][0] == '1' :
        print("...." + ParameterContent[-1][4:9] + AddresSignal[ParameterContent[-1][4:9]])
    else:
        print("...." + ParameterContent[-1][4:9] + AddresSignal[ParameterContent[-1][4:9]])
        print("...." + ParameterContent[-1][0:4] + AddresSignal[ParameterContent[-1][0:4]])

def ParseOptPartBasic(optPartHex,optPartBin):
    i=0
    while True:
        print(" ")
        print(optPartHex[i])
        print("Optional Parameter :" + indicatorTypeDict[optPartHex[i]])
        print("Parameter Length:", int(optPartHex[i+1],16))
        print("Parameter content: " + ' '.join(optPartHex[i+2:(i+2+int(optPartHex[i+1],16))]))
        if optPartHex[i]=='0a':
        #   print("Calling Part Number "+ ' '.join(optPartHex[(i+2):(i+int(optPartHex[i+1],16)+2)]))
            ParsePartyNumber(optPartBin[(i+2):(i+int(optPartHex[i+1],16)+2)])
        elif optPartHex[i]=='c0':
            print("Generic Number "+ ' '.join(optPartHex[(i+3):(i+int(optPartHex[i+1],16)+2)]))
            ParsePartyNumber(optPartBin[(i+3):(i+int(optPartHex[i+1],16)+2)])
        if optPartHex[i+int(optPartHex[i+1],16)+2] == '00':
            break
        else:
            i=i+int(optPartHex[i+1],16)+2
 

def ParseAddresSignal(PAS):
    print("...." + PAS[4:9] + AddresSignal[PAS[4:9]])
    print(PAS[0:4] + "...." + AddresSignal[PAS[0:4]])
     

def main():
    while True:

        hexdec = input("Enter the number you want to convert "); 
        messageHex = [hexdec[idx:idx+2]  for idx in range(len(hexdec)) if idx%2 == 0] # Seperate the number two by two
        messageBin = ['{:08b}'.format(int(n, 16)) for n in messageHex]
        parsedContent['messageType'] =  DetectMessageType(messageHex[0])
        print(" ")
        print("--ISDN User Part")
        print(" ")
        print("-Massage type: " + parsedContent['messageType'])
        if parsedContent['messageType'] == messageTypeDict['01']:
            #MAndatory Fixed part parsing
            print(" ")
            print("Nature of Connection Indicators :")
            print("Mandotary Parameter: " + indicatorTypeDict['06'])
            ParseNOC(messageBin[1])   # Parse the NOC for taking digits means
            print(" ")
            print("Forward Call Indicators: ")
            print("Mandatory Parameter: " + indicatorTypeDict['07'])
            ParseFCI(messageBin[2:4])
            print(" ")
            print("Calling Party's category: ")
            print("Mandatory Parameter: " + indicatorTypeDict['09'])
            print("Parameter content: " + messageHex[4])

            print(" ")
            print("Pointers to Mandatory Variable IEs: " +' '.join(messageHex[5:8]))
            MVPptrs =  messageHex[5:8]


            indexOfMVP = 8
            lengthOfUSI = 0
            if int(messageHex[7],16) > 0:
                indexOfOptPArms = 7 + int(messageHex[7],16)
            else:
                indexOfOptPArms = 0
            if int(messageHex[5],16) > 0:
                lengthOfUSI = int(messageHex[indexOfMVP],16)
                print("Mandatory Parameter: " + indicatorTypeDict['1d'])
                print("Parameter content: " + ' '.join(messageHex[indexOfMVP:(indexOfMVP + lengthOfUSI+1)]))
            else:
                pass    

            print(" ")
            CDN_index = 6 + int(messageHex[6],16) 
            print("Mandatory Parameter: " + indicatorTypeDict['04'])
            print("Parameter Length:", int(messageHex[CDN_index],16))
            print("Parameter content: "+ ' '.join(messageHex[(CDN_index+1):indexOfOptPArms]))
            ParsePartyNumber(messageBin[(CDN_index+1):indexOfOptPArms])
       
            if indexOfOptPArms > 0 :
                ParseOptPartBasic(messageHex[indexOfOptPArms:],messageBin[indexOfOptPArms:])

        elif parsedContent['messageType'] == 'ERR':
            pass
        else:
            print('!!!No Parser implemented for this message type')
main()


