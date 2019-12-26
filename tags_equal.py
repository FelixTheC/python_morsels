#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 17.12.19
@author: felix
"""
import re


def remove_signs(tag):
    pattern = r'[<>\"\']'
    return re.sub(pattern, '', tag)


def tag_parameter(tag):
    pattern = r"[a-z^]+[=\"'].+[$\"']"
    try:
        tag_str = re.findall(pattern, tag)[0]
    except IndexError:
        return tag
    else:
        if '"' in tag_str:
            pattern = r'(\")+'
        else:
            pattern = r"(\')+"
        return re.sub(pattern, '', tag_str)


def tag_dict(tag_str: str) -> dict:
    tag = tag_parameter(tag_str)
    pattern = r'[.a-zA-Z0-9=]+'
    tags_list = re.findall(pattern, tag)
    tag_val = ''
    for i in tags_list:
        if '=' in i:
            tag_val += ' '
            tag_val += i
        else:
            if i.lower() not in ['input', 'checked']:
                tag_val += f'#{i}'
            else:
                tag_val += f' {i}'
    tag_val = re.sub(r'^#', '', tag_val)
    tags = {}
    for i in tag_val.strip().split():
        if '=' in i:
            t = i.split('=')
            if t[0].lower() not in tags:
                tags[t[0].lower()] = t[1].strip()
        else:
            tags[i.lower()] = i.strip()
    return {k: v.replace('#', ' ').lower() for k, v in tags.items()}


def tags_equal(origin: str, other: str) -> bool:
    origin_t = tag_dict(origin)
    other_t = tag_dict(other)
    for k, v in origin_t.items():
        try:
            other_val = other_t[k]
        except KeyError:
            return False
        else:
            if v.lower().strip() != other_val.lower().strip():
                return False
    return True
