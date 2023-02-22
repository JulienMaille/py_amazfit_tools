import logging
import io


class Writer:
    def __init__(self, stream, images):
        self._stream = stream
        self._images = images


    def write(self, descriptor, specialPadding):
        logging.debug("Encoding parameters...")
        encodedParameters = {}
        for parameter in descriptor:
            logging.debug(f"Parameter: {parameter.getId()}")
            #print(f"Parameter: {parameter.getId()}")
            memoryStream = io.BytesIO()
            for child in parameter.getChildren():
                child.write(memoryStream)
#                print(".",end="")
            #print("")
            encodedParameters[parameter.getId()] = memoryStream
            #print ([ "%02x" % x for x in memoryStream.getvalue()])


        logging.debug("Encoding offsets and lengths...")
        parametersPositions = []
        offset = 0
        maxEncodedParametersLength = 0
        from watchFaceParser.models.parameter import Parameter
        for encodedParameterId in encodedParameters:
            #print ([ "%02x" % x for x in (encodedParameters[encodedParameterId].getbuffer())])
            encodedParameterLength = len(encodedParameters[encodedParameterId].getbuffer())
            maxEncodedParametersLength = max(maxEncodedParametersLength, encodedParameterLength)
#            print ("OFFSET %04x"%offset)
            parametersPositions.append(Parameter(encodedParameterId, [ Parameter(1, offset), Parameter(2, encodedParameterLength) ]))
            offset += encodedParameterLength
        from watchFaceParser.config import Config
        imageCount = len(self._images) + Config.getStartImageIndex()
        parametersPositions.insert(0, Parameter(1, [ Parameter(1, offset), Parameter(2, imageCount) ]))

        encodedParametersPositions = io.BytesIO()
        for parametersPosition in parametersPositions:
            parametersPosition.write(encodedParametersPositions)
#            print ([ "%02x" % x for x in encodedParametersPositions.getbuffer()])

        logging.debug("Writing header...")
        from watchFaceParser.models.header import Header
        maxEncodedParametersLength = max(maxEncodedParametersLength, len(encodedParametersPositions.getbuffer()))
        header = Header(unknown = maxEncodedParametersLength, parametersSize = len(encodedParametersPositions.getbuffer()))
        header.writeTo(self._stream)

        logging.debug("Writing parameters offsets and lengths...")
        encodedParametersPositions.seek(0, 0)
        self._stream.write(encodedParametersPositions.read())

        logging.debug("Writing parameters...")
        for encodedParameter in encodedParameters:
            #print ("parameterDescriptor",encodedParameter)
            stream = encodedParameters[encodedParameter]
            #stream.seek(0)
            #print ([ "%02x" % x for x in stream.read()])
            stream.seek(0, 0)
            self._stream.write(stream.read())

        logging.debug("Writing images...")
        from resources.writer import Writer
        Writer(self._stream).write(self._images, specialPadding)
        
