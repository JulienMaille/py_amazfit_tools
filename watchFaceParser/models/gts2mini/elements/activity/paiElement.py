﻿import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement

class PaiElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._image_number = None
        self._nodata = None
        self._icon = None
        super(PaiElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        if self._icon:
            self._icon.draw3(drawer, resources, state)
        if self._image_number:
            self._image_number.draw4(drawer,
                                     resources,
                                     state.getPai(),
                                     minimumDigits = 3,
                                     force_padding = False,
                                     followxy = None)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._image_number = NumberElement(parameter, self, 'ImageNumber')
            return self._image_number
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._nodata = parameter.getValue()
            return ValueElement(parameter, self, 'NoDataImageIndex')
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._icon = ImageElement(parameter=parameter, parent=self, name='Icon')
            return self._icon
        elif parameterId == 4:  # Shortcut
            pass
        else:
            super(PaiElement, self).createChildForParameter(parameter)
