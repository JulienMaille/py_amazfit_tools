from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.time import Time
from watchFaceParser.elements.gts2mini.basicElements.iconSet import IconSet

class TimeDigital:
    definitions = {
        1: {'Name': 'Hours', 'Type': Number},
        2: {'Name': 'HoursDataTypeImageIndex', 'Type': 'long'},
        3: {'Name': 'PaddingZeroHours', 'Type': 'bool'},
        4: {'Name': 'DelimiterHoursImageIndex', 'Type': 'long'},
        5: {'Name': 'DelimiterMinutesImageIndex', 'Type': 'long'},
        6: {'Name': 'HoursFollowPosition', 'Type': 'bool'}, # should be checked on watch, what does this do
        7: {'Name': 'DelimiterSecondsImageIndex', 'Type': 'long'},
        8: {'Name': 'Time', 'Type': Time},
    }

class TimeSpan:
    definitions = {
        1: {'Name': 'StartHour', 'Type': 'long'},
        2: {'Name': 'StartMin', 'Type': 'long'},
        3: {'Name': 'StopHour', 'Type': 'long'},
        4: {'Name': 'StopMin', 'Type': 'long'},
    }

class HourlyImage:
    definitions = {
        1: {'Name': 'IconSet', 'Type': IconSet},
        2: {'Name': 'TimeSpans', 'Type': [TimeSpan]},
    }

class HourlyImages:
    definitions = {
        1: {'Name': 'HourlyImage', 'Type': HourlyImage}, # limited to 24 images?
    }