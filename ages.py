#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 24.02.20
@author: felix
"""
import calendar
import datetime
from fractions import Fraction


def year_to_seconds(year: int):
    return year * (365*24*60*60)


def time_diff(dt_str: str):
    dt_time = datetime.datetime
    date = dt_time.strptime(dt_str, '%Y-%m-%d')
    abs(calendar.leapdays(dt_time.today().year, date.year))
    return dt_time.today() - date


def leap_days(dt_str: str):
    dt_time = datetime.datetime
    date = dt_time.strptime(dt_str, '%Y-%m-%d')
    return abs(calendar.leapdays(dt_time.today().year, date.year))


def is_over(*args, **kwargs):
    dt_dist = time_diff(args[1])
    check_age = args[0]
    return year_to_seconds(check_age) <= dt_dist.total_seconds()


def get_age(*args, **kwargs):
    dt_dist = time_diff(args[0])
    days = dt_dist.days
    years = days * 0.002737851
    exact = kwargs.get('exact', False)
    if exact:
        fraction = '83/366' if calendar.isleap(datetime.datetime.today().year) else '82/365'
        return int(years) + Fraction(fraction)
    if days == 366:
        return 1
    elif days < 366:
        return 0
    else:
        if leap_days(args[0]) > 100:
            years += leap_days(args[0])/1000
        y, dezi = str(years).split('.')
        if int(dezi[2]) < 9:
            return int(y)
        else:
            return int(y) + 1
