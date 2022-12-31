#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 24.01.21
@author: felix
"""
from codecs import Codec
from textwrap import dedent

tmp = {
    8220: ord('"'),
    8221: ord('"'),
    8216: ord("'"),
    8217: ord("'")
}


def unsmart():
    pass


def main():
    pass


if __name__ == '__main__':
    a = '"'
    contents = '“This is a quotation”'
    print(''.join([chr(ord(char)) if ord(char) < 122 else chr(tmp[ord(char)]) for char in contents]))
    print(contents.encode('utf8').replace(b'\xe2\x80\x9c', b'"').replace(b'\xe2\x80\x9d', b'"').decode('utf8'))
