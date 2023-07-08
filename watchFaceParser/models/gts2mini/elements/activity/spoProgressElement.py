import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement

class SpoProgressElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._image_number = None
        self._circular = None
        self._image_progress = None
        self._iconset_progress = None
        self._circle_scale = None
        self._scale = None
        self._background = None
        super(SpoProgressElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        maximal = 100 # SpO2 max 100%. >= 90% - night sleep, >= 95 - day activitys, < 90% - needed medical checkup
        import random
        state = random.randint(00, 100)
        if self._background:
            self._background.draw3(drawer, resources, state)
        if self._image_progress:
            self._image_progress.draw4(drawer, resources, state, maximal)
        if self._iconset_progress:
            self._iconset_progress.draw4(drawer, resources, state, maximal)
        if self._circle_scale:
            self._circle_scale.draw4(drawer, resources, state, maximal)
        if self._scale:
            self._scale.draw4(drawer, resources, state, maximal)
        if self._image_number:
            self._image_number.draw4(drawer,
                                     resources,
                                     state,
                                     minimum_digits= 3,
                                     force_padding = False,
                                     followxy = None)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._image_number = NumberElement(parameter, self, 'ImageNumber')
            return self._image_number
        elif parameterId == 2:
            pass
        elif parameterId == 3:
            pass
        elif parameterId == 4:
            pass
        elif parameterId == 5: 
            from watchFaceParser.models.gts2mini.elements.common.imageSetElement import ImageSetElement
            self._image_progress = ImageSetElement(parameter=parameter, parent=self, name='ImageProgress')
            return self._image_progress
        elif parameterId == 6:
            pass
        elif parameterId == 7: # BackgroundLayer 
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._background = ImageElement(parameter=parameter, parent=self, name='BackgroundLayer')
            return self._background
        elif parameterId == 8:
            pass
        else:
            print ("Unknown SpoProgressElement",parameterId)
            return super(SpoProgressElement, self).createChildForParameter(parameter)
