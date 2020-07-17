#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 17.07.20
@author: felix
"""
from collections import UserString


class MutableString(UserString):

    def __setitem__(self, key, value):
        data = list(self.data)
        data[key] = value
        self.data = ''.join(data)

    def __delitem__(self, key):
        data = list(self.data)
        del data[key]
        self.data = ''.join(data)

    def append(self, val):
        self.data = f'{self.data}{val}'

    def insert(self, pos, val):
        data = list(self.data)
        data.insert(pos, val)
        self.data = ''.join(data)

    def pop(self, pos=-1):
        data = list(self.data)
        val = data.pop(pos)
        self.data = ''.join(data)
        return MutableString(val)
