from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.basicElements.coordinates import Coordinates

class YearMonthAndDay:
    definitions = {
        1: {'Name': 'Year', 'Type': Number},
        2: {'Name': 'Month', 'Type': Number},
        3: {'Name': 'Day', 'Type': Number},
        4: {'Name': 'MonthFollowsYear', 'Type': 'bool'},
        5: {'Name': 'DayFollowsMonth', 'Type': 'bool'},
        6: {'Name': 'MonthAsWord', 'Type': ImageSet},
        7: {'Name': 'MonthAsWordChinese', 'Type': ImageSet},
        8: {'Name': 'YearDataTypeImageIndex', 'Type': 'long'},
        9: {'Name': 'MonthDataTypeImageIndex', 'Type': 'long'},
        10: {'Name': 'DayDataTypeImageIndex', 'Type': 'long'},
        11: {'Name': 'DelimiterYearImageIndex', 'Type': 'long'},
        12: {'Name': 'DelimiterMonthImageIndex', 'Type': 'long'},
        13: {'Name': 'DelimiterDayImageIndex', 'Type': 'long'},
        14: {'Name': 'YearDataTypeCoordinates', 'Type': Coordinates}, # Datatype coords
        15: {'Name': 'MonthDataTypeCoordinates', 'Type': Coordinates}, # Datatype coords
        16: {'Name': 'DayDataTypeCoordinates', 'Type': Coordinates}, # Datatype coords
    }
