import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement

class AlarmElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._no_alarm = None
        self._alarm = None
        self._alarm_time = None
        super(AlarmElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, images, state):
        if state.getAlarm():
            if self._alarm_time:
                self._alarm_time.draw3(drawer, images, state)
            if self._alarm:
                self._alarm.draw3(drawer, images, state)
        else:
            if self._no_alarm:
                self._no_alarm.draw3(drawer, images, state)
            

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            pass
        elif parameterId == 2:
            pass
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._no_alarm = ImageElement(parameter=parameter, parent=self, name='NoAlarmImage')
            return self._no_alarm
        elif parameterId == 4:
            pass
        elif parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._alarm = ImageElement(parameter=parameter, parent=self, name='AlarmImage')
            return self._alarm
        elif parameterId == 6:
            pass
        elif parameterId == 7:
            from watchFaceParser.models.gts2mini.elements.alarm.alarmTimeElement import AlarmTimeElement
            self._alarm_time = AlarmTimeElement(parameter=parameter, parent=self, name='AlarmTime')
            return self._alarm_time
        else:
            return super(AlarmElement, self).createChildForParameter(parameter)
