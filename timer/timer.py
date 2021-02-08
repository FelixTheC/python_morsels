#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 08.02.21
@author: felix
"""
import time
from functools import wraps
from statistics import mean
from statistics import median


class Timer:

    def __init__(self, func=None):
        self.func = func
        self._timer = None
        self.elapsed: float = 0.0
        self.runs = []
        self.__supported_statistics = {
            'min': min,
            'max': max,
            'mean': mean,
            'median': median,
        }
        wraps(self.func)(self)

    def __enter__(self):
        self._timer = time.perf_counter()
        self.elapsed = 0.0
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self._timer
        self.runs.append(self.elapsed)

    def __call__(self, *args, **kwargs):
        with self:
            return self.func(*args, **kwargs)

    def __getattr__(self, item):
        if item in self.__supported_statistics.keys():
            return self.__supported_statistics[item](self.runs)
        return object.__getattribute__(self, item)
