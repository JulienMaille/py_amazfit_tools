import logging
from watchFaceParser.config import Config

from watchFaceParser.models.gtr2.elements.basic.compositeElement import CompositeElement
from watchFaceParser.models.gtr2.elements.common.multilangImageElement import MultilangImageElement
from watchFaceParser.helpers.drawerHelper import DrawerHelper

class LinearSettingsElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._startX = None
        self._startY = None
        self._endX = None
        self._endY = None
        super(LinearSettingsElement, self).__init__(parameters=None, parameter = parameter, parent = parent, name = name)

    def getStartX(self):
        return self._startX

    def getStartY(self):
        return self._startY

    def getEndX(self):
        return self._endX

    def getEndY(self):
        return self._endY

    def drawLinearSettingsElement(self, drawer, resources,
              value,
              total,
              width,
              foregroundImageIndex = None,
              color = None,
              flatness = None,
              pointerImageIndex = None,
              backgroundImageIndex = None
              ):
        assert (type(resources) == list)
        assert (type(value) == int)
        assert (type(total) == int)
        if value > total:
            value = total

        sector_width = int((self.getEndX() - self.getStartX()) * value / total)

        if foregroundImageIndex:
            temp = resources[foregroundImageIndex - Config.getStartImageIndex()].getBitmap()
            from PIL import Image
            mask = Image.new('RGBA', temp.size, (0, 0, 0, 0))
            mask_color = (255, 255, 255, 255)

            from PIL import ImageDraw
            d = ImageDraw.Draw(mask)  # draw context

            if flatness == 0 or flatness is None:
                # round edges
                if value:
                    rect = ((width/2, 0), (sector_width-width/2, width))
                    d.rectangle(rect, fill=mask_color)
                    x = int(0)
                    y = int(width / 2)
                    d.ellipse((x, y - width / 2 + 1,
                               x + width, y + width / 2 - 1), fill=mask_color)

                    x = int(sector_width)
                    y = int(width / 2)
                    d.ellipse((x - width, y - width / 2 + 1,
                               x, y + width / 2 - 1), fill=mask_color)
            else:
                rect = ((0, 0), (sector_width, width))
                d.rectangle(rect, fill=mask_color)
                pass

            dX = int(self.getStartX())
            dY = int(self.getStartY())
            if backgroundImageIndex:
                back = resources[backgroundImageIndex - Config.getStartImageIndex()].getBitmap()
                drawer.paste(back, (dX, dY), back)

            temp2 = Image.new('RGBA', drawer.size, (0, 0, 0, 0))
            temp2.paste(temp, (dX, dY), mask)
            drawer.paste(temp2, (0, 0), temp2)

            if pointerImageIndex:
                pointer = resources[pointerImageIndex - Config.getStartImageIndex()].getBitmap()
                pw, ph = pointer.size
                px = int(self.getStartX() + sector_width - pw)
                py = int(self.getStartY() + (width / 2) - (ph / 2))
                drawer.paste(pointer, (px, py), pointer)
        else:
            from PIL import ImageDraw
            d = ImageDraw.Draw(drawer)  # draw context

            dX = int(self.getStartX())
            dY = int(self.getStartY())
            if backgroundImageIndex:
                back = resources[backgroundImageIndex - Config.getStartImageIndex()].getBitmap()
                drawer.paste(back, (dX, dY), back)

            rect = ((self.getStartX(), self.getStartY()),
                    (self.getStartX() + sector_width, self.getStartY()+width-1))

            if flatness == 0 or flatness is None:
                # round edges
                if value:
                    d.rectangle(rect, fill=color)
                    x = int(self.getStartX())
                    y = int(self.getStartY() + (width / 2))
                    d.ellipse((x - width / 2 + 1, y - width / 2 + 1, x + width / 2 - 1,
                               y + width / 2 - 1), fill=color)

                    x = int(self.getStartX() + sector_width )
                    y = int(self.getStartY() + (width / 2))
                    d.ellipse((x - width / 2 + 1, y - width / 2 + 1, x + width / 2 - 1,
                               y + width / 2 - 1), fill=color)
            elif flatness == 180 and value:
                d.rectangle(rect, fill=color)

            if pointerImageIndex:
                pointer = resources[pointerImageIndex - Config.getStartImageIndex()].getBitmap()
                pw, ph = pointer.size
                px = int(self.getStartX() + sector_width - (pw/2))
                py = int(self.getStartY() + (width / 2) - (ph / 2))
                drawer.paste(pointer, (px, py), pointer)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._startX = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'StartX')
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._startY = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'StartY')
        elif parameterId == 3:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._endX = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'EndX')
        elif parameterId == 4:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._endY = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'EndY')
        else:
            super(LinearSettingsElement, self).createChildForParameter(parameter)
