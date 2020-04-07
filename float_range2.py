#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 07.04.20
@author: felix
"""


class FloatRange:

    def __init__(self, *args):
        # simulation of a switch case functionality
        # depending on the length of the args run a specific function
        init_func = {
            1: self.__start_only__,
            2: self.__start_stop__,
            3: self.__start_stop_step__,
        }
        try:
            init_func[len(args)](*args)
        except KeyError:
            raise TypeError

    def __start_stop_step__(self, *args):
        self.start = args[0]
        self.stop = args[1]
        self.step = args[2]

    def __start_stop__(self, *args):
        self.start = args[0]
        self.stop = args[1]
        self.step = 1

    def __start_only__(self, *args):
        self.start = 0
        self.stop = args[0]
        self.step = 1

    def __float_list(self):
        start = self.start
        while True:
            if self.step < 0 and start <= self.stop:
                break
            elif self.step > 0 and start >= self.stop:
                break
            else:
                yield start
                start += self.step

    def __iter__(self):
        return self.__float_list()

    def __len__(self):
        return len(list(self.__float_list()))

    def __getitem__(self, item):
        return list(self.__float_list())[item]

    def __reversed__(self):
        return reversed(list(self.__float_list()))


def float_range(*args):
    return FloatRange(*args)
