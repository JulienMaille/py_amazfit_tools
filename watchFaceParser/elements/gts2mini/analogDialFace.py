from watchFaceParser.elements.gts2mini.analogDialFaceElements.clockHand import ClockHand

class AnalogDialFace:
    definitions = {
        1: {'Name': 'Unknown1', 'Type': 'long?'},
        2: {'Name': 'Unknown2', 'Type': 'long?'},
        3: { 'Name': 'Hours', 'Type': ClockHand},
        4: { 'Name': 'Minutes', 'Type': ClockHand},
        5: { 'Name': 'Seconds', 'Type': ClockHand},
    }

