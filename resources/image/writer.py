import logging
from watchFaceParser.config import Config

class Writer:
    signature = bytearray(b'BM\xff\xff')
    signatureMini16BME = bytearray(b'BM\x65\x00')
    signatureMini16 = bytearray(b'BM\x09\x00')
    signatureMini24 = bytearray(b'BM\x1C\x00')

    def __init__(self, stream):
        self._writer = stream

    def write(self, image):

        if Config.isGts2MiniMode() or Config.isBipUMode() or Config.isBip3Mode():
            self.writeGts2Mini(image)
        else:
            self.writeGts2(image)

    def writeGts2Mini(self, image):
        self._image = image
        self._width = image.size[0]
        self._height = image.size[1]
        self._bitsPerPixel = 16
        self._unknown2 = 0
        import math
        self._rowLengthInBytes = math.ceil(self._width * self._bitsPerPixel / 8)

        _hasHalfAlpha = self.hasHalfTransparency()
        _hasFullAlpha = self.hasFullTransparency()
        logging.debug(f" hasHalfAlpha: {_hasHalfAlpha}, has_transparency: {_hasFullAlpha}")

        if _hasFullAlpha or _hasHalfAlpha:
            if _hasHalfAlpha:
                self._bitsPerPixel = 24
                self._rowLengthInBytes = math.ceil(self._width * self._bitsPerPixel / 8)
                self._writer.write(Writer.signatureMini24)
                self.writeHeaderMini24()
                self.writeImageMini24()
            else:
                rawData = self.getImageDataBme()
                self._dataSize = len(rawData)
                self._writer.write(Writer.signatureMini16BME)
                self.writeHeaderMini16E()
                self._writer.write(rawData)
        else:
            self._writer.write(Writer.signatureMini16)
            self.writeHeaderMini16()
            self.writeImageMini16()

    def writeGts2(self, image):
        self._image = image
        self._width = image.size[0]
        self._height = image.size[1]

        isBigImg = (self._width == 206 and self._height == 640) or (self._width == 152 and self._height == 472)

        self._bitsPerPixel = 32
        self._unknown1 = 24
        self._unknown2 = 1

        if isBigImg:
            self._bitsPerPixel = 16

        import math
        self._rowLengthInBytes = math.ceil(self._width * self._bitsPerPixel / 8)

        self._writer.write(Writer.signature)

        self.writeHeader()
        if isBigImg:
            self.writeImage16()
        else:
            self.writeImage()
        #self.writeImage()

    def writeHeaderMini16(self):
        logging.debug("Writing image header mini...")
        logging.debug(f"Width: {self._width}, Height: {self._height}, RowLength: {self._rowLengthInBytes}")
        logging.debug(f"BPP: {self._bitsPerPixel}")

        self._writer.write(self._width.to_bytes(2, byteorder='little'))
        self._writer.write(self._height.to_bytes(2, byteorder='little'))
        self._writer.write(self._rowLengthInBytes.to_bytes(2, byteorder='little'))
        self._writer.write(self._bitsPerPixel.to_bytes(2, byteorder='little'))
        self._writer.write(self._unknown2.to_bytes(4, byteorder='little'))

    def writeHeaderMini16E(self):
        logging.debug("Writing image header mini...")
        logging.debug(f"Width: {self._width}, Height: {self._height}, RowLength: {self._rowLengthInBytes}")
        logging.debug(f"BPP: {self._bitsPerPixel}, DataSize: {self._dataSize}")

        self._writer.write(self._width.to_bytes(2, byteorder='little'))
        self._writer.write(self._height.to_bytes(2, byteorder='little'))
        self._writer.write(self._rowLengthInBytes.to_bytes(2, byteorder='little'))
        self._writer.write(self._bitsPerPixel.to_bytes(2, byteorder='little'))
        self._writer.write(self._dataSize.to_bytes(4, byteorder='little'))

    def writeHeaderMini24(self):
        logging.debug("Writing image header mini...")
        logging.debug(f"Width: {self._width}, Height: {self._height}, RowLength: {self._rowLengthInBytes}")
        logging.debug(f"BPP: {self._bitsPerPixel}, unknown2: {self._unknown2}")

        self._writer.write(self._width.to_bytes(2, byteorder='little'))
        self._writer.write(self._height.to_bytes(2, byteorder='little'))
        self._writer.write(self._rowLengthInBytes.to_bytes(2, byteorder='little'))
        self._writer.write(self._bitsPerPixel.to_bytes(2, byteorder='little'))
        self._writer.write(self._unknown2.to_bytes(4, byteorder='little'))

    def writeHeader(self):
        logging.debug("Writing image header...")
        logging.debug(f"Width: {self._width}, Height: {self._height}, RowLength: {self._rowLengthInBytes}")
        logging.debug(f"BPP: {self._bitsPerPixel}, Unknown1: {self._unknown1}, Unknown2: {self._unknown2}")

        self._writer.write(self._width.to_bytes(4, byteorder='little'))
        self._writer.write(self._height.to_bytes(4, byteorder='little'))
        self._writer.write(self._bitsPerPixel.to_bytes(4, byteorder='little'))
        self._writer.write(self._unknown1.to_bytes(4, byteorder='little'))
        self._writer.write(self._unknown2.to_bytes(4, byteorder='little'))


    def writeImage(self):
        logging.debug("Writing image...")

        pixels = self._image.convert('RGBA')
        data = pixels.getdata()

        for pixel in data:
            (r, g, b, a) = pixel
            self._writer.write(b.to_bytes(1, byteorder='little'))
            self._writer.write(g.to_bytes(1, byteorder='little'))
            self._writer.write(r.to_bytes(1, byteorder='little'))
            self._writer.write(a.to_bytes(1, byteorder='little'))

    def writeImage16(self):
        logging.debug("Writing image 16 bit/pixel...")

        pixels = self._image.convert('RGBA')
        data = pixels.getdata()

        for pixel in data:
            (r, g, b, a) = pixel
            #b = 0
            #g = 0
            temp_b = ((b >> 3) & 0x1f)
            temp_g = (((g >> 2) & 0x7) << 5)
            firstByte = (temp_b | temp_g)

            temp_g2 = ((g >> 5) & 0x07)
            temp_r = (((r >> 3) & 0x1f) << 3)
            secondByte = (temp_g2 | temp_r)
            self._writer.write(firstByte.to_bytes(1, byteorder='little'))
            self._writer.write(secondByte.to_bytes(1, byteorder='little'))
            #self._writer.write(b.to_bytes(1, byteorder='little'))
            #self._writer.write(g.to_bytes(1, byteorder='little'))

    def writeImageMini16(self):
        logging.debug("Writing image mini 16 bit/pixel...")

        pixels = self._image.convert('RGBA')
        data = pixels.getdata()

        for pixel in data:
            (r, g, b, a) = pixel

            #r = ((secondByte >> 3) & 0x1f) << 3
            #g = (((firstByte >> 5) & 0x7) | ((secondByte & 0x07) << 3)) << 2
            #b = (firstByte & 0x1f) << 3
            #alpha = 255

            temp_b = ((b >> 3) & 0x1f)
            temp_g = (((g >> 2) & 0x7) << 5)
            firstByte = (temp_b | temp_g)

            temp_g2 = ((g >> 5) & 0x07)
            temp_r = (((r >> 3) & 0x1f) << 3)
            secondByte = (temp_g2 | temp_r)
            self._writer.write(firstByte.to_bytes(1, byteorder='little'))
            self._writer.write(secondByte.to_bytes(1, byteorder='little'))

    def writeImageMini24(self):
        logging.debug("Writing image mini 24 bit/pixel...")

        pixels = self._image.convert('RGBA')
        data = pixels.getdata()

        for pixel in data:
            (r, g, b, a) = pixel

            alphaByte = 255 - a

            temp_b = ((b >> 3) & 0x1f)
            temp_g = (((g >> 2) & 0x7) << 5)
            secondByte = (temp_b | temp_g)

            temp_g2 = ((g >> 5) & 0x07)
            temp_r = (((r >> 3) & 0x1f) << 3)
            firstByte = (temp_g2 | temp_r)


            self._writer.write(alphaByte.to_bytes(1, byteorder='little'))
            self._writer.write(firstByte.to_bytes(1, byteorder='little'))
            self._writer.write(secondByte.to_bytes(1, byteorder='little'))

    def getImageDataBme(self):
        logging.debug("Generate image data bme 16 bit/pixel...")

        pixels = self._image.convert('RGBA')
        image_data = pixels.getdata()

        result = bytearray()
        y = 0
        x = 0
        temp_data = bytearray()
        start_x = 0
        pixel_width = 0

        for y in range(self._height):
            if len(temp_data) > 0:
                #logging.debug(f"1 y: {y}, x: {start_x}, data_length: {len(temp_data)}")
                result.extend((y-1).to_bytes(2, byteorder='little'))
                result.extend(start_x.to_bytes(2, byteorder='little'))
                result.extend(pixel_width.to_bytes(2, byteorder='little'))
                result.extend(temp_data)
            temp_data.clear()
            start_x = 0
            pixel_width = 0
            for x in range(self._width):
                pixel = image_data[y * self._width + x]

                (r, g, b, a) = pixel
                if a > 0: # skip full transparent pixels
                    if len(temp_data) == 0:
                        start_x = x
                    temp_b = ((b >> 3) & 0x1f)
                    temp_g = (((g >> 2) & 0x7) << 5)
                    firstByte = (temp_b | temp_g)

                    temp_g2 = ((g >> 5) & 0x07)
                    temp_r = (((r >> 3) & 0x1f) << 3)
                    secondByte = (temp_g2 | temp_r)

                    temp_data.extend(firstByte.to_bytes(1, byteorder='little'))
                    temp_data.extend(secondByte.to_bytes(1, byteorder='little'))
                    pixel_width += 1
                else:
                    if len(temp_data) > 0:
                        #logging.debug(f"2 y: {y}, x: {start_x}, data_length: {len(temp_data)}")
                        result.extend(y.to_bytes(2, byteorder='little'))
                        result.extend(start_x.to_bytes(2, byteorder='little'))
                        result.extend(pixel_width.to_bytes(2, byteorder='little'))
                        result.extend(temp_data)
                    temp_data.clear()
                    start_x = 0
                    pixel_width = 0
        if len(temp_data) > 0:
            #logging.debug(f"1 y: {y}, x: {start_x}, data_length: {len(temp_data)}")
            result.extend((y).to_bytes(2, byteorder='little'))
            result.extend(start_x.to_bytes(2, byteorder='little'))
            result.extend(pixel_width.to_bytes(2, byteorder='little'))
            result.extend(temp_data)

        return result

    def hasHalfTransparency(self):
        pixels = self._image.convert('RGBA')
        image_data = pixels.getdata()
        for pixel in image_data:
            (r, g, b, a) = pixel
            if 0 < a < 255:
                return True

        return False

    def hasFullTransparency(self):
        if self._image.mode == "P":
            transparent = self._image.info.get("transparency", -1)
            for _, index in self._image.getcolors():
                if index == transparent:
                    return True
        elif self._image.mode == "RGBA":
            extrema = self._image.getextrema()
            if extrema[3][0] < 255:
                return True

        return False

    def convert32Colorto16(self, pixel):
        (r, g, b, a) = pixel
        r = r >> 3
        g = g >> 3
        b = b >> 3
        return r, g, b
