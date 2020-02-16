#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 15.02.20
@author: felix
"""
from dataclasses import dataclass


@dataclass
class RomanNumeral:
    roman_num: str

    @classmethod
    def from_int(cls, number: int):
        roman_letters = ''
        for num, roman_letter in sorted(RomanNumeral.__number_roman_dict().items(), reverse=True):
            while number >= num:
                number -= num
                roman_letters += roman_letter
        return roman_letters

    def __int__(self):
        main_roman_nr = RomanNumeral.__roman_letters_dict()
        result = 0
        last_digit = 0
        for num in (main_roman_nr.get(char, 0) for char in self.roman_num):
            if last_digit < num:
                result -= last_digit
                result += (num - last_digit)
            else:
                result += num
            last_digit = num
        return result

    def __str__(self):
        return self.roman_num

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.roman_num}')"

    def __gt__(self, other):
        return self.__is__(other, '__gt__', False)

    def __lt__(self, other):
        return not self > other

    def __ge__(self, other):
        return self.__is__(other, '__ge__', False)

    def __le__(self, other):
        return self.__is__(other, '__le__', False)

    def __eq__(self, other):
        return self.__is__(other, '__eq__')

    def __is__(self, other, operation: any, allow_str: bool = True):
        if isinstance(other, RomanNumeral):
            is_equal = getattr(int(self), operation)(int(other))
        elif isinstance(other, int):
            is_equal = getattr(int(self), operation)(other)
        else:
            if not allow_str:
                raise TypeError
            is_equal = getattr(self.roman_num, operation)(other)
        return is_equal

    def __add__(self, other):
        return RomanNumeral(RomanNumeral.from_int(int(self) + int(other)))

    @staticmethod
    def __roman_letters_dict():
        return {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }

    @staticmethod
    def __number_roman_dict():
        return {v: k for k, v in RomanNumeral.__roman_letters_dict().items()}
