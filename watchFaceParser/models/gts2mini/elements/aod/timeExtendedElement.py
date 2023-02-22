import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class TimeExtendedElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._timeSeparateDigits = None
        self._timeAnalog = None
        self._timeDigital = None
        self._amPm = None
        self._timeDigital = None
        super(TimeExtendedElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.aod.timeSeparateDigitsElement import TimeSeparatedDigitsElement
            self._timeSeparateDigits = TimeSeparatedDigitsElement(parameter = parameter, parent = self, name='TimeSeparateDigits')
            return self._timeSeparateDigits
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.aod.analogDialElement import AnalogDialElement
            self._timeAnalog = AnalogDialElement(parameter = parameter, parent = self, name='TimeAnalog')
            return self._timeAnalog
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.date.ampmElement import AmPmElement
            self._amPm = AmPmElement(parameter = parameter, parent = self, name='AmPm')
            return self._amPm
        elif parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.aod.timeDigitalElement import TimeDigitalElement
            self._timeDigital = TimeDigitalElement(parameter = parameter, parent = self, name='TimeDigital')
            return self._timeDigital
        else:
            print ("Unknown TimeExtendedElement",parameterId)
            return super(TimeExtendedElement, self).createChildForParameter(parameter)

