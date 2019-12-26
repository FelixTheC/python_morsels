#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 23.12.19
@author: felix
"""
NO_RETURN = None


class RecordValues:

    def __init__(self, a, k, rv, ex=None):
        self.args = a
        self.kwargs = k
        self.return_value = rv
        self.exception = ex


class record_calls:
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
            self.calls.append(RecordValues(a=args, k=kwargs, rv=res, ex=ex))
        if ex is not None:
            raise ex
        return res

    def __getattr__(self, item):
        return getattr(self, item)


if __name__ == '__main__':
    @record_calls
    def my_func(*args, **kwargs): return args, kwargs
    print(my_func.calls)
    my_func()
