#!/usr/bin/env python

import fire
from extractor import Extractor
from nds import NDS


def start(input_rom: str = None, output_folder: str = "./out") -> None:
    '''
    Extracts data from the input rom.

    input_rom: str
        The path of the rom to extract data from.
    output_folder: str
        The path where the data extracted from the ROM will be saved. 
    '''

    nds: NDS = NDS()
    extractor = Extractor(input_rom=input_rom,
                          output_folder=output_folder, nds=nds)
    extractor.extract()


def main() -> None:
    fire.Fire(start)


if __name__ == "__main__":
    main()
