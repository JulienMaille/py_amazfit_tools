import logging
from typing import Optional

from watchFaceParser.config import Config

from watchFaceParser.models.elements.basic.containerElement import ContainerElement
from watchFaceParser.models.gtr2.elements.common.followObject import FollowObject


class DigitalTimeDigitElement(ContainerElement):
    def __init__(self, parameter, parent, name=None):
        self._timeType = None
        self._combingMode = None
        self._digit = None
        self._separator = None

        super(DigitalTimeDigitElement, self).__init__(parameters=None, parameter=parameter, parent=parent, name=name)

    def getTimeType(self):
        return self._timeType

    def getCombingMode(self):
        return self._combingMode

    def getDigit(self):
        return self._digit

    def getSeparator(self):
        return self._separator

    def drawDigitalTimeDigitElement(self, drawer, resources, state, ampm: bool, follow_object: FollowObject) -> Optional[FollowObject]:
        assert (type(resources) == list)

        unit = ('', '/', ':')
        separator = False

        if self.getSeparator():
            separator = True
            if self._separator.getImageIndex():
                self.getSeparator().draw3(drawer, resources, state)

        if self.getDigit():
            if self._combingMode == 1:
                follow_object = FollowObject(text=follow_object.getText())
            follow_object._combing = self._combingMode

            if self._timeType is None or self._timeType == 0:
                hours = state.getTime().hour if not ampm else state.getTime().hour % 12
                return self.getDigit().drawTextElement(drawer, resources, hours,
                                                       minimum_digits=2,
                                                       padding_zero_length=2,
                                                       follow_object=follow_object,
                                                       unit=unit,
                                                       separator=separator)
            elif self._timeType == 1:
                minutes = state.getTime().minute
                return self.getDigit().drawTextElement(drawer, resources, minutes,
                                                       minimum_digits=2,
                                                       padding_zero_length=2,
                                                       follow_object=follow_object,
                                                       padding_zero=True,
                                                       unit=unit,
                                                       separator=separator)
            elif self._timeType == 2:
                if not state.getScreenIdle():
                    seconds = state.getTime().second
                    return self.getDigit().drawTextElement(drawer, resources, seconds,
                                                           minimum_digits=2,
                                                           padding_zero_length=2,
                                                           follow_object=follow_object,
                                                           unit=unit,
                                                           padding_zero=True)
        return follow_object

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._timeType = parameter.getValue()
            return ValueElement(parameter, self, 'TimeType')
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._combingMode = parameter.getValue()
            return ValueElement(parameter, self, 'CombingMode')
        elif parameterId == 3:
            from watchFaceParser.models.gtr2.elements.common.textElement import TextElement
            self._digit = TextElement(parameter=parameter, parent=self, name='Digit')
            return self._digit
        elif parameterId == 4:
            from watchFaceParser.models.gtr2.elements.common.imageCoorsElement import ImageCoordsElement
            self._separator = ImageCoordsElement(parameter=parameter, parent=self, name='Separator')
            return self._separator
        else:
            super(DigitalTimeDigitElement, self).createChildForParameter(parameter)
