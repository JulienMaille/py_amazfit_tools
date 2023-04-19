from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image


class Humidity:
    definitions = {
        1: {'Name': 'HumidityNumber', 'Type': Number},
        2: {'Name': 'SuffixImageIndex', 'Type': 'long'},
        8: {'Name': 'PrefixImageIndex', 'Type': 'long'},
        9: {'Name': 'HumidityIcon', 'Type': Image},
    }

