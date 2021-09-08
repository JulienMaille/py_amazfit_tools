from watchFaceParser.elements.gtr2.basicElements.angleSettings import AngleSettings 
from watchFaceParser.elements.gtr2.basicElements.linearSettings import LinearSettings 
from watchFaceParser.models.color import Color
 
class ProgressBar:
    definitions = { 
        1: { 'Name': 'AngleSettings', 'Type': AngleSettings},
        2: { 'Name': 'LinearSettings', 'Type': LinearSettings},
        3: { 'Name': 'ForegroundImageIndex', 'Type': 'long'},
        4: { 'Name': 'Color', 'Type': Color},   
        5: { 'Name': 'Width', 'Type': 'long'},   
        6: { 'Name': 'Flatness', 'Type': 'long'}, #0 - flat, 90, triangle, 180 - arc 
        7: { 'Name': 'PointerImageIndex', 'Type': 'long'},
        8: { 'Name': 'BackgroundImageIndex', 'Type': 'long'},
    }
