import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
from watchFaceParser.config import Config

class ClockHandElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._x = 0
        self._y = 0
        self._scale = None
        self._pointer = None # pointerX, pointerY - rotateCenter
        self._cover = None
        self._startAngle = 0
        self._endAngle = 0
        super(ClockHandElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getX(self):
        return self._x if self._x else int(Config.getImageSize()[0]/2) # if None or 0 - set to Center

    def getY(self):
        return self._y if self._y else int(Config.getImageSize()[1]/2) # if None or 0 - set to Center

    def getScale(self):
        return self._scale

    def getPointer(self):
        return self._pointer

    def getCover(self):
        return self._cover

    def getStartAngle(self):
        return self._startAngle

    def getEndAngle(self):
        return self._endAngle

    def drawClockHandElement(self, drawer, resources, value, total):
        assert(type(resources) == list)

        if value > total:
            value = total

        if self._x is None:
            self._x = 0

        if self._y is None:
            self._y = 0

        if self.getScale():
            dX = 0 if self.getScale().getCoordinates() is None or self.getScale().getCoordinates().getX() is None else self.getScale().getCoordinates().getX()
            dY = 0 if self.getScale().getCoordinates() is None or self.getScale().getCoordinates().getY() is None else self.getScale().getCoordinates().getY()

            scaleImageIndex = self.getScale().getImageSetForLang(2).getImageSet().getImageIndex()
            temp = resources[scaleImageIndex - Config.getStartImageIndex()].getBitmap()
            drawer.paste(temp, (dX, dY), temp)

        _startAngle = 0
        _endAngle = 360
        if self.getStartAngle():
            _startAngle = self.getStartAngle()
        if self.getEndAngle():
            _endAngle = self.getEndAngle()

        #print ("_startAngle",_startAngle, "_endAngle",_endAngle)

        if self.getPointer():
            angle = 360 - _startAngle - int(value * (_endAngle - _startAngle ) / total)
            #print ("value", value, "total",total,"angle",angle)
            center = (self.getX(), self.getY()) if self.getX() is not None and self.getY() is not None else None
            self.getPointer().draw2(
                drawer, resources,
                angle,
                center)

        if self.getCover():
            dX = 0 if self.getCover().getCoordinates() is None or self.getCover().getCoordinates().getX() is None else self.getCover().getCoordinates().getX()
            dY = 0 if self.getCover().getCoordinates() is None or self.getCover().getCoordinates().getX() is None else self.getCover().getCoordinates().getY()

            coverImageIndex = self.getCover().getImageIndex()
            if coverImageIndex:
                temp = resources[coverImageIndex - Config.getStartImageIndex()].getBitmap()
                drawer.paste(temp, (dX, dY), temp)

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
            from watchFaceParser.models.gtr2.elements.common.multilangImageCoordsElement import MultilangImageCoordsElement
            self._scale = MultilangImageCoordsElement(parameter = parameter, parent = self, name = 'Scale')
            return self._scale
        if parameterId == 4:
            from watchFaceParser.models.gtr2.elements.common.imageCoorsElement import ImageCoordsElement
            self._pointer = ImageCoordsElement(parameter = parameter, parent = self, name = 'Pointer')
            return self._pointer
        elif parameterId == 5:
            from watchFaceParser.models.gtr2.elements.common.imageCoorsElement import ImageCoordsElement
            self._cover = ImageCoordsElement(parameter = parameter, parent = self, name = 'Cover')
            return self._cover
        elif parameterId == 6:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._startAngle = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'StartAngle')
        elif parameterId == 7:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._endAngle = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'EndAngle')
        else:
            return super(ClockHandElement, self).createChildForParameter(parameter)

