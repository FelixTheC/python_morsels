#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 11.12.20
@author: felix
"""
from types import FunctionType
from types import MethodType
from typing import Union


class class_property:

    def __init__(self, method: Union[FunctionType, MethodType]):
        self._method = method

    def __get__(self, instance, cls: object = None):
        return self._method(cls)


class class_only_property(class_property):

    def __get__(self, instance, cls):
        if instance is not None:
            raise AttributeError('This is a "class only" property')
        return super().__get__(instance, cls)


class class_only_method(classmethod):

    def __get__(self, obj, cls):
        if obj is not None:
            raise AttributeError('This is a "class only" method')
        return super().__get__(obj, cls)
