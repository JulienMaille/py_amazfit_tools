from watchFaceParser.elements.gtr2.digitalElements.digitalDateDigit import DigitalDateDigit
from watchFaceParser.elements.gtr2.digitalElements.digitalCommonDigit import DigitalCommonDigit
from watchFaceParser.elements.gtr2.basicElements.image import Image 
from watchFaceParser.elements.gtr2.dateClockHand import DateClockHand 
from watchFaceParser.elements.gtr2.dateProgressBar import DateProgressBar
class Date:
    definitions = {
        1: { 'Name': 'DateDigits', 'Type': [DigitalDateDigit] },
        2: { 'Name': 'WeeksDigits', 'Type': DigitalCommonDigit },
        3: { 'Name': 'DateClockHand', 'Type': DateClockHand},
		4: { 'Name': 'DateProgressBar', 'Type': DateProgressBar},
    }

