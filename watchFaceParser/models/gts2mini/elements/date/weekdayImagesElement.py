import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement

class WeekdayImagessElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._monday = None
        self._tuesday = None
        self._wednesday = None
        self._thursday = None
        self._friday = None
        self._saturday = None
        self._sunday = None
        super(WeekdayImagessElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, images, state):
        wd = state.getTime().weekday()
        if wd == 0 and self._monday:
            self._monday.draw3(drawer, images, state)
        elif wd == 1 and self._tuesday:
            self._tuesday.draw3(drawer, images, state)
        elif wd == 2 and self._wednesday:
            self._wednesday.draw3(drawer, images, state)
        elif wd == 3 and self._thursday:
            self._thursday.draw3(drawer, images, state)
        elif wd == 4 and self._friday:
            self._friday.draw3(drawer, images, state)
        elif wd == 5 and self._saturday:
            self._saturday.draw3(drawer, images, state)
        elif wd == 6 and self._sunday:
            self._sunday.draw3(drawer, images, state)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement # must be own. fix it!!
            self._monday = ImageElement(parameter = parameter, parent = self, name = 'Monday')
            return self._monday
        if parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement # must be own. fix it!!
            self._tuesday = ImageElement(parameter = parameter, parent = self, name = 'Tuesday')
            return self._tuesday
        if parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement # must be own. fix it!!
            self._wednesday = ImageElement(parameter = parameter, parent = self, name = 'Wednesday')
            return self._wednesday
        if parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement # must be own. fix it!!
            self._thursday = ImageElement(parameter = parameter, parent = self, name = 'Thursday')
            return self._thursday
        if parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement # must be own. fix it!!
            self._friday = ImageElement(parameter = parameter, parent = self, name = 'Friday')
            return self._friday
        if parameterId == 6:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement # must be own. fix it!!
            self._saturday = ImageElement(parameter = parameter, parent = self, name = 'Saturday')
            return self._saturday
        if parameterId == 7:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement # must be own. fix it!!
            self._sunday = ImageElement(parameter = parameter, parent = self, name = 'Sunday')
            return self._sunday
        else:
            return super(WeekdayImagessElement, self).createChildForParameter(parameter)
