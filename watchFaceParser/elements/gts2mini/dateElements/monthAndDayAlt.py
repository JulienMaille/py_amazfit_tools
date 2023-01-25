from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet

class MonthAndDayAlt:
    definitions = {
        1: {'Name': 'Month', 'Type': Number},
        2: {'Name': 'MonthAsWord', 'Type': ImageSet},
        3: {'Name': 'MonthAsWordChinese', 'Type': ImageSet},
        4: {'Name': 'Day', 'Type': Number},
    }
