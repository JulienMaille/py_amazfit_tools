import logging


from watchFaceParser.models.elements.basic.compositeElement import CompositeElement

class ImageSetGTR2Element(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._imageIndex = None
        self._imagesCount = None
        super(ImageSetGTR2Element, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getImageIndex(self):
        return self._imageIndex

    def getImagesCount(self):
        return self._imagesCount

    def createChildForParameter(self, parameter):
        if parameter.getId() == 1:
            self._imageIndex = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, '?ImageIndex?')
        elif parameter.getId() == 2:
            self._imagesCount = parameter.getValue()
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter, self, '?ImagesCount?')
        else:
            super(ImageSetGTR2Element, self).createChildForParameter(parameter)

