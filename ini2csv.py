#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 17.07.20
@author: felix
"""
import csv
import pathlib
from configparser import ConfigParser
from argparse import ArgumentParser


class Ini2Csv:
    __slots__ = ['ini_file', 'csv_file', 'collapsed']

    def __init__(self, ini_file: str, csv_file: str, collapsed: bool = False, *args):
        self.ini_file = pathlib.Path(ini_file)
        self.csv_file = pathlib.Path(csv_file)
        self.collapsed = collapsed

    def parse_file(self):
        config = ConfigParser()
        config.read(self.ini_file)

        headers = None
        rows = []
        for name, section in config.items():
            if name == 'DEFAULT':
                continue

            if self.collapsed:
                if headers is None:
                    headers = ['header', *section.keys()]
                rows.append([name, *section.values()])
            else:
                for key, value in section.items():
                    rows.append([name, key, value])

        with open(self.csv_file, mode='wt') as csv_file:
            csv_writer = csv.writer(csv_file)
            if self.collapsed:
                csv_writer.writerow(headers)
            csv_writer.writerows(rows)

    def __call__(self, *args, **kwargs):
        self.parse_file()


def main():
    parser = ArgumentParser()
    parser.add_argument('ini_file')
    parser.add_argument('csv_file')
    parser.add_argument('--collapsed', action='store_true')
    args = parser.parse_args()

    ini_2_csv = Ini2Csv(ini_file=args.ini_file, csv_file=args.csv_file, collapsed=args.collapsed)
    ini_2_csv()


if __name__ == '__main__':
    main()
