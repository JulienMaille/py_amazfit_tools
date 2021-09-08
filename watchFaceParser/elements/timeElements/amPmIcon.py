from watchFaceParser.elements.basicElements.imageSet import ImageSet
from watchFaceParser.elements.basicElements.coordinates import Coordinates

class AmPmIcon:
    definitions = {
        1: { 'Name': 'Coordinates', 'Type': Coordinates},
        2: { 'Name': 'AmImageIndex', 'Type': 'long'},
        3: { 'Name': 'PmImageIndex', 'Type': 'long'},
        4: { 'Name': 'ImageIndex4', 'Type': 'long'},
        5: { 'Name': 'ImageIndex5', 'Type': 'long'},
    }

