from typing import Optional


class FollowObject:
    def __init__(self, x=0, y=0, text='', combing=0, angle=0, radius=0, size=0, color=0):
        self._x = x
        self._y = y
        self._angle = angle
        self._radius = radius
        self._text = text
        self._combing = combing
        self._size=size
        self._color=color

    def getX(self) -> int:
        return self._x

    def setX(self, x: int):
        self._x = x

    def getY(self) -> int:
        return self._y

    def setY(self, y: int):
        self._y = y

    def getText(self) -> str:
        return self._text

    def setText(self, text: str):
        self._text = text

    def getCombing(self) -> Optional[int]:
        return self._combing

    def getAngle(self) -> Optional[int]:
        return self._angle

    def setAngle(self, angle: int):
        self._angle = angle

    def getRadius(self) -> Optional[int]:
        return self._radius

    def setRadius(self, radius: int):
        self._radius = radius

    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color=color

    def getSize(self):
        return self._size

    def setSize(self, size):
        self._size=size
