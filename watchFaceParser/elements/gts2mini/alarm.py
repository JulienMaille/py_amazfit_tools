from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.basicElements.coordinates import Coordinates
from watchFaceParser.elements.gts2mini.shortcutsElements.element import Element

class AlarmTime:
    definitions = {
        1: { 'Name': 'Hours', 'Type': Number},
        2: { 'Name': 'Minutes', 'Type': Number},
        3: { 'Name': 'HoursDataTypeImageIndex', 'Type': 'long'},
        5: { 'Name': 'DelimiterHoursImageIndex', 'Type': 'long'},
        6: { 'Name': 'DelimiterMinutesImageIndex', 'Type': 'long'},
        7: { 'Name': 'PaddingZeroHours', 'Type': 'bool'},
        8: { 'Name': 'PaddingZeroMinutes', 'Type': 'bool'},
        9: { 'Name': 'HoursDataTypeCoordinates', 'Type': Coordinates}, # needed only when MinutesFollowHours == False
        11: { 'Name': 'MinutesFollowHours', 'Type': 'bool'},
    }

class Alarm:
    definitions = {
        3: {'Name': 'NoAlarmImage', 'Type': Image},
        5: {'Name': 'AlarmImage', 'Type': Image},
        6: {'Name': 'ShortcutArea', 'Type': Element},
        7: {'Name': 'AlarmTime', 'Type': AlarmTime},
    }

