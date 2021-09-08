from watchFaceParser.elements.gtr2.digitalElements.digitalCommonDigit import DigitalCommonDigit
from watchFaceParser.elements.gtr2.basicElements.imageCoord import ImageCoord 
from watchFaceParser.elements.gtr2.basicElements.imageProgress import ImageProgress 
from watchFaceParser.elements.gtr2.basicElements.progressBar import ProgressBar  
from watchFaceParser.models.gtr2.activityType import ActivityType
from watchFaceParser.elements.gtr2.shortcut import Shortcut
from watchFaceParser.elements.gtr2.analogDialFaceElements.clockHand import ClockHand 

class Activity:
    definitions = {
        1: { 'Name': 'Type', 'Type': ActivityType }, 
        2: { 'Name': 'PointerProgress', 'Type': ClockHand }, 
        3: { 'Name': 'ProgressBar', 'Type': ProgressBar }, 
        4: { 'Name': 'ImageProgress', 'Type': ImageProgress },
        5: { 'Name': 'Digits', 'Type': [DigitalCommonDigit] },   
        6: { 'Name': 'Shortcut', 'Type': Shortcut },
        7: { 'Name': 'Icon', 'Type': ImageCoord },
    }