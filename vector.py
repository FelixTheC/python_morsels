#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 31.05.20
@author: felix
"""
from dataclasses import dataclass
from functools import wraps
from numbers import Number


def except_only(_func=None, *, instance_of: any):
    def wrapper(func):
        @wraps(func)
        def inner(self, other):
            if isinstance(instance_of, str):
                if instance_of != other.__class__.__name__:
                    raise TypeError
            elif not isinstance(other, instance_of):
                raise TypeError
            return func(self, other)
        return inner
    if _func is not None:
        return wrapper(_func)
    else:
        return wrapper


@dataclass
class Vector:
    __slots__ = ('x', 'y', 'z')
    x: int
    y: int
    z: int

    def __iter__(self):
        return (field for field in (self.x, self.y, self.z))

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __repr__(self):
        return f'Vector ({self.x}, {self.y}, {self.z})'

    @except_only(instance_of='Vector')
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    @except_only(instance_of='Vector')
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    @except_only(instance_of=Number)
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other: int):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: int):
        return Vector(self.x // other, self.y // other, self.z // other)

    def __setattr__(self, key, value):
        if hasattr(self, key):
            raise Exception
        return super(Vector, self).__setattr__(key, value)


if __name__ == '__main__':
    v1 = Vector(1, 2, 3)
    v3 = v1 * 4
    print(v3)
    # assert v2 != v1
    # assert v1 == v3
    # print('Test success')
