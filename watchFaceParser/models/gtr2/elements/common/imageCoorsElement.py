import logging

from watchFaceParser.config import Config

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class ImageCoordsElement(ContainerElement):
    def __init__(self, parameter, parent, name=None):
        self._coordinates = None
        self._imageIndex = None
        self._imageIndex2 = None
        self._imageIndex3 = None
        super(ImageCoordsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getCoordinates(self):
        return self._coordinates

    def getImageIndex(self):
        return self._imageIndex

    def getImageIndex2(self):
        return self._imageIndex2

    def getImageIndex3(self):
        return self._imageIndex3

    def drawImageCoordsElement(self, drawer, resources, state):
        self.draw3(drawer, resources, state)

    def draw3(self, drawer, resources, state):
        if not self.getImageIndex():
            return
        image_index = self.getImageIndex()-Config.getStartImageIndex()
        temp = resources[image_index].getBitmap()
        x = 0 if self.getCoordinates() is None or self.getCoordinates().getX() is None else self.getCoordinates().getX()
        y = 0 if self.getCoordinates() is None or self.getCoordinates().getY() is None else self.getCoordinates().getY()
        drawer.paste(temp, (x, y), temp)

    def draw2(self, drawer, images, angle, center = None):
        x = 0 if self.getCoordinates() is None or self.getCoordinates().getX() is None else self.getCoordinates().getX()
        y = 0 if self.getCoordinates() is None or self.getCoordinates().getY() is None else self.getCoordinates().getY()

        image_index = self.getImageIndex()-Config.getStartImageIndex()

        if angle is None:
            temp = images[image_index].getBitmap()
            drawer.paste(temp, (x,y), temp)
        else:
            bitmap = images[image_index].getBitmap()
            from PIL import Image

            temp = Image.new('RGBA', Config.getImageSize())
            temp.paste(bitmap, (Config.getImageSizeHalf()[0] - x, Config.getImageSizeHalf()[1] - y), bitmap)
            temp = temp.rotate(angle)

            if center is None:
                drawer.paste(temp, (0,0), temp)
            else:
                width, height = temp.size
                drawer.paste(temp, ( int(center[0] - width / 2), int(center[1] - height / 2)), temp)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.common.coordinatesElement import CoordinatesElement
            self._coordinates = CoordinatesElement(parameter, self, 'Coordinates')
            return self._coordinates
        elif parameter.getId() == 2:
            self._imageIndex = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, '?ImageIndex?')
        elif parameter.getId() == 3:
            self._imageIndex2 = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, '?ImageIndex2?')
        elif parameter.getId() == 4:
            self._imageIndex3 = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, '?ImageIndex3?')
        else:
            super(ImageCoordsElement, self).createChildForParameter(parameter)
