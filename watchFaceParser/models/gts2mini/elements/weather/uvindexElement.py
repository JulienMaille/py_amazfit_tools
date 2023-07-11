import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement
from watchFaceParser.utils.parametersConverter import uint2int


class UvindexElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._number = None
        self._nodata = None
        self._suffix = None
        self._prefix = None
        self._image = None
        super(UvindexElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)

        if self._number:
            self._number.draw4(drawer, resources, state.getUVindex(), prefix = self._prefix, suffix = self._suffix)

        if self._image:
            self._image.draw3(drawer, resources, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._number = NumberElement(parameter, self, 'UVindexNumber')
            return self._number
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._suffix = parameter.getValue()
            return ValueElement(parameter, self, 'SuffixImageIndex')
        elif parameterId == 5:  # Shortcut
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._prefix = parameter.getValue()
            return ValueElement(parameter, self, 'PrefixImageIndex')
        elif parameterId == 6:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._nodata = parameter.getValue()
            return ValueElement(parameter, self, 'NoDataImageIndex')
        elif parameterId == 9:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._image = ImageElement(parameter, self, 'UVindexIcon')
            return self._image
        else:
            print ("Unknown UVindexElement",parameterId)
            super(UvindexElement, self).createChildForParameter(parameter)
