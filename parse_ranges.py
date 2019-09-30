#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 30.09.19
@author: felix
"""


def split_nums(num: str) -> tuple:
    nums = num.split('-')
    start = int(nums[0])
    try:
        end = int(nums[1])
    except (IndexError, ValueError):
        end = start
    return start, end


def parse_ranges(args: str):
    ranges = args.split(',')
    for num in ranges:
        start, end = split_nums(num)
        while start <= end:
            yield start
            start += 1
