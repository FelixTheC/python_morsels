#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 07.04.20
@author: felix
"""
from copy import deepcopy
from random import choice
from typing import Union


class RandomLooper:

    def __init__(self, value_1, value_2=()):
        self.values_1 = self.__check_if_iterable(value_1)
        self.values_2 = self.__check_if_iterable(value_2)

    @staticmethod
    def __check_if_iterable(value) -> Union[list, tuple]:
        return value if isinstance(value, (list, tuple)) else list(value)

    def _random_loop(self) -> iter:
        val = deepcopy(self.values_1)
        val2 = deepcopy(self.values_2)
        for i in range(len(val)):
            val_choice = choice(val)
            val.remove(val_choice)
            yield val_choice
        for i in range(len(val2)):
            val_choice = choice(val2)
            val2.remove(val_choice)
            yield val_choice

    def __iter__(self):
        return self._random_loop()

    def __len__(self):
        return len(self.values_1) + len(self.values_2)
