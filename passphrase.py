#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 09.01.21
@author: felix
"""
import argparse
import math
import sys
from secrets import choice


parser = argparse.ArgumentParser(description='generates {x}-word passphrases')
parser.add_argument('file',
                    type=argparse.FileType('rt'),
                    help='The text file with words to create the passphrase')

parser.add_argument('--words', '-w',
                    dest='words',
                    type=int,
                    default=4)

parser.add_argument('--verbose', '-v',
                    dest='verbose',
                    default=False,
                    action='store_true')  # important when handling boolean arguments


def main(file_data, *, words: int = 4, verbose: bool = False):

    content = file_data.readlines()
    data = (choice(content) for _ in range(words))

    verbose_msg = None

    if verbose:
        total_words = len(content)
        entropy = round(math.log2(total_words ** words))
        equiv_len = round(entropy / math.log2(62))
        verbose_msg = f'This {words}-word passphrase' \
                      f' picked from {len(content)} words ' \
                      f'is similar to a {equiv_len} character password (entropy {entropy})'

    return ' '.join((elem.strip() for elem in data)), verbose_msg


if __name__ == '__main__':
    args = parser.parse_args()
    passphrase, verbose_msg = main(args.file,
                                   words=args.words,
                                   verbose=args.verbose is not False)
    print(passphrase)
    if verbose_msg:
        print(verbose_msg, file=sys.stderr)

