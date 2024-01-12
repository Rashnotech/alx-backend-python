#!/usr/bin/env python3
""" a module that takes a string and returns tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    a function that takes a string
    params:
        k: a string character
        v: a union type of int | float
    returns:
        a tuples is returned
    """
    return (k, v**2)
