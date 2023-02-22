from watchFaceParser.elements.gts2mini.timeElements.twoDigits import TwoDigits
from watchFaceParser.elements.gts2mini.timeElements.amPmIcon import AmPmIcon
from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.analogDialFaceElements.clockHand import ClockHand
from watchFaceParser.elements.gts2mini.basicElements.coordinates import Coordinates


class AoDTimeSeparateDigits:
    definitions = {
        1: {'Name': 'Hours', 'Type': TwoDigits},
        2: {'Name': 'Minutes', 'Type': TwoDigits},
        3: {'Name': 'Separator', 'Type': Image},
        4: {'Name': 'PaddingZeroHours', 'Type': 'bool'},
    }

class AoDTimeDigital: # similar to class AlarmTime?
    definitions = {
        1: {'Name': 'Hours', 'Type': Number},
        2: {'Name': 'Minutes', 'Type': Number},
        3: {'Name': 'HoursDataTypeImageIndex', 'Type': 'long'},
        4: {'Name': 'MinutesDataTypeImageIndex', 'Type': 'long'},
        5: {'Name': 'DelimiterHoursImageIndex', 'Type': 'long'},
        6: {'Name': 'DelimiterMinutesImageIndex', 'Type': 'long'},
        7: {'Name': 'PaddingZeroHours', 'Type': 'bool'},
        8: {'Name': 'PaddingZeroMinutes', 'Type': 'bool'},
        9: {'Name': 'HoursDataTypeCoordinates', 'Type': Coordinates},
        10: {'Name': 'MinutesDataTypeCoordinates', 'Type': Coordinates},
        11: {'Name': 'MinutesFollowHours', 'Type': 'bool'},
    }

class AoDAnalogDialFace:
    definitions = {
        1: {'Name': 'CommonCenterCoordinates', 'Type': Coordinates},
        2: {'Name': 'Hours', 'Type': ClockHand},
        3: {'Name': 'Minutes', 'Type': ClockHand},
    }

class AoDTimeExtended:
    definitions = {
        1: {'Name': 'TimeSeparateDigits', 'Type': AoDTimeSeparateDigits},
        # 2:
        3: {'Name': 'TimeAnalog', 'Type': AoDAnalogDialFace}, # incompatible with AoDTimeSeparateDigits and TimeDigital
        4: {'Name': 'AmPm', 'Type': AmPmIcon},
        5: {'Name': 'TimeDigital', 'Type': AoDTimeDigital},
    }

class AoDDateOneLine:
    definitions = {
        1: {'Name': 'MonthAndDay', 'Type': Number},
        2: {'Name': 'SeparatorImageIndex', 'Type': 'long'},
    }

class AoDDate:
    definitions = {
        1: {'Name': 'Month', 'Type': Number},
        2: {'Name': 'Day', 'Type': Number},
        3: {'Name': 'MonthDataTypeImageIndex', 'Type': 'long'}, # used in combination with DayFollowsMonth
        4: {'Name': 'DayDataTypeImageIndex', 'Type': 'long'},
        5: {'Name': 'DelimiterMonthImageIndex', 'Type': 'long'},
        6: {'Name': 'DelimiterDayImageIndex', 'Type': 'long'},
        7: {'Name': 'PaddingZeroMonth', 'Type': 'bool'},
        8: {'Name': 'PaddingZeroDay', 'Type': 'bool'},
        9: {'Name': 'MonthDataTypeCoordinates', 'Type': Coordinates},
        10: {'Name': 'DayDataTypeCoordinates', 'Type': Coordinates},
        11: {'Name': 'DayFollowsMonth', 'Type': 'bool'}, # mostly false except in a611dc2d3574c2645bcbbb64028103ad.bin
    }

class AoDWeek:
    definitions = {
        1: { 'Name': 'Weekday', 'Type': ImageSet},
        2: { 'Name': 'WeekdayChinese', 'Type': ImageSet},
        3: { 'Name': 'WeekdayTradChinese', 'Type': ImageSet},
    }

class Steps:
    definitions = {
        1: { 'Name': 'ImageNumber', 'Type': Number},
        2: { 'Name': 'PrefixImageIndex', 'Type': 'long'},
        3: { 'Name': 'SuffixImageIndex', 'Type': 'long'},
    }

class AlwaysOnDisplay:
    definitions = {
        1: { 'Name': 'TimeExtended', 'Type': AoDTimeExtended},
        2: { 'Name': 'DateOneLine', 'Type': AoDDateOneLine},
        3: { 'Name': 'Week', 'Type': AoDWeek},
        4: { 'Name': 'Steps', 'Type': Steps},
        5: { 'Name': 'Date', 'Type': AoDDate},
    }

