#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 10.10.19
@author: felix
"""
from contextlib import ContextDecorator


class suppress(ContextDecorator):

    """Context manager that suppresses exceptions of given types."""

    def __init__(self, *exception_types, default=None):
        self.exception_types = exception_types
        self.default = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exception = exc_val
        self.traceback = exc_tb
        return isinstance(exc_val, self.exception_types)
