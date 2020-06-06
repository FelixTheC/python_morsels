#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 06.06.20
@author: felix
"""
from itertools import zip_longest
from typing import Optional


class Unpacker:

    def __init__(self, data: Optional[dict] = None):
        if data is not None:
            self._data = {k: v for k, v in data.items()}

    def __getitem__(self, item):
        if isinstance(item, (tuple, list)):
            return tuple(self._data[i] for i in item)
        return self._data[item]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            for k, v in zip_longest(key, value):
                if k is not None and v is not None:
                    self._data[k] = v
                else:
                    raise ValueError
        else:
            self._data[key] = value

    def __getattr__(self, item):
        return self._data[item]

    def __setattr__(self, key, value):
        if not isinstance(value, dict):
            self._data[key] = value
            return
        super(Unpacker, self).__setattr__(key, value)

    def __iter__(self):
        return (v for v in self._data.values())

    def __repr__(self):
        data_str = ', '.join([f'{k}={repr(v)}' for k, v in self._data.items()])
        return f'{self.__class__.__name__}({data_str})'
