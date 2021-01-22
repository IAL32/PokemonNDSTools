import binascii
import codecs
import io
import os
from pprint import pprint

from crccheck.checksum import Checksum16

from core import ByteReaderWrapper
from nds import NDS


class Extractor:
    input_rom_path: str
    output_folder_path: str
    nds: NDS
    shared_buffer: ByteReaderWrapper

    def __init__(self, input_rom: str = None, output_folder: str = "./out", nds: NDS = None) -> None:
        if input_rom is None:
            raise Exception("Cannot have empty path as input rom")
        self.input_rom_path = input_rom
        self.output_folder_path = output_folder
        if nds is None:
            raise Exception(
                "A problem while creating Extractor instance from nds occured")
        self.nds = nds

    def extract(self) -> None:
        self.setup_buffers()
        self.extract_header()
        self.extract_banner()
        self.destroy_buffers()

    def setup_buffers(self) -> None:
        """
        Set up the shared buffer from the file
        """
        # For a start, we will create a shared buffer
        self.shared_buffer = ByteReaderWrapper(open(self.input_rom_path, "rb"))

    def extract_header(self) -> None:
        """
        Extracts the first bytes of the game
        """

        self.shared_buffer.seek(0, 0)
        self.nds.header.title_s = self.shared_buffer.readChars(12)
        self.nds.header.gameCode_s = self.shared_buffer.readChars(4)
        self.nds.header.makerCode_s = self.shared_buffer.readChars(2)
        self.nds.header.unitCode_b = self.shared_buffer.readByte()
        self.nds.header.encryptionSeed_ui8 = self.shared_buffer.readUInt8()
        self.nds.header.deviceCapacity_ui8 = self.shared_buffer.readUInt8()

        self.nds.header.reserved_b = self.shared_buffer.readBytes(8)
        self.nds.header.region_b = self.shared_buffer.readByte()
        self.nds.header.version_ui8 = self.shared_buffer.readUInt8()
        self.nds.header.autostart_ui8 = self.shared_buffer.readUInt8()

        self.nds.header.arm9ROMOffset_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.arm9EntryAddress_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.arm9RAMAddress_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.arm9Size_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.arm7ROMOffset_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.arm7EntryAddress_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.arm7RAMAddress_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.arm7Size_ui32 = self.shared_buffer.readUInt32()

        self.nds.header.fileNameTableOffset_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.fileNameTableSize_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.fileAllocationTableOffset_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.fileAllocationTableSize_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.fileARM9OverlayOffset_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.fileARM9OverlaySize_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.fileARM7OverlayOffset_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.fileARM7OverlaySize_ui32 = self.shared_buffer.readUInt32()

        self.nds.header.portSettingNormalCommands_b = self.shared_buffer.readBytes(
            4)
        self.nds.header.portSettingKey1Commands_b = self.shared_buffer.readBytes(
            4)

        self.nds.header.iconOffset_ui32 = self.shared_buffer.readUInt32()

        self.nds.header.secureAreaChecksum_ui16 = self.shared_buffer.readUInt16()
        self.nds.header.secureAreaDelay_b = self.shared_buffer.readBytes(2)
        self.nds.header.arm9AutoLoadListRAMAddress_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.arm7AutoLoadListRAMAddress_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.secureAreaDisable_b = self.shared_buffer.readBytes(8)
        self.nds.header.totalUsedROMSize_ui32 = self.shared_buffer.readUInt32()

        self.nds.header.romHeaderSize_ui32 = self.shared_buffer.readUInt32()

        self.nds.header.reserved56_b = self.shared_buffer.readBytes(56)
        self.nds.header.nintendoLogo_b = self.shared_buffer.readBytes(156)

        self.nds.header.logoCRC16_ui16 = self.shared_buffer.readUInt16()
        self.nds.header.headerCRC16_ui16 = self.shared_buffer.readUInt16()

        self.nds.header.debugROMOffset_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.debugSize_ui32 = self.shared_buffer.readUInt32()
        self.nds.header.debugRAMAddress_ui32 = self.shared_buffer.readUInt32()

    def extract_banner(self) -> None:
        if not self.nds.header.iconOffset_ui32:
            raise Exception("Icon offset not yet set")
        self.shared_buffer.seek(self.nds.header.iconOffset_ui32)
        self.nds.banner.version_ui16 = self.shared_buffer.readUInt16()
        self.nds.banner.crc16_ui16 = self.shared_buffer.readUInt16()
        self.nds.banner.reserved_b = self.shared_buffer.readBytes(0x1C)

        self.nds.banner.iconBitmap_b = self.shared_buffer.readBytes(0x200)
        self.nds.banner.iconPalette_b = self.shared_buffer.readBytes(0x20)

        self.nds.banner.title0Japanese_s = self.shared_buffer.readChars(
            0x100, encoding="utf-16", trim_padding=True)
        self.nds.banner.title1English_s = self.shared_buffer.readChars(
            0x100, encoding="utf-16", trim_padding=True)
        self.nds.banner.title2French_s = self.shared_buffer.readChars(
            0x100, encoding="utf-16", trim_padding=True)
        self.nds.banner.title3German_s = self.shared_buffer.readChars(
            0x100, encoding="utf-16", trim_padding=True)
        self.nds.banner.title4Italian_s = self.shared_buffer.readChars(
            0x100, encoding="utf-16", trim_padding=True)
        self.nds.banner.title5Spanish_s = self.shared_buffer.readChars(
            0x100, encoding="utf-16", trim_padding=True)
        self.nds.banner.title6Chinese_s = self.shared_buffer.readChars(
            0x100, encoding="utf-16", trim_padding=True)
        self.nds.banner.title7Korean_s = self.shared_buffer.readChars(
            0x100, encoding="utf-16", trim_padding=True)

        pprint(vars(self.nds.banner))

    # def calculate_header_checksum(self, header_b: bytes):
    #     print(self.crc16(binascii.hexlify(header_b)))

    def bytesToBitmap(list_b: bytes):
        pass

    def destroy_buffers(self) -> None:
        """
        Flushes pending data and closes the buffer
        """
        self.shared_buffer.flush()
        self.shared_buffer.close()
