import logging

from watchFaceParser.models.gtr2.elements.basic.containerElement import ContainerElement


class SystemElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._status = None
        self._date = None
        self._activity = []
        super(SystemElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getStatus(self):
        return self._status

    def getDate(self):
        return self._date

    def getActivity(self):
        return self._activity

    def drawSystemElement(self, drawer, images, state):
        self.draw3(drawer, images, state)

    def draw3(self, drawer, images, state):
        if self.getStatus():
            self.getStatus().drawStatusElement(drawer, images, state)
        if self.getDate():
            self.getDate().drawDateElement(drawer, images, state)
        if self.getActivity():
            for activity in self.getActivity():
                activity.drawActivityElement(drawer, images, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.statusElement import StatusElement
            self._status = StatusElement(parameter = parameter, parent = self, name = 'Status')
            return self._status
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.dateElement import DateElement
            self._date = DateElement(parameter, parent = self, name = 'Date')
            return self._date
        elif parameterId == 3:
            from watchFaceParser.models.gtr2.elements.activityElement import ActivityElement
            self._activity.append(ActivityElement(parameter = parameter, parent = self, name = 'Activity'))
            return self._activity
        else:
            print ("Unknown SystemElement",parameterId)
            return super(SystemElement, self).createChildForParameter(parameter)

