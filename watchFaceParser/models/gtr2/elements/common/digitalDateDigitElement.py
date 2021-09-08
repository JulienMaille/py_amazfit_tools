import logging
from typing import Optional

from watchFaceParser.config import Config

from watchFaceParser.models.elements.basic.containerElement import ContainerElement
from watchFaceParser.models.gtr2.elements.common.followObject import FollowObject


class DigitalDateDigitElement(ContainerElement):
    def __init__(self, parameter, parent, name=None):
        self._dateType = None
        self._combingMode = None
        self._digit = None
        self._separator = None
        super(DigitalDateDigitElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getDateType(self):
        return self._dateType

    def getCombingMode(self):
        return self._combingMode

    def getDigit(self):
        return self._digit

    def getSeparator(self):
        return self._separator
    
    def drawDigitalDateDigitElement(self, drawer, resources, state, follow_object) -> Optional[FollowObject]:
        assert(type(resources) == list)

        unit = ('', '/', '.')
        separator = False

        if self.getSeparator():
            separator = True
            if self._separator.getImageIndex():
                self.getSeparator().draw3(drawer, resources, state)

        if self.getDigit():

            if self._combingMode == 1:
                follow_object = FollowObject(text=follow_object.getText())
            follow_object._combing = self._combingMode

            if self._dateType is None or self._dateType == 0:
                #
                #  weird logic from Huami (GTS2):
                #   PaddingZero = true -> year has only 2 digits
                #   PaddingZero = false -> year has 4 digits
                #
                if self.getDigit().getPaddingZero():
                    return self.getDigit().drawTextElement(drawer, resources, state.getTime().year % 2000,
                                                           minimum_digits=2,
                                                           padding_zero_length=2,
                                                           follow_object=follow_object,
                                                           padding_zero=None,
                                                           unit=unit,
                                                           separator=separator)
                else:
                    return self.getDigit().drawTextElement(drawer, resources, state.getTime().year,
                                                           minimum_digits=4,
                                                           padding_zero_length=4,
                                                           follow_object=follow_object,
                                                           padding_zero=None,
                                                           unit=unit,
                                                           separator=separator)
            if self._dateType == 1:
                return self.getDigit().drawTextElement(drawer,
                                                       resources,
                                                       state.getTime().month,
                                                       minimum_digits=2,
                                                       padding_zero_length=2,
                                                       follow_object=follow_object,
                                                       padding_zero=None,
                                                       unit=unit,
                                                       separator=separator)
            if self._dateType == 2:
                return self.getDigit().drawTextElement(drawer, resources, state.getTime().day,
                                                       minimum_digits=2,
                                                       padding_zero_length=2,
                                                       follow_object=follow_object,
                                                       padding_zero=None,
                                                       unit=unit,
                                                       separator=separator)
        return None

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._dateType = parameter.getValue()
            return ValueElement(parameter, self, 'TimeType')
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._combingMode = parameter.getValue()
            return ValueElement(parameter, self, 'CombingMode')
        elif parameterId == 3:
            from watchFaceParser.models.gtr2.elements.common.textElement import TextElement
            self._digit = TextElement(parameter = parameter, parent = self, name = 'Digit')
            return self._digit
        elif parameterId == 4:
            from watchFaceParser.models.gtr2.elements.common.imageCoorsElement import ImageCoordsElement
            self._separator = ImageCoordsElement(parameter = parameter, parent = self, name = 'Separator')
            return self._separator
        else:
            super(DigitalDateDigitElement, self).createChildForParameter(parameter)
