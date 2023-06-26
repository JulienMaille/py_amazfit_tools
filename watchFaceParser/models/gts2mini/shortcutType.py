class ShortcutType:
    ShortcutType0 = 0
    ShortcutType1 = 1
    ShortcutType2 = 2
    ShortcutType3 = 3
    ShortcutType4 = 4
    Workout = 5
    ShortcutType6 = 6
    ShortcutType7 = 7
    ShortcutType8 = 8
    ShortcutType9 = 9
    CycleTracking = 10
    ShortcutType11 = 11
    ShortcutType12 = 12
    ShortcutType13 = 13
    ShortcutType14 = 14
    ShortcutType15 = 15
    Music = 16
    Countdown = 17
    StopWatch = 18
    Pomodoro = 19
    ShortcutType20 = 20
    ShortcutType21 = 21
    Compass = 22
    ShortcutType23 = 23
    ShortcutType24 = 24
    Voice = 25
    # tested all up to 67

    Converter = {
        ShortcutType0: "ShortcutType0",
        ShortcutType1: "ShortcutType1",
        ShortcutType2: "ShortcutType2",
        ShortcutType3: "ShortcutType3",
        ShortcutType4: "ShortcutType4",
        Workout: "Workout",
        ShortcutType6: "ShortcutType6",
        ShortcutType7: "ShortcutType7",
        ShortcutType8: "ShortcutType8",
        ShortcutType9: "ShortcutType9",
        CycleTracking: "CycleTracking",
        ShortcutType11: "ShortcutType11",
        ShortcutType12: "ShortcutType12",
        ShortcutType13: "ShortcutType13",
        ShortcutType14: "ShortcutType14",
        ShortcutType15: "ShortcutType15",
        Music: "Music",
        Countdown: "Countdown",
        StopWatch: "StopWatch",
        Pomodoro: "Pomodoro",
        ShortcutType20: "ShortcutType20",
        ShortcutType21: "ShortcutType21",
        Compass: "Compass",
        ShortcutType23: "ShortcutType23",
        ShortcutType24: "ShortcutType24",
        Voice: "Voice",
    }

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

    def toJSON(self):
        if self._flag == None:
            self._flag = 0
        print(self._flag)
        return ShortcutType.Converter[self._flag]

    @staticmethod
    def fromJSON(strFlag):
        for flag in ShortcutType.Converter:
            if strFlag == ShortcutType.Converter[flag]:
                return flag
        return 0
