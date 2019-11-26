#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 25.11.19
@author: felix
"""
from typing import Mapping, Optional


class PermaDict(dict):
    silent: bool

    def __init__(self, seq=None, **kwargs):
        self.silent = kwargs.pop('silent', False)
        seq = seq if seq is not None else {}
        super(PermaDict, self).__init__(seq, **kwargs)

    def __setitem__(self, key, value):
        if key in self:
            if self.silent is False:
                raise KeyError(f"'{key}' already in dictionary.")
        else:
            super(PermaDict, self).__setitem__(key, value)

    def force_set(self, key, value):
        super(PermaDict, self).__setitem__(key, value)

    def update(self, __m: Optional[Mapping[any, any]] = None, **kwargs: any) -> None:
        force = kwargs.pop('force', False)
        func_options = {
            True: super(PermaDict, self).__setitem__,
            False: self.__setitem__,
        }
        func = func_options[force]
        if kwargs:
            __m = kwargs
        if isinstance(__m, dict):
            for key, val in __m.items():
                func(key, val)
        else:
            for item in __m:
                func(item[0], item[1])


if __name__ == '__main__':
    locations = PermaDict()
    locations.update(c=3)
    print(locations)
