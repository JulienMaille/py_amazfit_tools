class ShortcutType:
    Workout = 5
    CycleTracking = 10
    Music = 16
    Countdown = 17
    StopWatch = 18
    Pomodoro = 19
    Compass = 22
    Voice = 25
    # tested all up to 67

    Converter = {
        Workout: "Workout",
        CycleTracking: "CycleTracking",
        Music: "Music",
        Countdown: "Countdown",
        StopWatch: "StopWatch",
        Pomodoro: "Pomodoro",
        Compass: "Compass",
        Voice: "Voice",
    }

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

    def toJSON(self):
        if self._flag == None:
            self._flag = 0
        return ShortcutType.Converter[self._flag]

    @staticmethod
    def fromJSON(strFlag):
        for flag in ShortcutType.Converter:
            if strFlag == ShortcutType.Converter[flag]:
                return flag
        return 0
