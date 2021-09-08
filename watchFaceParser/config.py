import logging
class Config:
    _deviceId = None
    _is_gtr = False
    _is_gtr2_mini = False
    _is_gtr2 = False
    _is_gts = False
    _is_gts2 = False
    _is_trex = False
    _is_trexpro = False
    _is_amazfitx = False
    _image_size = (360, 360)
    _preview_size = (210, 210)
    _autodetect = True

    _startImageIndex = 0

    _is_to_raw = False
    _is_from_raw = False

    _size_gtr2_mini = (306, 354)
    _size_gtr_47 = (454, 454)
    _size_gtr_42 = (390, 390)
    _size_trex = (360, 360)
    _size_gts = (348,442)
    _size_amazfitx = (206,640)
    _oldformat = False

    _border_alignment = False

    @staticmethod
    def setDeviceId(deviceId):
        Config._deviceId = deviceId
        if Config._autodetect:
            if deviceId == 0x20:
                print("Detected Verge Lite")
                Config.setVergeLiteMode(True)
            elif deviceId == 0x28:
                print("Detected GTR (47mm)")
                Config.setGtrMode(47)
            elif deviceId == 0x2a:
                print("Detected GTR (42mm)")
                Config.setGtrMode(42)
            elif deviceId == 0x2e:
                print("Detected GTS")
                Config.setGtsMode(True)
            elif deviceId == 0x34:
                print("Detected T-Rex")
                Config.setTrexMode(True)
            elif deviceId == 0x35:
                print("Detected AmazfitX")
                Config.setAmazfitXMode(True)
            elif deviceId == 0x3b:
                print("Detected GTR2")
                Config.setGtr2Mode(True)
            elif deviceId == 0x41:
                print("Detected GTS2")
                Config.setGts2Mode(True)
            elif deviceId == 0x53:
                print("Detected TrexPro")
                Config.setTrexProMode(True)
            elif deviceId == 0x49:
                print("Detected GTR2 Mini")
                Config.setGtr2MiniMode(True)
    @staticmethod
    def setToRaw(val):
        Config._is_to_raw = val 

    @staticmethod
    def setFromRaw(val):
        Config._is_from_raw = val 

    @staticmethod
    def getDeviceId():
        return Config._deviceId

    @staticmethod
    def getAutodetect():
        return Config._autodetect

    @staticmethod
    def setXMode(isX):
        if isX:
            Config._autodetect = False
            Config._is_amazfitx = True
            Config._preview_size = (152, 472)


    @staticmethod
    def setGtr2MiniMode(gtr):
        Config._is_gtr2_mini = gtr 
        if gtr:
            Config._autodetect = False
            Config._image_size = Config._size_gtr2_mini
            Config._preview_size = (306, 354)

    @staticmethod
    def setGtrMode(gtr):
        Config._is_gtr = gtr
        if Config._is_gtr == 47:
            Config._autodetect = False
            Config._image_size = Config._size_gtr_47
            Config._preview_size = (266, 266)
        if Config._is_gtr == 42:
            Config._autodetect = False
            Config._image_size = Config._size_gtr_42
            Config._preview_size = (266, 266) 

    @staticmethod
    def setGtrMode2(gtr2, oldformat=False):
        if oldformat:
            Config._oldformat = True
        Config._is_gtr2 = gtr2
        if Config._is_gtr2 == 47:  
            Config._autodetect = False
            Config._image_size = Config._size_gtr_47
            Config._preview_size = (306, 306)
            if not oldformat:
                Config._startImageIndex = 0
        if Config._is_gtr2 == 42: 
            Config._autodetect = False
            Config._image_size = Config._size_gtr_42
            Config._preview_size = (306, 306)
            if not oldformat:
                Config._startImageIndex = 1 

    @staticmethod
    def isGtrMode():
        return Config._is_gtr

    @staticmethod
    def isGtr2Mode():
        return Config._is_gtr2

    @staticmethod
    def isGtr2MiniMode():
        return Config._is_gtr2_mini

    @staticmethod
    def isGts2Mode():
        return Config._is_gts2

    @staticmethod
    def isTrexMode():
        return Config._is_trex

    @staticmethod
    def isTrexProMode():
        return Config._is_trexpro

    @staticmethod
    def isAmazfitXMode():
        return Config._is_amazfitx

    @staticmethod
    def setVergeLiteMode(vergelite):
        if vergelite:
            Config._autodetect = False

    @staticmethod
    def setTrexMode(trex):
        if trex:
            Config._autodetect = False
            Config._is_trex = 50

    @staticmethod
    def setTrexProMode(trex, oldformat=False):
        if oldformat:
            Config._oldformat = True
        if trex:
            Config._autodetect = False
            Config._is_trexpro = 50
            Config._image_size = Config._size_trex
            Config._preview_size = (220,220)
            if not oldformat:
                 Config._startImageIndex = 1
    
    @staticmethod
    def setGtr2Mode(gtr2):
        if gtr2:
            Config._autodetect = False
            Config._is_gtr2 = 47

    @staticmethod
    def setAmazfitXMode(amazfitx):
        if amazfitx:
            Config._autodetect = False
            Config._is_amazfitx = 53
            Config._image_size = Config._size_amazfitx
            Config._preview_size = (152,472)

    @staticmethod
    def setGtsMode(gts):
        if gts:
            Config._autodetect = False
            Config._is_gts = 40
            Config._image_size = Config._size_gts
            Config._preview_size = (242,304)

    @staticmethod
    def setGts2Mode(gts2, oldformat=False):
        if oldformat:
            Config._oldformat = True
        if gts2:
            Config._autodetect = False
            Config._is_gts2 = 40
            Config._image_size = Config._size_gts
            Config._preview_size = (254,323)
            if not oldformat:
                 Config._startImageIndex = 1
    
    @staticmethod
    def isOldFormat():
        return Config._oldformat
    
    @staticmethod
    def setOldFormat(oldformat):
        Config._oldformat = oldformat
        if oldformat == True:
            Config._startImageIndex = 0

    @staticmethod
    def isGtsMode():
        return Config._is_gts

    @staticmethod
    def getImageSize():
        return Config._image_size

    @staticmethod
    def getStartImageIndex():
        return Config._startImageIndex


    @staticmethod
    def getImageSizeHalf():
        return (int(Config._image_size[0] / 2),int(Config._image_size[1] / 2))


    @staticmethod
    def getPreviewSize():
        # return (Config._preview_size, Config._preview_size)
        return Config._preview_size

    @staticmethod
    def isToRaw():
        return Config._is_to_raw
    @staticmethod
    def isFromRaw():
        return Config._is_from_raw

    @staticmethod
    def setBorderAlignment(border_alignment):
        Config._border_alignment = border_alignment

    @staticmethod
    def getBorderAlignment():
        return Config._border_alignment
