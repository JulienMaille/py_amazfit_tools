import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement

class DateElement(CompositeElement):
    def __init__(self, parameter, parent, name=None):
        self._month = None
        self._day = None
        self._delimiter = None
        self._padding_zero_month = None
        self._padding_zero_day = None
        self._day_follow_month = None
        super(DateElement, self).__init__(parameters=None, parameter=parameter, parent=parent, name=name)

    def draw3(self, drawer, images, state):
        followxy = None
        if self._month:
            followxy = self._month.draw4(drawer, images, state.getTime().month, 2,
                                         force_padding = self._padding_zero_month,
                                         followxy = None,
                                         suffix = self._delimiter)

        if self._day:
            self._day.draw4(drawer, images, state.getTime().day, 2,
                            force_padding = self._padding_zero_day,
                            followxy = followxy if self._day_follow_month else None)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._month = NumberElement(parameter, self, 'Month')
            return self._month
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._day = NumberElement(parameter, self, 'Day')
            return self._day
        elif parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._delimiter = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterMonthImageIndex')
        elif parameterId == 7:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._padding_zero_month = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroMonth')
        elif parameterId == 8:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._padding_zero_day = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroDay')
        elif parameterId == 11:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._day_follow_month = parameter.getValue()
            return ValueElement(parameter, self, 'DayFollowsMonth')
            pass
        else:
            super(DateElement, self).createChildForParameter(parameter)
