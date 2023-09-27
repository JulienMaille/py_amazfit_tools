from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.shortcutsElements.element import Element

class Steps:
    definitions = {
        1: {'Name': 'ImageNumber', 'Type': Number},
        2: {'Name': 'PrefixImageIndex', 'Type': 'long'},
        3: {'Name': 'SuffixImageIndex', 'Type': 'long'},
        4: {'Name': 'Icon', 'Type': Image},
        6: {'Name': 'Shortcut', 'Type': Element},
        7: {'Name': 'DelimiterTotalImageIndex', 'Type': 'long'}, # zepp - c11e6b385afd124e9e8af15131c1092e TODO check on watch
    }
