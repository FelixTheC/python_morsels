#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 04.02.21
@author: felix
"""
from typing import Any
from typing import Iterator

EMPTY = object()


def chunked(obj: Any, num: int, *, fill: Any = EMPTY):

    class Chunks:

        def __init__(self, iter_obj: Iterator, chunk_size: int, _fill: Any):
            self._iter_obj = iter_obj
            self._chunk_size = chunk_size
            self._fill = _fill

        def __next__(self):
            return self

        def __iter__(self):
            while True:
                chunks = []
                for val in range(self._chunk_size):
                    try:
                        chunks.append(next(self._iter_obj))
                    except StopIteration:
                        break
                if chunks:
                    if len(chunks) != self._chunk_size:
                        if self._fill != EMPTY:
                            for _ in range(self._chunk_size - len(chunks)):
                                chunks.append(self._fill)
                    yield chunks
                else:
                    break

    _chunks = Chunks(iter(obj), num, fill)
    return iter(_chunks)


if __name__ == '__main__':
    print(list(chunked(range(10), 4)))
