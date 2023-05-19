import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement

class DistanceElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._image_number = None
        self._suffix_km = None
        self._suffix_mi = None
        self._decimalpointer = None
        self._icon = None
        self._suffixcoord = None
        super(DistanceElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):

        if self._icon:
            self._icon.draw3(drawer, resources, state)
        if self._image_number:
            self._image_number.draw4(drawer,
                                     resources,
                                     int(state.getDistance() / 10),
                                     minimum_digits= 3,
                                     force_padding = False,
                                     decimal_pointer = self._decimalpointer,
                                     suffix = ( self._suffix_km if self._suffix_km else self._suffix_mi) if not self._suffixcoord else None)
            if self._suffixcoord:
                temp = resources[self._suffix_km if self._suffix_km else self._suffix_mi].getBitmap()
                drawer.paste(temp, (self._suffixcoord._x, self._suffixcoord._y), temp)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._image_number = NumberElement(parameter, self, 'ImageNumber')
            return self._image_number
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._suffix_km = parameter.getValue()
            return ValueElement(parameter, self, 'SuffixKMImageIndex')
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._decimalpointer = parameter.getValue()
            return ValueElement(parameter, self, 'DecimalPointImageIndex')
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._suffix_mi = parameter.getValue()
            return ValueElement(parameter, self, 'SuffixMIImageIndex')
        elif parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._icon = ImageElement(parameter=parameter, parent=self, name='Icon')
            return self._icon
        elif parameterId == 6:  # Shortcut
            pass
        elif parameterId == 8:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._suffixcoord = CoordinatesElement(parameter=parameter, parent=self, name='SuffixImageCoordinates')
            return self._suffixcoord
        else:
            super(DistanceElement, self).createChildForParameter(parameter)

