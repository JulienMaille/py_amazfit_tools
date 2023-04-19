import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement
from watchFaceParser.utils.parametersConverter import uint2int


class HumidityElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._humidity_number = None
        self._suffix = None
        self._prefix = None
        self._humidity_image = None
        super(HumidityElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)

        if self._humidity_number:
            self._humidity_number.draw4(drawer, resources, state.getHumidity(), prefix=self._prefix, suffix = self._suffix)

        if self._humidity_image:
            self._humidity_image.draw3(drawer, resources, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._humidity_number = NumberElement(parameter, self, 'HumidityNumber')
            return self._humidity_number
        if parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._suffix = parameter.getValue()
            return ValueElement(parameter, self, 'SuffixImageIndex')
        if parameterId == 8:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._prefix = parameter.getValue()
            return ValueElement(parameter, self, 'PrefixImageIndex')
        if parameterId == 9:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._humidity_image = ImageElement(parameter, self, 'HumidityIcon')
            return self._humidity_image
        else:
            print ("Unknown HumidityElement",parameterId)
            super(HumidityElement, self).createChildForParameter(parameter)
