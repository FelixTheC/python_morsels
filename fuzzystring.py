#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 07.12.19
@author: felix
"""
from collections import UserString
import unicodedata
from functools import total_ordering


def normalize(string):
    return unicodedata.normalize("NFD", string.casefold())


@total_ordering
class FuzzyStringMixin:

    @property
    def __get_str_repr(self):
        return normalize(self.data)

    def __eq__(self, other):
        return self.__get_str_repr.lower() == normalize(other.lower())

    def __gt__(self, other):
        return self.__get_str_repr > other

    def __lt__(self, other):
        return self.__get_str_repr < other

    def __contains__(self, item):
        return item.lower() in self.__get_str_repr.lower()


class FuzzyString(FuzzyStringMixin, UserString):

    def __add__(self, other):
        self.data += other
        return self

    def __str__(self):
        return self.data

    def __repr__(self):
        return repr(self.data)


if __name__ == '__main__':
    apple = FuzzyString("Apple")
    print(apple > 'animal')
