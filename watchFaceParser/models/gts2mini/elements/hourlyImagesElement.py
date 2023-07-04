import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement

class TimeSpanElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._start_hour = None
        self._start_min = None
        self._stop_hour = None
        self._stop_min = None
        super(TimeSpanElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            self._start_hour = parameter._value
            return self._start_hour
        elif parameterId == 2:
            self._start_min = parameter._value
            return self._start_min
        elif parameterId == 3:
            self._stop_hour = parameter._value
            return self._stop_hour
        elif parameterId == 4:
            self._stop_min = parameter._value
            return self._stop_min
        else:
            return super(TimeSpanElement, self).createChildForParameter(parameter)

class HourlyImageElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._iconset_progress = None
        self._timespans = []
        super(HourlyImageElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        if self._iconset_progress:
            hours = state.getTime().hour
            mins = state.getTime().minute
            idx = 0
            while idx < (len(self._timespans)-1) and not(self._timespans[idx]._start_hour*60 + self._timespans[idx]._start_hour
                      <= hours*60 + mins
                      <= self._timespans[idx]._stop_hour*60 + self._timespans[idx]._stop_min):
                idx += 1
            self._iconset_progress.draw2(drawer, resources, hours, True)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.iconSetElement import IconSetElement
            self._iconset_progress = IconSetElement(parameter = parameter, parent = self, name ='IconSetProgress')
            return self._iconset_progress
        elif parameterId == 2:
            self._timespans.append(TimeSpanElement(parameter = parameter, parent = self, name = 'TimeSpan'))
            return self._timespans
            pass
        else:
            print ("Unknown HourlyImageElement", parameterId)
            return super(HourlyImageElement, self).createChildForParameter(parameter)


class HourlyImagesElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._hourlyImages = None
        super(HourlyImagesElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        assert(type(images) == list)
        self._hourlyImages.draw3(drawer, images, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            self._hourlyImages = HourlyImageElement(parameter = parameter, parent = self, name = 'HourlyImage')
            return self._hourlyImages
        else:
            print ("Unknown HourlyImagesElement", parameterId)
            return super(HourlyImagesElement, self).createChildForParameter(parameter)


