from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.basicElements.iconSet import IconSet
from watchFaceParser.elements.gts2mini.basicElements.scale import Scale
from watchFaceParser.elements.gts2mini.basicElements.circleScale import CircleScale

class Progress:
    definitions = {
        #1: {'Name': 'Unknown1', 'Type': 'long?'}, #Text ?
        2: {'Name': 'ImageProgress', 'Type': ImageSet},
        3: {'Name': 'IconSetProgress', 'Type': IconSet},
        4: {'Name': 'CircleScale', 'Type': CircleScale}, # will work for StepProgress and CaloriesProgress only
        #5: {'Name': 'Unknown5', 'Type': 'long?'},
        6: {'Name': 'Scale', 'Type': Scale},
        7: {'Name': 'NoDataImage', 'Type': Image},
        8: {'Name': 'UnknownImage', 'Type': Image}, # 5bd18e5a9f7568d42f984fe540d992e9.bin
    }

class ProgressAlt1:
    definitions = {
        2: {'Name': 'ImageProgress', 'Type': ImageSet},
        6: {'Name': 'NoDataImage', 'Type': Image},
    }

class ProgressAlt2:
    definitions = {
        1: {'Name': 'ImageProgress', 'Type': ImageSet},
        5: {'Name': 'NoDataImage', 'Type': Image},
    }

class ProgressAlt3:
    definitions = {
        2: {'Name': 'ImageProgress', 'Type': ImageSet},
        8: {'Name': 'NoDataImage', 'Type': Image},
    }

class ProgressAlt4:
    definitions = {
        5: {'Name': 'ImageProgress', 'Type': ImageSet},
        7: {'Name': 'NoDataImage', 'Type': Image},
    }

class ProgressAlt5:
    definitions = {
        2: {'Name': 'ImageProgress', 'Type': ImageSet},
        3: {'Name': 'IconSetProgress', 'Type': IconSet},
        4: {'Name': 'PointerProgress', 'Type': Scale},
    }
