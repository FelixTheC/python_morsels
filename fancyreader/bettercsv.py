#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 15.02.21
@author: felix
"""
import csv
from collections import namedtuple
from textwrap import dedent


class FancyReader:

    def __init__(self, iterable, *, fieldnames=None, **kwargs):
        self.reader = csv.reader(iterable, **kwargs)
        self.line_num = 0
        self.fieldnames = fieldnames
        self.Row = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.Row is None:
            if self.fieldnames is None:
                self.fieldnames = next(self.reader)
                self.line_num += 1
            self.Row = namedtuple('Row', self.fieldnames)
        row = self.Row(*next(self.reader))
        self.line_num += 1
        return row


if __name__ == '__main__':
    text = dedent("""
            Julia,Spender,purple,Two in the hand is worth one in the fridge
            Sarah,Taylor,green,"Learn from yesterday, live for today"
            Gary,Richter,blue,Be someone you would be proud to know
            Kathleen,Blocker,red,Live everyday like it's your last
            Angelo,Griffith,pink,Don't do today what you could do tomorrow
        """).lstrip()
    reader = FancyReader(
        text.splitlines(),
        fieldnames=['first', 'last', 'color', 'saying'],
    )
