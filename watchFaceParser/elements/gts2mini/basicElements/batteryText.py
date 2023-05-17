from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.shortcutsElements.element import Element

class BatteryText:
    definitions = {
        1: {'Name': 'ImageNumber', 'Type': Number},
        2: {'Name': 'UnknownLong2', 'Type': 'long'}, # TODO: prüfen
        3: {'Name': 'PrefixImageIndex', 'Type': 'long'}, # zepp: 164024822b00d28891e2061e418fc1a4
        4: {'Name': 'SuffixImageIndex', 'Type': 'long'}, # zepp: 164024822b00d28891e2061e418fc1a4
        5: {'Name': 'Icon', 'Type': Image},
        6: {'Name': 'Shortcut', 'Type': Element},
    }