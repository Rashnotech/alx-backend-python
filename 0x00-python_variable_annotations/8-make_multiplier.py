#!/usr/bin/env python3
""" a module that takes float and return float"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    a function that takes a float
    params:
        multiplier: a floating point number
    Return:
        callable object
    """
    def inc(num: float) -> float:
        return multiplier * num
    return inc
