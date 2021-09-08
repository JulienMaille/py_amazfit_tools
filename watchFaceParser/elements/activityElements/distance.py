from watchFaceParser.elements.basicElements.number import Number
from watchFaceParser.models.color import Color
from watchFaceParser.elements.basicElements.image import Image

class Distance:
    definitions = {
        1: { 'Name': 'Number', 'Type': Number},
        2: { 'Name': 'SuffixImageIndex', 'Type': 'long?'},
        3: { 'Name': 'DecimalPointImageIndex', 'Type': 'long?'},
	    4: { 'Name': 'Color', 'Type': Color},
	    5: { 'Name': 'Unknown5', 'Type': Image},
    }

