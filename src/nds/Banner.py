
class Banner():

    # NOTE:
    # 0001h = Original
    # 0002h = With Chinese Title
    # 0003h = With Chinese+Korean Titles
    # 0103h = With Chinese+Korean Titles and animated DSi icon
    # UINT16
    version: int
    # 2 bytes
    crc16: bytes
    # NOTE: according to the documentation, there are more CRC16 entries,
    # but we will treat these entries just as reserved bytes.
    # 28 bytes
    reserved: bytes
    # 512 bytes
    iconBitmap: bytes
    # NOTE: 16 colors, 16 bt, range 0x000 - 0x7FFF
    # 32 bytes
    iconPalette: bytes
    # 256 bytes
    title0Japanese: str
    # 256 bytes
    title1English: str
    # 256 bytes
    title2French: str
    # 256 bytes
    title3German: str
    # 256 bytes
    title4Italian: str
    # 256 bytes
    title5Spanish: str
    # NOTE: version 0x0002 and up
    # 256 bytes
    title6Chinese: str
    # NOTE: version 0x0003 and up
    # 256 bytes
    title7Korean: str

    def __init__(self) -> None:
        super().__init__()
