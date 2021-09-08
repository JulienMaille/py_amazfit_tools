import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class BatteryElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._text = None
        self._percent = None
        self._percentImage = None
        self._scale = None
        self._images = None
        self._unknown4 = None
        self._batteryLinear = None
        super(BatteryElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getText(self):
        return self._text


    def getPercent(self):
        return self._percent


    def getScale(self):
        return self._scale


    def getImages(self):
        return self._images

    def getPercentImage(self):
        return self._percentImage


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        from watchFaceParser.models.elements.basic.valueElement import ValueElement
        if parameterId == 1: #text
            from watchFaceParser.models.elements.battery.batteryNumberElement import BatteryNumberElement
            self._text = BatteryNumberElement(parameter = parameter, parent = self, name = '?_text?')
            return self._text
        elif parameterId == 2: #images
            from watchFaceParser.models.elements.battery.batteryGaugeElement import BatteryGaugeElement # temp.
            self._images = BatteryGaugeElement(parameter = parameter, parent = self, name = '?_images?')
            return self._images
        elif parameterId == 3: #icons - this is the circular battery element found in GTS - Silver Watchface
            from watchFaceParser.models.elements.battery.batteryLinearElement import BatteryLinearElement
            self._batteryLinear = BatteryLinearElement(parameter = parameter, parent = self, name = '?pulseLinear?')
            return self._batteryLinear
        elif parameterId == 4: #unknown4
            from watchFaceParser.models.elements.analogDial.secondsClockHandElement import SecondsClockHandElement # must must be own. fix it!!
            self._unknown4 = SecondsClockHandElement(parameter = parameter, parent = self, name = 'Unknown4')
            return self._unknown4			
        elif parameterId == 5: #percentImage
            from watchFaceParser.models.elements.common.imageElement import ImageElement
            self._percentImage = ImageElement(parameter = parameter, parent = self, name = 'PercentImage')
            return self._percentImage
        elif parameterId == 6: #percent
            from watchFaceParser.models.elements.battery.percentElement import PercentElement
            self._percent = PercentElement(parameter = parameter, parent = self, name = '?_images?')
            return self._percent
        elif parameterId == 7: #scale
            from watchFaceParser.models.elements.battery.circularBatteryElement import CircularBatteryElement
            self._scale = CircularBatteryElement(parameter = parameter, parent = self, name = '_scale')
            return self._scale
        else:
            print ("batteryElement - unimplemented:", parameterId)
            return super(BatteryElement, self).createChildForParameter(parameter)

