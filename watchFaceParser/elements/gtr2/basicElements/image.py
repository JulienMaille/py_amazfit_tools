from watchFaceParser.elements.gtr2.basicElements.multilangImage import MultilangImage 

class Image:
    definitions = {
        1: { 'Name': 'X', 'Type': 'long'},
        2: { 'Name': 'Y', 'Type': 'long'}, 
        3: { 'Name': 'NoDataImageIndex', 'Type': 'long'}, 
        4: { 'Name': 'MultilangImage', 'Type': [MultilangImage]},
        5: { 'Name': 'DecimalPointImageIndex', 'Type': 'long'},
        6: { 'Name': 'MultilangImageUnit', 'Type': [MultilangImage]},
        7: { 'Name': 'DelimiterImageIndex', 'Type': 'long'},
        8: { 'Name': 'MultilangImageUnitMile', 'Type': [MultilangImage]},
    }