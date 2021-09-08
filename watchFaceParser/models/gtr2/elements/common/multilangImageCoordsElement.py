import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement
from watchFaceParser.config import Config


class MultilangImageCoordsElement(ContainerElement):
    def __init__(self, parameter, parent, name = None):
        self._coordinates = None
        self._imageSet = []
        super(MultilangImageCoordsElement, self).__init__(parameters=None, parameter = parameter, parent = parent, name = name)

    def getCoordinates(self):
        return self._coordinates

    def getImageSet(self):
        return self._imageSet

    def getImageSetForLang(self, lang = 0):
        for i in self._imageSet:
            if i.getLandCode() == lang:
                return i
        return self._imageSet[0]

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.common.coordinatesElement import CoordinatesElement
            self._coordinates = CoordinatesElement(parameter, self, 'Coordinates')
            return self._coordinates
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.common.multilangImageElement import MultilangImageElement
            self._imageSet.append(MultilangImageElement(parameter, parent = self, name = 'ImageSet'))
            return self._imageSet
        else:
            super(MultilangImageCoordsElement, self).createChildForParameter(parameter)
