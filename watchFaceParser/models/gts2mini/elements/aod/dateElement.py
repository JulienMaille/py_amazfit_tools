import logging

from watchFaceParser.models.gts2mini.elements.basic.compositeElement import CompositeElement

class DateElement(CompositeElement):
    def __init__(self, parameter, parent, name=None):
        self._month = None
        self._day = None
        self._delimiter_month = None
        self._delimiter_day = None
        self._padding_zero_month = None
        self._padding_zero_day = None
        self._datatype_month = None
        self._datatype_month_coords = None
        self._datatype_day = None
        self._datatype_day_coords = None
        self._day_follow_month = False
        super(DateElement, self).__init__(parameters=None, parameter=parameter, parent=parent, name=name)

    def draw3(self, drawer, images, state):
        followxy = None
        if self._month:
            followxy = self._month.draw4(drawer, images, state.getTime().month, 2,
                                         force_padding = self._padding_zero_month,
                                         followxy = None,
                                         suffix = self._delimiter_month)

            if self._datatype_month_coords:
                self.drawDelimiter(drawer, images, self._datatype_month,
                                    self._datatype_month_coords.getX(),
                                    self._datatype_month_coords.getY())
        if self._day:
            followxy = self._day.draw4(drawer, images, state.getTime().day, 2,
                                       force_padding = self._padding_zero_day,
                                       followxy = followxy if self._day_follow_month else None,
                                       suffix=self._delimiter_day)

            if self._datatype_day:
                if self._day_follow_month:
                    followxy = self.drawDelimiter(drawer, images, self._datatype_day, followxy[0], followxy[1])
                elif self._datatype_day_coords:
                    self.drawDelimiter(drawer, images, self._datatype_day,
                                       self._datatype_day_coords.getX(),
                                       self._datatype_day_coords.getY())

    def drawDelimiter(self, drawer, images, index, x, y):
        temp = images[index].getBitmap()
        drawer.paste(temp, (x, y), temp)
        return x + temp.size[0], y

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
        from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._month = NumberElement(parameter, self, 'Month')
            return self._month
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._day = NumberElement(parameter, self, 'Day')
            return self._day
        elif parameterId == 3:
            self._datatype_month = parameter.getValue()
            return ValueElement(parameter, self, 'MonthDataTypeImageIndex')
        elif parameterId == 4:
            self._datatype_day = parameter.getValue()
            return ValueElement(parameter, self, 'DayDataTypeImageIndex')
        elif parameterId == 5:
            self._delimiter_month = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterMonthImageIndex')
        elif parameterId == 6:
            self._delimiter_day = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterDayImageIndex')
        elif parameterId == 7:
            self._padding_zero_month = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroMonth')
        elif parameterId == 8:
            self._padding_zero_day = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroDay')
        elif parameterId == 9:
            self._datatype_month_coords = CoordinatesElement(parameter = parameter, parent = self, name ='MonthDataTypeCoordinates')
            return self._datatype_month_coords
        elif parameterId == 10:
            self._datatype_day_coords = CoordinatesElement(parameter = parameter, parent = self, name ='DayDataTypeCoordinates')
            return self._datatype_day_coords
        elif parameterId == 11:
            self._day_follow_month = parameter.getValue()
            return ValueElement(parameter, self, 'DayFollowsMonth')
        else:
            super(DateElement, self).createChildForParameter(parameter)
