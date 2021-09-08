from watchFaceParser.models.gtr2.elements.common.imageCoorsElement import ImageCoordsElement


class BluetoothElement(ImageCoordsElement):
    def __init__(self, parameter, parent, name = None):
        super(BluetoothElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def switchState(self, state):
        return state.getBluetooth()
    
    def draw3(self, drawer, resources, state):
        if not self.switchState(state):
            return super().draw3(drawer, resources, state)

