import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement
from watchFaceParser.models.gtr2.elements.common.followObject import FollowObject


class DateElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._dateDigits = []
        self._weeksDigits = None
        self._dateProgress = None
        self._dowProgress = None		
        super(DateElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getDateDigits(self):
        return self._dateDigits

    def getWeeksDigits(self):
        return self._weeksDigits

    def getDateProgress(self):
        return self._dateProgress

    def getDOWProgress(self):
        return self._dowProgress

    def drawDateElement(self, drawer, images, state):
        self.draw3(drawer, images, state)

    def draw3(self, drawer, images, state):
        if self.getDateDigits():
            follow_object = FollowObject()
            for d in self.getDateDigits():
                follow_object = d.drawDigitalDateDigitElement(drawer, images, state, follow_object)
        if self.getWeeksDigits():
            self.getWeeksDigits().drawDigitalCommonDigitElement(drawer, images, state.getTime().weekday(), number_min=1,
                                                                number_max=31, minimum_digits=2, padding_zero_length=2)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.common.digitalDateDigitElement import DigitalDateDigitElement
            self._dateDigits.append(DigitalDateDigitElement(parameter, parent = self, name = 'DateDigits'))
            return self._dateDigits
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.common.digitalCommonDigitElement import DigitalCommonDigitElement
            self._weeksDigits = DigitalCommonDigitElement(parameter = parameter, parent = self, name = 'WeeksDigits')
            return self._weeksDigits
        elif parameterId == 3:
            #TODO: DateProgress als ProgressElement
            pass
        elif parameterId == 4:
            #TODO: DOWProgress als DOWProgressElement
            pass
        else:
            return super(DateElement, self).createChildForParameter(parameter)
