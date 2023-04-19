from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.shortcutsElements.element import Element

class UVindex:
    definitions = {
        1: {'Name': 'UVindexNumber', 'Type': Number},
        2: {'Name': 'SuffixImageIndex', 'Type': 'long'},
        3: {'Name': 'Shortcut', 'Type': Element},
        5: {'Name': 'PrefixImageIndex', 'Type': 'long'},
        6: {'Name': 'NoDataImageIndex', 'Type': 'long'},
        9: {'Name': 'UVindexIcon', 'Type': Image},
    }

