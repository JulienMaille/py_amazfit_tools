import logging
from watchFaceParser.config import Config

from watchFaceParser.models.gtr2.elements.basic.compositeElement import CompositeElement


class AngleSettingsElement(CompositeElement):
    def __init__(self, parameter, parent, name=None):
        self._x = 0
        self._y = 0
        self._startAngle = 0
        self._endAngle = 0
        self._radius = None
        super(AngleSettingsElement, self).__init__(parameters=None, parameter=parameter, parent=parent, name=name)

    def getX(self):
        return 0 if self._x is None else self._x

    def getY(self):
        return 0 if self._y is None else self._y

    def getStartAngle(self):
        return self._startAngle

    def getEndAngle(self):
        return self._endAngle

    def getRadius(self):
        return self._radius

    def drawAngleSettingsElement(self, drawer, resources,
              value,
              total,
              width,
              foregroundImageIndex=None,
              color=None,
              flatness=None,
              pointerImageIndex=None,
              backgroundImageIndex=None
              ):
        assert (type(resources) == list)
        assert (type(value) == int)
        assert (type(total) == int)
        if value > total:
            value = total
        sector_angle = int(1.0 * (self.getEndAngle() - self.getStartAngle()) * value / total)
        start = -90 + self.getStartAngle()
        end = -90 + self.getStartAngle() + sector_angle

        if start > end:
            start, end = end, start

        if foregroundImageIndex:
            temp = resources[foregroundImageIndex - Config.getStartImageIndex()].getBitmap()
            from PIL import Image
            # mask = Image.new('RGBA',temp.size,self.getColor())
            mask = Image.new('RGBA', temp.size, (0, 0, 0, 0))
            mask_color = (255, 255, 255, 255)

            from PIL import ImageDraw
            d = ImageDraw.Draw(mask)  # draw context
            radius = self._radius + int(width / 2)  # patch for PIL arc

            rect = (0, 0,
                    int(radius * 2), int(radius * 2))

            d.arc(rect,
                  start,
                  end,
                  fill=mask_color, width=width)

            if (flatness == 0 or flatness is None) and value:
                # round edges
                import math
                x = int(temp.size[0] / 2 + (radius - width / 2) *
                        math.cos(math.pi * (self.getStartAngle() - 90) / 180))
                y = int(temp.size[1] / 2 + (radius - width / 2) *
                        math.sin(math.pi * (self.getStartAngle() - 90) / 180))
                d.ellipse((x - width / 2 + 1, y - width / 2 + 1, x + width / 2 - 1,
                           y + width / 2 - 1), fill=mask_color)

                x = int(temp.size[0] / 2 + (radius - width / 2) *
                        math.cos(math.pi * (self.getStartAngle() + sector_angle - 90) / 180))
                y = int(temp.size[1] / 2 + (radius - width / 2) *
                        math.sin(math.pi * (self.getStartAngle() + sector_angle - 90) / 180))
                d.ellipse((x - width / 2 + 1, y - width / 2 + 1, x + width / 2 - 1,
                           y + width / 2 - 1), fill=mask_color)
            elif flatness == 90 and value:
                # spike
                import math
                x1 = int(temp.size[0] / 2 + (radius - width) * math.cos(
                    math.pi * (self.getStartAngle() - 90) / 180))
                y1 = int(temp.size[1] / 2 + (radius - width) * math.sin(
                    math.pi * (self.getStartAngle() - 90) / 180))

                x2 = int(temp.size[0] / 2 + radius *
                         math.cos(math.pi * (self.getStartAngle() - 90) / 180))
                y2 = int(temp.size[1] / 2 + radius *
                         math.sin(math.pi * (self.getStartAngle() - 90) / 180))

                x3 = int(temp.size[0] / 2 + (radius - width / 2) * math.cos(math.pi * (
                        self.getStartAngle() - width * 360 / (
                        2 * math.pi * (radius - width / 2)) - 90) / 180))
                y3 = int(temp.size[1] / 2 + (radius - width / 2) * math.sin(math.pi * (
                        self.getStartAngle() - width * 360 / (
                        2 * math.pi * (radius - width / 2)) - 90) / 180))
                d.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=mask_color)

                x1 = int(temp.size[0] / 2 + (radius - width) * math.cos(
                    math.pi * (self.getStartAngle() + sector_angle - 90) / 180))
                y1 = int(temp.size[1] / 2 + (radius - width) * math.sin(
                    math.pi * (self.getStartAngle() + sector_angle - 90) / 180))

                x2 = int(
                    temp.size[0] / 2 + radius *
                    math.cos(math.pi * (self.getStartAngle() + sector_angle - 90) / 180))
                y2 = int(
                    temp.size[1] / 2 + radius *
                    math.sin(math.pi * (self.getStartAngle() + sector_angle - 90) / 180))

                x3 = int(temp.size[0] / 2 + (radius - width / 2) * math.cos(math.pi * (
                        self.getStartAngle() + sector_angle + width * 360 / (
                        2 * math.pi * (radius - width / 2)) - 90) / 180))
                y3 = int(temp.size[1] / 2 + (radius - width / 2) * math.sin(math.pi * (
                        self.getStartAngle() + sector_angle + width * 360 / (
                        2 * math.pi * (radius - width / 2)) - 90) / 180))
                d.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=mask_color)
            elif flatness == 180 and value:
                pass
            dX = int(self.getX() - self._radius - (width / 2))
            dY = int(self.getY() - self._radius - (width / 2))
            if backgroundImageIndex:
                back = resources[backgroundImageIndex - Config.getStartImageIndex()].getBitmap()
                drawer.paste(back, (dX, dY), back)
            temp2 = Image.new('RGBA', drawer.size, (0, 0, 0, 0))
            temp2.paste(temp, (dX, dY), mask)
            drawer.paste(temp2, (0, 0), temp2)
        else:
            from PIL import ImageDraw
            d = ImageDraw.Draw(drawer)  # draw context
            radius = self._radius + int(width / 2)  # patch for PIL arc

            dX = int(self.getX() - radius - int(width / 2))
            dY = int(self.getY() - radius - int(width / 2))
            if backgroundImageIndex:
                back = resources[backgroundImageIndex - Config.getStartImageIndex()].getBitmap()
                drawer.paste(back, (dX, dY), back)

            rect = (int(self.getX() - radius), int(self.getY() - radius),
                    int(self.getX() + radius), int(self.getY() + radius))

            d.arc(rect,
                  start,
                  end,
                  fill=color,
                  width=width)

            if flatness == 0 and value:
                # round edges
                import math
                x = int(self.getX() + (radius - width / 2) *
                        math.cos(math.pi * (self.getStartAngle() - 90) / 180))
                y = int(self.getY() + (radius - width / 2) *
                        math.sin(math.pi * (self.getStartAngle() - 90) / 180))
                d.ellipse((x - width / 2 + 1, y - width / 2 + 1, x + width / 2 - 1,
                           y + width / 2 - 1), fill=color)

                x = int(self.getX() + (radius - width / 2) *
                        math.cos(math.pi * (self.getStartAngle() + sector_angle - 90) / 180))
                y = int(self.getY() + (radius - width / 2) *
                        math.sin(math.pi * (self.getStartAngle() + sector_angle - 90) / 180))
                d.ellipse((x - width / 2 + 1, y - width / 2 + 1, x + width / 2 - 1,
                           y + width / 2 - 1), fill=color)
            elif flatness == 90 and value:
                # spike
                import math
                x1 = int(self.getX() + (radius - width) *
                         math.cos(math.pi * (self.getStartAngle() - 90) / 180))
                y1 = int(self.getY() + (radius - width) *
                         math.sin(math.pi * (self.getStartAngle() - 90) / 180))

                x2 = int(self.getX() + radius * math.cos(math.pi * (self.getStartAngle() - 90) / 180))
                y2 = int(self.getY() + radius * math.sin(math.pi * (self.getStartAngle() - 90) / 180))

                x3 = int(self.getX() + (radius - width / 2) *
                         math.cos(math.pi * (self.getStartAngle() - width * 360 / (
                                 2 * math.pi * (radius - width / 2)) - 90) / 180))
                y3 = int(self.getY() + (radius - width / 2) *
                         math.sin(math.pi * (self.getStartAngle() - width * 360 / (
                                 2 * math.pi * (radius - width / 2)) - 90) / 180))
                d.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=color)

                x1 = int(self.getX() + (radius - width) * math.cos(
                    math.pi * (self.getStartAngle() + sector_angle - 90) / 180))
                y1 = int(self.getY() + (radius - width) * math.sin(
                    math.pi * (self.getStartAngle() + sector_angle - 90) / 180))

                x2 = int(self.getX() + radius *
                         math.cos(math.pi * (self.getStartAngle() + sector_angle - 90) / 180))
                y2 = int(self.getY() + radius *
                         math.sin(math.pi * (self.getStartAngle() + sector_angle - 90) / 180))

                x3 = int(self.getX() + (radius - width / 2) *
                         math.cos(math.pi * (self.getStartAngle() + sector_angle + width * 360 / (
                                 2 * math.pi * (radius - width / 2)) - 90) / 180))
                y3 = int(self.getY() + (radius - width / 2) *
                         math.sin(math.pi * (self.getStartAngle() + sector_angle + width * 360 / (
                                 2 * math.pi * (radius - width / 2)) - 90) / 180))
                d.polygon([(x1, y1), (x2, y2), (x3, y3)], fill=color)
            elif flatness == 180:
                pass

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
            self._startAngle = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='StartAngle')
        elif parameterId == 4:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._endAngle = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='EndAngle')
        elif parameterId == 5:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._radius = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='Radius')
        else:
            super(AngleSettingsElement, self).createChildForParameter(parameter)
