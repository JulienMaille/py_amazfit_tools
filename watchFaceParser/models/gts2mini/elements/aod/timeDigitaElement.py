import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class TimeDigitalElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._hours = None
        self._minutes = None
        self._padding_zero_hours = None
        self._padding_zero_minutes = None
        self._hours_data_type_image_index = None
        self._minutes_data_type_image_index = None
        self._hours_delimiter_image_index = None
        self._minutes_delimiter_image_index = None
        self._minutes_data_type_coordinates = None
        self._hours_data_type_coordinates = None
        self._minutes_follow_hours = False
        super(TimeDigitalElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, images, state):
        assert(type(images) == list)

        hours = state.getTime().hour

        followxy = None

        if self._hours:
            followxy = self._hours.draw4(drawer, images, hours, 2, self._padding_zero_hours, suffix=self._hours_delimiter_image_index)

            if self._minutes_delimiter_image_index:
                if self._minutes_follow_hours:
                    followxy = self.drawDelimiter(drawer, images, self._minutes_delimiter_image_index,
                                                  followxy[0], followxy[1])
                elif self._hours_data_type_coordinates:
                    self.drawDelimiter(drawer, images, self._hours_data_type_image_index,
                                       self._hours_data_type_coordinates.getX(),
                                       self._hours_data_type_coordinates.getY())

        if self._minutes:
            followxy = self._minutes.draw4(drawer,
                                           images,
                                           state.getTime().minute,
                                           minimum_digits= 2,
                                           force_padding = self._padding_zero_minutes,
                                           followxy = followxy if self._minutes_follow_hours else None,
                                           suffix = self._minutes_delimiter_image_index)

            if self._minutes_data_type_image_index:
                if self._minutes_data_type_coordinates:
                    self.drawDelimiter(drawer, images, self._minutes_data_type_image_index,
                                       self._minutes_data_type_coordinates.getX(),
                                       self._minutes_data_type_coordinates.getY())


    def drawDelimiter(self, drawer, images, index, x, y):
        temp = images[index].getBitmap()
        drawer.paste(temp, (x, y), temp)
        return x + temp.size[0], y


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
            self._hours_data_type_image_index = parameter.getValue()
            return ValueElement(parameter, self, 'HoursDataTypeImageIndex')
        elif parameterId == 4:
            self._minutes_data_type_image_index = parameter.getValue()
            return ValueElement(parameter, self, 'MinutesDataTypeImageIndex')
        elif parameterId == 5:
            self._hours_delimiter_image_index = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterHoursImageIndex')
        elif parameterId == 6:
            self._minutes_delimiter_image_index = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterMinutesImageIndex')
        elif parameterId == 7:
            self._padding_zero_hours = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroHours')
        elif parameterId == 8:
            self._padding_zero_minutes = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroMinutes')
        elif parameterId == 9:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._hours_data_type_coordinates = CoordinatesElement(parameter = parameter, parent = self, name ='HoursDataTypeCoordinates')
            return self._hours_data_type_coordinates
        elif parameterId == 10:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._minutes_data_type_coordinates = CoordinatesElement(parameter = parameter, parent = self, name ='MinutesDataTypeCoordinates')
            return self._minutes_data_type_coordinates
        elif parameterId == 11:
            self._minutes_follow_hours = parameter.getValue()
            return ValueElement(parameter, self, 'MinutesFollowHours')
        else:
            print ("Unknown TimeExtendedElement",parameterId)
            return super(TimeDigitalElement, self).createChildForParameter(parameter)

