class WeatherCondition():
    Unknown = 0
    PartlyCloudy = 1
    CloudyAndRain = 2
    CloudyAndSnow = 3
    Sunny = 4
    Cloudy = 5
    LightRain = 6
    LightSnow = 7
    Rain = 8
    Snow = 9
    HeavySnow = 10
    HeavyRain = 11
    SandStorm = 12
    SnowAndRain = 13
    Fog = 14
    Haze = 15
    Storm = 16
    VeryHeavySnow = 17
    FloatingDust = 18
    Downpour = 19
    Hail = 20
    HailStorm = 21
    HeavyDownpour = 22
    BlowingDust = 23
    Tornado = 24
    VeryHeavyDownpour = 25

    def __init__(self, v):
        self.v = v

    def toJSON(self):
        return self.vs

