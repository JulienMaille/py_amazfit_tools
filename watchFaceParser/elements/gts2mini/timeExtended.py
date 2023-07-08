from watchFaceParser.elements.gts2mini.timeElements.twoDigits import TwoDigits
from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.shortcutsElements.element import Element

class TimeSeparateDigits:
    definitions = {
        1: {'Name': 'Hours', 'Type': TwoDigits},
        2: {'Name': 'Minutes', 'Type': TwoDigits},
        3: {'Name': 'Seconds', 'Type': TwoDigits},
        4: {'Name': 'DrawOrder', 'Type': 'long?'}, # fa8a3747713543ddbfebbfcf25cfe3f8.bin - 13330 0x3412 -> 3,4,1,2 -> m1,m2,h1,h2
        5: {'Name': 'SeparatorHours', 'Type': Image}, # separator hours ?
        6: {'Name': 'SeparatorMinutes', 'Type': Image}, # separator minutes ?
        7: {'Name': 'UnknowBoolean7', 'Type': 'bool'}, # no effect on padding zerro. no idea
        8: {'Name': 'PaddingZeroMinutes', 'Type': 'bool'}, # padding zero for both: hours and minutes
    }

class TimeExtended:
    definitions = {
        1: {'Name': 'TimeSeparateDigits', 'Type': TimeSeparateDigits},
        2: {'Name': 'SunsetTimeOneLine', 'Type': Number},
        3: {'Name': 'DelimiterSunsetImageIndex', 'Type': 'long'},
        4: {'Name': 'SunriseTimeOneLine', 'Type': Number},
        5: {'Name': 'DelimiterSunriseImageIndex', 'Type': 'long'},
        6: {'Name': 'SunsetIcon', 'Type': Image},
        7: {'Name': 'SunriseIcon', 'Type': Image},
        8: {'Name': 'SunsetShortcut', 'Type': Element},
        9: {'Name': 'SunriseShortcut', 'Type': Element},
        11: {'Name': 'SunriseImageIndex', 'Type': 'long'},
        12: {'Name': 'SunsetImageIndex', 'Type': 'long'},
    }

