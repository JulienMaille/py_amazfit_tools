import logging

from watchFaceParser.models.gtr2.elements.basic.containerElement import ContainerElement


class WatchFace(ContainerElement):
    def __init__(self, parameters):
        self._background = None
        self._dialface = None
        self._system = None
        self._widgets = None
        self._screenidle = None
        super(WatchFace, self).__init__(parameters, parameter = None, parent = None, name = '')


    def getBackground(self):
        return self._background


    def getDialFace(self):
        return self._dialface

    def getSystem(self):
        return self._system

    def getWidgets(self):
        return self._widgets

    def getScreenIdle(self):
        return self._screenidle

    def draw3(self, drawer, images, state):
        if state.getScreenIdle() is None:
            if self.getBackground():
                self.getBackground().drawBackgroundElement(drawer, images, state)
            if self.getSystem():
                self.getSystem().drawSystemElement(drawer, images, state)
            if self.getWidgets():
                self.getWidgets().drawWidgetsElement(drawer, images, state)
            if self.getDialFace():
                self.getDialFace().drawScreenNormalElement(drawer, images, state)
        else:
            if self._screenidle:
                self._screenidle.drawScreenIdleElement(drawer, images, state)
            else:
                self.drawBackground(drawer)
            if self._screenidle is None or self._screenidle.getScreenNormal() is None:
                if self.getDialFace():
                    self.getDialFace().drawScreenNormalElement(drawer, images, state)

    def drawBackground(self, drawer):
        x = 0
        y = 0
        from PIL import ImageDraw, Image
        from resources.image.color import Color
        from watchFaceParser.config import Config
        color = Color.fromArgb(0xff000000)
        size = Config.getImageSize()
        d = ImageDraw.Draw(drawer)
        d.rectangle([(x, y), size], fill=color)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        logging.debug(f'>>>>>>>>>>>> {parameterId} {parameter}')
        if parameterId == 0:
            pass
        elif parameterId == 3:
            from watchFaceParser.models.gtr2.elements.backgroundElement import BackgroundElement
            self._background = BackgroundElement(parameter)
            return self._background
        elif parameterId == 4:
            pass
            from watchFaceParser.models.gtr2.elements.screenNormalElement import ScreenNormalElement
            self._dialface = ScreenNormalElement(parameter)
            return self._dialface
        elif parameterId == 5:
            pass
            from watchFaceParser.models.gtr2.elements.systemElement import SystemElement
            self._system = SystemElement(parameter)
            return self._system
        elif parameterId == 6:
            pass
            from watchFaceParser.models.gtr2.elements.widgetsElement import WidgetsElement
            self._widgets = WidgetsElement(parameter)
            return self._widgets
        elif parameterId == 10:
            from watchFaceParser.models.gtr2.elements.screenIdleElement import ScreenIdleElement
            self._screenidle = ScreenIdleElement(parameter)
            return self._screenidle
        else:
            print ("Unknown WatchFace",parameterId)
            return super(WatchFace, self).createChildForParameter(parameter)
