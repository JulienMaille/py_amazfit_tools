import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class TimeSeparateDigitsElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._hours = None
        self._minutes = None
        self._seconds = None
        self._amPm = None
        self._drawingOrder = [1, 2, 3, 4]
        self._separatorHours = None
        self._separatorMinutes = None
        self._padding_zero_hours = None
        self._padding_zero_minutes = None
        super(TimeSeparateDigitsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, images, state):
        assert(type(images) == list)

        hours = state.getTime().hour

        for i in range(0, 4):
            if self._hours and self._hours.getTens() and self._drawingOrder[i] == 1:
                if self._padding_zero_hours or int(hours % 100 / 10) > 0:
                    self._hours.getTens().draw3(drawer, images, int(hours % 100 / 10))
            if self._hours and self._hours.getOnes() and self._drawingOrder[i] == 2:
                self._hours.getOnes().draw3(drawer, images, hours % 10)

            if self._minutes and self._minutes.getTens() and self._drawingOrder[i] == 3:
                if self._padding_zero_minutes or int(state.getTime().minute % 100 / 10) > 0:
                    self._minutes.getTens().draw3(drawer, images, int(state.getTime().minute % 100 / 10))
            if self._minutes and self._minutes.getOnes() and self._drawingOrder[i] == 4:
                self._minutes.getOnes().draw3(drawer, images, state.getTime().minute % 10)

        if self._seconds:
            self._seconds.draw3(drawer, images, state.getTime().second)

        if self._separatorHours:
            self._separatorHours.draw3(drawer, images, state)
        if self._separatorMinutes:
            self._separatorMinutes.draw3(drawer, images, state)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.twoDigitsElement import TwoDigitsElement
            self._hours = TwoDigitsElement(parameter = parameter, parent = self, name = 'Hours')
            return self._hours
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.twoDigitsElement import TwoDigitsElement
            self._minutes = TwoDigitsElement(parameter = parameter, parent = self, name = 'Minutes')
            return self._minutes
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.common.twoDigitsElement import TwoDigitsElement
            self._seconds = TwoDigitsElement(parameter = parameter, parent = self, name = 'Seconds')
            return self._seconds
        elif parameterId == 4:
            self._drawingOrder = [(parameter._value & 0xF000) >> 12, (parameter._value & 0xF00) >> 8, (parameter._value & 0xF0) >> 4, parameter._value & 0xF]
        elif parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._separatorHours = ImageElement(parameter = parameter, parent = self, name = 'SeparatorHours')
            return self._separatorHours
        elif parameterId == 6:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._separatorMinutes = ImageElement(parameter = parameter, parent = self, name ='SeparatorMinutes')
            return self._separatorMinutes
        elif parameterId == 7:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._padding_zero_hours = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroHours')
        elif parameterId == 8:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._padding_zero_minutes = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroMinutes')
        else:
            print ("Unknown TimeSeparateDigitsElement",parameterId)
            return super(TimeSeparateDigitsElement, self).createChildForParameter(parameter)

