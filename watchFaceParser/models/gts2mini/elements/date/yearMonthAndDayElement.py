import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class YearMonthAndDayElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._year = None
        self._month = None
        self._day = None
        self._month_follow_year = False
        self._day_follow_month = False
        self._month_as_word = None
        self._year_data_type = None
        self._month_data_type = None
        self._day_data_type = None
        self._delimiter_year = None
        self._delimiter_month = None
        self._delimiter_day = None
        self._datetype_year_coords = None
        self._datetype_month_coords = None
        self._datetype_day_coords = None
        super(YearMonthAndDayElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw4(self, drawer, images, state,
              padding_zero_day = False, padding_zero_month = False, padding_zero_year = False):
        followxy = None
        if self._year:
            followxy = self._year.draw4(drawer, images, state.getTime().year, 4,
                                        force_padding = padding_zero_year,
                                        followxy = None,
                                        suffix = self._delimiter_year)
            if self._year_data_type:
                if self._month_follow_year:
                    followxy = self.drawDelimiter(drawer, images, self._year_data_type, followxy[0], followxy[1])
                elif self._datetype_year_coords:
                    self.drawDelimiter(drawer, images, self._year_data_type,
                                       self._datetype_year_coords.getX(),
                                       self._datetype_year_coords.getY())

        if self._month:
            followxy = self._month.draw4(drawer, images, state.getTime().month, 2,
                                         force_padding = padding_zero_month,
                                         followxy = followxy if self._month_follow_year else None,
                                         suffix = self._delimiter_month)
            if self._month_data_type:
                if self._day_follow_month:
                    followxy = self.drawDelimiter(drawer, images, self._month_data_type, followxy[0], followxy[1])
                elif self._datetype_month_coords:
                    self.drawDelimiter(drawer, images, self._month_data_type,
                                       self._datetype_month_coords.getX(),
                                       self._datetype_month_coords.getY())

        if self._day:
            followxy = self._day.draw4(drawer, images, state.getTime().day, 2,
                                       force_padding = padding_zero_day,
                                       followxy = followxy if self._day_follow_month else None,
                                       suffix = self._delimiter_day)
            if self._day_data_type:
                if self._day_follow_month:
                    followxy = self.drawDelimiter(drawer, images, self._day_data_type, followxy[0], followxy[1])
                elif self._datetype_day_coords:
                    self.drawDelimiter(drawer, images, self._day_data_type,
                                       self._datetype_day_coords.getX(),
                                       self._datetype_day_coords.getY())

        if self._month_as_word:
            self._month_as_word.draw3(drawer, images, state.getTime().month)

    def drawDelimiter(self, drawer, images, index, x, y):
        temp = images[index].getBitmap()
        drawer.paste(temp, (x, y), temp)
        return x + temp.size[0], y


    def createChildForParameter(self, parameter):
        from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._year = NumberElement(parameter=parameter, parent=self, name='Year')
            return self._year
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._month = NumberElement(parameter=parameter, parent=self, name='Month')
            return self._month
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._day = NumberElement(parameter=parameter, parent=self, name='Day')
            return self._day
        elif parameterId == 4:
            self._month_follow_year = parameter.getValue()
            return ValueElement(parameter, self, 'MonthFollowsYear')
        elif parameterId == 5:
            self._day_follow_month = parameter.getValue()
            return ValueElement(parameter, self, 'DayFollowsMonth')
        elif parameterId == 6:
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._month_as_word = ImageSetElement(parameter=parameter, parent=self, name='MonthAsWord')
            return self._month_as_word
        elif parameterId == 7: # MonthAsWordChinese
            pass
        elif parameterId == 8:
            self._year_data_type = parameter.getValue()
            return ValueElement(parameter, self, 'YearDataTypeImageIndex')
        elif parameterId == 9:
            self._month_data_type = parameter.getValue()
            return ValueElement(parameter, self, 'MonthDataTypeImageIndex')
        elif parameterId == 10:
            self._day_data_type = parameter.getValue()
            return ValueElement(parameter, self, 'DayDataTypeImageIndex')
        elif parameterId == 11:
            self._delimiter_year = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterYearImageIndex')
        elif parameterId == 12:
            self._delimiter_month = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterMonthImageIndex')
        elif parameterId == 13:
            self._delimiter_day = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterDayImageIndex')
        elif parameterId == 14:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._datetype_year_coords = CoordinatesElement(parameter=parameter, parent=self, name='YearDataTypeCoordinates')
            return self._datetype_year_coords
        elif parameterId == 15:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._datetype_month_coords = CoordinatesElement(parameter=parameter, parent=self, name='MonthDataTypeCoordinates')
            return self._datetype_month_coords
        elif parameterId == 16:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._datetype_day_coords = CoordinatesElement(parameter=parameter, parent=self, name='DayDataTypeCoordinates')
            return self._datetype_day_coords
        else:
            return super(YearMonthAndDayElement, self).createChildForParameter(parameter)

