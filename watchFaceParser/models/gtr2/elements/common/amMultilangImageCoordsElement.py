import logging

from watchFaceParser.models.gtr2.elements.common.multilangImageCoordsElement import MultilangImageCoordsElement
from watchFaceParser.config import Config


class AmMultilangImageCoordsElement(MultilangImageCoordsElement):
    def __init__(self, parameter, parent, name = None):
        super(AmMultilangImageCoordsElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def drawAmMultilangImageCoordsElement(self, drawer, resources, state):
        assert(type(resources) == list)

        x = 0 if self.getCoordinates() is None or self.getCoordinates().getX() is None else self.getCoordinates().getX()
        y = 0 if self.getCoordinates() is None or self.getCoordinates().getY() is None else self.getCoordinates().getY()

        if state.getTime().hour < 12:
            image_index = self.getImageSetForLang(2).getImageSet().getImageIndex()-1
            temp = resources[image_index].getBitmap()
            
            drawer.paste(temp, (x, y), temp)
