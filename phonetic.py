#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 13.01.21
@author: felix
"""
import argparse
import pathlib
import sys
from typing import List
from typing import Union
from unicodedata import normalize

nato_alphabet = {
    'A': 'Alfa',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'Juliett',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'X-ray',
    'Y': 'Yankee',
    'Z': 'Zulu',
}

parser = argparse.ArgumentParser(description='Spell Nato.')
parser.add_argument('words', type=str, nargs='+')
parser.add_argument('--file', '-f', type=pathlib.Path)


def _normalize_word(char: str) -> str:
    tmp = normalize('NFD', char)
    if len(tmp) == 1:
        return tmp
    return tmp[0]


def spell_word(word: str):
    for _char in word:
        char = _normalize_word(_char)
        if char == ' ' and char not in nato_alphabet:
            print()
            continue
        if char.isnumeric():
            print(nato_alphabet[char])
            continue
        if char.upper() in nato_alphabet:
            print(nato_alphabet[char.upper()])
        if char.lower() in nato_alphabet:
            print(nato_alphabet[char.lower()])


def create_custom_dict(lines: list):
    global nato_alphabet
    nato_alphabet = dict([((l := line.split(' '))[0].strip(), l[1].strip())
                          for line in lines
                          ])


def main(word: Union[str, List[str]] = None, file: pathlib.Path = None):
    if file is not None:
        with file.open('rt') as f:
            create_custom_dict(f.readlines())
    if word is None:
        word = input('Text to spell out: ')
    if isinstance(word, list):
        word = ' '.join(word)
    spell_word(word)


if __name__ == '__main__':
    words = parser.parse_args().words if len(sys.argv) > 1 else None
    arg_file: Union[pathlib.Path, None] = parser.parse_args().file if len(sys.argv) > 1 else None
    main(words, arg_file)
