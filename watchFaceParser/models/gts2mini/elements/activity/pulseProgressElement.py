import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement

class PulseProgressElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._circular = None
        self._image_progress = None
        self._iconset_progress = None
        self._circle_scale = None
        self._scale = None
        self._background = None
        super(PulseProgressElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        import random
        maximal = 150
        if self._background:
            self._background.draw3(drawer, resources, state)
        if self._image_progress:
            self._image_progress.draw4(drawer, resources, state.getPulse(), maximal)
        if self._iconset_progress:
            self._iconset_progress.draw4(drawer, resources, state.getPulse(), maximal)
        if self._circle_scale:
            self._circle_scale.draw4(drawer, resources, state.getPulse(), maximal)
        if self._scale:
            self._scale.draw4(drawer, resources, state.getPulse(), maximal)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            pass
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._image_progress = ImageSetElement(parameter=parameter, parent=self, name='ImageProgress')
            return self._image_progress
        elif parameterId == 3:
            pass
            from watchFaceParser.models.gts2mini.elements.common.iconSetElement import IconSetElement
            self._iconset_progress = IconSetElement(parameter = parameter, parent = self, name ='IconSetProgress')
            return self._iconset_progress
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.common.circularProgressElement import CircularProgressElement
            self._circle_scale = CircularProgressElement(parameter=parameter, parent=self, name='CircleScale')
            return self._circle_scale
        elif parameterId == 5:
            pass
        elif parameterId == 6:
            pass
            from watchFaceParser.models.gts2mini.elements.common.scaleElement import ScaleElement
            self._scale = ScaleElement(parameter = parameter, parent = self, name = 'Scale')
            return self._scale
        elif parameterId == 7: # BackgroundLayer
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._background = ImageElement(parameter=parameter, parent=self, name='BackgroundLayer')
            return self._background
        else:
            print ("Unknown PulseProgressElement",parameterId)
            return super(PulseProgressElement, self).createChildForParameter(parameter)
