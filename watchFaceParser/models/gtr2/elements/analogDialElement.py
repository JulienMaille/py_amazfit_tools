import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class AnalogDialElement(ContainerElement):
    def __init__(self, parameter, parent=None, name=None):
        self._hours = None
        self._minutes = None
        self._seconds = None
        super(AnalogDialElement, self).__init__(parameters=None, parameter=parameter, parent=parent, name=name)

    def getHours(self):
        return self._hours

    def getMinutes(self):
        return self._minutes

    def getSeconds(self):
        return self._seconds

    def drawAnalogDialElement(self, drawer, resources, state):

        # display order of clock hand by Amazfit:
        # 1 All hands are centered - hour > minute > second
        # 2 The second hand is shifted - seconds > hour > minute
        # 3 All hands are displaced - hour > minute > second

        if self.getSeconds():
            if self.getHours() or self.getMinutes():
                if ((self.getHours() and self.getMinutes() and
                     self.getHours().getX() == self.getMinutes().getX() and
                     self.getHours().getY() == self.getMinutes().getY()) and
                        (self.getHours() and (self.getSeconds().getX() != self.getHours().getX() or
                                              self.getSeconds().getY() != self.getHours().getY())) or
                        (self.getMinutes() and (self.getSeconds().getX() != self.getMinutes().getX() or
                                                self.getSeconds().getY() != self.getMinutes().getY()))):
                    if self.getSeconds():
                        self.getSeconds().drawSecondsClockHandElement(drawer, resources, state)
                    if self.getHours():
                        self.getHours().drawHoursClockHandElement(drawer, resources, state)
                    if self.getMinutes():
                        self.getMinutes().drawMinutesClockHandElement(drawer, resources, state)
                else:
                    if self.getHours():
                        self.getHours().drawHoursClockHandElement(drawer, resources, state)
                    if self.getMinutes():
                        self.getMinutes().drawMinutesClockHandElement(drawer, resources, state)
                    if self.getSeconds():
                        self.getSeconds().drawSecondsClockHandElement(drawer, resources, state)
            else:
                self.getSeconds().drawSecondsClockHandElement(drawer, resources, state)
        else:
            if self.getHours():
                self.getHours().drawHoursClockHandElement(drawer, resources, state)
            if self.getMinutes():
                self.getMinutes().drawMinutesClockHandElement(drawer, resources, state)
                
    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.analogDial.hoursClockHandElement import HoursClockHandElement
            self._hours = HoursClockHandElement(parameter=parameter, parent=self, name='Hours')
            return self._hours
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.analogDial.minutesClockHandElement import MinutesClockHandElement
            self._minutes = MinutesClockHandElement(parameter=parameter, parent=self, name='Minutes')
            return self._minutes
        elif parameterId == 3:
            from watchFaceParser.models.gtr2.elements.analogDial.secondsClockHandElement import SecondsClockHandElement
            self._seconds = SecondsClockHandElement(parameter=parameter, parent=self, name='Seconds')
            return self._seconds
        else:
            return super(AnalogDialElement, self).createChildForParameter(parameter)
