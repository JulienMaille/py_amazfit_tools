import logging

from watchFaceParser.config import Config

from watchFaceParser.models.elements.basic.containerElement import ContainerElement
from watchFaceParser.helpers.drawerHelper import DrawerHelper
from watchFaceParser.models.gtr2.elements.common.followObject import FollowObject


class SystemFontElement(ContainerElement):
    def __init__(self, parameter, parent, name=None):
        self._fontRotate = None
        self._coordinates = None
        self._angle = None
        self._size = None
        self._color = None
        self._showUnitCheck = None
        super(SystemFontElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getFontRotate(self):
        return self._fontRotate

    def getCoordinates(self):
        return self._coordinates

    def getAngle(self):
        return 0 if self._angle is None else self._angle

    def getSize(self):
        return 10 if self._size is None else self._size
    
    def getColor(self):
        return (0) if self._color is None else self._color

    def getShowUnitCheck(self):
        return self._showUnitCheck

    def drawSystemFont(self,
                       drawer,
                       number,
                       spacing=1,
                       padding_zero=False,
                       minimum_digits=1,
                       unit=('', '', ''),
                       separator=False,
                       follow_object=FollowObject()) -> FollowObject:

        string_number = number if isinstance(number, str) else str(abs(number))
        if padding_zero:
            string_number = string_number.zfill(minimum_digits)
        if not isinstance(number, str) and number < 0:
            string_number = '-' + string_number
        if self._showUnitCheck == -1:
            string_number = string_number + unit[0]
        elif self._showUnitCheck == 1:
            string_number = string_number + unit[1]
        elif self._showUnitCheck == 2:
            string_number = string_number + unit[2]
        if separator:
            string_number = string_number + "/"

        string_number = follow_object.getText() + string_number

        if follow_object:
            if follow_object.getCombing() != 1:
                self._size = follow_object.getSize()
                self._color = follow_object.getColor()
            else:
                follow_object.setSize(self.getSize())
                follow_object.setColor(self.getColor())

        if self.getFontRotate():
            follow_object = self.getFontRotate().drawFontRotateElement(drawer, string_number, self.getAngle(), self.getSize(), self.getColor(), spacing, follow_object)
        else:
            follow_object = self.drawLinear(drawer, string_number, follow_object, spacing)

        follow_object.setText(string_number)

        return follow_object
    
    def drawLinear(self, drawer, string_number, follow_object: FollowObject, spacing=0):
        x = self.getCoordinates().getX()
        y = self.getCoordinates().getY()
        if follow_object:
            if follow_object.getCombing() == 1:
                follow_object.setX(self.getCoordinates().getX())
                follow_object.setY(self.getCoordinates().getY())
                follow_object.setAngle(self.getAngle())
            else:
                x = follow_object.getX()
                y = follow_object.getY()
                self._angle = follow_object.getAngle()

        from PIL import ImageDraw, Image, ImageFont
        import os
        font_path = os.path.dirname(os.path.realpath(__file__))
        font_path = os.path.abspath(os.path.join(font_path, os.pardir, os.pardir, os.pardir, os.pardir, os.pardir))
        font_path = os.path.abspath(os.path.join(font_path, "font", "roboto-condensed.regular.ttf"))
        #print(font_path)
        font = ImageFont.truetype(font_path, self.getSize())

        text_size = ImageDraw.Draw(drawer).textsize(string_number, font=font)
        temp = Image.new('RGBA', (text_size[0]*4,text_size[0]*4), (0, 0, 0, 0))
        draw = ImageDraw.Draw(temp)
        draw.text(( text_size[0] * 2, text_size[0]*2 - text_size[1]), string_number,
                  fill=self.getColor(),
                  font=font,
                  anchor=None,
                  spacing=spacing,
                  align='left',
                  direction=None,
                  features=None,
                  language=None,
                  stroke_width=0,
                  stroke_fill=None,
                  embedded_color=False)
        if self._angle:
            temp = temp.rotate(-self._angle, expand=1)
        if self.getCoordinates():
            w, h = temp.size
            drawer.paste(temp, (x-int(w/2), y-int(h/2)), temp)



        return follow_object

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.common.fontRotateElement import FontRotateElement
            self._fontRotate = FontRotateElement(parameter, self, name='FontRotate')
            return self._fontRotate
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.common.coordinatesElement import CoordinatesElement
            self._coordinates = CoordinatesElement(parameter, self, 'Coordinates')
            return self._coordinates
        elif parameterId == 3:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._angle = parameter.getValue()
            return ValueElement(parameter, self, 'Angle')
        elif parameterId == 4:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._size = parameter.getValue()
            return ValueElement(parameter, self, 'Size')
        elif parameterId == 5:
            from resources.image.color import Color
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._color = Color.fromArgb(0xff000000 | parameter.getValue())
            return ValueElement(parameter=parameter, parent=self, name='Color')
        elif parameterId == 6:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._showUnitCheck = parameter.getValue()
            return ValueElement(parameter, self, 'ShowUnitCheck')
        else:
            super(SystemFontElement, self).createChildForParameter(parameter)
