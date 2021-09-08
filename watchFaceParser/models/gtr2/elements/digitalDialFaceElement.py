import logging

from watchFaceParser.models.gtr2.elements.basic.containerElement import ContainerElement
from watchFaceParser.models.gtr2.elements.common.followObject import FollowObject


class DigitalDialFaceElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._digits = []
        self._am = None
        self._pm = None
        super(DigitalDialFaceElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getDigits(self):
        return self._digits

    def getAm(self):
        return self._am

    def getPm(self):
        return self._pm

    def drawDigitalDialFaceElement(self, drawer, images, state):
        self.draw3(drawer, images, state)

    def draw3(self, drawer, images, state):
        assert(type(images) == list)

        if self.getDigits():
            follow_object = FollowObject()
            for d in self.getDigits():
                follow_object = d.drawDigitalTimeDigitElement(drawer, images, state,
                                                              (self.getAm() or self.getPm()),
                                                              follow_object)
        if self.getAm():
            self.getAm().drawAmMultilangImageCoordsElement(drawer, images, state)
        if self.getPm():
            self.getPm().drawPmMultilangImageCoordsElement(drawer, images, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.common.digitalTimeDigitElement import DigitalTimeDigitElement
            self._digits.append(DigitalTimeDigitElement(parameter, parent = self, name = 'Digits'))
            return self._digits
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.common.amMultilangImageCoordsElement import AmMultilangImageCoordsElement
            self._am = AmMultilangImageCoordsElement(parameter = parameter, parent = self, name = 'AM')
            return self._am
        elif parameterId == 3:
            from watchFaceParser.models.gtr2.elements.common.pmMultilangImageCoordsElement import PmMultilangImageCoordsElement
            self._pm = PmMultilangImageCoordsElement(parameter=parameter, parent = self, name = 'PM')
            return self._pm
        else:
            print ("Unknown DigitalDialFaceElement",parameterId)
            return super(DigitalDialFaceElement, self).createChildForParameter(parameter)

