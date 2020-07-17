#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 11.04.20
@author: felix
"""
from textwrap import dedent
import re


def replace_2_ending_whitespace(text_line: str) -> str:
    pattern = r'[ ]{2,}$'
    replace_str = '#$#'
    if re.findall(pattern, text_line):
        text_line += replace_str
    return text_line


def replace_placeholder(lines_of_text: str) -> str:
    pattern = r'(#\$# )'
    return re.sub(pattern, '\n', lines_of_text)


def linebreak_before_list_elem(text_line) -> str:
    pattern = r'^[-0-9.]+'
    if re.findall(pattern, text_line):
        return f'\n{text_line}'
    return text_line


def unwrap_lines(text: str) -> str:
    result = []
    solution = ''
    text_list = text.rstrip().split('\n')
    if len(text_list) == 1:
        return text
    for index, line in enumerate(text_list):
        if line:
            result.append(linebreak_before_list_elem(replace_2_ending_whitespace(line)).rstrip())
        else:
            solution += ' '.join(result)
            solution += '\n' if text_list[index - 1] == '' else '\n\n'
            result = []

    if result:
        solution += ' '.join(result)
        solution += '\n'
    return replace_placeholder(solution)


if __name__ == '__main__':
    text = dedent("""
            This text has bullet points:
            - Point 1
            - Point 2

            There are also numbered points:
            1. First item
            2. Second item
        """).lstrip()
    unwrapped_text = unwrap_lines(text)
    print(text)
