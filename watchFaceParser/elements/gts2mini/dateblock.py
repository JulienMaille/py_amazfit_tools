from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.date import Date
from watchFaceParser.elements.gts2mini.timeElements.amPmIcon import AmPmIcon
from watchFaceParser.elements.gts2mini.progress import ProgressWeekday
from watchFaceParser.elements.gts2mini.basicElements.pointerScale import PointerScale


class WeekdayPointerScale:
    definitions = {
        1: {'Name': 'PointerScale', 'Type': PointerScale},
    }

class DateBlock:
    definitions = {
        1: { 'Name': 'Date', 'Type': Date},
        2: { 'Name': 'AmPm', 'Type': AmPmIcon},
        #3: { 'Name': 'Unknown3', 'Type': 'long?'},
        4: { 'Name': 'Weekday', 'Type': ImageSet},
        5: { 'Name': 'WeekdayChinese', 'Type': ImageSet},
        6: { 'Name': 'WeekdayTradChinese', 'Type': ImageSet},
        7: { 'Name': 'WeekdayProgress', 'Type': ProgressWeekday}, # 6608e628967af66d1b74f8f9952596d7.bin
        8: { 'Name': 'WeekdayPointerScale', 'Type': WeekdayPointerScale}
    }


class WeekDayImages:
    definitions = {
        1: {'Name': 'Monday', 'Type': Image},
        2: {'Name': 'Tuesday', 'Type': Image},
        3: {'Name': 'Wednesday', 'Type': Image},
        4: {'Name': 'Thursday', 'Type': Image},
        5: {'Name': 'Friday', 'Type': Image},
        6: {'Name': 'Saturday', 'Type': Image},
        7: {'Name': 'Sunday', 'Type': Image},
    }
