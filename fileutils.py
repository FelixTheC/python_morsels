#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 12.09.20
@author: felix
"""
import io
import os
import re

CHUNK_SIZE = 1024


def is_start_byte(byte):
    """Return True if given byte starts a UTF-8 character."""
    return (byte >> 6) != 0b10


def seek_and_read(file_object, position, chunk_size, wiggle=4):
    """Seek to position, find first UTF-8 start byte, and read chunk."""
    position = file_object.seek(position, os.SEEK_SET)
    data = file_object.read(chunk_size)
    for i in range(wiggle):
        if is_start_byte(data[i]):
            return position, data[i:].decode('utf-8')
        position += 1
    raise UnicodeDecodeError(f"Invalid UTF-8 data found: {data}")


def last_lines(filename, *, chunk_size=io.DEFAULT_BUFFER_SIZE):
    data = ''
    with open(filename, mode='rb') as f:
        position = f.seek(0, os.SEEK_END)
        while position:
            position, previous = max(0, position-chunk_size), position
            position, new = seek_and_read(f, position, previous-position)
            data, *lines = re.findall(r'.*\n|.+$', new + data)
            yield from reversed(lines)
        yield data
