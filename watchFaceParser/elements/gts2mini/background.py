from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.models.color import Color
from watchFaceParser.elements.gts2mini.backgroundElements.backgroundCustomTextLayer import BackgroundZeppCustomTextLayer

class Background:
    definitions = {
        1: { 'Name': 'Image', 'Type': Image},
        2: { 'Name': 'BackgroundColor', 'Type': Color},
        3: { 'Name': 'Preview', 'Type': Image},
        4: { 'Name': 'PreviewTradChinese', 'Type': Image},
        5: { 'Name': 'PreviewChinese', 'Type': Image},
        6: { 'Name': 'FloatingLayer', 'Type': Image},
        7: { 'Name': 'ZeppCustomBackgroundPreview', 'Type': Image},
        8: { 'Name': 'ZeppCustomTextLayerTradChinese', 'Type': BackgroundZeppCustomTextLayer},
        9: { 'Name': 'ZeppCustomTextLayer', 'Type': BackgroundZeppCustomTextLayer},
        10: { 'Name': 'ZeppCustomTextLayerChinese', 'Type': BackgroundZeppCustomTextLayer},
    }