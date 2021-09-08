import logging
from watchFaceParser.config import Config

from watchFaceParser.models.gtr2.elements.basic.compositeElement import CompositeElement
from watchFaceParser.models.gtr2.elements.common.multilangImageElement import MultilangImageElement
from watchFaceParser.helpers.drawerHelper import DrawerHelper

class WidgetContainerElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._x = None
        self._y = None
        self._width = None
        self._height = None
        self._widgetElement = []
        self._borderActivImageIndex = None
        self._borderInactivImageIndex = None
        self._descriptionImageBackground = None
        self._descriptionWidthCheck = None
        super(WidgetContainerElement, self).__init__(parameters=None, parameter = parameter, parent = parent, name = name)

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def getWidgetElement(self):
        return self._widgetElement

    def getBorderActivImageIndex(self):
        return self._borderActivImageIndex

    def getBorderInactivImageIndex(self):
        return self._borderInactivImageIndex

    def getDescriptionImageBackground(self):
        return self._descriptionImageBackground

    def getDescriptionWidthCheck(self):
        return self._descriptionWidthCheck

    def drawWidgetContainerElement(self, drawer, images, state):
        self.draw3(drawer, images, state)

    def draw3(self, drawer, images, state):
        if self.getWidgetElement():
            #for w in self.getWidgetElement():
            #    w.draw3(drawer, images, state)
            # draw only first widget
            self.getWidgetElement()[0].drawWidgetElement(drawer, images, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._x = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'X')
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._y = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'Y')
        elif parameterId == 3:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._width = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'Width')
        elif parameterId == 4:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._height = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'Height')
        elif parameterId == 5:
            from watchFaceParser.models.gtr2.elements.common.widgetElement import WidgetElement
            self._widgetElement.append(WidgetElement(parameter = parameter, parent = self, name = 'WidgetElement'))
            return self._widgetElement
        elif parameterId == 6:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._borderActivImageIndex = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'BorderActivImageIndex')
        elif parameterId == 7:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._borderInactivImageIndex = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'BorderInactivImageIndex')
        elif parameterId == 8:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._descriptionImageBackground = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'DescriptionImageBackground')
        elif parameterId == 9:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._descriptionWidthCheck = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'DescriptionWidthCheck')
        else:
            super(WidgetContainerElement, self).createChildForParameter(parameter)
