import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class DateBlockElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._date = None
        self._ampm = None
        self._weekDay = None
        self._weekDayProgress = None
        self._weekDayPointerScale = None
        super(DateBlockElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        assert(type(images) == list)

        for element in self.getDrawableChildren():
            element.draw3(drawer, images, state)

        if self._weekDayPointerScale:
            self._weekDayPointerScale.draw4(drawer, images, state.getTime().weekday(), 6)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.dateElement import DateElement
            self._date = DateElement(parameter = parameter, parent = self, name = 'Date')
            return self._date
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.date.ampmElement import AmPmElement
            self._ampm = AmPmElement(parameter = parameter, parent = self, name = 'AmPm')
            return self._ampm
        elif parameterId == 3:
            pass
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.date.weekDayElement import WeekDayElement
            self._weekDay = WeekDayElement(parameter = parameter, parent = self, name = 'Weekday')
            return self._weekDay
        elif parameterId == 5: # WeekdayChinese
            pass
        elif parameterId == 6: # WeekdayTradChinese
            pass
        elif parameterId == 7:
            from watchFaceParser.models.gts2mini.elements.date.weekDayProgressElement import WeekDayProgressElement
            self._weekDayProgress = WeekDayProgressElement(parameter=parameter, parent=self, name='WeekdayProgress')
            return self._weekDayProgress
        elif parameterId == 8:
            from watchFaceParser.models.gts2mini.elements.common.scaleElement import ScaleElement
            self._weekDayPointerScale = ScaleElement(parameter=parameter, parent=self, name='WeekdayPointerScale')
            return self._weekDayPointerScale
        else:
            return super(DateBlockElement, self).createChildForParameter(parameter)
