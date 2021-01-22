
class Banner():

    # NOTE:
    # 0001h = Original
    # 0002h = With Chinese Title
    # 0003h = With Chinese+Korean Titles
    # 0103h = With Chinese+Korean Titles and animated DSi icon
    # UInt16
    version_ui16: int
    # UInt16
    crc16_ui16: int
    # NOTE: according to the documentation, there are more CRC16 entries,
    # but we will treat these entries just as reserved bytes.
    # 28 bytes
    reserved_b: bytes
    # 512 bytes
    iconBitmap_b: bytes
    # NOTE: 16 colors, 16 bt, range 0x000 - 0x7FFF
    # 32 bytes
    iconPalette_b: bytes
    # 256 bytes
    title0Japanese_s: str
    # 256 bytes
    title1English_s: str
    # 256 bytes
    title2French_s: str
    # 256 bytes
    title3German_s: str
    # 256 bytes
    title4Italian_s: str
    # 256 bytes
    title5Spanish_s: str
    # NOTE: version 0x0002 and up
    # 256 bytes
    title6Chinese_s: str
    # NOTE: version 0x0003 and up
    # 256 bytes
    title7Korean_s: str

    def __init__(self) -> None:
        super().__init__()
