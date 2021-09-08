import logging

from watchFaceParser.models.gtr2.elements.basic.containerElement import ContainerElement
from watchFaceParser.config import Config
from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
from resources.image.color import Color

class BackgroundElement(ContainerElement):
    def __init__(self, parameter, parent=None, name=None):
        self._backgroundImageIndex = None
        self._color = None
        super(BackgroundElement, self).__init__(parameters=None, parameter=parameter, parent=parent, name=name)

    def getBackgroundImageIndex(self):
        return self._backgroundImageIndex

    def getColor(self):
        return self._color

    def drawBackgroundElement(self, drawer, resources, state):
        self.draw3(drawer, resources, state)

    def draw3(self, drawer, resources, state):
        self.draw2(drawer, resources, None)

    def draw2(self, drawer, images, angle, center=None):
        x = 0
        y = 0

        from PIL import ImageDraw, Image

        if self._backgroundImageIndex is None:
            if self._color is None:
                self._color = Color.fromArgb(0xff000000)
            size = Config.getImageSize()
            d = ImageDraw.Draw(drawer)
            d.rectangle([(x, y), size], fill=self.getColor())
        else:
            temp = images[self._backgroundImageIndex].getBitmap()
            drawer.paste(temp, (x, y), temp)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            pass
        elif parameterId == 2:
            self._backgroundImageIndex = parameter.getValue() - Config.getStartImageIndex()
            return ValueElement(parameter, self, '?ImageIndex?')
        elif parameterId == 3:
            self._color = Color.fromArgdBackground(0xff0000 | parameter.getValue())
            return ValueElement(parameter = parameter, parent = self, name = '?_color?')
        else:
            return super(BackgroundElement, self).createChildForParameter(parameter)
