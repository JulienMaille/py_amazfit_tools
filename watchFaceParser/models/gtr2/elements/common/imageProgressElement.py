import logging

from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
from watchFaceParser.config import Config


class ImageProgressElement(CoordinatesElement):
    def __init__(self, parameter, parent, name=None):
        self._coordinates = []
        self._imageSet = None
        self._displayType = None
        super(ImageProgressElement, self).__init__(parameter=parameter, parent=parent, name=name)

    def getCoordinates(self):
        return self._coordinates

    def getImageSet(self):
        return self._imageSet

    def getDisplayType(self):
        return self._displayType

    def drawImageProgressElement(self, drawer, resources, state):
        self.draw2(drawer, resources, state)

    def draw2(self, drawer, images, state):
        initial = 0
        number = state[0]
        maxnumber = state[1]
        count = self.getImageSet().getImagesCount() - 1

        s = int(number / (maxnumber / count))
        if s > count:
            s = count

        if not self.getDisplayType():
            initial = s
        for i in range(initial, s + 1):
            x = self.getCoordinates()[i].getX() if i < len(self.getCoordinates()) else self.getCoordinates()[-1].getX()
            y = self.getCoordinates()[i].getY() if i < len(self.getCoordinates()) else self.getCoordinates()[-1].getY()
            imageIndex = self.getImageSet().getImageIndex() + i - Config.getStartImageIndex()
            temp = images[imageIndex].getBitmap()
            print(x, y, imageIndex, state)
            drawer.paste(temp, (x, y), temp)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.common.coordinatesElement import CoordinatesElement
            self._coordinates.append(CoordinatesElement(parameter, self, 'Coordinates'))
            return self._coordinates
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.common.imageSetGTR2Element import ImageSetGTR2Element
            self._imageSet = ImageSetGTR2Element(parameter, self, name='ImageSet')
            return self._imageSet
        elif parameterId == 3:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._displayType = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='DisplayType')
        else:
            super(ImageProgressElement, self).createChildForParameter(parameter)
