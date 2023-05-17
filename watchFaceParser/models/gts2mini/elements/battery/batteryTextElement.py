from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class BatteryTextElement(ContainerElement):
    def __init__(self, parameter, parent, name = None):
        self._image_number = None
        self._prefix = None
        self._nodata = None
        self._unknown2 = None
        self._suffix = None
        self._icon = None
        super(BatteryTextElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):

        if self._image_number:
            self._image_number.draw4(drawer, 
                                     resources,
                                     state.getBatteryLevel(),
                                     minimum_digits= 3,
                                     force_padding = False,
                                     prefix = self._prefix,
                                     suffix = self._suffix)
        if self._icon:
            self._icon.draw3(drawer, resources, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._image_number = NumberElement(parameter, self, 'ImageNumber')
            return self._image_number
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._unknown2 = parameter.getValue()
            return ValueElement(parameter, self, 'UnknownLong2')
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._prefix = parameter.getValue()
            return ValueElement(parameter, self, 'PrefixImageIndex')
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._suffix = parameter.getValue()
            return ValueElement(parameter, self, 'SuffixImageIndex')
        elif parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._icon = ImageElement(parameter=parameter, parent=self, name='Icon')
            return self._icon
        elif parameterId == 6:  # Shortcut
            pass
        else:
            super(BatteryTextElement, self).createChildForParameter(parameter)
