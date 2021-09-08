class ImageProgressDisplayType:
    Single = 0
    Continuous = 1

    Converter = {
        Single : "Single",
        Continuous : "Continuous", 
    }

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

    def toJSON(self):
        if self._flag == None:
            self._flag = 0
        return ImageProgressDisplayType.Converter[self._flag]

    @staticmethod
    def fromJSON(strFlag):
        for flag in ImageProgressDisplayType.Converter:
            if strFlag == ImageProgressDisplayType.Converter[flag]:
                return flag
        return 0
