import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class TimeSeparateDigitsElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._hours = None
        self._minutes = None
        self._seconds = None
        self._amPm = None
        self._drawingOrder = [1, 2, 3, 4]
        self._separator_hours = None
        self._delimiter2 = None
        self._pm = None
        super(TimeSeparateDigitsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getHours(self):
        return self._hours

    def getMinutes(self):
        return self._minutes

    def getSeconds(self):
        return self._seconds

    def draw3(self, drawer, images, state):
        assert(type(images) == list)

        hours = state.getTime().hour

        for i in range(0, 4):
            if self.getHours() and self.getHours().getTens() and self._drawingOrder[i] == 1:
                self.getHours().getTens().draw3(drawer, images, int(hours % 100 / 10))
            if self.getHours() and self.getHours().getOnes() and self._drawingOrder[i] == 2:
                self.getHours().getOnes().draw3(drawer, images, hours % 10)

            if self.getMinutes() and self.getMinutes().getTens() and self._drawingOrder[i] == 3:
                self.getMinutes().getTens().draw3(drawer, images, int(state.getTime().minute % 100 / 10))
            if self.getMinutes() and self.getMinutes().getOnes() and self._drawingOrder[i] == 4:
                self.getMinutes().getOnes().draw3(drawer, images, state.getTime().minute % 10)

        if self.getSeconds():
            self.getSeconds().draw3(drawer, images, state.getTime().second)

        if self._separator_hours:
            self._separator_hours.draw3(drawer, images, state)


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
            self._separator_hours = ImageElement(parameter=parameter, parent=self, name='Separator')
            return self._separator_hours
        elif parameterId == 6:
            pass
        elif parameterId == 7:
            pass
        elif parameterId == 8:
            pass
        else:
            print ("Unknown TimeSeparateDigitsElement",parameterId)
            return super(TimeSeparateDigitsElement, self).createChildForParameter(parameter)

