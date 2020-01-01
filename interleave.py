#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 01.01.20
@author: felix
"""
from itertools import zip_longest


def interleave(*args):
    NULL = object()
    return (elem for z in zip_longest(*(list(t) for t in args), fillvalue=NULL) for elem in z if elem is not NULL)


if __name__ == '__main__':
    in1 = [1, 2, 3, 4]
    in2 = (n ** 2 for n in in1)
    print(list(interleave(in1, in2)))
