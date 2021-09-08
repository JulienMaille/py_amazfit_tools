import logging

from watchFaceParser.models.gtr2.elements.basic.containerElement import ContainerElement


class ScreenNormalElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._digitaldialface = None
        self._analogdialface = None
        self._progressdialface = None
        super(ScreenNormalElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getDigitalDialFace(self):
        return self._digitaldialface


    def getAnalogDialFace(self):
        return self._analogdialface


    def getProgressDialFace(self):
        return self._progressdialface

    def drawScreenNormalElement(self, drawer, images, state):
        self.draw3(drawer, images, state)

    def draw3(self, drawer, images, state):
        if self.getDigitalDialFace():
            self.getDigitalDialFace().drawDigitalDialFaceElement(drawer, images, state)
        if self.getProgressDialFace():
            self.getProgressDialFace().drawProgressDialFaceElement(drawer, images, state)
        if self.getAnalogDialFace():
            self.getAnalogDialFace().drawAnalogDialElement(drawer, images, state)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.digitalDialFaceElement import DigitalDialFaceElement
            self._digitaldialface = DigitalDialFaceElement(parameter = parameter, parent = self, name = 'DigitalDialFace')
            return self._digitaldialface
        elif parameterId == 2:
            pass
            from watchFaceParser.models.gtr2.elements.analogDialElement import AnalogDialElement
            self._analogdialface = AnalogDialElement(parameter = parameter, parent = self, name = 'AnalogDialFace')
            return self._analogdialface
        elif parameterId == 3:
            pass
            from watchFaceParser.models.gtr2.elements.progressDialFaceElement import ProgressDialFaceElement
            self._progressdialface = ProgressDialFaceElement(parameter = parameter, parent = self, name = 'ProgressDialFace')
            return self._progressdialface
        else:
            print ("Unknown ScreenNormalElement",parameterId)
            return super(ScreenNormalElement, self).createChildForParameter(parameter)

