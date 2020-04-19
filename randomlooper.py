#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 07.04.20
@author: felix
"""
from random import shuffle
from itertools import chain


class RandomLooper:

    def __init__(self, *args):
        self.values = list(chain.from_iterable(args))

    def __iter__(self):
        shuffle(self.values)
        yield from self.values

    def __len__(self):
        return len(self.values)
