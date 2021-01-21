from . import Banner


class Header():
    # 12 bytes
    title_s: str
    # 4 bytes
    gameCode_s: str
    # 2 bytes
    makerCode_s: str
    # 1 byte
    unitCode_b: bytes
    # UInt8
    encryptionSeed_ui8: int
    # UInt8
    deviceCapacity_ui8: int
    # 7 reserved zero-filled bytes
    # 1 reserved zero, used on DSi
    reserved_b: bytes
    # 1 byte
    region_b: bytes
    # UInt8
    version_ui8: int
    # 1 byte
    autostart_ui8: int
    # UInt32
    arm9ROMOffset_ui32: int
    # UInt2
    arm9EntryAddress_ui32: int
    # UInt32
    arm9RAMAddress_ui32: int
    # UInt32
    arm9Size_ui32: int
    # UInt32
    arm7ROMOffset_ui32: int
    # UInt32
    arm7EntryAddress_ui32: int
    # UInt32
    arm7RAMAddress_ui32: int
    # UInt32
    arm7Size_ui32: int
    # UInt32
    fileNameTableOffset_ui32: int
    # UInt32
    fileNameTableSize_ui32: int
    # UInt32
    fileAllocationTableOffset_ui32: int
    # UInt32
    fileAllocationTableSize_ui32: int
    # UInt32
    fileARM9OverlayOffset_ui32: int
    # UInt32
    fileARM9OverlaySize_ui32: int
    # UInt32
    fileARM7OverlayOffset_ui32: int
    # UInt32
    fileARM7OverlaySize_ui32: int
    # 4 bytes
    portSettingNormalCommands_b: bytes
    # 4 bytes
    portSettingKey1Commands_b: bytes
    # UInt32
    iconOffset_ui32: int
    # UInt16
    secureAreaChecksum_ui16: int
    # 2 bytes
    secureAreaDelay_b: bytes
    # UInt32
    arm9AutoLoadListRAMAddress_ui32: int
    # UInt32
    arm7AutoLoadListRAMAddress_ui32: int
    # 8 bytes
    secureAreaDisable_b: bytes
    # UInt32
    totalUsedROMSize_ui32: int
    # UInt32
    romHeaderSize_ui32: int
    # 56 bytes zero-filled
    reserved56_b: bytes
    # 156 bytes for Nintendo Logo
    nintendoLogo_b: bytes
    # UInt16 CRC-16 of nintendoLogo_b [0xC0:0x15B] === 0xCF56
    logoCRC16_ui16: int
    # UInt16 CRC of header section [0x00:0x15D]
    headerCRC16_ui16: int
    # UInt32
    debugROMOffset_ui32: int
    # UInt32
    debugSize_ui32: int
    # UInt32
    debugRAMAddress_ui32: int

    def __init__(self) -> None:
        super().__init__()
