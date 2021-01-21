#!/usr/bin/env python

import fire

from extractor import Extractor


def start(input_rom: str = None, output_folder: str = "./out") -> None:
    '''
    Extracts data from the input rom.

    input_rom: str
        The path of the rom to extract data from.
    output_folder: str
        The path where the data extracted from the ROM will be saved. 
    '''
    extractor = Extractor(input_rom=input_rom, output_folder=output_folder)
    extractor.setup_buffers()
    extractor.extract_header()
    extractor.destroy_buffers()


def main() -> None:
    fire.Fire(start)


if __name__ == "__main__":
    main()
