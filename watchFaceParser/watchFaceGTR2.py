from watchFaceParser.elements.deviceId import DeviceId
from watchFaceParser.elements.gtr2.background import Background
from watchFaceParser.elements.gtr2.system import System
from watchFaceParser.elements.gtr2.screenNormal import ScreenNormal
from watchFaceParser.elements.gtr2.screenIdle import ScreenIdle
from watchFaceParser.elements.gtr2.widgets import Widgets
from watchFaceParser.elements.gtr2.shortcuts import Shortcuts

class WatchFace:
    definitions = {
        0: { 'Name': 'Info', 'Type': DeviceId},
        3: { 'Name': 'Background', 'Type': Background},
        4: { 'Name': 'DialFace', 'Type': ScreenNormal},
        5: { 'Name': 'System', 'Type': System},
        6: { 'Name': 'Widgets', 'Type': Widgets},
        10: { 'Name': 'ScreenIdle', 'Type': ScreenIdle},
    }
