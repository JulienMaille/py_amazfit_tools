from watchFaceParser.elements.gts2mini.basicElements.batteryText import BatteryText
from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.basicElements.iconSet import IconSet
from watchFaceParser.elements.gts2mini.basicElements.scale import Scale
from watchFaceParser.elements.gts2mini.basicElements.image import Image

class Battery:
    definitions = {
        1: {'Name': 'BatteryText', 'Type': BatteryText},
        2: {'Name': 'ImageProgress', 'Type': ImageSet},
        3: {'Name': 'IconSetProgress', 'Type': IconSet},
        #4: {'Name': 'Unknown4', 'Type': 'long?'},
        5: {'Name': 'Scale', 'Type': Scale},
        6: {'Name': 'Icon', 'Type': Image},
    }
