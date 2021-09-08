import logging
import random

from watchFaceParser.models.elements.basic.containerElement import ContainerElement
from watchFaceParser.models.gtr2.elements.common.followObject import FollowObject


class ActivityElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._type = None
        self._pointerProgress = None
        self._progressBar = None
        self._imageProgress = None
        self._digits = []
        self._icon = None
        super(ActivityElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getType(self):
        return self._type

    def getPointerProgress(self):
        return self._pointerProgress

    def getProgressBar(self):
        return self._progressBar

    def getImageProgress(self):
        return self._imageProgress

    def getDigits(self):
        return self._digits

    def getIcon(self):
        return self._icon

    from watchFaceParser.models.watchState import WatchState

    def drawActivityElement(self, drawer, images, state: WatchState):
        self.draw3(drawer, images, state)

    def draw3(self, drawer, images, state: WatchState):
        if self.getIcon():
            self.getIcon().draw3(drawer, images, None)
        number = None
        numberMin = None
        numberMax = None
        max_number = None
        max_number_length = 1
        padding_zero_length = None
        image_progress_state = None
        unit = ('', '', '')
        if self.getType() == 1 and state.getBatteryLevel() is not None: # Battery
            number = state.getBatteryLevel()
            max_number = 100
            max_number_length = 3
            image_progress_state = ( number, max_number)
            unit = ('%', "%", '%')
        elif self.getType() == 2 and state.getSteps() is not None:      # Steps
            number = state.getSteps()
            numberMin = state.getGoal()
            numberMax = state.getGoal()
            max_number = state.getGoal()
            max_number_length = 5
            image_progress_state = (number, max_number)
            unit = ('', "Steps", 'STEPS')
        elif self.getType() == 3 and state.getCalories() is not None:   # Calories
            number = state.getCalories()
            max_number = 700
            max_number_length = 4
            image_progress_state = (number, max_number)
            unit = ('', "kcal", 'Cal')
        elif self.getType() == 4 and state.getPulse() is not None:      # Pulse
            number = state.getPulse()
            max_number = 250
            max_number_length = 3
            image_progress_state = (number, max_number)
            unit = ('', "bpm", 'BPM')
        elif self.getType() == 5 and state.getPai() is not None:        # PAI
            number = state.getPai()
            max_number = 100
            max_number_length = 3
            image_progress_state = (number, max_number)
        elif self.getType() == 6 and state.getDistance() is not None:   # Distance
            number = state.getDistance() 
            max_number = state.getGoal() / 1000
            max_number_length = 4
            unit = ('', "km", 'KM')
        elif self.getType() == 7 and state.getStand() is not None:      # Stand
            number = state.getStand()
            max_number = 12
            max_number_length = 2
            image_progress_state = (number, max_number)
        elif self.getType() == 8:                                       # Weather
            number = state.getCurrentTemperature() 
            numberMin = state.getCurrentTemperature() - 10
            numberMax = state.getCurrentTemperature() + 10
            max_number = 99
            image_progress_state = (state.getCurrentWeather(), 29)
            max_number_length = 2
            padding_zero_length = 3
            unit = ('°C', '°C', '°C')
        elif self.getType() == 9:                                       # UV Index
            number = state.getUVindex()
            max_number = 12
            max_number_length = 2
            image_progress_state = (number, max_number)
        elif self.getType() == 10:                                      # AirQuality
            number = state.getUVindex() * 40
            max_number = 500
            max_number_length = 3
            image_progress_state = (number, max_number)
        elif self.getType() == 11:                                      # Humidity
            number = state.getHumidity()
            max_number = 100
            max_number_length = 3
            image_progress_state = (number, max_number)
            unit = ('°C', '%', '%')
        elif self.getType() == 12:                                      # Sunrise
            number = random.randint(1, 2)
            number = "06:33"
            numberMin = "06:33"
            numberMax = "19:42"
            max_number = 2
            max_number_length = 5
            image_progress_state = (random.randint(1, 2), 29)
        elif self.getType() == 13:                                      # WindForce
            number = random.randint(1, 12)
            max_number = 12
            max_number_length = 2
            image_progress_state = (number, max_number)
        elif self.getType() == 14:                                      # Altitude
            number = random.randint(1, 999)
            max_number = 999
            max_number_length = 3
            image_progress_state = (number, max_number)
        elif self.getType() == 15:                                      # AirPressure
            number = random.randint(1, 999)
            max_number = 999
            max_number_length = 3
            image_progress_state = (number, max_number)
            unit = ('', 'KPA', 'KPA')
        elif self.getType() == 16:                                      # Stress
            number = random.randint(1, 999)
            max_number = 999
            max_number_length = 3
            image_progress_state = (number, max_number)
        elif self.getType() == 17:                                      # ActivityGoal
            number = random.randint(1, 999)
            max_number = 999
            max_number_length = 3
            padding_zero_length = 4
            image_progress_state = (number, max_number)
        elif self.getType() == 18:                                      # FatBurning
            number = random.randint(1, 99)
            max_number = 99
            max_number_length = 3
            image_progress_state = (number, max_number)

        if padding_zero_length is None:
            padding_zero_length = max_number_length
            
        if self.getIcon():
            self.getIcon().draw3(drawer, images, None)
        if number is not None:
            if self.getImageProgress():
                self.getImageProgress().drawImageProgressElement(drawer, images, image_progress_state)
            if self.getProgressBar():
                self.getProgressBar().drawProgressBarElement(drawer, images, number, max_number)
            if self.getPointerProgress():
                self.getPointerProgress().drawClockHandElement(drawer, images, number, max_number)
            if self.getDigits():
                follow_object = FollowObject()
                for d in self.getDigits():
                    follow_object = d.drawDigitalCommonDigitElement(drawer,
                                                                    images,
                                                                    number,
                                                                    numberMin,
                                                                    numberMax,
                                                                    max_number_length,
                                                                    padding_zero_length,
                                                                    unit,
                                                                    follow_object)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._type = parameter.getValue()
            return ValueElement(parameter, self, 'Type')
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.common.clockHandElement import ClockHandElement
            self._pointerProgress = ClockHandElement(parameter = parameter, parent = self, name = 'PointerProgress')
            return self._pointerProgress
        elif parameterId == 3:
            from watchFaceParser.models.gtr2.elements.common.progressBarElement import ProgressBarElement
            self._progressBar = ProgressBarElement(parameter = parameter, parent = self, name = 'ProgressBar')
            return self._progressBar
        elif parameterId == 4:
            from watchFaceParser.models.gtr2.elements.common.imageProgressElement import ImageProgressElement
            self._imageProgress = ImageProgressElement(parameter=parameter, parent=self, name='ImageProgress')
            return self._imageProgress
        elif parameterId == 5:
            from watchFaceParser.models.gtr2.elements.common.digitalCommonDigitElement import DigitalCommonDigitElement
            self._digits.append(DigitalCommonDigitElement(parameter = parameter, parent = self, name = 'Digits'))
            return self._digits
        elif parameterId == 7:
            from watchFaceParser.models.gtr2.elements.common.imageCoorsElement import ImageCoordsElement
            self._icon = ImageCoordsElement(parameter = parameter, parent = self, name = 'Icon')
            return self._icon
        else:
            return super(ActivityElement, self).createChildForParameter(parameter)

