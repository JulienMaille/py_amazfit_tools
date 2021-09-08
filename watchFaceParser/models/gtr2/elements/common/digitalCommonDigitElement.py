import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement
from watchFaceParser.models.gtr2.elements.common.followObject import FollowObject


class DigitalCommonDigitElement(ContainerElement):
    def __init__(self, parameter, parent, name=None):
        self._type = None
        self._combingMode = None
        self._digit = None
        self._separator = None
        super(DigitalCommonDigitElement, self).__init__(parameters=None, parameter=parameter, parent=parent, name=name)

    def getType(self):
        return self._type

    def getCombingMode(self):
        return self._combingMode

    def getDigit(self):
        return self._digit

    def getSeparator(self):
        return self._separator

    def drawDigitalCommonDigitElement(self,
                                      drawer,
                                      images,
                                      number,
                                      number_min=None,
                                      number_max=None,
                                      minimum_digits=1,
                                      padding_zero_length=1,
                                      unit=('', '', ''),
                                      follow_object=FollowObject()):
        assert (type(images) == list)

        number = number_max if self._type == 2 else number_min if self._type == 1 else number
        separator = False

        if self.getSeparator():
            separator = True
            if self._separator.getImageIndex():
                self.getSeparator().drawImageCoordsElement(drawer, images, None)
        if self.getDigit():
            if self._combingMode == 1:
                follow_object = FollowObject(text=follow_object.getText())
            follow_object._combing = self._combingMode
            return self.getDigit().drawTextElement(drawer,
                                                   images,
                                                   number,
                                                   minimum_digits,
                                                   padding_zero_length,
                                                   follow_object,
                                                   padding_zero=None,
                                                   unit=unit,
                                                   check_display_form_analog=False,
                                                   separator=separator)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._type = parameter.getValue()
            return ValueElement(parameter, self, 'Type')
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
            super(DigitalCommonDigitElement, self).createChildForParameter(parameter)
