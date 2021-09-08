import logging

from watchFaceParser.models.gtr2.elements.basic.containerElement import ContainerElement


class WidgetsElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._widgets = []
        self._topMaskImageIndex = None
        self._underMaskImageIndex = None
        super(WidgetsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getWidgets(self):
        return self._widgets

    def getTopMaskImageIndex(self):
        return self._topMaskImageIndex

    def getUnderMaskImageIndex(self):
        return self._underMaskImageIndex

    def drawWidgetsElement(self, drawer, images, state):
        self.draw3(drawer, images, state)

    def draw3(self, drawer, images, state):
        if self.getWidgets():
            for w in self.getWidgets():
                w.drawWidgetContainerElement(drawer, images, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.common.widgetContainerElement import WidgetContainerElement
            self._widgets.append(WidgetContainerElement(parameter = parameter, parent = self, name = 'Widget'))
            return self._widgets
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._topMaskImageIndex = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='TopMaskImageIndex')
        elif parameterId == 3:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._underMaskImageIndex = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='UnderMaskImageIndex')
        else:
            print ("Unknown SystemElement",parameterId)
            return super(WidgetsElement, self).createChildForParameter(parameter)

