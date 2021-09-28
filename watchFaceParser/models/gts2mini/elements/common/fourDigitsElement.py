﻿import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement


class FourDigitsElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._tens = None
        self._ones = None
        self._hundreds = None
        self._thousands = None
        super(FourDigitsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getTens(self):
        return self._tens

    def getOnes(self):
        return self._ones

    def getHundreds(self):
        return  self._hundreds

    def getThousands(self):
        return  self._thousands

    def draw4(self, drawer, images, number, padding_zero = False):
        assert(type(images) == list)
        assert(type(number) == int)

        if number > 9999:
            number = number % 10000

        if self.getOnes():
            if padding_zero or int(number / 1000) > 0:
                self.getOnes().draw3(drawer, images, int(number / 1000))
        if self.getTens():
            if padding_zero or (int(number / 1000) > 0 or int(number % 1000 / 100) > 0):
                self.getTens().draw3(drawer, images, int(number % 1000 / 100))
        if self.getHundreds():
            if padding_zero or (int(number / 1000) > 0 or int(number % 1000 / 100) > 0 or int(number % 1000 % 100 / 10) > 0):
                self.getHundreds().draw3(drawer, images, int(number % 1000 % 100 / 10))
        if self.getThousands():
            self.getThousands().draw3(drawer, images, int(number % 1000 % 100 % 10))

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            pass
        if parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._thousands = ImageSetElement(parameter, self, 'Thousands')
            return self._thousands
        if parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._hundreds = ImageSetElement(parameter, self, 'Hundreds')
            return self._hundreds
        if parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._tens = ImageSetElement(parameter, self, 'Tens')
            return self._tens
        elif parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._ones = ImageSetElement(parameter, self, 'Ones')
            return self._ones
        elif parameterId == 6:
            pass
        elif parameterId == 7: # nodata
            pass
        else:
            super(FourDigitsElement, self).createChildForParameter(parameter)
