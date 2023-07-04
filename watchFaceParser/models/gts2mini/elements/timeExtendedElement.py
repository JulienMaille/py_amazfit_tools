import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class TimeExtendedElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._time_separate_digits = None
        self._sunset_time = None
        self._delimiter_sunset = None
        self._sunrise_time = None
        self._delimiter_sunrise = None
        self._sunset_icon = None
        self._sunrise_icon = None
        self._sunset_prefix = None
        self._sunrise_prefix = None
        super(TimeExtendedElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        if self._time_separate_digits:
            self._time_separate_digits.draw3(drawer, images, state)

        import random
        if self._sunset_icon:
            self._sunset_icon.draw3(drawer, images, state)
        if self._sunset_time:
            number = random.randint(17, 21) * 100 + random.randint(00, 59)
            self._sunset_time.draw4(drawer, images, number, minimum_digits= 4,
                                    force_padding = True,
                                    followxy = None,
                                    delimiter_time = self._delimiter_sunset if self._delimiter_sunset else None,
                                    minus = None,
                                    prefix = self._sunset_prefix if self._sunset_prefix else None,
                                    suffix = None)

        if self._sunrise_icon:
            self._sunrise_icon.draw3(drawer, images, state)
        if self._sunrise_time:
            number = random.randint(4, 10) * 100 + random.randint(00, 59)
            self._sunrise_time.draw4(drawer, images, number, minimum_digits= 4,
                                     force_padding = True,
                                     followxy = None,
                                     delimiter_time = self._delimiter_sunrise if self._delimiter_sunrise else None,
                                     minus = None,
                                     prefix = self._sunrise_prefix if self._sunrise_prefix else None,
                                     suffix = None)

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.time.timeSeparateDigitsElement import TimeSeparateDigitsElement
            self._time_separate_digits = TimeSeparateDigitsElement(parameter = parameter, parent = self, name ='Time')
            return self._time_separate_digits
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._sunset_time = NumberElement(parameter=parameter, parent=self, name='SunsetTimeOneLine')
            return self._sunset_time
        elif parameterId == 3:
            self._delimiter_sunset = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='DelimiterSunsetImageIndex')
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._sunrise_time = NumberElement(parameter=parameter, parent=self, name='SunriseTimeOneLine')
            return self._sunrise_time
        elif parameterId == 5:
            self._delimiter_sunrise = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='DelimiterSunriseImageIndex')
        elif parameterId == 6:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._sunset_icon = ImageElement(parameter=parameter, parent=self, name='SunsetIcon')
            return self._sunset_icon
        elif parameterId == 7:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._sunrise_icon = ImageElement(parameter=parameter, parent=self, name='SunriseIcon')
            return self._sunrise_icon
        elif parameterId == 8:
            pass
        elif parameterId == 9:
            pass
        elif parameterId == 11:
            self._sunrise_prefix = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='SunriseImageIndex')
        elif parameterId == 12:
            self._sunset_prefix = parameter.getValue()
            return ValueElement(parameter=parameter, parent=self, name='SunsetImageIndex')
        else:
            print ("Unknown TimeExtended",parameterId)
            return super(TimeExtendedElement, self).createChildForParameter(parameter)

