import logging

from watchFaceParser.models.gtr2.elements.basic.compositeElement import CompositeElement
from watchFaceParser.models.gtr2.elements.common.followObject import FollowObject

class FontRotateElement(CompositeElement):
    def __init__(self, parameter, parent, name=None):
        self._x = None
        self._y = None
        self._radius = None
        self._rotateDirection = None

        super(FontRotateElement, self).__init__(parameters=None, parameter=parameter, parent=parent, name=name)

    def getX(self):
        return 0 if self._x is None else self._x

    def getY(self):
        return 0 if self._y is None else self._y

    def getRadius(self):
        return 0 if self._radius is None else self._radius

    def getRotateDirection(self):
        return self._rotateDirection

    def drawFontRotateElement(self, drawer, string_number, start_angle, size, color, spacing, follow_object: FollowObject):
        spacing = 0 if spacing is None else spacing
        if follow_object:
            if follow_object.getCombing() != 1:
                self._x = follow_object.getX()
                self._y = follow_object.getY()
                self._radius = follow_object.getRadius()
                start_angle = follow_object.getAngle()
            else:
                follow_object.setX(self.getX())
                follow_object.setY(self.getY())
                follow_object.setAngle(start_angle)
                follow_object.setRadius(self._radius)

        temp = self.drawText(string_number, size, color, spacing, start_angle)
        if temp:
            (wt, ht) = temp.size
            drawer.paste(temp, (self.getX() - int(wt / 2), self.getY() - int(ht / 2)), temp)
        return follow_object

    def drawText(self, text, size, color, spacing=0, startAngle=0):
        from PIL import ImageDraw, Image, ImageFont, ImageOps
        import math

        import os
        font_path = os.path.dirname(os.path.realpath(__file__))
        font_path = os.path.abspath(os.path.join(font_path, os.pardir, os.pardir, os.pardir, os.pardir, os.pardir))
        font_path = os.path.abspath(os.path.join(font_path, "font", "roboto-condensed.regular.ttf"))
        font = ImageFont.truetype(font_path, size)

        iw = self.getRadius() * 4
        ih = self.getRadius() * 4
        temp = Image.new('RGBA', (iw, ih), (0, 0, 0, 0))
        x = int(iw / 2)
        y = int(ih / 2)

        clockwise = False if self._rotateDirection == 1 else True

        initial_angle = -startAngle # revers initial angle
        angle = 0

        print( (x,y), "text", text, "initangle", initial_angle, "radius", self.getRadius())

        for tx in text:
            text_layer = Image.new('RGBA', (iw, ih), (0, 0, 0, 0))
            draw = ImageDraw.Draw(text_layer)
            (w, h) = draw.textsize(tx, font=font)
            alpha = math.degrees(2 * math.asin((w + spacing) / (2 * self.getRadius())))
            if clockwise:
                draw.text((int(x - w), int(y - self.getRadius() - h)), tx, font=font, fill=color)
                rotated_text_layer = text_layer.rotate(initial_angle - angle - alpha , expand=1)
            else:
                draw.text((int(x - w), int(y + self.getRadius() - h)), tx, font=font, fill=color)
                rotated_text_layer = text_layer.rotate(180 - initial_angle + angle + alpha , expand=1)
            (rtw, rth) = rotated_text_layer.size
            temp.paste(rotated_text_layer, (x - int(rtw / 2), y - int(rth / 2)), rotated_text_layer)
            angle = angle + alpha
        return temp

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._x = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='X')
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._y = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='Y')
        elif parameterId == 3:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._radius = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='Radius')
        elif parameterId == 4:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._rotateDirection = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='RotateDirection')
        else:
            super(FontRotateElement, self).createChildForParameter(parameter)
