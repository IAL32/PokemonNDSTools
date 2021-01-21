import io
import codecs
import os
import binascii
from crccheck.checksum import Checksum16

from constants import Header


class Extractor:
    input_rom_path: str
    output_folder_path: str

    shared_buffer: io.BufferedReader

    def __init__(self, input_rom=None, output_folder="./out") -> None:
        self.input_rom_path = input_rom
        self.output_folder_path = output_folder

    def setup_buffers(self) -> None:
        """
        Set up the shared buffer from the file
        """
        # For a start, we will create a shared buffer
        self.shared_buffer = open(self.input_rom_path, "rb")
        self.shared_buffer.seek(0, 0)

    def extract_header(self) -> None:
        """
        Extracts the first bytes of the game
        """

        self.shared_buffer.seek(Header.HEADER_START_POS.value)
        header_b: bytes = self.shared_buffer.read(Header.HEADER_END_POS.value)

        title_b: bytes = header_b[Header.GAME_TITLE_POS.value:
                                  Header.GAME_TITLE_POS.value + Header.GAME_TITLE_SIZE.value]
        gamecode_b: bytes = header_b[Header.GAME_CODE_POS.value:
                                     Header.GAME_CODE_POS.value + Header.GAME_CODE_SIZE.value]
        makercode_b: bytes = header_b[Header.MAKER_CODE_POS.value:
                                      Header.MAKER_CODE_POS.value + Header.MAKER_CODE_SIZE.value]
        nintendologo_b: bytes = header_b[Header.NINTENDO_LOGO_POS.value:
                                         Header.NINTENDO_LOGO_POS.value + Header.NINTENDO_LOGO_SIZE.value]
        nintendologochecksum_b: bytes = header_b[Header.NINTENDO_LOGO_CHECKSUM_POS.value:
                                                 Header.NINTENDO_LOGO_CHECKSUM_POS.value + Header.NINTENDO_LOGO_CHECKSUM_SIZE.value]

        print("title:", title_b.decode('utf-8'))
        print("gamecode:", gamecode_b.decode('utf-8'))
        print("markercode:", makercode_b.decode('utf-8'))
        print(0xCF56)

        self.shared_buffer.seek(Header.HEADER_CHECKSUM_POS.value, io.SEEK_SET)
        headerchecksum_b: bytes = self.shared_buffer.read(2)

        print("headerchecksum:", int.from_bytes(
            headerchecksum_b, byteorder="little", signed=False))
        print("nintendologochecksum:", int.from_bytes(
            nintendologochecksum_b, byteorder="little", signed=False))
        print(Checksum16.calcbytes(header_b))
        print(Checksum16.calcbytes(nintendologo_b))

    # def calculate_header_checksum(self, header_b: bytes):
    #     print(self.crc16(binascii.hexlify(header_b)))

    def destroy_buffers(self) -> None:
        """
        Flushes pending data and closes the buffer
        """
        self.shared_buffer.flush()
        self.shared_buffer.close()
