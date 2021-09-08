class ActivityType:
    Date = 0
    Battery = 1
    Steps = 2
    Calories = 3
    HeartRate = 4
    PAI = 5
    Distance = 6
    StandUp = 7
    Weather = 8
    UVindex = 9
    AirQuality = 10
    Humidity = 11
    Sunrise = 12 # Two Images possible
    WindForce = 13 
    Altitude = 14
    AirPressure = 15
    Stress = 16
    ActivityGoal = 17
    FatBurning = 18
   
    Converter = {
        Date: 'Date',
        Battery : "Battery",
        Steps : "Steps", 
        Calories : "Calories", 
        HeartRate : "HeartRate", 
        Distance : "Distance", 
        Weather : "Weather",  
        PAI : "PAI",  
        StandUp : "StandUp",  
        UVindex : "UVindex",  
        AirQuality : "AirQuality",  
        Humidity : "Humidity",  
        Sunrise : "Sunrise",  
        WindForce : "WindForce",  
        Altitude : "Altitude",  
        AirPressure : "AirPressure",  
        Stress : "Stress",  
        ActivityGoal : "ActivityGoal",
        FatBurning  : "FatBurning",
    }

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

    def toJSON(self):
        if self._flag == None:
            self._flag = 0
        return ActivityType.Converter[self._flag]

    @staticmethod
    def fromJSON(strFlag):
        for flag in ActivityType.Converter:
            if strFlag == ActivityType.Converter[flag]:
                return flag
        return 0
