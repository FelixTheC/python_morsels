#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 28.10.20
@author: felix
"""
from itertools import zip_longest


def strict_zip(*iterables):
    empty = object()
    for items in zip_longest(*iterables, fillvalue=empty):
        if empty in items:
            raise ValueError("Given iterables must have same number of items")
        yield items
