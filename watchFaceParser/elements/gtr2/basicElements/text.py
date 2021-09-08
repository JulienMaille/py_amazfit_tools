from watchFaceParser.elements.gtr2.basicElements.image import Image 
from watchFaceParser.elements.gtr2.basicElements.systemFont import SystemFont 
from watchFaceParser.models.gtr2.textAlignment import TextAlignmentGTR2

class Text:
    definitions = { 
        1: { 'Name': 'Image', 'Type': Image},
        2: { 'Name': 'SystemFont', 'Type': SystemFont},
        3: { 'Name': 'Alignment', 'Type': TextAlignmentGTR2},
        4: { 'Name': 'Spacing', 'Type': 'long'}, 
        5: { 'Name': 'PaddingZero', 'Type': 'bool'},
        6: { 'Name': 'DisplayFormAnalog', 'Type': 'bool'}, 
    }
