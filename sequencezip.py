#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 09.08.20
@author: felix
"""
from collections.abc import Sequence


class SequenceZip(Sequence):

    def __init__(self, *iterables):
        self.data = iterables

    def __len__(self):
        return min(len(item) for item in self.data)

    def __getitem__(self, item):
        if isinstance(item, slice):
            start, stop, step = item.indices(len(self))
            if step < 0:
                stop = -(len(self) + 1 - stop)
            return SequenceZip(*(d[start:stop:step] for d in self.data))
        else:
            if item < 0:
                item += len(self)
            return tuple(val[item] for val in self.data)

    def __eq__(self, other):
        if not isinstance(other, SequenceZip):
            return NotImplemented
        a = tuple(value[:len(self)] for value in self.data)
        b = tuple(value[:len(self)] for value in other.data)
        return a == b

    def __repr__(self):
        return f'SequenceZip{self.data}'
