import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class TimeSeparatedDigitsElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._hours = None
        self._minutes = None
        self._separatorHours = None
        self._padding_zero_hours = None
        self._drawingOrder = [1, 2, 3, 4]
        super(TimeSeparatedDigitsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

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
                self._minutes.getTens().draw3(drawer, images, int(state.getTime().minute % 100 / 10))
            if self._minutes and self._minutes.getOnes() and self._drawingOrder[i] == 4:
                self._minutes.getOnes().draw3(drawer, images, state.getTime().minute % 10)

        if self._separatorHours:
            self._separatorHours.draw3(drawer, images, state)


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
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._separatorHours = ImageElement(parameter = parameter, parent = self, name = 'SeparatorHours')
            return self._separatorHours
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._padding_zero_hours = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroHours')

        else:
            print ("Unknown TimeSeparatedDigitsElement",parameterId)
            return super(TimeSeparatedDigitsElement, self).createChildForParameter(parameter)

