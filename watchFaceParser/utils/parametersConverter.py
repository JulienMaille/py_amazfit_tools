import logging
import os.path

from watchFaceParser.utils.elementsHelper import ElementsHelper
from watchFaceParser.models.parameterFlags import ParameterFlags
from watchFaceParser.models.textAlignment import TextAlignment
from watchFaceParser.models.gts2mini.textAlignmentGts2Mini import TextAlignmentGts2Mini
from watchFaceParser.models.color import Color
from watchFaceParser.models.parameter import Parameter
from watchFaceParser.config import Config 
from watchFaceParser.models.gtr2.timeType import TimeType
from watchFaceParser.models.gtr2.dateType import DateType
from watchFaceParser.models.gtr2.combingModeType import CombingModeType
from watchFaceParser.models.gtr2.digitType import DigitType
from watchFaceParser.models.gtr2.imageprogressDisplayType import ImageProgressDisplayType
from watchFaceParser.models.gtr2.langCodeType import LangCodeType
from watchFaceParser.models.gtr2.textAlignment import TextAlignmentGTR2
from watchFaceParser.models.gtr2.activityType import ActivityType
from watchFaceParser.models.gts2mini.shortcutType import ShortcutType

def ulong2long(n):
    if type(n) == int:
        if n >= 0x7fffffffffffffff:
            n = -(0xffffffffffffffff - n + 1)
    return n

def uint2int(n):
    if type(n) == int:
        if n >= 0x7fffffff:
            return -(0xffffffff - n + 1)
    return n

def toSigned32(n):
    n = n & 0xffffffff
    return (n ^ 0x80000000) - 0x80000000

class ParametersConverter:
    @staticmethod
    def getValue(propertyInfo, serializable):
        propertyInfoName = propertyInfo['Name']
        if not propertyInfoName in serializable:
            return None
        return serializable[propertyInfoName]


    @staticmethod
    def build(T, serializable, path = ""):
        result = []
        #print ("T",T)
        properties = ElementsHelper.sortedProperties(T)
        for _id in properties:
            currentPath = str(_id) if path == None or path == '' else ''.join([path, '.', str(_id)])

            propertyInfo = properties[_id]
            #propertyType = propertyInfo['Type']
            if isinstance(propertyInfo['Type'],list):
                propertyType = propertyInfo['Type'][0]
            else:
                propertyType = propertyInfo['Type']			
            propertyValue = ParametersConverter.getValue(propertyInfo, serializable)
            #print("QUI",propertyInfo['Name'],serializable,propertyValue)

            if propertyValue is None:
                continue
            if ( 
                    propertyType == 'int' or 
                    propertyType == 'long' or 
                    propertyType == 'long?' or 
                    propertyType == 'float' or 
                    propertyType == TextAlignment or 
                    propertyType == TextAlignmentGTR2 or 
                    propertyType == TextAlignmentGts2Mini or 
                    propertyType == ActivityType or 
                    propertyType == ShortcutType or 
                    propertyType == Color or 
                    propertyType == LangCodeType or 
                    propertyType == TimeType or 
                    propertyType == DigitType or 
                    propertyType == ImageProgressDisplayType or 
                    propertyType == DateType or 
                    propertyType == CombingModeType or 
                    propertyType == 'bool'
                ):
                value = propertyValue
                flags = None
                if propertyType == 'bool' or type(propertyValue) == bool:
                    value = 1 if propertyValue else 0
                elif propertyType == TextAlignment:
                    value = TextAlignment.fromJSON(propertyValue)
                elif propertyType == TextAlignmentGTR2:
                    value = TextAlignmentGTR2.fromJSON(propertyValue)
                elif propertyType == TextAlignmentGts2Mini:
                    value = TextAlignmentGts2Mini.fromJSON(propertyValue)
                elif propertyType == DigitType:
                    value = DigitType.fromJSON(propertyValue)
                elif propertyType == LangCodeType:
                    value = LangCodeType.fromJSON(propertyValue)
                elif propertyType == Color:
                    value = Color.fromJSON(propertyValue)
                elif propertyType == ActivityType:
                    value = ActivityType.fromJSON(propertyValue)
                elif propertyType == ShortcutType:
                    value = ShortcutType.fromJSON(propertyValue)
                elif propertyType == TimeType:
                    value = TimeType.fromJSON(propertyValue)
                elif propertyType == DigitType:
                    value = DigitType.fromJSON(propertyValue)
                elif propertyType == ImageProgressDisplayType:
                    value = ImageProgressDisplayType.fromJSON(propertyValue)
                elif propertyType == DateType:
                    value = DateType.fromJSON(propertyValue)
                elif propertyType == CombingModeType:
                    value = CombingModeType.fromJSON(propertyValue)
                elif propertyType == 'long' or propertyType == 'long?':
                    value = int(value)
                elif propertyType == 'int':
                    value = int(value)
                elif propertyType == 'float':
                    value = float(value)
                logging.debug(f"{currentPath} '{propertyInfo['Name']}': {value}")
                result.append(Parameter(_id, value, None, propertyType))
            #elif isinstance(propertyValue,list): 
            #    print ("e' una lista... fai qualcosa",propertyType)
            #    for i in propertyValue:
            #        print ("I1",i)
            #        innerParameters = ParametersConverter.build(propertyType, i, currentPath)
            #        print ("I2",i,innerParameters)
            #        if len(innerParameters) > 0:
            #            logging.debug(f"{currentPath} '{propertyInfo['Name']}'")
            #            result.append(Parameter(_id, innerParameters))
            #        else:
            #            logging.debug(f"{currentPath} '{propertyInfo['Name']}': Skipped because of empty(loop)")
            elif propertyType == ParameterFlags:
                flags = ParameterFlags.fromJSON(propertyValue)
                logging.debug(f"{currentPath} '{propertyInfo['Name']}': {flags}")
                result.append(Parameter(_id, None, flags = flags))

            else:

#                logging.debug ("childIsList "+str(childIsList)+" "+str(propertyType))
                if isinstance(propertyValue,list):
                    for i in propertyValue:
                        #d={}
                        #d[propertyInfo['Name']] = i
#                        print ("1propertyType",propertyType, d, currentPath )			
                        innerParameters = ParametersConverter.build(propertyType, i, currentPath)
                        #logging.debug(i)

                        if len(innerParameters) > 0:
                            #print ("I0",propertyType, propertyValue)
                            logging.debug(f"{currentPath} '{propertyInfo['Name']}'")
                            result.append(Parameter(_id, innerParameters))
                        else: 
                            logging.debug(f"{currentPath} '{propertyInfo['Name']}': empty1")
                            result.append(Parameter(_id, []))
                    continue
                innerParameters = ParametersConverter.build(propertyType, propertyValue, currentPath)
 #               print ("2propertyType",propertyType, propertyValue, currentPath )			
  #              logging.debug(propertyValue)
  #              logging.debug(propertyType)
#            if not childIsList:

                if len(innerParameters) > 0:
                    #print ("Ip",innerParameters)
                    logging.debug(f"{currentPath} '{propertyInfo['Name']}'")
                    result.append(Parameter(_id, innerParameters))
                else:
                    logging.debug(f"{currentPath} '{propertyInfo['Name']}': empty2")
                    result.append(Parameter(_id, []))
 #                   print ("propertyType",propertyType, propertyValue )			
 #                   sys.exit(1)

        return result

    @staticmethod
    def childIsList(paramType, descriptor, path = ""):
        assert(type(descriptor) == type([]))
        assert(type(path) == type(""))
        properties = ElementsHelper.sortedProperties(paramType)
        currentType = paramType

        for parameter in descriptor:
            parameterId = parameter.getId()

            currentPath = str(parameterId) if not path else os.path.join(path, '.', str(parameterId))

            if parameterId not in properties:
                logging.warn(f"[ParamConv:parse] currentPath {currentPath} / Parameter {parameterId} isn't supported for {currentType}")
                raise IndexError(f"Parameter {parameterId} isn't supported for {currentType}")

            propertyInfo = properties[parameterId]

            if isinstance(propertyInfo['Type'],list):
                childIsList = True
            else:
                childIsList = False
        return childIsList

    @staticmethod
    def listParams(descriptor, path = ""):
        for parameter in descriptor:
            parameterId = parameter.getId()
            currentPath = str(parameterId) if not path else path + '.' + str(parameterId)
            logging.debug(f"{currentPath} Value: {parameter.getValue()}")
            if ( parameter.getChildren() is not None):
                for x in parameter.getChildren():
                    ParametersConverter.listParams([x], currentPath)

    @staticmethod
    def parse(paramType, descriptor, path = ""):
        assert(type(descriptor) == type([]))
        assert(type(path) == type(""))
        properties = ElementsHelper.sortedProperties(paramType)
        result = paramType()
        currentType = paramType

        prevPath = None
        artmp=[]

        for parameter in descriptor:
            parameterId = parameter.getId()

            currentPath = str(parameterId) if not path else os.path.join(path, '.', str(parameterId))

            if parameterId not in properties:
                logging.warn(f"[ParamConv:parse] currentPath {currentPath} / Parameter {parameterId} isn't supported for {currentType}")
                raise IndexError(f"Parameter {parameterId} isn't supported for {currentType}")

            propertyInfo = properties[parameterId]
            
            if isinstance(propertyInfo['Type'],list):
                propertyType = propertyInfo['Type'][0]
            else:
                propertyType = propertyInfo['Type']

            propertyInfoName = propertyInfo['Name']
            string = (f"{currentPath}-{propertyInfoName}")
            logging.debug(string.replace("\\",""))
             
            if propertyType == TextAlignment:
                setattr(result, propertyInfoName, TextAlignment(parameter.getValue()))
            elif propertyType == TextAlignmentGTR2:
                setattr(result, propertyInfoName, TextAlignmentGTR2(parameter.getValue()))
            elif propertyType == TextAlignmentGts2Mini:
                setattr(result, propertyInfoName, TextAlignmentGts2Mini(parameter.getValue()))
            elif propertyType == ParameterFlags:
                setattr(result, propertyInfoName, ParameterFlags(parameter.getValue()))
            elif propertyType == TimeType:
                setattr(result, propertyInfoName, TimeType(parameter.getValue()))
            elif propertyType == ActivityType:
                setattr(result, propertyInfoName, ActivityType(parameter.getValue()))
            elif propertyType == ShortcutType:
                setattr(result, propertyInfoName, ShortcutType(parameter.getValue()))
            elif propertyType == DateType:
                setattr(result, propertyInfoName, DateType(parameter.getValue()))
            elif propertyType == CombingModeType:
                setattr(result, propertyInfoName, CombingModeType(parameter.getValue()))
            elif propertyType == DigitType:
                setattr(result, propertyInfoName, DigitType(parameter.getValue()))
            elif propertyType == ImageProgressDisplayType:
                setattr(result, propertyInfoName, ImageProgressDisplayType(parameter.getValue()))
            elif propertyType == LangCodeType:
                setattr(result, propertyInfoName, LangCodeType(parameter.getValue()))
            elif propertyType == Color:
                setattr(result, propertyInfoName, Color(parameter.getValue()))
            elif propertyType == 'bool':
                setattr(result, propertyInfoName, parameter.getValue() > 0)
            elif propertyType == 'long':
                setattr(result, propertyInfoName, toSigned32(parameter.getValue()))
            elif propertyType == 'int':
                setattr(result, propertyInfoName, uint2int(parameter.getValue()))
            elif propertyType == 'float':
                setattr(result, propertyInfoName, ulong2long(parameter.getValue()))
            elif propertyType == 'long?':
                setattr(result, propertyInfoName, ulong2long(parameter.getValue() or None))
            elif propertyType == '[]':
                assert(False) # not tested yet
            else:		
                tmp = propertyType()	
                #childIsList = False
                artmp = []
                arrDict = {}
                for x in parameter.getChildren():
                   
                    #if not childIsList:
                        #childIsList = ParametersConverter.childIsList(propertyType, [x], currentPath)
                    childIsList = ParametersConverter.childIsList(propertyType, [x], currentPath)

                    psd = ParametersConverter.parse(propertyType, [x], currentPath)
                    import json

                    for kk in psd.__dict__:
                        vv = psd.__dict__[kk]
                        if not childIsList:
                            attr = getattr(tmp, kk, "None")
                            if (attr != "None"):
                                 raise IndexError(f"Parameter {kk} already exist and it is not defined as array")
                            setattr(tmp, kk, vv)
                        else:
                            #artmp.append(vv)
                            if (not kk in arrDict):
                                arrDict[kk] = []
                            arrDict[kk].append(vv)
                    #if childIsList:
                    #    setattr(tmp, kk, artmp)
                for x in arrDict:
                    setattr(tmp, x, arrDict[x])
                setattr(result, propertyInfoName, tmp)
        return result
