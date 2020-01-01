#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 23.12.19
@author: felix
"""
from functools import wraps

from dataclasses import dataclass

NO_RETURN = None


@dataclass
class RecordValues:
    args: tuple
    kwargs: dict
    return_value: any
    exception: Exception


class RecordCalls:
    call_count = 0

    def __init__(self, *args, **kwargs):
        self.func = args[0]
        self.calls = []

    def __call__(self, *args, **kwargs):
        res = NO_RETURN
        ex = None
        try:
            res = self.func(*args, **kwargs)
        except Exception as e:
            ex = e
        finally:
            self.call_count += 1
            self.calls.append(RecordValues(args, kwargs, res, ex))
        if ex is not None:
            raise ex
        return res

    def __getattr__(self, item):
        return getattr(self, item)


def record_calls(func):
    @wraps(func)
    def inner(*args, **kwargs):
        result = ex = None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            ex = e
        finally:
            inner.call_count += 1
            inner.calls.append(RecordValues(args, kwargs, result, ex))
        if ex is not None:
            raise ex
        else:
            return result
    inner.call_count = 0
    inner.calls = []
    return inner


if __name__ == '__main__':
    @record_calls
    def my_func(*args, **kwargs): return args, kwargs
    print(my_func.calls)
    my_func()
