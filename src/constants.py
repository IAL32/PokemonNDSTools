from enum import Enum

# Byte size and position extracted from: http://dsibrew.org/wiki/DSi_Cartridge_Header


class Header(Enum):
    HEADER_START_POS: int = 0x00
    HEADER_END_POS: int = 0x15D + 1

    GAME_TITLE_POS: int = 0x00
    GAME_TITLE_SIZE: int = 12
    GAME_CODE_POS: int = 0x0C
    GAME_CODE_SIZE: int = 4
    MAKER_CODE_POS: int = 0x10
    MAKER_CODE_SIZE: int = 2
    NINTENDO_LOGO_POS: int = 0xC0
    NINTENDO_LOGO_SIZE: int = 156
    # CRC-16 of [0xC0:0x15B]
    NINTENDO_LOGO_CHECKSUM_POS: int = 0x15C
    NINTENDO_LOGO_CHECKSUM_SIZE: int = 2
    # CRC-16 of [0x00:0x15D]
    HEADER_CHECKSUM_POS: int = 0x15E
    HEADER_CHECKSUM_SIZE: int = 2
