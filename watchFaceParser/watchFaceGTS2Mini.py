from watchFaceParser.elements.gts2mini.deviceId import DeviceId
from watchFaceParser.elements.gts2mini.background import Background
from watchFaceParser.elements.gts2mini.timeDigital import TimeDigital, HourlyImages
from watchFaceParser.elements.gts2mini.activity import Activity
from watchFaceParser.elements.gts2mini.dateblock import DateBlock, WeekDayImages
from watchFaceParser.elements.gts2mini.battery import Battery
from watchFaceParser.elements.gts2mini.analogDialFace import AnalogDialFace
from watchFaceParser.elements.gts2mini.progress import Progress, ProgressPAI, ProgressUVI, ProgressAirQ, ProgressHumidity, ProgressSpo, ProgressStress, ProgressStandUp
from watchFaceParser.elements.gts2mini.status import Status
from watchFaceParser.elements.gts2mini.weather import Weather
from watchFaceParser.elements.gts2mini.animation import Animation
from watchFaceParser.elements.gts2mini.timeExtended import TimeExtended
from watchFaceParser.elements.gts2mini.activitySeparateDigits import ActivitySeparateDigits
from watchFaceParser.elements.gts2mini.shortcuts import Shortcuts
from watchFaceParser.elements.gts2mini.alarm import Alarm
from watchFaceParser.elements.gts2mini.alwaysOnDisplay import AlwaysOnDisplay

class WatchFace:
    definitions = {
        0: {'Name': 'Info', 'Type': DeviceId},
        #1: {'Name': 'Unknown1', 'Type': 'long?'},
        2: {'Name': 'Background', 'Type': Background},
        3: {'Name': 'TimeExtended', 'Type': TimeExtended}, #b29f1f0bd97cf0712b72dfe50fed2577.bin
        4: {'Name': 'Activity', 'Type': Activity},
        5: {'Name': 'DateBlock', 'Type': DateBlock},
        6: {'Name': 'Weather', 'Type': Weather},
        7: {'Name': 'StepProgress', 'Type': Progress},
        8: {'Name': 'Status', 'Type': Status},
        9: {'Name': 'Battery', 'Type': Battery},
        #10: {'Name': 'Unknown10', 'Type': 'long?'}, # not Progress, shows nothing
        11: {'Name': 'Animation', 'Type': Animation},
        12: {'Name': 'HeartProgress', 'Type': Progress},
        #13: {'Name': 'Unknown13', 'Type': 'long?'}, # not Progress, show a chinese character
        14: {'Name': 'WeekDayImages', 'Type': WeekDayImages}, #56bda72eb651d3cba751c9453203bd44.bin
        15: {'Name': 'CaloriesProgress', 'Type': Progress},
        #16: {'Name': 'Unknown16', 'Type': Progress},  # Progress but for unknown parameter
        17: {'Name': 'HumidityProgress', 'Type': ProgressHumidity},
        18: {'Name': 'Alarm', 'Type': Alarm},
        19: {'Name': 'Shortcuts', 'Type': Shortcuts},
        20: {'Name': 'TimeAnalog', 'Type': AnalogDialFace},
        21: {'Name': 'TimeDigital', 'Type': TimeDigital},
        22: {'Name': 'HourlyImages', 'Type': HourlyImages}, #eddc844402b6157dfb01e2b780b64b0b.bin
        23: {'Name': 'PaiProgress', 'Type': ProgressPAI}, #9ab2ccafb3b7b67fd47cc350236ddffe.bin
        24: {'Name': 'StandUpProgress', 'Type': ProgressStandUp},
        25: {'Name': 'AirQualityProgress', 'Type': ProgressAirQ},
        26: {'Name': 'UviProgress', 'Type': ProgressUVI}, #9ab2ccafb3b7b67fd47cc350236ddffe.bin
        27: {'Name': 'StressProgress', 'Type': ProgressStress}, # bipu - 4c8c5364650875f4aad4a90663e51f4a.bin
        28: {'Name': 'SPO2Progress', 'Type': ProgressSpo}, # bipu - 4c8c5364650875f4aad4a90663e51f4a.bin
        29: {'Name': 'AlwaysOnDisplay', 'Type': AlwaysOnDisplay},
        30: {'Name': 'ActivitySeparateDigits', 'Type': ActivitySeparateDigits}, #468da72c923467e6ac1c2752a238a4b3.bin
    }
