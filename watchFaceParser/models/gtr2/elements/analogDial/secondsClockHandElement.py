from watchFaceParser.models.gtr2.elements.common.clockHandElement import ClockHandElement


class SecondsClockHandElement(ClockHandElement):
    def __init__(self, parameter, parent = None, name = None):
        super(SecondsClockHandElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def drawSecondsClockHandElement(self, drawer, resources, state):
        assert(type(resources) == list)
        if state.getScreenIdle():
            return
        value = state.getTime().second
        maxvalue = 60
        super(SecondsClockHandElement, self).drawClockHandElement(drawer, resources, value, maxvalue)
