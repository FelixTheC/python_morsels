#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 25.09.19
@author: Python Morsels
"""
from collections.abc import Iterable


def deep_flatten(iterable):
    """Flatten an iterable of iterables."""
    iterators = [iter(iterable)]
    while iterators:
        for item in iterators[-1]:
            if (isinstance(item, Iterable)
                    and not isinstance(item, (str, bytes))):
                iterators.append(iter(item))
                break
            else:
                yield item
        else:  # nobreak
            iterators.pop()
