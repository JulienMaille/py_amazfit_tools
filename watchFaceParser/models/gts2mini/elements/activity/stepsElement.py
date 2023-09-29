import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement

class StepsElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._image_number = None
        self._prefix = None
        self._suffix = None
        self._icon = None
        self._delimiter = None
        super(StepsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        if self._icon:
            self._icon.draw3(drawer, resources, state)
        if self._image_number:
            if self._delimiter:
                self._image_number.draw5(drawer,
                                        resources,
                                        [ state.getSteps(), state.getGoal()],
                                        minimum_digits_array= [5, 5],
                                        force_padding_array = [False, False],
                                        prefix = self._prefix,
                                        suffix = self._suffix,
                                        delimiter = self._delimiter)
            else:
                self._image_number.draw4(drawer,
                                        resources,
                                        state.getSteps(),
                                        minimum_digits= 5,
                                        force_padding = False,
                                        prefix = self._prefix,
                                        suffix = self._suffix)
                
            

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._image_number = NumberElement(parameter, self, 'ImageNumber')
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._prefix = parameter.getValue()
            return ValueElement(parameter, self, 'PrefixImageIndex')
            return self._image_number
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._suffix = parameter.getValue()
            return ValueElement(parameter, self, 'SuffixImageIndex')
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._icon = ImageElement(parameter=parameter, parent=self, name='Icon')
            return self._icon
        elif parameterId == 6:  # Shortcut
            pass
        elif parameterId == 7:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._delimiter = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterTotalImageIndex')
        else:
            super(StepsElement, self).createChildForParameter(parameter)
