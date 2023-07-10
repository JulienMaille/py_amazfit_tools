import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement
from watchFaceParser.helpers.drawerHelper import DrawerHelper


class Box:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def getX(self):
        return self._x

    def setX(self, x):
        self._x = x

    def getY(self):
        return self._y
    
    def setY(self, y):
        self._y = y

    def getWidth(self):
        return self._width

    def setWidth(self, width):
        self._width = width

    def getHeight(self):
        return self._height

    def setHeight(self, height):
        self._height = height

    def getLeft(self):
        return self._x

    def getRight(self):
        return self._x + self._width

    def getTop(self):
        return self._y

    def getBottom(self):
        return self._y + self._height


class NumberElement(ContainerElement):
    def __init__(self, parameter, parent, name):
        self._topLeftX = None
        self._topLeftY = None
        self._bottomRightX = None
        self._bottomRightY = None
        self._alignment = None
        self._spacing = 0
        self._imageIndex = None
        self._imagesCount = None
        self._maxTextWidth = None
        self._box = None
        self._followxy = None
        self._verticalOffset = None
        super(NumberElement, self).__init__(None, parameter = parameter, parent = parent, name = name)

    def getTopLeftX(self):
        return self._topLeftX

    def getTopLeftY(self):
        return self._topLeftY

    def getBox(self):
        #return Box(self._topLeftX, self._topLeftY, self._bottomRightX - self._topLeftX, self._bottomRightY - self._topLeftY)
        return self._box

    def getAltBox(self, altCoordinates):
        return Box(altCoordinates._x, altCoordinates._y, self._bottomRightX - self._topLeftX, self._bottomRightY - self._topLeftY)

    def setBox(self, images, spacing, followxy):
        (bitmapWidth, bitmapHeight) = DrawerHelper.calculateBounds(images, spacing)
        x = self._topLeftX if followxy is None else followxy[0]
        y = self._topLeftY if followxy is None else followxy[1]
        if bitmapWidth > self._maxTextWidth:
            self._box = Box(x, y, bitmapWidth, bitmapHeight)
        else:
            self._box = Box(x, y, self._maxTextWidth, bitmapHeight)
        if self._bottomRightX > self._box.getX() + self._box.getWidth():
            self._box.setWidth(self._bottomRightX - self._box.getX())
        from watchFaceParser.models.textAlignment import TextAlignment
        alignmentFlag = TextAlignment(self._alignment)
        if alignmentFlag.hasFlag(TextAlignment.Right) and self._box.getRight() > self._bottomRightX:
            self._box.setX(self._bottomRightX  - self._box.getWidth())
        if self._bottomRightY > self._box.getY() + self._box.getHeight():
            self._box.setHeight(self._bottomRightY - self._box.getY())
        return self._box

    def addTextWidth(self, width, spacing):
        if self._maxTextWidth > 0:
            if spacing > 0:
                self._maxTextWidth += spacing
        self._maxTextWidth += width

    def draw5(self, drawer, images, number_array=None, minimum_digits_array=None,
              force_padding_array=None, followxy=None, prefix=None, minus=None, suffix=None, delimiter=None):
        from watchFaceParser.helpers.drawerHelper import DrawerHelper

        if not number_array:
            return followxy

        self._maxTextWidth = 0
        ar = []
        if prefix:
            ar.append(images[prefix])
            self.addTextWidth(images[prefix].getBitmap().size[0], self._spacing)
        for index in range(len(number_array)):
            padding_zero = False
            if force_padding_array:
                if index <= len(force_padding_array):
                    padding_zero = force_padding_array[index]

            minimum_digits = 1
            if minimum_digits_array:
                if index <= len(minimum_digits_array) and minimum_digits_array[index]:
                    minimum_digits = minimum_digits_array[index]

            ar.extend(self.getImagesForNumber(images, number_array[index], minimum_digits,
                                              minus=minus, padding_zero=padding_zero))

            if delimiter and index < len(number_array)-1:
                ar.append(images[delimiter])
                self.addTextWidth(images[delimiter].getBitmap().size[0], self._spacing)

        if suffix:
            ar.append(images[suffix])
            self.addTextWidth(images[suffix].getBitmap().size[0], self._spacing)

        self.setBox(ar, self._spacing, followxy)

        DrawerHelper.drawImages(drawer,
                                ar,
                                self._spacing,
                                self._alignment,
                                self._box)

        self._followxy = (self._box.getX() + self._box.getWidth() + 1, self._box.getY())
        return self._followxy

    def draw4(self, drawer, images, number, minimum_digits=1,
              force_padding=False, followxy=None, decimal_pointer=None,
              minus=None, prefix=None, suffix=None, delimiter_time=None):

        from watchFaceParser.helpers.drawerHelper import DrawerHelper

        self._maxTextWidth = 0
        ar = self.getImagesForNumber(images, number, minimum_digits,
                                     decimal_pointer=decimal_pointer, minus=minus,
                                     prefix=prefix, suffix=suffix,
                                     delimiter_time=delimiter_time, padding_zero=force_padding)

        self.setBox(ar, self._spacing, followxy)

        DrawerHelper.drawImages(drawer,
                                ar,
                                self._spacing,
                                self._alignment,
                                self._box,
                                self._verticalOffset)

        self._followxy = (self._box.getX() + self._box.getWidth() + 1, self._box.getY())
        return self._followxy

    def getImagesForNumber(self, images, number, minimum_digits = 1, decimal_pointer = None, minus = None, prefix = None,
                           suffix = None, delimiter_time = None, padding_zero=False):
        padding_length = 1
        if padding_zero:
            padding_length = minimum_digits

        if number < 0:
            string_number = str(-number).zfill(padding_length)
        else:
            string_number = str(number).zfill(padding_length)

        ar = []
        if prefix:
            ar.append(images[prefix])
            self.addTextWidth(images[prefix].getBitmap().size[0], self._spacing)
        if number < 0 and minus:
            ar.append(images[minus])
            self.addTextWidth(images[minus].getBitmap().size[0], self._spacing)
        for digitIndex in range(len(string_number)):
            if decimal_pointer:
                if digitIndex == len(string_number)-1:
                    ar.append(images[decimal_pointer])
                    self.addTextWidth(images[decimal_pointer].getBitmap().size[0], self._spacing)
            if delimiter_time and digitIndex == len(string_number)-2:
                ar.append(images[delimiter_time])
                self.addTextWidth(images[delimiter_time].getBitmap().size[0], self._spacing)
            digit = string_number[digitIndex]
            if int(digit) < self._imagesCount:
                image_index = self._imageIndex + int(digit)
                ar.append(images[image_index])
                self.addTextWidth(images[image_index].getBitmap().size[0], self._spacing)
            if decimal_pointer:
                if digitIndex == len(string_number)-1:
                    break
        if suffix:
            ar.append(images[suffix])
            self.addTextWidth(images[suffix].getBitmap().size[0], self._spacing)

        i = minimum_digits - len(string_number)
        self.addTextWidth(images[self._imageIndex].getBitmap().size[0] * i, self._spacing)

        return ar

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement

        parameterId = parameter.getId()
        if parameterId == 1:
            self._topLeftX = parameter.getValue()
            return ValueElement(parameter, self, 'TopLeftX')
        elif parameterId == 2:
            self._topLeftY = parameter.getValue()
            return ValueElement(parameter, self, 'TopLeftY')
        if parameterId == 3:
            self._bottomRightX = parameter.getValue()
            return ValueElement(parameter, self, 'BottomRightX')
        elif parameterId == 4:
            self._bottomRightY = parameter.getValue()
            return ValueElement(parameter, self, 'BottomRightY')
        elif parameterId == 5:
            self._alignment = parameter.getValue()
            return ValueElement(parameter, self, 'Alignment')
        elif parameterId == 6:
            self._spacing = parameter.getValue()
            return ValueElement(parameter, self, 'Spacing')
        elif parameterId == 7:
            self._verticalOffset = parameter.getValue()
            return ValueElement(parameter, self, 'VerticalOffset')
        elif parameterId == 8:
            self._imageIndex = parameter.getValue()
            return ValueElement(parameter, self, 'ImageIndex')
        elif parameterId == 9:
            self._imagesCount = parameter.getValue()
            return ValueElement(parameter, self, 'ImagesCount')
        else:
            super(NumberElement, self).createChildForParameter(parameter)

