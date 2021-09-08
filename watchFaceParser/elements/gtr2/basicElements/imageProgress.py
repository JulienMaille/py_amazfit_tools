from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.elements.gtr2.basicElements.imageSet import ImageSetGTR2
from watchFaceParser.models.gtr2.imageprogressDisplayType import ImageProgressDisplayType

class ImageProgress:
    definitions = { 
        1: { 'Name': 'Coordinates', 'Type': [Coordinates]},
        2: { 'Name': 'ImageSet', 'Type': ImageSetGTR2},
        3: { 'Name': 'DisplayType', 'Type': ImageProgressDisplayType}, # Continius / Single
    }
