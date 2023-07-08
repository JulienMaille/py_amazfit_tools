import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class BatteryElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._text = None
        self._imageprogress = None
        self._iconset_progress = None
        self._scale = None
        self._icon = None
        super(BatteryElement, self).__init__(parameters=None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        if self._icon:
            self._icon.draw3(drawer, resources, state)
        if self._imageprogress:
            self._imageprogress.draw4(drawer, resources, state.getBatteryLevel(), 100)
        if self._iconset_progress:
            self._iconset_progress.draw4(drawer, resources, state.getBatteryLevel(), 100)
        if self._scale:
            self._scale.draw4(drawer, resources, state.getBatteryLevel(), 100)
        if self._text:
            self._text.draw3(drawer, resources, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.battery.batteryTextElement import BatteryTextElement
            self._text = BatteryTextElement(parameter = parameter, parent = self, name = 'BatteryText')
            return self._text
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._imageprogress = ImageSetElement(parameter = parameter, parent = self, name ='ImageProgress')
            return self._imageprogress
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.common.iconSetElement import IconSetElement
            self._iconset_progress = IconSetElement(parameter = parameter, parent = self, name ='IconSetProgress')
            return self._iconset_progress
        elif parameterId == 4:
            pass
        elif parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.common.scaleElement import ScaleElement
            self._scale = ScaleElement(parameter = parameter, parent = self, name = '_scale')
            return self._scale
        elif parameterId == 6:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._icon = ImageElement(parameter=parameter, parent=self, name='Icon')
            return self._icon
        else:
            print ("batteryElement - unimplemented:", parameterId)
            return super(BatteryElement, self).createChildForParameter(parameter)

