﻿from watchFaceParser.elements.gts2mini.basicElements.pointerScale import PointerScale
from watchFaceParser.elements.gts2mini.basicElements.image import Image


class Scale:
    definitions = {
        1: { 'Name': 'PointerScale', 'Type': PointerScale},
        2: { 'Name': 'BottomImageIndex', 'Type': Image},
        3: { 'Name': 'BottomImageIndexChinese', 'Type': Image},
        4: { 'Name': 'BottomImageIndexTradChinese', 'Type': Image},
    }
