#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 23.10.19
@author: felix
"""
from dataclasses import dataclass


@dataclass
class OrderedSet:
    __vals: list
    __counter = 0

    def __init__(self, arg):
        self.__vals = []
        self.__sort_set__(arg)

    def __sort_set__(self, val):
        [self.__vals.append(i) for i in val if i not in self.__vals]

    def __contains__(self, item):
        return item in self.__vals

    def __getitem__(self, item):
        return self.__vals[item]

    def __len__(self):
        return len(self.__vals)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            r = self.__vals[self.__counter]
            self.__counter += 1
            return r
        except IndexError:
            raise StopIteration

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return self.__vals == other.__vals
        else:
            return set(self.__vals) == other

    def add(self, other):
        if other not in self.__vals:
            vals = self.__vals
            vals.append(other)
            self.__sort_set__(vals)

    def discard(self, other):
        if other in self.__vals:
            vals = self.__vals
            vals.remove(other)
            self.__sort_set__(vals)


if __name__ == '__main__':
    numbers = OrderedSet([1, 2, 3])
    numbers.discard(4)
    print(numbers)
