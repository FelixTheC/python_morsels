#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 04.02.20
@author: felix
"""
from itertools import count


class CyclicList(list):

    def __iter__(self):
        for i in count():
            yield self[i]

    def __setitem__(self, key, value):
        super().__setitem__(key % len(self), value)

    def __getitem__(self, item):
        if isinstance(item, slice):
            if item.stop is None:
                return super().__getitem__(item)
            start = item.start if item.start is not None else 0
            stop = item.stop if item.stop is not None else 0
            result = [x for x, _ in zip(self, range(max(abs(start), abs(stop)) + 1))][item]
            if (start < stop) and (stop == 0):
                item = slice(stop, abs(start))
                result = [x for x, _ in zip(self, range(abs(start) + 1))][item]
            if (start < stop) and (start < 0) and (stop > 0):
                item = slice(0, abs(stop))
                items = [x for x, _ in zip(self, range(stop + 1))]
                result = items[start:] + items[item]
            return result
        else:
            return super().__getitem__(item % len(self))


if __name__ == '__main__':
    numbers = CyclicList([1, 2, 3, 4, 5])
    print(numbers[-10:0])
    # print(numbers[-1:9])
