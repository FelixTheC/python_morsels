#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 04.11.20
@author: felix
"""
from typing import Iterable

EMPTY = object()


class LoopHelper:
    index: int = 0
    is_first: bool = True
    is_last: bool = False
    current = EMPTY
    previous = None
    next = EMPTY

    def __init__(self, iterable: Iterable, previous_default, next_default):
        self._iter = iter(iterable)
        self.previous = previous_default
        self.next_default = next_default

    def get_current(self):
        if self.current is EMPTY:
            self.current = next(self._iter)
        else:
            self.is_first = False
            self.index += 1
            self.previous, self.current = self.current, self.next

    def get_next(self):
        try:
            self.next = next(self._iter)
        except StopIteration:
            self.next = self.next_default
            self.is_last = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_last:
            raise StopIteration
        self.get_current()
        self.get_next()

        return self.current, self


def loop_helper(iterable: Iterable, previous_default=None, next_default=None):
    return LoopHelper(iterable, previous_default, next_default)
