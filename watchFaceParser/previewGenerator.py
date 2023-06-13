from watchFaceParser.config import Config

class PreviewGenerator:
    @staticmethod
    def createAnimation(descriptor, images, states):
        if not Config.isOldFormat() and (Config.isGtr2Mode() or Config.isGts2Mode() or Config.isTrexProMode()):
            from watchFaceParser.models.gtr2.elements.watchFace import WatchFace
        elif Config.isGts2MiniMode() or Config.isBipUMode() or Config.isBip3Mode():
            from watchFaceParser.models.gts2mini.elements.watchFace import WatchFace
        else:
            from watchFaceParser.models.elements.watchFace import WatchFace

        previewWatchFace = WatchFace(descriptor)
        for watchState in states:
            image = PreviewGenerator.createFrame(previewWatchFace, images, watchState)
            yield image


    @staticmethod
    def createImage(descriptor, images, state):
        if not Config.isOldFormat() and (Config.isGtr2Mode() or Config.isGts2Mode() or Config.isTrexProMode()):
            from watchFaceParser.models.gtr2.elements.watchFace import WatchFace
        elif Config.isGts2MiniMode() or Config.isBipUMode() or Config.isBip3Mode():
            from watchFaceParser.models.gts2mini.elements.watchFace import WatchFace
        else:
            from watchFaceParser.models.elements.watchFace import WatchFace
                    
        previewWatchFace = WatchFace(descriptor)
        return PreviewGenerator.createFrame(previewWatchFace, images, state)


    @staticmethod
    def createFrame(watchFace, resources, state):
        from PIL import Image

        graphics = Image.new('RGB', Config.getImageSize())
        watchFace.draw3(graphics, resources, state)
        graphics = graphics.convert('RGBA')

        if Config.isGtrMode() or Config.isGtr2Mode() or Config.isTrexMode() or Config.isTrexProMode():
            graphics = PreviewGenerator.cutCircled(graphics)
        elif Config.isGtsMode() or Config.isGts2Mode() or Config.isBipUMode() or Config.isBip3Mode():
            graphics = PreviewGenerator.cutRoundedRectangle(graphics, 38)
        elif Config.isGts2MiniMode():
            graphics = PreviewGenerator.cutRoundedRectangle(graphics, 72)

        #graphics.show()
        return graphics

    @staticmethod
    def cutCircled(image):
        from PIL import Image, ImageDraw
        mask = Image.new('L', image.size, 0)
        draw = ImageDraw.Draw(mask)
        color = 255
        draw.ellipse((0, 0, mask.size[0], mask.size[1]), fill=color)
        image.putalpha(mask)
        return image

    @staticmethod
    def cutRoundedRectangle(image, radius):
        from PIL import Image, ImageDraw
        l, t, r, b = (0, 0, image.size[0], image.size[1])
        d = radius * 2
        mask = Image.new('L', image.size, 0)
        draw = ImageDraw.Draw(mask)
        color = 255
        draw.ellipse((l, t, l + d, t + d), fill=color)
        draw.ellipse((r - d, t, r, t + d), fill=color)
        draw.ellipse((l, b - d, l + d, b), fill=color)
        draw.ellipse((r - d, b - d, r, b), fill=color)
        d = radius
        draw.rectangle((l, t + d, r, b - d), fill=color)
        draw.rectangle((l + d, t, r - d, b), fill=color)
        image.putalpha(mask)
        return image