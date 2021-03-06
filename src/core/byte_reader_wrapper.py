import io


class ByteReaderWrapper:
    buffer: io.BufferedReader

    def __init__(self, buffer: io.BufferedReader):
        if not buffer.seekable:
            raise Exception("Cannot seek buffer")
        self.buffer = buffer

    def readUInt8(self) -> int:
        return int.from_bytes(self.readByte(), byteorder="little", signed=False)

    def readUInt16(self) -> int:
        return int.from_bytes(self.readBytes(2), byteorder="little", signed=False)

    def readUInt32(self) -> int:
        return int.from_bytes(self.readBytes(4), byteorder="little", signed=False)

    def readChars(self, nbytes: int, encoding='utf-8', trim_padding=False) -> str:
        chars: str = self.readBytes(nbytes=nbytes).decode(encoding)

        if trim_padding:
            chars = chars.replace('\x00', '')
            chars = chars.replace('\uFFFF', '')

        return chars

    def readByte(self) -> bytes:
        return self.readBytes(nbytes=1)

    def readBytes(self, nbytes: int) -> bytes:
        return self.buffer.read(nbytes)

    def seek(self, offset, whence=io.SEEK_SET) -> int:
        return self.buffer.seek(offset, whence)

    def flush(self) -> None:
        self.buffer.flush()

    def close(self) -> None:
        self.buffer.close()
