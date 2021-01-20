# Introduction

Hack ROM Pokémon projects always had a huge fascination to me. Hundreds of hack ROMs were created, and with great success. However, collaboration amongst the community is a problem. When modifying a Pokémon ROM, only a single person can modify it at a time, as the tools available modify ROMS in such a way that they cannot be easily versioned.

One could think that maybe it might be possible to version the binary extracted file, but that would actually be illegal, since the ROMs internal files are still intellectual property of Nintendo.

The solution proposed by PokemonNDSTools is to re-create some tools that we already have today in such a way that they can create a versioned environment where multiple people can work at the same time. It is also a hope that projects that are still alive to contribute to this project by providing some kind of connecting utility or support for the functionalities provided by this collection of tools.

Another problem of hack ROMs is reproducibility. Not everyone uses the same tools, and not everyone uses the same version of such tools, which means that it could happen that hack ROMs can have subtle, breakable changes if they are modified by multiple people by sharing the NDS file itself, or the extracted files. The collection of tools of this project also aims to solve that by using a more reproducible approach, discussed in the Reproducibility section.

At the beginning, this tool will just be a command-line tool, with no GUI. Graphical User Interface will be added once we have something to actually show.

The way that we want to achieve that is rather simple in theory, and will be discussed in the Mining section of this document. In the Extractor section I will explain how the extraction part takes place.

# Installation

<!-- TODO: add installation instructions -->

# Development

It is highly recommended to use Visual Studio Code for contributing.

In order to start developing this tool, you need the following list of software installed on your computer:

* Python 3.7+, for running the scripts
* PIP3, for package management
* python3-venv, for creating the local virtual environment

After having installed the software above, you have to create the python virtual environment.

To do this, you have to run the following command on the root folder of this project:

```
$ python3 -m venv venv
```

This will create a `venv` folder inside the root directory of this project. In order to activate the virtual environment, you have to run the following command:

Linux:
```
$ source ./venv/bin/activate
```
Windows: <!-- TODO: add instructions for Windows -->
Mac OS: <!-- TODO: add instructions for Mac OS -->

Then, with your virtual environment active, you have to install this project's dependencies with the following command:

```
(venv) $ pip install -r requirements.txt
```

And you will be ready to go! <!-- TODO: at least for now... -->

# Mining

We have vast, yet sparse, knowledge of how data in Pokémon ROMs is arranged. A few files over there handle events, while other bytes over here manage the text, and so on.

Editing these files and saving them directly into the target NDS file, as I mentioned before, is not a great idea if you want other to be able to contribute easily to your project without intellectual property concerns.

The general idea is that from this data we can extract a consistent set of human-readable text files on a per-ROM and per-game basis (this is due to the immense difference between ROMs file structure). In turn, these files will be the ones to be versioned. Because they have been manually generated from this tool, there **should** be no actual intellectual concern (*).

(*) I say **should** because I don't actually know. This whole project could reveal to be useless if proven otherwise. Please, let me know if I should be aware of problems of this kind.

# Reproducibility

After the process of mining takes place, the next natural step is to edit the generated files as one pleases, and then to modify the original ROM with said changes. This tool makes the effort for making this process **reversible**, which means that when a hack ROM edited with this tool gets fed into the extractor tool, the generated files should be exactly as the ones that generated said ROM.

This is fundamental to this project's mission and success.

# Extractor

The role of the extractor functionality is to take a ROM as an input, possibly automatically detect the game, and extract the features of the game. 

# Supported Games

* None

# TODO

1. NDS file extractor
2. Pokémon Diamond support
3. Pokémon Perl support
4. Pokémon Platinum support
5. Pokémon Heart Gold support
6. Pokémon Soul Silver support
7. Pokémon Black support
8. Pokémon White support
9. Pokémon Black 2 support
10. Pokémon White 2 support

# Contributors

* IAL32

# Credits to

* Trifindo Pokemon DS Map Studio - https://github.com/Trifindo/Pokemon-DS-Map-Studio
