from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class TimeDigitalElement(ContainerElement):
    def __init__(self, parameter, parent, name = None):
        self._hours = None
        self._minutes = None
        self._data_type_hours = None
        self._minutes_data_type = None
        self._padding_zero_hours = None
        self._padding_zero_minutes = None
        self._delimiter_hours = None
        self._delimiter_minutes = None
        self._data_type_hours_coordinates = None
        self._data_type_minutes_coordinates = None
        self._minutes_follow_hours = None
        super(TimeDigitalElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        assert(type(images) == list)

        if self._hours:
            followxy = self._hours.draw4(drawer, images, state.getTime().hour, 2, self._padding_zero_hours, suffix=self._delimiter_hours)

            if self._data_type_hours:
                if self._minutes_follow_hours:
                    followxy = self.drawDelimiter(drawer, images, self._data_type_hours, followxy[0], followxy[1])
                elif self._data_type_hours_coordinates:
                    self.drawDelimiter(drawer, images, self._data_type_hours,
                                       self._data_type_hours_coordinates.getX(),
                                       self._data_type_hours_coordinates.getY())

        if self._minutes:
            self._minutes.draw4(drawer, images, state.getTime().minute, 2, self._padding_zero_minutes,
                                followxy = followxy if self._minutes_follow_hours else None,
                                suffix = self._delimiter_minutes)

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement

        parameterId = parameter.getId()

        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._hours = NumberElement(parameter, self, 'Hours')
            return self._hours
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._minutes = NumberElement(parameter, self, 'Minutes')
            return self._minutes
        elif parameterId == 3:
            self._data_type_hours = parameter.getValue()
            return ValueElement(parameter, self, 'HoursDataTypeImageIndex')
            return self._seconds
        elif parameterId == 4:
            self._data_type_minutes = parameter.getValue()
            return ValueElement(parameter, self, 'MinutesDataTypeImageIndex')
        elif parameterId == 5:
            self._delimiter_hours = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterHours')
        elif parameterId == 6:
            self._delimiter_minutes = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterMinutes')
        elif parameterId == 7:
            self._padding_zero_hours = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroHours')
        elif parameterId == 8:
            self._padding_zero_minutes = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroMinutes')
        elif parameterId == 9:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._data_type_hours_coordinates = CoordinatesElement(parameter = parameter, parent = self, name ='HoursDataTypeCoordinates')
            return self._data_type_hours_coordinates
        elif parameterId == 10:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._data_type_minutes_coordinates = CoordinatesElement(parameter = parameter, parent = self, name ='MinutesDataTypeCoordinates')
            return self._data_type_minutes_coordinates
        elif parameterId == 11:
            self._minutes_follow_hours = parameter.getValue()
            return ValueElement(parameter, self, 'MinutesFollowHours')
            return self._minutes_follow_hours
        else:
            super(TimeDigitalElement, self).createChildForParameter(parameter)
