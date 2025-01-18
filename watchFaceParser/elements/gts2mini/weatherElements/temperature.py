from watchFaceParser.elements.gts2mini.weatherElements.texttemperature import TextTemperature
from watchFaceParser.elements.gts2mini.weatherElements.oneLine import OneLine

class Temperature:
    definitions = {
        1: {'Name': 'Current', 'Type': TextTemperature},
        2: {'Name': 'OneLine', 'Type': OneLine},
        3: {'Name': 'Highest', 'Type': TextTemperature},
        4: {'Name': 'Lowest', 'Type': TextTemperature},
    }

