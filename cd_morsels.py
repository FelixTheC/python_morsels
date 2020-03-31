#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 31.03.20
@author: felix
"""
import os
from os.path import abspath, exists, dirname, realpath
from pathlib import Path
from typing import Optional
from tempfile import mkdtemp


def cd(directory: Optional[str] = None):

    class MorselsCd:
        current: Path
        previous: Path
        tmp_dir = False

        def __init__(self, _directory: Optional[str] = None):
            self.directory = _directory

        def __enter__(self, *args, **kwargs):
            self.previous = Path.cwd()
            if self.directory is not None:
                os.chdir(self.directory)
            else:
                os.chdir(self._create_tmp_dir())
                self.tmp_dir = True
            self.current = Path.cwd()
            return self

        def __exit__(self, *args, **kwargs):
            if args:
                exc_type, exc_val, exc_tb = args
            else:
                exc_type = exc_val = exc_tb = None
            if exc_type:
                os.chdir(str(self.previous.absolute()))
                raise exc_type
            else:
                os.chdir(str(self.previous.absolute()))
                if self.tmp_dir:
                    [os.remove(str(i.absolute())) for i in self.current.iterdir()]
                    self.current.rmdir()
            return True

        @staticmethod
        def _create_tmp_dir():
            _directory = realpath(mkdtemp())
            if not Path(_directory).is_dir():
                Path(_directory).mkdir()
            return _directory

        def enter(self, *args, **kwargs):
            return self.__enter__(*args, **kwargs)

        def exit(self, *args, **kwargs):
            return self.__exit__(*args, **kwargs)

    return MorselsCd(directory)
