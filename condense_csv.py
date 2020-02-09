#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 25.01.20
@author: felix
"""
from textwrap import dedent
from typing import Optional


def condense_csv(text: str, id_name: Optional[str] = None):
    col_name = id_name if id_name is not None else 'NN'
    col_names = [col_name, ]
    objs = {}
    start = 0 if id_name is not None else 1
    for line in text.split('\n')[start:]:
        num, col, *data = line.split(',')
        col = col.replace('"', '')
        data = ','.join(data)
        if ',' not in data:
            data = data.replace('"', '')
        if col not in col_names:
            col_names.append(col)
        if num not in objs:
            objs[num] = {col: data}
        else:
            objs[num][col] = data

    resp_text = ','.join(col_names)
    resp_text += '\n'
    for row in objs.keys():
        tmp_txt = [row, ]
        for col in col_names[1:]:
            if col in objs[row]:
                tmp_txt.append(objs[row][col])
            else:
                tmp_txt.append('')
        resp_text += ','.join(tmp_txt)
        resp_text += '\n'
    return resp_text


if __name__ == '__main__':
    text = dedent("""
            01,Artist,Otis Taylor
            01,Title,Ran So Hard the Sun Went Down
            01,Time,3:52
            02,Artist,Waylon Jennings
            02,Title,Honky Tonk Heroes (Like Me)
            02,"Time","3:29"
            03,Artist,David Allan Coe
            03,Title,"Willie, Waylon, And Me"
            03,Time,3:26
        """).strip()
    print(condense_csv(text, id_name='Track'))
