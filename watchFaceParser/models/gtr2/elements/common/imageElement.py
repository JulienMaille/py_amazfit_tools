import logging
from typing import Optional

from watchFaceParser.config import Config

from watchFaceParser.models.gtr2.elements.basic.compositeElement import CompositeElement
from watchFaceParser.models.gtr2.elements.common.multilangImageElement import MultilangImageElement
from watchFaceParser.helpers.drawerHelper import DrawerHelper
from watchFaceParser.models.gtr2.elements.common.followObject import FollowObject

class Box:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def getLeft(self):
        return self._x

    def getRight(self):
        return self._x + self._width

    def getTop(self):
        return self._y

    def getBottom(self):
        return self._y + self._height


class ImageElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._x = None
        self._y = None
        self._noDataImageIndex = None
        self._multilangImage = []
        self._decimalPointImageIndex = None
        self._multilangImageUnit = []
        self._delimiterImageIndex = None
        self._multilangImageUnitMile = []
        self._maxTextWidth = None
        self._box = None
        self._followObject = None
        super(ImageElement, self).__init__(parameters=None, parameter = parameter, parent = parent, name = name)

    def getX(self):
        return 0 if self._x is None else self._x

    def getY(self):
        return 0 if self._y is None else self._y

    def getNoDataImageIndex(self):
        return self._noDataImageIndex

    def getMultilangImage(self) -> [MultilangImageElement]:
        return self._multilangImage

    def getDecimalPointImageIndex(self):
        return self._decimalPointImageIndex

    def getMultilangImageUnit(self) -> [MultilangImageElement]:
        return self._multilangImageUnit

    def getDelimiterImageIndex(self):
        return self._delimiterImageIndex

    def getMultilangImageUnitMile(self) -> [MultilangImageElement]:
        return self._multilangImageUnitMile

    def getBox(self):
        return self._box

    def getFollowObject(self) -> Optional[FollowObject]:
        return self._followObject

    def setBox(self, images, spacing, followObject: Optional[FollowObject]):
        (bitmapWidth, bitmapHeight) = DrawerHelper.calculateBounds(images, spacing)
        x = followObject.getX() if followObject and followObject.getCombing() != 1 else self.getX()
        y = followObject.getY() if followObject and followObject.getCombing() != 1 else self.getY()
        if bitmapWidth > self._maxTextWidth:
            self._box = Box(x, y, bitmapWidth, bitmapHeight)
        else:
            self._box = Box(x, y, self._maxTextWidth, bitmapHeight)
        return self._box


    def addTextWidth(self, width, spacing):
        if self._maxTextWidth > 0:
            if spacing > 0:
                self._maxTextWidth += spacing
        self._maxTextWidth += width

    def drawImageElement(self, drawer, images, number, alignment, spacing,
                         padding_zero, padding_zero_digits, padding_zero_length,
                         display_form_analog, followObject) -> Optional[FollowObject]:
        if number is None:
            return None
        
        if not alignment:
            alignment = 0
        if not padding_zero:
            padding_zero = 0
        if not spacing:
            spacing = 0
        if not display_form_analog:
            display_form_analog = False

        if display_form_analog:
            number = number - 1

        ar = self.getImagesForNumber(images, number, alignment, spacing, padding_zero, padding_zero_digits,
                                     padding_zero_length, display_form_analog)
        self.setBox(ar, spacing, followObject)
        self.drawImages(drawer, ar, spacing, alignment, self.getBox())
        self._followObject = FollowObject(self._box.getX() + self._box.getWidth() + 1, self._box.getY(),
                                          followObject.getText(), followObject.getCombing())
        return self._followObject

    def getImagesForNumber(self, images, number, alignment, spacing, padding_zero, padding_zero_digits,
                           padding_zero_length, display_form_analog):
        ar = []
        self._maxTextWidth = 0

        multilang_image = self.getImageForLand(2)
        multilang_image_unit = self.getImageUnitForLand(2)
        multilang_image_unit_mile = self.getImageUnitMileForLand(2)
        minus_sign = number < 0
        number = abs(number)

        if multilang_image:
            if display_form_analog:
                if int(number) <= multilang_image.getImageSet().getImagesCount():
                    image_index = multilang_image.getImageSet().getImageIndex() + int(number) - Config.getStartImageIndex()
                    ar.append(images[image_index])
                    self.addTextWidth(images[image_index].getBitmap().size[0], spacing)
            else:
                if self.getDecimalPointImageIndex():
                    kilometers = int(int(number) / 1000)
                    decimals = int(int(number) % 1000 / 10)
                    ar.extend(self.getImagesForNumber2(
                        images, kilometers, multilang_image, alignment, spacing,
                        padding_zero, padding_zero_digits - 2, padding_zero_length - 2))
                    decimal_point_image_index = self.getDecimalPointImageIndex() - Config.getStartImageIndex()
                    ar.append(images[decimal_point_image_index])
                    self.addTextWidth(images[decimal_point_image_index].getBitmap().size[0], spacing)
                    ar.extend(self.getImagesForNumber2(images, str(decimals),
                                                       multilang_image, alignment, spacing, padding_zero, 2, 2))
                elif self.getDelimiterImageIndex():
                    delimiter_point_image_index = self.getDelimiterImageIndex() - Config.getStartImageIndex()
                    self.addTextWidth(images[delimiter_point_image_index].getBitmap().size[0], spacing)
                    if minus_sign:
                        ar.append(images[delimiter_point_image_index])
                    ar.extend(self.getImagesForNumber2(images, number, multilang_image, alignment, spacing,
                                                       padding_zero, padding_zero_digits, padding_zero_length))
                else:
                    ar.extend(self.getImagesForNumber2(images, number, multilang_image, alignment, spacing,
                                                       padding_zero, padding_zero_digits, padding_zero_length))
        if multilang_image_unit:
            image_index = multilang_image_unit.getImageSet().getImageIndex() - Config.getStartImageIndex()
            ar.append(images[image_index])
            self.addTextWidth(images[image_index].getBitmap().size[0], spacing)
        elif multilang_image_unit_mile:
            image_index = multilang_image_unit_mile.getImageSet().getImageIndex() - Config.getStartImageIndex()
            ar.append(images[image_index])
            self.addTextWidth(images[image_index].getBitmap().size[0], spacing)

        return ar

    def getImagesForNumber2(self, images, number, multilang_image, alignment, spacing,
                            padding_zero, padding_zero_digits, padding_zero_length):
        ar = []

        image_index = multilang_image.getImageSet().getImageIndex() - Config.getStartImageIndex()
        string_number = str(number)
        if padding_zero:
            string_number = string_number.zfill(padding_zero_digits)

        for digit in string_number:
            if int(digit) < multilang_image.getImageSet().getImagesCount():
                image_index = multilang_image.getImageSet().getImageIndex() + int(digit) - Config.getStartImageIndex()
                ar.append(images[image_index])
                self.addTextWidth(images[image_index].getBitmap().size[0], spacing)
        i = padding_zero_length - len(string_number)
        while i > 0:
            self.addTextWidth(images[image_index].getBitmap().size[0], spacing)
            i = i - 1
        return ar

    def getImageForLand(self, land = 0):
        if self._multilangImage:
            for i in self._multilangImage:
                if i.getLandCode() == land:
                    return i
            return self._multilangImage[0]
        return None

    def getImageUnitForLand(self, land = 0):
        if self._multilangImageUnit:
            for i in self._multilangImageUnit:
                if i.getLandCode() == land:
                    return i
            return self._multilangImageUnit[0]
        return None

    def getImageUnitMileForLand(self, land = 0):
        if self._multilangImageUnitMile:
            for i in self._multilangImageUnitMile:
                if i.getLandCode() == land:
                    return i
            return self._multilangImageUnitMile[0]
        return None

    @staticmethod
    def drawImages(drawer, images, spacing, alignment, box):
        assert(type(images) == list)
        assert(type(spacing) == int)
        assert(type(alignment) == int)

        (bitmapWidth, bitmapHeight) = DrawerHelper.calculateBounds(images, spacing)

        print(alignment, box.getLeft(), box.getTop(), box.getRight(), box.getBottom(), bitmapWidth, bitmapHeight)

        x = 0
        y = 0
        if alignment == 0 or alignment is None:
            x = box.getX()
        elif alignment == 2:
            x = box.getRight() - bitmapWidth + 1
        else:
            x = (box.getLeft() + box.getRight() - bitmapWidth) >> 1

        y = box.getTop()

        if x < box.getLeft():
            x = box.getLeft()

        for image in images:
            temp = image.getBitmap()
            print('x', x, 'y', y, 'box', box.getLeft())
            drawer.paste(temp, (x, y), temp)

            imageWidth = image.getBitmap().size[0]
            x += imageWidth + int(spacing)

        if Config.getBorderAlignment():
            from PIL import ImageDraw
            d = ImageDraw.Draw(drawer)
            d.rectangle((box.getLeft(),box.getTop(),box.getRight(), box.getBottom()), outline=(200, 200, 200))

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
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._noDataImageIndex = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'NoDataImageIndex')
        elif parameterId == 4:
            self._multilangImage.append(MultilangImageElement(parameter, parent = self, name = 'MultilangImage'))
            return self._multilangImage
        elif parameterId == 5:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._decimalPointImageIndex = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'DecimalPointImageIndex')
        elif parameterId == 6:
            self._multilangImageUnit.append(MultilangImageElement(parameter, parent = self, name = 'MultilangImageUnit'))
            return self._multilangImageUnit
        elif parameterId == 7:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._delimiterImageIndex = parameter.getValue()
            return ValueElement(parameter = parameter, parent = self, name = 'DelimiterImageIndex')
        elif parameterId == 8:
            self._multilangImageUnitMile.append(MultilangImageElement(parameter, parent = self, name = 'MultilangImageUnitMile'))
            return self._multilangImageUnitMile
        else:
            super(ImageElement, self).createChildForParameter(parameter)
