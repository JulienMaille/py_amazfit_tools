from watchFaceParser.elements.gts2mini.deviceId import DeviceId
from watchFaceParser.elements.gts2mini.background import Background
from watchFaceParser.elements.gts2mini.timeDigital import TimeDigital
from watchFaceParser.elements.gts2mini.activity import Activity
from watchFaceParser.elements.gts2mini.dateblock import DateBlock
from watchFaceParser.elements.gts2mini.battery import Battery
from watchFaceParser.elements.gts2mini.analogDialFace import AnalogDialFace
from watchFaceParser.elements.gts2mini.progress import Progress
from watchFaceParser.elements.gts2mini.status import Status
from watchFaceParser.elements.gts2mini.weather import Weather
from watchFaceParser.elements.gts2mini.animation import Animation
from watchFaceParser.elements.gts2mini.timeSeparateDigits import TimeSeparateDigits
from watchFaceParser.elements.gts2mini.activitySeparateDigits import ActivitySeparateDigits
from watchFaceParser.elements.gts2mini.shortcuts import Shortcuts

class WatchFace:
    definitions = {
        0: {'Name': 'Info', 'Type': DeviceId},
        1: {'Name': 'Unknown1', 'Type': 'long?'},
        2: {'Name': 'Background', 'Type': Background},
        3: {'Name': 'TimeSeparateDigits', 'Type': TimeSeparateDigits}, #b29f1f0bd97cf0712b72dfe50fed2577.bin
        4: {'Name': 'Activity', 'Type': Activity},
        5: {'Name': 'DateBlock', 'Type': DateBlock},
        6: {'Name': 'Weather', 'Type': Weather},
        7: {'Name': 'StepProgress', 'Type': Progress},
        8: {'Name': 'Status', 'Type': Status},
        9: {'Name': 'Battery', 'Type': Battery},
        10: {'Name': 'Unknown10', 'Type': 'long?'},
        11: {'Name': 'Animation', 'Type': Animation},
        12: {'Name': 'HearthProgress', 'Type': Progress},
        13: {'Name': 'Unknown13', 'Type': 'long?'},
        14: {'Name': 'Unknown14', 'Type': 'long?'},
        15: {'Name': 'CaloriesProgress', 'Type': Progress},
        16: {'Name': 'Unknown16', 'Type': 'long?'},
        17: {'Name': 'Unknown17', 'Type': 'long?'},
        18: {'Name': 'Unknown18', 'Type': 'long?'},
        19: {'Name': 'Shortcuts', 'Type': Shortcuts},
        20: {'Name': 'TimeAnalog', 'Type': AnalogDialFace},
        21: {'Name': 'TimeDigital', 'Type': TimeDigital},
        22: {'Name': 'Unknown22', 'Type': 'long?'},
        23: {'Name': 'Unknown23', 'Type': 'long?'},
        24: {'Name': 'StandUpProgress', 'Type': Progress},
        25: {'Name': 'Unknown25', 'Type': 'long?'},
        26: {'Name': 'Unknown26', 'Type': 'long?'},
        27: {'Name': 'Unknown27', 'Type': 'long?'},
        28: {'Name': 'Unknown28', 'Type': 'long?'},
        29: {'Name': 'AOD', 'Type': 'long?'}, # is this aod screen?
        30: {'Name': 'ActivitySeparateDigits', 'Type': ActivitySeparateDigits}, #468da72c923467e6ac1c2752a238a4b3.bin
    }
