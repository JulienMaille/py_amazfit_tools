import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement
from watchFaceParser.config import Config

class WatchFace(ContainerElement):
    def __init__(self, parameters):
        self._background = None
        self._time_extended = None
        self._activity = None
        self._date = None
        self._weather = None
        self._stepsProgress = None
        self._caloriesProgress = None
        self._heartProgress = None
        self._standUpProgress = None
        self._humidityProgress = None
        self._uviProgress = None
        self._airQualityProgress = None
        self._daysProgress = None
        self._status = None
        self._battery = None
        self._animation = None
        self._analogDial = None
        self._shortcuts = None
        self._digitalTime = None
        self._hourlyImages = None
        self._weather = None
        self._activity_separate_digits = None
        self._paiProgress = None
        self._stressProgress = None
        self._spoProgress = None
        self._alarm = None
        self._aod = None
        super(WatchFace, self).__init__(parameters, parameter = None, parent = None, name = '')

    def draw3(self, drawer, images, state):
        if state.getScreenIdle() is None:
            super(WatchFace, self).draw3(drawer, images, state)
            if self._animation:
                self._animation.draw3(drawer, images, state) # draw animaiton on top
        else:
            if self._aod and not Config.isBip3Mode():
                self.drawBlackBackground(drawer)
                self._aod.draw3(drawer, images, state)
            else: # no AOD - normal Screen
                super(WatchFace, self).draw3(drawer, images, state)
                if self._animation:
                    self._animation.draw3(drawer, images, state) # draw animaiton on top
            return

    def drawBlackBackground(self, drawer):
        from resources.image.color import Color
        from PIL import ImageDraw, Image
        from watchFaceParser.config import Config
        _color = Color.fromArgb(0xff000000)
        size = Config.getImageSize()
        d = ImageDraw.Draw(drawer)
        d.rectangle([(0, 0), size], fill=_color)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        logging.debug(f'>>>>>>>>>>>> {parameterId} {parameter}')
        if parameterId == 0:
            pass
        elif parameterId == 1:
            pass
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.backgroundElement import BackgroundElement
            self._background = BackgroundElement(parameter)
            return self._background
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.timeExtendedElement import TimeExtendedElement
            self._time_extended = TimeExtendedElement(parameter)
            return self._time_extended
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.activityElement import ActivityElement
            self._activity = ActivityElement(parameter)
            return self._activity
        elif parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.dateBlockElement import DateBlockElement
            self._date = DateBlockElement(parameter)
            return self._date
        elif parameterId == 6:
            from watchFaceParser.models.gts2mini.elements.weatherElement import WeatherElement
            self._weather = WeatherElement(parameter)
            return self._weather
        elif parameterId == 7:
            from watchFaceParser.models.gts2mini.elements.activity.stepProgressElement import StepProgressElement
            self._stepsProgress = StepProgressElement(parameter)
            return self._stepsProgress
        elif parameterId == 8:
            from watchFaceParser.models.gts2mini.elements.statusElement import StatusElement
            self._status = StatusElement(parameter)
            return self._status
        elif parameterId == 9:
            from watchFaceParser.models.gts2mini.elements.batteryElement import BatteryElement
            self._battery = BatteryElement(parameter)
            return self._battery
        elif parameterId == 10:
            pass
        elif parameterId == 11: # animation
            from watchFaceParser.models.gts2mini.elements.animationContainerElement import AnimationContainerElement
            self._animation = AnimationContainerElement(parameter)
            return self._animation
        elif parameterId == 12: # heart progress
            from watchFaceParser.models.gts2mini.elements.activity.pulseProgressElement import PulseProgressElement
            self._heartProgress = PulseProgressElement(parameter)
            return self._heartProgress
        elif parameterId == 13: #
            pass
        elif parameterId == 14: #
            pass
        elif parameterId == 15: # calories progress
            from watchFaceParser.models.gts2mini.elements.activity.caloriesProgressElement import CaloriesProgressElement
            self._caloriesProgress = CaloriesProgressElement(parameter)
            return self._caloriesProgress
        elif parameterId == 16:  #
            pass
        elif parameterId == 17:  #
            from watchFaceParser.models.gts2mini.elements.weather.humidityProgressElement import HumidityProgressElement
            self._humidityProgress = HumidityProgressElement(parameter)
            return self._humidityProgress
        elif parameterId == 18:  # Alarm
            from watchFaceParser.models.gts2mini.elements.alarmElement import AlarmElement
            self._alarm = AlarmElement(parameter)
            return self._alarm
        elif parameterId == 19: #
            from watchFaceParser.models.gts2mini.elements.shortcutsElement import ShortcutsElement
            self._shortcuts = ShortcutsElement(parameter)
            return self._shortcuts
        elif parameterId == 20:
            from watchFaceParser.models.gts2mini.elements.analogDialElement import AnalogDialElement
            self._analogDial = AnalogDialElement(parameter)
            return self._analogDial
        elif parameterId == 21:
            from watchFaceParser.models.gts2mini.elements.digitalDialElement import DigitalDialElement
            self._digitalTime = DigitalDialElement(parameter)
            return self._digitalTime
        elif parameterId == 22:
            from watchFaceParser.models.gts2mini.elements.hourlyImagesElement import HourlyImagesElement
            self._hourlyImages = HourlyImagesElement(parameter)
            return self._hourlyImages
        elif parameterId == 23:
            from watchFaceParser.models.gts2mini.elements.activity.paiProgressElement import PaiProgressElement
            self._paiProgress = PaiProgressElement(parameter)
            return self._paiProgress
        elif parameterId == 24:
            from watchFaceParser.models.gts2mini.elements.activity.standupProgressElement import StandUpProgressElement
            self._standUpProgress = StandUpProgressElement(parameter)
            return self._standUpProgress
        elif parameterId == 25:
            from watchFaceParser.models.gts2mini.elements.weather.airQualityProgressElement import AirQualityProgressElement
            self._airQualityProgress = AirQualityProgressElement(parameter)
            return self._airQualityProgress
        elif parameterId == 26:
            from watchFaceParser.models.gts2mini.elements.weather.uviProgressElement import UviProgressElement
            self._uviProgress = UviProgressElement(parameter)
            return self._uviProgress
        elif parameterId == 27:
            from watchFaceParser.models.gts2mini.elements.activity.stressProgressElement import StressProgressElement
            self._stressProgress = StressProgressElement(parameter)
            return self._stressProgress
        elif parameterId == 28:
            from watchFaceParser.models.gts2mini.elements.activity.spoProgressElement import SpoProgressElement
            self._spoProgress = SpoProgressElement(parameter)
            return self._spoProgress
        elif parameterId == 29:
            from watchFaceParser.models.gts2mini.elements.aodElement import AodElement
            self._aod = AodElement(parameter)
            return self._aod
        elif parameterId == 30:
            from watchFaceParser.models.gts2mini.elements.activity.activitySeparateDigitsElement import \
                ActivitySeparateDigitsElement
            self._activity_separate_digits = ActivitySeparateDigitsElement(parameter)
            return self._activity_separate_digits
        else:
            print ("Unknown WatchFace",parameterId)
            return super(WatchFace, self).createChildForParameter(parameter)
