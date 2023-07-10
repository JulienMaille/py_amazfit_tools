class TextAlignmentGts2Mini:
    Default = 0
    Left = 2
    Right = 4
    HCenter = 8

    Top = 16
    Bottom = 32
    VCenter = 64

    TopCenter = Top | HCenter
    TopLeft = Top | Left
    TopRight = Top | Right

    Center = VCenter | HCenter
    CenterLeft = VCenter | Left
    CenterRight = VCenter | Right

    BottomCenter = Bottom | HCenter
    BottomLeft = Bottom | Left
    BottomRight = Bottom | Right

    Vertical = 128 # gts2min - 531199d7cab489d94fdec39e0b6e5b6a
    VerticalLeft = Vertical | Left # 130 - bipu - d45d3d25a9e51c543a9d47dc39c5b068
    VerticalRight = Vertical | Right # 132

    Converter = {
        Default : "Default",
        Left : "Left",
        Right : "Right",
        HCenter : "HCenter",
        Top : "Top",
        Bottom : "Bottom",
        VCenter : "VCenter",

        TopCenter : "TopCenter",
        TopLeft : "TopLeft",
        TopRight : "TopRight",
        Center : "Center",
        CenterLeft : "CenterLeft",
        CenterRight : "CenterRight",
        BottomCenter : "BottomCenter",
        BottomLeft : "BottomLeft",
        BottomRight : "BottomRight",

        Vertical: "Vertical",
        VerticalLeft: "VerticalLeft",
        VerticalRight: "VerticalRight"
    }

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

    def toJSON(self):
        if self._flag == None:
            self._flag = 0
        return TextAlignmentGts2Mini.Converter[self._flag]

    @staticmethod
    def fromJSON(strFlag):
        for flag in TextAlignmentGts2Mini.Converter:
            if strFlag == TextAlignmentGts2Mini.Converter[flag]:
                return flag
        return 0
