#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 11.11.19
@author: felix
"""
from typing import Optional
from collections import Counter
from calendar import monthrange
import datetime
import pandas as pd


class Weekday:
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(year: int, month: int, *,
                nth: Optional[int] = None,
                weekday: Optional[any] = None) -> datetime.date:
    thursday = weekday if weekday is not None else 3
    dates = [datetime.date(year=year, month=month, day=i) for i in range(1, monthrange(year, month)[1] + 1)]

    df = pd.DataFrame(data=dates, columns=['date', ])
    df['date'] = pd.to_datetime(df['date'])
    df['week'] = df['date'].apply(lambda x: x.week)
    df['weekday'] = df['date'].apply(lambda x: x.weekday())
    if month == 1:
        # january can have weeks from the year before => week 52
        df = df[df['week'] <= 5]

    length = 7 if nth is not None and nth > 0 else 1
    complete_weeks = [k for k, v in Counter(df.week.values).items() if v >= length]
    week_num = complete_weeks[0] + (nth - 1) if nth is not None and nth > 0 else complete_weeks[-1]

    try:
        week_num = week_num if nth is not None and nth > 0 else week_num + (nth + 1)
    except TypeError:
        pass

    if nth is None and week_num > 1 and month != 1:
        # check if month has 5 weeks if so remove 1 to choose week number 4
        week_num = week_num if len(df.week.values) < 5 else week_num - 1
    try:
        dt = df[(df.week == week_num) & (df.weekday == thursday)].date.values[0]
    except IndexError:
        dt = df[(df.week == week_num - 1) & (df.weekday == thursday)].date.values[0]
    finally:
        result = pd.Timestamp(dt)
        return datetime.date(year=result.year, month=result.month, day=result.day)


if __name__ == '__main__':
    print(meetup_date(2018, 1, nth=1, weekday=Weekday.MONDAY))
    print(meetup_date(2018, 1, nth=-1, weekday=2))
