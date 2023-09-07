from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.basicElements.iconSet import IconSet
from watchFaceParser.elements.gts2mini.basicElements.scale import Scale
from watchFaceParser.elements.gts2mini.basicElements.circleScale import CircleScale
from watchFaceParser.elements.gts2mini.basicElements.pointerScale import PointerScale
from watchFaceParser.elements.gts2mini.basicElements.number import Number

class ProgressWeekday:
    definitions = {
        2: {'Name': 'ImageProgress', 'Type': ImageSet}, # TODO: not found in standard, should by tested
        3: {'Name': 'IconSetProgress', 'Type': IconSet}, # mini: 6608e628967af66d1b74f8f9952596d7
        4: {'Name': 'CircleScale', 'Type': CircleScale}, # TODO: not found in standard, should by tested
        6: {'Name': 'Scale', 'Type': Scale}, # TODO: not found in standard, should by tested
        8: {'Name': 'BackgroundLayer', 'Type': Image}, # TODO: not found in standard, should by tested
    }
    
class ProgressSteps:
    definitions = {
        2: {'Name': 'ImageProgress', 'Type': ImageSet},
        3: {'Name': 'IconSetProgress', 'Type': IconSet}, # bipu: 20faa5500f2060aa1809814531221b88
        4: {'Name': 'CircleScale', 'Type': CircleScale}, # bipu: de43dcb071d889905665656e6964a97d
        6: {'Name': 'Scale', 'Type': Scale}, # bip3: 41cbe44c719d423e271288cf79fcec10
        8: {'Name': 'BackgroundLayer', 'Type': Image}, # gts2mini: f458b060c4c5dd855fee965c0de750dd
    }

class Alt1PointerScale:
    definitions = {
        1: {'Name': 'PointerScale', 'Type': PointerScale},
    }

class ProgressCalories:
    definitions = {
        2: {'Name': 'ImageProgress', 'Type': ImageSet},
        3: {'Name': 'IconSetProgress', 'Type': IconSet}, # bipu: 4c67a37e2e128a0a48cca11c539540cf
        4: {'Name': 'CircleScale', 'Type': CircleScale}, # bipu: de43dcb071d889905665656e6964a97d, mini: 9dd4668a2762a86e8b837b933a23efe4
        6: {'Name': 'Scale', 'Type': Scale}, # TODO: not found in standard, should by tested
        8: {'Name': 'BackgroundLayer', 'Type': Image}, # TODO: not found in standard, should by tested
    }

class ProgressHeart:
    definitions = {
        2: {'Name': 'ImageProgress', 'Type': ImageSet},
        3: {'Name': 'IconSetProgress', 'Type': IconSet}, # bipu: 4961c75712fb6f7082040899ff1d3b72
        6: {'Name': 'Scale', 'Type': Alt1PointerScale}, # bip3: 3a0b16e4d9d88b336ff9d0ae1d3d1364, bip3: 859cd15f139cb32cd15a215b1ae53d88
        7: {'Name': 'BackgroundLayer', 'Type': Image}, # 5bd18e5a9f7568d42f984fe540d992e9.bin 4961c75712fb6f7082040899ff1d3b72.bin f458b060c4c5dd855fee965c0de750dd.bin
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
