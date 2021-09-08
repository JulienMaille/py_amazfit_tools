import logging

from watchFaceParser.config import Config

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class MultilangImageElement(ContainerElement):
    def __init__(self, parameter, parent, name=None):
        self._landCode = None
        self._imageSet = None
        super(MultilangImageElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getLandCode(self):
        return self._landCode

    def getImageSet(self):
        return self._imageSet

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._landCode = parameter.getValue()
            return ValueElement(parameter, self, 'LandCode')
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.common.imageSetGTR2Element import ImageSetGTR2Element
            self._imageSet = ImageSetGTR2Element(parameter, self, name='ImageSet')
            return self._imageSet
        else:
            super(MultilangImageElement, self).createChildForParameter(parameter)
