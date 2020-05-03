#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 03.05.20
@author: felix
"""
from dataclasses import dataclass


@dataclass
class alias:  # no pep8
    """
    This class is a descriptor
    """

    attr_name: str
    write: bool = False

    def __get__(self, instance, owner):
        obj = instance if instance is not None else owner
        return getattr(obj, self.attr_name)

    def __set__(self, instance, value):
        if self.write:
            setattr(instance, self.attr_name, value)
        else:
            raise AttributeError
