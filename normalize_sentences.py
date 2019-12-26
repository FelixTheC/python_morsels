#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 18.12.19
@author: felix
"""
import re


def _normalize(sentence: str) -> str:
    try:
        sentence[-1]
    except IndexError:
        return sentence
    else:
        s = sentence[:-1]
        # s = re.sub(r'[  ]{2}', ' ', s)
        s = re.sub(r'(\. )', '.  ', s)
        s = re.sub(r'[?]', '? ', s)
        s = re.sub(r'[!]', '! ', s)
        s += sentence[-1]
        return s


def sentence_contains_break(sentence: str) -> bool:
    return len(sentence.strip().split('\n')) > 1


def normalize_sentences(sentence: str) -> str:
    s = '\n'.join([_normalize(s) for s in sentence.split('\n')])
    return s


if __name__ == '__main__':
    sentences = """
            Sentence 1.  And two spaces after. But one space after this.
        """
    print(normalize_sentences(sentences))
