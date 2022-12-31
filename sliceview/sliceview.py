#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 23.02.21
@author: felix
"""


class SliceView:

    def __init__(self, data, start=None, stop=None, step=None):
        self.data = list(iter(data))
        start, stop, step = slice(start, stop, step).indices(len(data))
        self.range = range(start, stop, step)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return SliceView(self, start=item.start or 0, stop=item.stop, step=item.step or 1)
        else:
            return self.data[self.range[item]]

    def __next__(self):
        return self

    def __len__(self):
        return len(self.range)

    def __iter__(self):
        for i in self.range:
            yield self.data[i]


if __name__ == '__main__':
    numbers = [2, 1, 3, 4, 7, 11, 18]
    view = SliceView(numbers, start=1, stop=5)
    print(len(view))
