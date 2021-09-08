from watchFaceParser.models.gtr2.elements.common.imageCoorsElement import ImageCoordsElement

class UnlockedElement(ImageCoordsElement):
    def __init__(self, parameter, parent, name = None):
        super(UnlockedElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def switchState(self, state):
        return state.getUnlocked()

    def draw3(self, drawer, resources, state):
        if self.switchState(state):
            return super().draw3(drawer, resources, state)
