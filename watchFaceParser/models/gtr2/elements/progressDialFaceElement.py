import logging

from watchFaceParser.models.gtr2.elements.basic.containerElement import ContainerElement


class ProgressDialFaceElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._progressBar = None
        super(ProgressDialFaceElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getProgressBar(self):
        return self._progressBar

    def drawProgressDialFaceElement(self, drawer, images, state):
        self.draw3(drawer, images, state)

    def draw3(self, drawer, images, state):
        if self.getProgressBar():
            value = state.getTime().hour % 12 + state.getTime().minute / 60.
            maxvalue = 12
            self.getProgressBar().drawProgressBarElement(self, drawer, images, value, maxvalue)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.common.progressBarElement import ProgressBarElement
            self._progressBar.append(ProgressBarElement(parameter, parent = self, name = 'ProgressBar'))
            return self._progressBar
        else:
            print ("Unknown ProgressDialFaceElement",parameterId)
            return super(ProgressDialFaceElement, self).createChildForParameter(parameter)

