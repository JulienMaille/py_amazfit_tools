import logging

from watchFaceParser.models.elements.common.coordinatesElement import CoordinatesElement
from watchFaceParser.config import Config


class ProgressBarElement(CoordinatesElement):
    def __init__(self, parameter, parent, name=None):
        self._angleSettings = None
        self._linearSettings = None
        self._foregroundImageIndex = None
        self._color = None
        self._width = None
        self._flatness = None
        self._pointerImageIndex = None
        self._backgroundImageIndex = None
        super(ProgressBarElement, self).__init__(parameter=parameter, parent=parent, name=name)

    def getAngleSettings(self):
        return self._angleSettings

    def getLinearSettings(self):
        return self._linearSettings

    def getForegroundImageIndex(self):
        return self._foregroundImageIndex

    def getColor(self):
        return self._color

    def getWidth(self):
        return self._width

    def getFlatness(self):
        return self._flatness

    def getPointerImageIndex(self):
        return self._pointerImageIndex

    def getBackgroundImageIndex(self):
        return self._backgroundImageIndex

    def drawProgressBarElement(self, drawer, images, value, total):
        if self.getAngleSettings():
            self.getAngleSettings().drawAngleSettingsElement(drawer, images, value, total,
                                          self.getWidth(),
                                          self.getForegroundImageIndex(),
                                          self.getColor(),
                                          self.getFlatness(),
                                          self.getPointerImageIndex(),
                                          self.getBackgroundImageIndex()
                                          )
        if self.getLinearSettings():
            self.getLinearSettings().drawLinearSettingsElement(drawer, images, value, total,
                                           self.getWidth(),
                                           self.getForegroundImageIndex(),
                                           self.getColor(),
                                           self.getFlatness(),
                                           self.getPointerImageIndex(),
                                           self.getBackgroundImageIndex()
                                           )

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.common.angleSettingsElement import AngleSettingsElement
            self._angleSettings = AngleSettingsElement(parameter, self, name='AngleSettings')
            return self._angleSettings
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.common.linearSettingsElement import LinearSettingsElement
            self._linearSettings = LinearSettingsElement(parameter, self, name='LinearSettings')
            return self._linearSettings
        elif parameterId == 3:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._foregroundImageIndex = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='ForegroundImageIndex')
        elif parameterId == 4:
            from resources.image.color import Color
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._color = Color.fromArgb(0xff000000 | parameter.getValue())
            return ValueElement(parameter=parameter, parent=self, name='Color')
        elif parameterId == 5:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._width = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='Width')
        elif parameterId == 6:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._flatness = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='Flatness')
        elif parameterId == 7:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._pointerImageIndex = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='PointerImageIndex')
        elif parameterId == 8:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._backgroundImageIndex = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='BackgroundImageIndex')
        else:
            super(ProgressBarElement, self).createChildForParameter(parameter)
