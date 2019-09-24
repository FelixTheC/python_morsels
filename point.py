#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 16.09.19
@author: felix
"""
from dataclasses import astuple
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
    z: float

    def __str__(self):
        return f'Point(x={self.x}, y={self.y}, z={self.z})'

    def __repr__(self):
        return self.__str__()

    def __add__(self, other: 'Point') -> 'Point':
        x1, x2, x3 = self
        y1, y2, y3 = other
        return Point(x1 + y1, x2 + y2, x3 + y3)

    def __sub__(self, other: 'Point') -> 'Point':
        x1, x2, x3 = self
        y1, y2, y3 = other
        return Point(x1 - y1, x2 - y2, x3 - y3)

    def __mul__(self, other) -> 'Point':
        return Point(self.x * other, self.y * other, self.z * other)

    __rmul__ = __mul__

    def __iter__(self):
        yield from astuple(self)


if __name__ == '__main__':
    p1 = Point(1, 2, 3)
    p2 = p1 * 2
    assert (p2.x, p2.y, p2.z) == (2, 4, 6)
    p3 = 3 * p1
    assert (p3.x, p3.y, p3.z) == (3, 6, 9)
    print(p1 == p2)
    print(p1)
