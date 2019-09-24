#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 24.09.19
@author: felix
"""
from collections import deque


def deep_flatten(arg):
    res = []
    if 'generator' in repr(arg):
        tmp = next(arg)
        if 'iterator' in repr(tmp):
            arg = list(tmp) + list([list(a) for a in arg])
        elif isinstance(tmp, (tuple, list)):
            arg = list(tmp) + list(arg)
        else:
            yield tmp
    for val in arg:
        if isinstance(val, (list, tuple, deque)):
            res.extend(list(deep_flatten(val)))
        else:
            res.append(val)
    for r in res:
        yield r


if __name__ == '__main__':
    assert list(deep_flatten((n, (n**3, n**2)) for n in [2, 3])) == [2, 8, 4, 3, 27, 9]
    print(True)
