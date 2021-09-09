from watchFaceParser.elements.basicElements.image import Image
from watchFaceParser.models.color import Color

class Background:
    definitions = {
        1: { 'Name': 'Image', 'Type': Image},
        2: {'Name': 'SolidColor', 'Type': Color},
        3: { 'Name': 'Preview', 'Type': Image},
        4: { 'Name': 'FrontImage', 'Type': Image},
        5: { 'Name': 'UnknownImage', 'Type': Image},
    }