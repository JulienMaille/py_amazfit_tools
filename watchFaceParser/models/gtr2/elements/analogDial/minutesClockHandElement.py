﻿from watchFaceParser.models.gtr2.elements.common.clockHandElement import ClockHandElement


class MinutesClockHandElement(ClockHandElement):
    def __init__(self, parameter, parent = None, name = None):
        super(MinutesClockHandElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        value = state.getTime().minute
        maxvalue = 60
        super(MinutesClockHandElement, self).draw4(drawer, resources, value, maxvalue)
