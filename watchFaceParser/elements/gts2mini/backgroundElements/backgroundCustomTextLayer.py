from watchFaceParser.elements.gts2mini.basicElements.coordinates import Coordinates

class BackgroundZeppCustomTextLayer:
    definitions = {
        1: { 'Name': 'StartImageIndex', 'Type': 'long'}, # zepp - gts2mini - 9a176bd9b22f22168e70acf83416d751
        2: { 'Name': 'Coordinates', 'Type': [Coordinates]}, 
    }