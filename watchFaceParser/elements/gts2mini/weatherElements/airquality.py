from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet

class AirQuality:
    definitions = {
        1: {'Name': 'AirQualityNumber', 'Type': Number},
        2: {'Name': 'IconProgress', 'Type': ImageSet}, #copied from
        3: {'Name': 'AirQualityIcon', 'Type': Image},
        4: {'Name': 'Icon', 'Type': Image},
        5: {'Name': 'IconChinese', 'Type': Image},
        6: {'Name': 'IconTradChinese', 'Type': Image},
    }

