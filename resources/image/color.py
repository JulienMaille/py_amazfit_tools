import logging

class Color:
    @staticmethod
    def fromArgb(a, r = None, g = None, b = None):
        if r is None and g is None and b is None:
            v = a
            a = (v & 0xff000000) >> 24
            r = (v & 0xff0000) >> 16
            g = (v & 0xff00) >> 8
            b = (v & 0xff)
        return (r, g, b, a)

    @staticmethod
    def fromArgdBackground(v):
        bytes = v.to_bytes(4, 'big')
        print(bytes, len(bytes))
        firstByte = bytes[2]
        secondByte = bytes[2 + 1]
        r = ((firstByte >> 3) & 0x1f) << 3
        g = (((secondByte >> 5) & 0x7) | ((firstByte & 0x07) << 3)) << 2
        b = (secondByte & 0x1f) << 3
        alpha = 255
        color = Color.fromArgb(alpha, r, g, b)
        return (color)

