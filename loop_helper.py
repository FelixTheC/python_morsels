#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 04.11.20
@author: felix
"""
from collections import namedtuple
from queue import Queue
from typing import Iterable

EMPTY = object()


class LoopHelper:
    index: int = 0
    is_first: bool = True
    is_last: bool = False
    current = EMPTY
    previous = None
    next = EMPTY
    q: Queue = None

    def __init__(self, q: Queue, previous_default):
        self.q = q
        self.previous = previous_default
        self.l_helper = namedtuple('l_helper',
                                   ('index', 'is_first',
                                    'current', 'previous',
                                    'next', 'is_last')
                                   )

    def get_current(self):
        if self.current is EMPTY and self.next is EMPTY:
            self.current = self.q.queue.popleft()

    def get_next(self):
        try:
            self.next = self.q.queue.popleft()
        except IndexError:
            self.next = EMPTY

    def __iter__(self):
        return self

    def __next__(self):
        self.get_current()
        self.get_next()
        self.is_last = self.q.empty() and self.next is EMPTY

        yield self.current, self.l_helper(index=self.index,
                                          is_first=self.is_first,
                                          current=self.current,
                                          previous=self.previous,
                                          next=self.next if self.next is not EMPTY else None,
                                          is_last=self.is_last)
        self.index += 1
        self.is_first = False
        self.previous = self.current
        self.current = self.next


def loop_helper(iterable: Iterable, previous_default=None):
    q = Queue()
    lh = LoopHelper(q, previous_default)

    values = iter(iterable)
    try:
        q.put(next(values))
    except StopIteration:
        # check if we have an empty iterable
        # if so we return an empty list
        return []

    run_loop = True
    while run_loop:

        try:
            q.put(next(values))
        except StopIteration:
            # catching StopIteration to be able to yield
            # the last loop helper value
            run_loop = False

        obj = list(next(lh))[0]
        yield obj[0], obj[1]
