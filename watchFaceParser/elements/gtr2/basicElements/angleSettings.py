from watchFaceParser.elements.gtr2.basicElements.multilangImage import MultilangImage 

class AngleSettings:
    definitions = {
        1: { 'Name': 'X', 'Type': 'long'}, # circle center
        2: { 'Name': 'Y', 'Type': 'long'}, # circle center
        3: { 'Name': 'StartAngle', 'Type': 'float'}, # 0 center top, 0 - (-180) - left, 0 - 180 - right
        4: { 'Name': 'EndAngle', 'Type': 'float'}, # 0 center top, 0 - (-180) - left, 0 - 180 - right
        5: { 'Name': 'Radius', 'Type': 'float'}, # radius from center to middle of indicator line
    }