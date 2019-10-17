#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 16.10.19
@author: python morsels
"""
from collections import Counter


def format_ranges(numbers):
    pairs = []
    counts = Counter(sorted(numbers))
    while counts:
        start = end = None
        for n in counts.keys():
            counts[n] -= 1
            if start is None:
                start = n
            elif n > end+1:
                pairs.append((start, end))
                start = n
            end = n
        pairs.append((start, end))
        counts = +counts
    pairs.sort()
    return ",".join(f"{start}-{end}" if start != end else f"{start}" for (start, end) in pairs)


if __name__ == '__main__':
    print(format_ranges([1, 9, 1, 7, 3, 8, 2, 4, 2, 4, 7]))
