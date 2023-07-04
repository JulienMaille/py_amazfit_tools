import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class AnalogDialElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._hours = None
        self._minutes = None
        self._seconds = None
        self._common_center = None
        super(AnalogDialElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, images, state):
        if self._hours:
            if self._common_center and not self._hours._center:
                self._hours._center = self._common_center
            self._hours.draw3(drawer, images, state)
        if self._minutes:
            if self._common_center and not self._minutes._center:
                self._minutes._center = self._common_center
            self._minutes.draw3(drawer, images, state)
        if self._seconds:
            if self._common_center and not self._seconds._center:
                self._seconds._center = self._common_center
            self._seconds.draw3(drawer, images, state)
    

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            pass
        elif parameterId == 2: # CommonCenterCoordinates
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._common_center = CoordinatesElement(parameter = parameter, parent = self, name = 'CommonCenterCoordinates')
            return self._common_center
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.analogDial.hoursClockHandElement import HoursClockHandElement
            self._hours = HoursClockHandElement(parameter = parameter, parent = self, name = 'Hours')
            return self._hours
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.analogDial.minutesClockHandElement import MinutesClockHandElement
            self._minutes = MinutesClockHandElement(parameter = parameter, parent = self, name = 'Minutes')
            return self._minutes
        elif parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.analogDial.secondsClockHandElement import SecondsClockHandElement
            self._seconds = SecondsClockHandElement(parameter = parameter, parent = self, name = 'Seconds')
            return self._seconds
        else:
            return super(AnalogDialElement, self).createChildForParameter(parameter)