class DrawerHelper:
    @staticmethod
    def calculateBounds(images, spacing):
        assert(type(images) == list)
        assert(type(spacing) == int)

        width = 0
        height = 0

        for image in images:
            imageWidth = image.getBitmap().size[0]
            imageHeight = image.getBitmap().size[1]

            width += imageWidth + spacing
            if imageHeight > height:
                height = imageHeight

        width -= spacing
        return (int(width), height)


    @staticmethod
    def drawImages(drawer, images, spacing, alignment, box, verticalOffset=0):
        assert(type(images) == list)
        assert(type(spacing) == int)
        assert(type(alignment) == int)

        (bitmapWidth, bitmapHeight) = DrawerHelper.calculateBounds(images, spacing)

        from watchFaceParser.models.textAlignment import TextAlignment
        alignmentFlag = TextAlignment(alignment)

        x = 0
        y = 0
        if alignmentFlag.hasFlag(TextAlignment.Left):
            x = box.getX()
        elif alignmentFlag.hasFlag(TextAlignment.Right):
            x = box.getRight() - bitmapWidth + 1
        else:
            x = box.getLeft() + int((box.getRight() - box.getLeft() - bitmapWidth) / 2)

        if (not alignmentFlag.hasFlag(TextAlignment.Vertical) and alignmentFlag.hasFlag(TextAlignment.Top)) or (
                alignmentFlag.hasFlag(TextAlignment.Vertical) and alignmentFlag.hasFlag(TextAlignment.Left)):
            y = box.getTop()
        elif (not alignmentFlag.hasFlag(TextAlignment.Vertical) and alignmentFlag.hasFlag(TextAlignment.Bottom)) or (
                  alignmentFlag.hasFlag(TextAlignment.Vertical) and alignmentFlag.hasFlag(TextAlignment.Right)):
            y = box.getBottom() - bitmapHeight + 1
        else:
            y = box.getTop() + int((box.getBottom() - box.getTop() - bitmapHeight) / 2)

        if x < box.getLeft():
            x = box.getLeft()
        if y < box.getTop():
            y = box.getTop()

        for image in images:
            temp = image.getBitmap()
            drawer.paste(temp, (x,y), temp)

            if alignmentFlag.hasFlag(TextAlignment.Vertical):
                y += image.getBitmap().size[1]
            else:
                x += image.getBitmap().size[0]
            x += int(spacing)
            if alignmentFlag.hasFlag(TextAlignment.Right):
                y -= verticalOffset
            else:
                y += verticalOffset

        from watchFaceParser.config import Config
        if Config.getBorderAlignment():
            from PIL import ImageDraw
            d = ImageDraw.Draw(drawer)
            d.rectangle((box.getLeft(), box.getTop(), box.getRight(), box.getBottom()), outline=(200, 200, 200))