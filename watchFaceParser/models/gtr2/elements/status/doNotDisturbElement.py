from watchFaceParser.models.gtr2.elements.common.imageCoorsElement import ImageCoordsElement

class DoNotDisturbElement(ImageCoordsElement):
    def __init__(self, parameter, parent, name = None):
        super(DoNotDisturbElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def switchState(self, state):
        return state.getDoNotDisturb()

    def draw3(self, drawer, resources, state):
        if self.switchState(state):
            return super().draw3(drawer, resources, state)
