from __future__ import annotations
from typing import Any, Iterable
import sys


class Color:
    r: int  # 0-255
    g: int  # 0-255
    b: int  # 0-255
    a: int  # 0-255

    def __init__(self, r: int, g: int, b: int, a: int) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @classmethod
    def fromRGB(cls, r: int, g: int, b: int) -> None:
        cls(r, g, b, 255)

    @classmethod
    def fromRGBA(cls, r: bytes, g: bytes, b: bytes, a: bytes) -> None:
        cls(
            int.from_bytes(r, byteorder="big"),
            int.from_bytes(g, byteorder="big"),
            int.from_bytes(b, byteorder="big"),
            int.from_bytes(a, byteorder="big"),
        )

    @classmethod
    def BGR555ToColor(cls, byte1: bytes, byte2) -> Color:
        r: int
        g: int
        b: int

        bgr: int = int.from_bytes(
            byte1 + byte2, byteorder="little", signed=False)

        r = (bgr & int('000000000011111', 2)) * 0x08
        g = ((bgr & int('000001111100000', 2)) >> 5) * 0x08
        b = ((bgr & int('111110000000000', 2)) >> 10) * 0x08

        return cls(r, g, b, 255)

    @classmethod
    def BGR555ToColors(cls, bgr555: bytes) -> list[Color]:
        colors: list[Color] = [Any] * (len(bgr555) // 2)

        for i in range(len(bgr555) // 2):
            colors[i] = cls.BGR555ToColor(
                bytes([bgr555[i * 2]]), bytes([bgr555[i * 2 + 1]]))

        return colors

    def toHex(self) -> str:
        return '{:0>2X}{:0>2X}{:0>2X}{:0>2X}'.format(self.r, self.g, self.b, self.a)

    def toHexNoAlpha(self) -> str:
        return '{:0>2X}{:0>2X}{:0>2X}'.format(self.r, self.g, self.b)

    def toBytes(self) -> bytes:
        return bytes([self.r, self.g, self.b, self.a])

    def toBytesNoAlpha(self) -> bytes:
        return bytes([self.r, self.g, self.b])

    def toTuple(self) -> tuple[int, int, int, int]:
        return (self.r, self.g, self.b, self.a)

    def toTupleNoAlpha(self) -> tuple[int, int, int]:
        return (self.r, self.g, self.b)
