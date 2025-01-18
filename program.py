import os.path
import logging
import json
import io

from watchFaceParser.reader import Reader
from watchFaceParser.writer import Writer
from watchFaceParser.utils.parametersConverter import ParametersConverter
from watchFaceParser.utils.resourcesLoader import ResourcesLoader 
from watchFaceParser.models.fileDescriptor import FileDescriptor
from watchFaceParser.models.watchState import WatchState
from watchFaceParser.previewGenerator import PreviewGenerator
from watchFaceParser.config import Config
from watchFaceParser.models.weatherCondition import WeatherCondition
from watchFaceParser.models.parameter import Parameter


def dumper(obj):
    try:
        return obj.toJSON()
    except AttributeError:
        return obj.__dict__


class Parser:
    raw_header_file_name = "raw_header.bin"

    @staticmethod
    def createOutputDirectory(originalFileName):
        path = os.path.dirname(originalFileName)
        name, _ = os.path.splitext(os.path.basename(originalFileName))
        unpackedPath = os.path.join(path, name)
        if not os.path.exists(unpackedPath):
            os.mkdir(unpackedPath)
        return unpackedPath


    @staticmethod
    def readWatchFaceConfig(jsonFileName):
        assert(type(jsonFileName) == str)
        logging.debug("Reading config...")
        try:
            with open(jsonFileName, 'rb') as fileStream:
                return json.load(fileStream)

        except Exception as e:
            logging.fatal(e, exc_info=True)
            return None


    @staticmethod
    def setupLogger(logFileName):
        logging.basicConfig(filename=logFileName, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


    @staticmethod
    def writeWatchFace(outputDirectory, outputFileName, imagesDirectory, watchFace):
        assert(type(outputDirectory) == str)
        assert(type(outputFileName) == str)
        assert(type(imagesDirectory) == str)
        try:
            if not Config.isOldFormat() and (Config.isGtr2Mode() or Config.isGts2Mode() or Config.isTrexProMode()): 
                from watchFaceParser.watchFaceGTR2 import WatchFace
            elif Config.isGts2MiniMode() or Config.isBipUMode() or Config.isBip3Mode():
                from watchFaceParser.watchFaceGTS2Mini import WatchFace
            else:
                from watchFaceParser.watchFace import WatchFace
            logging.debug(f"Reading referenced images from '{imagesDirectory}'")
            imagesReader = ResourcesLoader(imagesDirectory)
            imagesReader.process(WatchFace, watchFace)

            logging.debug("Building parameters for watch face...")
            descriptor = ParametersConverter.build(WatchFace, watchFace)
            if descriptor[0].getId() == 0:
                #dirty hack to retrieve the deviceid from json
                Config.setDeviceId(descriptor.pop(0).getChildren()[0].getValue())

            baseName, _ = os.path.splitext(os.path.basename(outputFileName))
            Parser.generatePreviews(descriptor, imagesReader.getImages(), outputDirectory, baseName)

            logging.debug(f"Writing watch face to '{outputFileName}'")
            with open(outputFileName, 'wb') as fileStream:
                writer = Writer(fileStream, imagesReader.resources())
                writer.write(descriptor, ( Config.isGts2MiniMode() or Config.isBipUMode() or Config.isBip3Mode() ) )
                fileStream.flush() 
            from watchFaceParser.models.header import Header
            Header.patchHeaderAfter( outputFileName )

        except Exception as e:
            logging.fatal(e, exc_info=True)
            os.remove(outputFileName)


    @staticmethod
    def readWatchFace(inputFileName):
        logging.debug(f"Opening watch face '{inputFileName}'")
        try:
            with open(inputFileName, 'rb') as fileStream:
                reader = Reader(fileStream)
                logging.debug("Reading parameters...")
                reader.read()
                return reader
        except Exception as e:
            import traceback
            traceback.print_stack()
            logging.exception(e)
            return None


    @staticmethod
    def packWatchFace(inputFileName):
        assert(type(inputFileName) == str)
        baseName, _ = os.path.splitext(os.path.basename(inputFileName))
        outputDirectory = os.path.dirname(inputFileName)
        outputFileName = os.path.join(outputDirectory, f"{baseName}_packed.bin")
        Parser.setupLogger(os.path.join(outputDirectory, f'{baseName}_packed.log'))

        watchFace = Parser.readWatchFaceConfig(inputFileName)

        t = json.dumps(watchFace, default=dumper, indent = 2)
        logging.debug(f't: {t}')
        if not watchFace:
            return

        imagesDirectory = os.path.dirname(inputFileName)
        try:
            Parser.writeWatchFace(outputDirectory, outputFileName, imagesDirectory, watchFace)
        except Exception as e:
            os.remove(outputFileName)
            raise e

    @staticmethod
    def packRawWatchFace(inputFileName):
        assert(type(inputFileName) == str)
        baseName, _ = os.path.splitext(os.path.basename(inputFileName))
        outputFileName = os.path.join(inputFileName, f"{baseName}_packed.bin")
        Parser.setupLogger(os.path.join(inputFileName, f'{baseName}_packed.log'))
        imagesCount = 0
        try:
            headerFileName = os.path.join(inputFileName, f"{Parser.raw_header_file_name}") 
            with open(headerFileName, 'rb') as f: 
                logging.info("Reading raw header...")
                from watchFaceParser.models.header import Header
                header = Header.readFrom(f)
                logging.info("Header was read:")
                if not header.isValid():
                    logging.info("Header is not valid!")
                    return                 
                logging.info("Reading parameter offsets...")
                tmpArray = bytearray(f.read(header.parametersSize))
                parametersStream = io.BytesIO(tmpArray) 
                logging.info("Parameter offsets were read from file")

                logging.info("Reading parameters descriptor...")
                from watchFaceParser.models.parameter import Parameter
                mainParam = Parameter.readFrom(parametersStream)
                logging.info("getParameters descriptor was read:")
                parametersTableLength = mainParam.getChildren()[0].getValue()
                imagesCount = mainParam.getChildren()[1].getValue()
                f.seek(0)
                tmpArray = bytearray( f.read() )
                f.close() 
                logging.info("Header was read") 
        except Exception as e:
            import traceback
            traceback.print_stack()
            logging.exception(e)
            return None 
        try:
            logging.debug(f"Writing watch  to '{outputFileName}'") 
            with open(outputFileName, 'wb') as fileStream: 
                fileStream.write(tmpArray) 
                imagesReader = ResourcesLoader(inputFileName)
                imageStartIndex = Config.getStartImageIndex()
                for i in range(imagesCount-imageStartIndex):
                    imagesReader.loadImage(i+imageStartIndex)
                logging.debug("Writing images...")
                from resources.writer import Writer
                Writer(fileStream).write( imagesReader.resources())
                fileStream.flush()
        except Exception as e:
            os.remove(outputFileName)
            raise e

    @staticmethod
    def unpackRawWatchFace(inputFileName):
        outputDirectory = Parser.createOutputDirectory(inputFileName)
        baseName, _ = os.path.splitext(os.path.basename(inputFileName))
        Parser.setupLogger(os.path.join(outputDirectory, f'{baseName}.log'))

        logging.debug(f"Opening watch face '{inputFileName}'")
        try:
            with open(inputFileName, 'rb') as f:
                logging.info("Reading header...")
                from watchFaceParser.models.header import Header
                header = Header.readFrom(f)
                logging.info("Header was read:")
                if not header.isValid():
                    logging.info("Header is not valid!")
                    return 
                logging.info("Reading parameter offsets...")
                tmpArray = bytearray(f.read(header.parametersSize))
                parametersStream = io.BytesIO(tmpArray) 
                logging.info("Parameter offsets were read from file")

                logging.info("Reading parameters descriptor...")
                mainParam = Parameter.readFrom(parametersStream)
                logging.info("getParameters descriptor was read:")
                parametersTableLength = mainParam.getChildren()[0].getValue()
                headerSize = f.tell();
                f.seek(0) 
                tmpArray = bytearray(f.read(headerSize + parametersTableLength))
                f.close()

                outputFileName = os.path.join(outputDirectory, f"{Parser.raw_header_file_name}") 
                logging.debug(f"Writing watch face raw header to '{outputFileName}'") 
                with open(outputFileName, 'wb') as fileStream: 
                    fileStream.write(tmpArray)
                    fileStream.flush()
        except Exception as e:
            import traceback
            traceback.print_stack()
            logging.exception(e)
            return None

        reader = Parser.readWatchFace(inputFileName)
        if not reader:
            return

        logging.debug("Exporting resources to '%s'" % (outputDirectory, ))
        reDescriptor = FileDescriptor(Resources = reader.getResources())

        from resources.extractor import extractor
        extractor(reDescriptor).extract(outputDirectory) 


    @staticmethod
    def unpackWatchFace(inputFileName):
        outputDirectory = Parser.createOutputDirectory(inputFileName)
        baseName, _ = os.path.splitext(os.path.basename(inputFileName))
        Parser.setupLogger(os.path.join(outputDirectory, f'{baseName}.log'))

        reader = Parser.readWatchFace(inputFileName)
        if not reader:
            return

        watchFace = Parser.parseResources(reader)
        if not watchFace:
            return

        logging.debug("generatePreviews")
        #TODO implement models
        Parser.generatePreviews(reader.getParameters(), reader.getImages(), outputDirectory, baseName)
        logging.debug("generatePreviews done")

        logging.debug("Exporting resources to '%s'" % (outputDirectory, ))
        reDescriptor = FileDescriptor(Resources = reader.getResources())

        from resources.extractor import extractor
        extractor(reDescriptor).extract(outputDirectory)
        Parser.exportWatchFaceConfig(watchFace, os.path.join(outputDirectory, f'{baseName}.json'))


    @staticmethod
    def exportWatchFaceConfig(watchFace, jsonFileName):
        assert(type(jsonFileName) == str)
        logging.debug("Exporting config...")
        try:
            with open(jsonFileName, 'w') as fileStream:
                fileStream.write(json.dumps(watchFace, default=dumper, indent = 2))
                fileStream.flush()
        except Exception as e:
            logging.fatal(e, exc_info=True)


    @staticmethod
    def parseResources(reader):
        logging.debug("Parsing parameters...")
        if not Config.isOldFormat() and (Config.isGtr2Mode() or Config.isGts2Mode() or Config.isTrexProMode()): 
            from watchFaceParser.watchFaceGTR2 import WatchFace
        elif Config.isGts2MiniMode() or Config.isBipUMode() or Config.isBip3Mode():
            from watchFaceParser.watchFaceGTS2Mini import WatchFace
        else:
            from watchFaceParser.watchFace import WatchFace
        try:
            ParametersConverter.listParams(reader.getParameters())
            return ParametersConverter.parse(WatchFace, reader.getParameters())
        except Exception as e:
            logging.fatal(e, exc_info=True)
            return None


    @staticmethod
    def generatePreviews(parameters, images, outputDirectory, baseName):
        assert(type(parameters) == list)
        assert(type(images) == list)
        assert(type(outputDirectory) == str)
        assert(type(baseName) == str)

        logging.debug("Generating previews...")

        states = Parser.getPreviewStates(outputDirectory)
        import sys
        try:
            logging.debug("Generating states done...")
            staticPreview = PreviewGenerator.createImage(parameters, images, WatchState())

            logging.debug("Generating static preview gen done...")
            staticPreview.save(os.path.join(outputDirectory, f"{baseName}_static.png"))

            #generate small preview image for Preview section.
            from PIL import Image, ImageDraw, ImageOps
            new_w, new_h = Config.getPreviewSize()
            if Config.isGtsMode() or Config.isGts2Mode():
                im_resized = ImageOps.expand(staticPreview, border=5)
                im_resized = im_resized.resize((new_w, new_h), resample = Image.LANCZOS)
            else:
                im_resized = staticPreview.resize((new_w, new_h), resample = Image.LANCZOS)
                
            def rounded_rectangle(draw, box, radius, color):
                l, t, r, b = box
                d = radius * 2
                draw.ellipse((l, t, l + d, t + d), color)
                draw.ellipse((r - d, t, r, t + d), color)
                draw.ellipse((l, b - d, l + d, b), color)
                draw.ellipse((r - d, b - d, r, b), color)
                d = radius
                draw.rectangle((l, t + d, r, b - d), color)
                draw.rectangle((l + d, t, r - d, b), color)

            corner_radius = 38

            if Config.isGtsMode():
                mask = Image.new("RGBA", Config.getPreviewSize(), (255, 255, 255, 0))
                d = ImageDraw.Draw(mask)

                rounded_rectangle(d,(3,3 , new_w -3,new_h-3),corner_radius,(180,180,180,255))
                rounded_rectangle(d,(5,5 , new_w-5,new_h-5),corner_radius,(255,255,255,0))
                im_resized.paste(mask,(0,0),mask)

            # remove transparent background from static preview image
            back = Image.new('RGB', im_resized.size)
            d = ImageDraw.Draw(back)
            d.rectangle([(0, 0), im_resized.size], fill="#000000")
            back.paste(im_resized)

            back.save(os.path.join(outputDirectory, f"{baseName}_static_{new_h}.png"))
            logging.debug("Generating static preview save done...")

            previewImages = PreviewGenerator.createAnimation(parameters, images, states)
            logging.debug("Generating anim preview gen done...")

            images = []

            for previewImage in previewImages:
                images.append(previewImage)
            if len(images) > 0:
                images[0].save(os.path.join(outputDirectory, f"{baseName}_animated.gif"),
                               save_all=True,
                               append_images=images[1:],
                               duration=1000,
                               loop=0)
            else:
                logging.debug("Nothing to save in animated gif...")
        except Exception as e:
            logging.error("Preview Generate Error...")
            logging.error(e, exc_info=True)

    @staticmethod
    def getPreviewStates(outputDirectory):
        import os
        preview_states_path = os.path.join(outputDirectory, "Preview.States")

        if os.path.exists(preview_states_path):
            preview_states = []
            try:
                with open(preview_states_path, 'rb') as stream:
                    data = json.load(stream)
                    if isinstance(data, list):
                        for d in data:
                            w = WatchState.fromJson(d)
                            preview_states.append(w)
                    else:
                        w = WatchState.fromJson(data)
                        preview_states.append(w)
                    return preview_states
            except Exception as e:
                logging.error("States Parse Error...")
                logging.error(e, exc_info=True)
                return preview_states

        preview_states = Parser.generateSampleStates()
        with open(preview_states_path, 'w') as stream:
            stream.write(json.dumps(preview_states, default=dumper, indent = 2))
            stream.flush()

        return preview_states


    @staticmethod
    def generateSampleStates():
        import datetime
        time = datetime.datetime.now()
        states = []

        for i in range(12):
            num = i + 1
            watchState = WatchState(
                BatteryLevel = 0 if i >= 10 else (100 - i * 10),
                Pulse = 60 + i * 12,
                Steps = num * 1000,
                Calories = num * 75,
                Distance = num * 70,
                Bluetooth = num < 6,
                Unlocked = num < 6,
                Alarm = num < 8,
                DoNotDisturb = num > 4 and num < 9,
                CurrentTemperature = -15 + 6 * i,
                Stand=num,
                PAI=num*9,
                Humidity=i*8,
                UVindex=i,
                AirQuality=i*41,
                Animation=i
            )

            watchState.setCurrentWeather(i)
            watchState.setCurrentTemperature(-15 + i * 6)

            watchState.setTime(datetime.datetime(year = time.year, month = num, day = num * 2 + 5, hour = i * 2, minute = i * 5, second = i))
            watchState.setScreenIdle(None)
            states.append(watchState)

        states[-2].setScreenIdle(True)
        states[-1].setScreenIdle(True)
        return states
