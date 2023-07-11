from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.basicElements.iconSet import IconSet
from watchFaceParser.elements.gts2mini.basicElements.scale import Scale
from watchFaceParser.elements.gts2mini.basicElements.circleScale import CircleScale
from watchFaceParser.elements.gts2mini.basicElements.pointerScale import PointerScale
from watchFaceParser.elements.gts2mini.basicElements.number import Number
class Progress:
    definitions = {
        #1: {'Name': 'Unknown1', 'Type': 'long?'}, #Text ?
        2: {'Name': 'ImageProgress', 'Type': ImageSet},
        3: {'Name': 'IconSetProgress', 'Type': IconSet},
        4: {'Name': 'CircleScale', 'Type': CircleScale}, # will work for StepProgress and CaloriesProgress only
        #5: {'Name': 'Unknown5', 'Type': 'long?'},
        6: {'Name': 'Scale', 'Type': Scale},
        8: {'Name': 'BackgroundLayer', 'Type': Image}, # 5bd18e5a9f7568d42f984fe540d992e9.bin 4961c75712fb6f7082040899ff1d3b72.bin f458b060c4c5dd855fee965c0de750dd.bin
    }

class Alt1PointerScale:
    definitions = {
        1: {'Name': 'PointerScale', 'Type': PointerScale},
    }

class ProgressPAI:
    definitions = {
        1: {'Name': 'PointerScale', 'Type': PointerScale},
        2: {'Name': 'ImageProgress', 'Type': ImageSet},
        4: {'Name': 'Alt1PointerScale', 'Type': Alt1PointerScale},
        6: {'Name': 'BackgroundLayer', 'Type': Image},
    }

class ProgressUVI:
    definitions = {
        1: {'Name': 'ImageProgress', 'Type': ImageSet},
        3: {'Name': 'Scale', 'Type': Scale},
        5: {'Name': 'BackgroundLayer', 'Type': Image},
    }

class ProgressAirQ:
    definitions = {
        1: {'Name': 'ImageProgress', 'Type': ImageSet},
        3: {'Name': 'Scale', 'Type': Scale},
        5: {'Name': 'BackgroundLayer', 'Type': Image},
    }

class ProgressHumidity:
    definitions = {
        2: {'Name': 'ImageProgress', 'Type': ImageSet},
        8: {'Name': 'BackgroundLayer', 'Type': Image},
    }

class ProgressSpo:
    definitions = {
        1: {'Name': 'Text', 'Type': Number},
        3: {'Name': 'PrefixImageIndex', 'Type': 'long'},
        5: {'Name': 'ImageProgress', 'Type': ImageSet},
        7: {'Name': 'BackgroundLayer', 'Type': Image},
    }

class ProgressStress:
    definitions = {
        1: {'Name': 'Text', 'Type': Number},
        3: {'Name': 'PrefixImageIndex', 'Type': 'long'},
        5: {'Name': 'ImageProgress', 'Type': ImageSet},
        7: {'Name': 'BackgroundLayer', 'Type': Image},
    }

class ProgressStandUp:
    definitions = {
        2: {'Name': 'ImageProgress', 'Type': ImageSet},
        3: {'Name': 'IconSetProgress', 'Type': IconSet},
        4: {'Name': 'PointerProgress', 'Type': Scale},
    }
