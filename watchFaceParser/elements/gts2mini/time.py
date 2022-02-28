from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.coordinates import Coordinates

class Time:
    definitions = {
        1: { 'Name': 'Unknown1', 'Type': 'long'}, #bool? always 1
        2: { 'Name': 'Minutes', 'Type': Number},
        3: { 'Name': 'Seconds', 'Type': Number},
        4: { 'Name': 'PaddingZeroMinutes', 'Type': 'bool'},
        5: { 'Name': 'PaddingZeroSeconds', 'Type': 'bool'},
        6: { 'Name': 'MinutesDataTypeImageIndex', 'Type': 'long'},
        7: { 'Name': 'SecondsDataTypeImageIndex', 'Type': 'long'},
        8: { 'Name': 'MinutesFollowHours', 'Type': 'bool'}, # if set to true, seconds will only show if they follow minutes
        9: { 'Name': 'SecondsFollowMinutes', 'Type': 'bool'},
        10: { 'Name': 'HoursDataTypeCoordinates', 'Type': Coordinates}, # needed only when MinutesFollowHours == False
        11: { 'Name': 'MinutesDataTypeCoordinates', 'Type': Coordinates}, # needed only when SecondsFollowMinutes == False
        12: { 'Name': 'SecondsDataTypeCoordinates', 'Type': Coordinates},
    }

