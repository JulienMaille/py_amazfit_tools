from watchFaceParser.models.gtr2.elements.common.imageCoorsElement import ImageCoordsElement

class AlarmElement(ImageCoordsElement):
    def __init__(self, parameter, parent, name = None):
        super(AlarmElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def switchState(self, state):
        return state.getAlarm()

    def draw3(self, drawer, resources, state):
        if self.switchState(state):
            return super().draw3(drawer, resources, state)
