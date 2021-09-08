import logging

from watchFaceParser.models.gtr2.elements.basic.containerElement import ContainerElement


class WidgetElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._preview = []
        self._date = None
        self._activity = []
        super(WidgetElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getPreview(self):
        return self._preview

    def getDate(self):
        return self._date

    def getActivity(self):
        return self._activity

    def drawWidgetElement(self, drawer, images, state):
        self.draw3(drawer, images, state)

    def draw3(self, drawer, images, state):
        if self.getDate():
            self.getDate().drawDateElement(drawer, images, state)
        if self.getActivity():
            for a in self.getActivity():
                a.drawActivityElement(drawer, images, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.common.multilangImageElement import MultilangImageElement
            self._preview.append(MultilangImageElement(parameter = parameter, parent = self, name = 'Preview'))
            return self._activity
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.dateElement import DateElement
            self._date = DateElement(parameter, parent = self, name = 'Date')
            return self._date
        elif parameterId == 3:
            from watchFaceParser.models.gtr2.elements.activityElement import ActivityElement
            self._activity.append(ActivityElement(parameter = parameter, parent = self, name = 'Activity'))
            return self._activity
        else:
            return super(WidgetElement, self).createChildForParameter(parameter)

