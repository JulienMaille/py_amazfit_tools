import datetime

from watchFaceParser.models.weatherCondition import WeatherCondition


class WatchState:
    def __init__(self, BatteryLevel=67, Pulse=62, Steps=14876, Calories=764, Distance=2367,
                 Bluetooth=False, Unlocked=True, Alarm=True, DoNotDisturb=True,
                 CurrentTemperature=-10, Stand=3, PAI=30, Humidity=50, UVindex=5, AirQuality=5):
        self._time = datetime.datetime.now().replace(hour = 10, minute = 10, second = 30)
        self._steps = Steps
        self._goal = 8000
        self._distance = Distance
        self._calories = Calories
        self._pulse = Pulse
        self._batteryLevel = BatteryLevel
        self._bluetooth = Bluetooth
        self._unlocked = Unlocked
        self._alarm = Alarm
        self._doNotDisturb = DoNotDisturb
        self._stand = Stand
        self._pai = PAI
        self._humidity = Humidity
        self._uvindex = UVindex
        self._airquality = AirQuality
        self._screenidle = None
        self._currentWeather = WeatherCondition.PartlyCloudy
        self._currentTemperature = CurrentTemperature

    def getTime(self):
        return self._time

    def setTime(self, _time):
        self._time = _time

    def getSteps(self):
        return self._steps

    def getGoal(self):
        return self._goal

    def getPulse(self):
        return self._pulse

    def getBatteryLevel(self):
        return self._batteryLevel

    def getDistance(self):
        return self._distance

    def getCalories(self):
        return self._calories

    def getBluetooth(self):
        return self._bluetooth

    def getUnlocked(self):
        return self._unlocked

    def getAlarm(self):
        return self._alarm

    def getDoNotDisturb(self):
        return self._doNotDisturb

    def getWeather(self):
        return self._weather

    def getCurrentWeather(self):
        return self._currentWeather

    def getCurrentTemperature(self):
        return self._currentTemperature

    def setCurrentWeather(self, n):
        self._currentWeather = n

    def setCurrentTemperature(self, n):
        self._currentTemperature = n

    def getStand(self):
        return self._stand

    def getPai(self):
        return self._pai

    def getHumidity(self):
        return self._humidity

    def getUVindex(self):
        return self._uvindex

    def getAirQuality(self):
        return self._airquality

    def getScreenIdle(self):
        return self._screenidle

    def setScreenIdle(self, screenIdle):
        self._screenidle = screenIdle

    def toJSON(self):
        return {
            'Time': self.datetimeToJson(),
            'Steps': self._steps,
            'Goal': self._goal,
            'Pulse': self._pulse,
            'BatteryLevel': self._batteryLevel,
            'Distance': self._distance,
            'Calories': self._calories,
            'Bluetooth': self._bluetooth,
            'Unlocked': self._unlocked,
            'Alarm': self._alarm,
            'DoNotDisturb': self._doNotDisturb,
            'CurrentWeather': self._currentWeather,
            'CurrentTemperature': self._currentTemperature,
            'Stand': self._stand,
            'PAI': self._pai,
            'Humidity': self._humidity,
            'UVindex': self._uvindex,
            'AirQuality': self._airquality,
            'ScreenIdle': self._screenidle
        }

    def datetimeToJson(self):
        t = self._time
        return {'Year': t.year, 'Month': t.month, 'Day': t.day, 'Hour': t.hour, 'Minute': t.minute, 'Second': t.second}

    @staticmethod
    def fromJson(json):
        watch_state = WatchState()
        if 'Time' in json:
            time = json['Time']
            watch_state._time = datetime.datetime.now().replace(
                year=time['Year'] if 'Year' in time else watch_state._time.year,
                month=time['Month'] if 'Month' in time else watch_state._time.month,
                day=time['Day'] if 'Day' in time else watch_state._time.day,
                hour=time['Hour'] if 'Hour' in time else watch_state._time.hour,
                minute=time['Minute'] if 'Minute' in time else watch_state._time.minute,
                second=time['Second']) if 'Second' in time else watch_state._time.second
        watch_state._steps = json['Steps'] if 'Steps' in json else watch_state._steps
        watch_state._goal = json['Goal'] if 'Goal' in json else watch_state._goal
        watch_state._pulse = json['Pulse'] if 'Pulse' in json else watch_state._pulse
        watch_state._batteryLevel = json['BatteryLevel'] if 'BatteryLevel' in json else watch_state._batteryLevel
        watch_state._distance = json['Distance'] if 'Distance' in json else watch_state._distance
        watch_state._calories = json['Calories'] if 'Calories' in json else watch_state._calories
        watch_state._bluetooth = json['Bluetooth'] if 'Bluetooth' in json else watch_state._bluetooth
        watch_state._unlocked = json['Unlocked'] if 'Unlocked' in json else watch_state._unlocked
        watch_state._alarm = json['Alarm'] if 'Alarm' in json else watch_state._alarm
        watch_state._doNotDisturb = json['DoNotDisturb'] if 'DoNotDisturb' in json else watch_state._doNotDisturb
        watch_state._currentWeather = json['CurrentWeather'] if 'CurrentWeather' in json else watch_state._currentWeather
        watch_state._currentTemperature = json['CurrentTemperature'] if 'CurrentTemperature' in json else watch_state._currentTemperature
        watch_state._stand = json['Stand'] if 'Stand' in json else watch_state._stand
        watch_state._pai = json['PAI'] if 'PAI' in json else watch_state._pai
        watch_state._humidity = json['Humidity'] if 'Humidity' in json else watch_state._humidity
        watch_state._uvindex = json['UVindex'] if 'UVindex' in json else watch_state._uvindex
        watch_state._airquality = json['AirQuality'] if 'AirQuality' in json else watch_state._airquality
        watch_state._screenidle = json['ScreenIdle'] if 'ScreenIdle' in json else watch_state._screenidle
        return watch_state

