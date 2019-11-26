#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 25.11.19
@author: felix
"""
from typing import Iterable


def window(inputs: Iterable, window_size: int, **kwargs) -> iter:
    data = list(inputs)
    size = window_size
    if len(data) < size:
        fillval = kwargs.pop('fillvalue', None)
        data.extend([fillval for _ in range(size - len(data))])
    if size > 0:
        while len(data) >= size:
            yield tuple(data[i] for i in range(size))
            try:
                data.pop(0)
            except AttributeError:
                data = data[1:]


if __name__ == '__main__':
    print(list(window([], 1)))
