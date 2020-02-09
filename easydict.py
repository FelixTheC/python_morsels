#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 22.01.20
@author: felix
"""

NORMALIZE = False


class EasyDict(dict):

    def __init__(self, *args, **kwargs):
        global NORMALIZE
        NORMALIZE = kwargs.pop('normalize', False)
        super(EasyDict, self).__init__(*args, **kwargs)

    def __getattr__(self, item):
        if NORMALIZE and item.replace('_', ' ') in self.keys():
            return self.get(item)
        elif item not in self.keys():
            raise AttributeError()
        else:
            return self.get(item)

    def __setattr__(self, key, value):
        if NORMALIZE:
            key = key.replace('_', ' ')
        self.__setitem__(key, value)

    def get(self, k, *args):
        if NORMALIZE:
            k = k.replace('_', ' ')
        if k not in self.keys() and len(args) == 1:
            return args[0]
        else:
            return super().get(k)
