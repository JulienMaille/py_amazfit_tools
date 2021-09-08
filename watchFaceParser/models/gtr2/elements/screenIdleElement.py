import logging

from watchFaceParser.models.gtr2.elements.basic.containerElement import ContainerElement
from watchFaceParser.config import Config
from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
from resources.image.color import Color

class ScreenIdleElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._screennormal = None
        self._date = None
        self._activity = []
        self._backgroundImageIndex = None

        super(ScreenIdleElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getScreenNormal(self):
        return self._screennormal

    def getDate(self):
        return self._date

    def getActivity(self):
        return self._activity

    def getBackgroundImageIndex(self):
        return self._backgroundImageIndex

    def drawScreenIdleElement(self, drawer, images, state):
        self.draw3(drawer, images, state)

    def draw3(self, drawer, images, state):
        self.drawBackground(drawer, images)
        if self.getDate():
            self.getDate().drawDateElement(drawer, images, state)
        if self.getActivity():
            for a in self.getActivity():
                a.drawActivityElement(drawer, images, state)
        if self.getScreenNormal():
            self.getScreenNormal().drawScreenNormalElement(drawer, images, state)

    def drawBackground(self, drawer, images):
        x = 0
        y = 0

        from PIL import ImageDraw, Image

        if self._backgroundImageIndex is None:
            color = Color.fromArgb(0xff000000)
            size = Config.getImageSize()
            d = ImageDraw.Draw(drawer)
            d.rectangle([(x, y), size], fill=color)
        else:
            temp = images[self._backgroundImageIndex].getBitmap()
            drawer.paste(temp, (x, y), temp)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.screenNormalElement import ScreenNormalElement
            self._screennormal = ScreenNormalElement(parameter = parameter)
            return self._screennormal
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.dateElement import DateElement
            self._date = DateElement(parameter, parent = self, name = 'Date')
            return self._date
        elif parameterId == 3:
            from watchFaceParser.models.gtr2.elements.activityElement import ActivityElement
            self._activity.append(ActivityElement(parameter = parameter))
            return self._activity
        elif parameterId == 4:
            self._backgroundImageIndex = parameter.getValue() - Config.getStartImageIndex()
            return ValueElement(parameter, self, '?BackgroundImageIndex?')
        else:
            print ("Unknown ScreenIdleElement",parameterId)
            return super(ScreenIdleElement, self).createChildForParameter(parameter)

