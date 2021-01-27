
from typing import Any, List


class BytesHelper:
    @staticmethod
    def byteToBit4(b: int) -> List[int]:
        result: list[int] = [Any] * 2
        result[0] = b & 0x0F
        result[1] = b & 0xF0 >> 4
        return result

    @staticmethod
    def bytesToBit4(icon_b: bytes) -> List[int]:
        bytes4: list[int] = [0] * len(icon_b) * 2

        for i in range(len(icon_b)):
            b4: list[int] = BytesHelper.byteToBit4(icon_b[i])
            bytes4[i * 2] = b4[0]
            bytes4[i * 2 + 1] = b4[1]

        return bytes4
