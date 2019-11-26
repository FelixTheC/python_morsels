#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 10.11.19
@author: felix
"""
from math import ceil


class float_range:

    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        (self.start, self.stop, self.step) = (start, stop, step)

    def __iter__(self):
        i = self.start
        for _ in range(len(self)):
            yield i
            i += self.step

    def __len__(self):
        return max(ceil((self.stop-self.start) / self.step), 0)

    def __reversed__(self):
        i = self.start + (len(self) - 1) * self.step
        for _ in range(len(self)):
            yield i
            i -= self.step

    @staticmethod
    def _attrs(self):
        if len(self) == 0:
            return ()
        step = 1 if len(self) else self.step
        return next(iter(self)), next(reversed(self)), step

    def __eq__(self, other):
        if isinstance(other, (float_range, range)):
            return self._attrs(self) == self._attrs(other)
        else:
            return NotImplemented
