import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement

class PaiProgressElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._circular = None
        self._pointer_scale = None
        self._image_progress = None
        self._iconset_progress = None
        self._circle_scale = None
        self._scale = None
        self._background = None
        super(PaiProgressElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        goal = 100
        if self._background:
            self._background.draw3(drawer, resources, state)
        if self._pointer_scale:
            self._pointer_scale.draw4(drawer, resources, state.getPai(), goal)
        if self._image_progress:
            self._image_progress.draw4(drawer, resources, state.getPai(), goal)
        if self._iconset_progress:
            self._iconset_progress.draw4(drawer, resources, state.getPai(), goal)
        if self._circle_scale:
            self._circle_scale.draw4(drawer, resources, state.getPai(), goal)
        if self._scale:
            self._scale.draw4(drawer, resources, state.getPai(), goal)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.pointerScaleElement import PointerScaleElement
            self._pointer_scale = PointerScaleElement(parameter=parameter, parent=self, name='ImageProgress')
            return self._pointer_scale
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._image_progress = ImageSetElement(parameter=parameter, parent=self, name='ImageProgress')
            return self._image_progress
        elif parameterId == 3:
            pass
        elif parameterId == 4:
            pass
        elif parameterId == 5:
            pass
        elif parameterId == 6: # BackgroundLayer 
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._background = ImageElement(parameter=parameter, parent=self, name='BackgroundLayer')
            return self._background
        elif parameterId == 7:
            pass
        elif parameterId == 8:
            pass
        else:
            print ("Unknown PaiProgressElement",parameterId)
            return super(PaiProgressElement, self).createChildForParameter(parameter)
