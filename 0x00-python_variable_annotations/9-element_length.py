#!/usr/bin/env python3
""" a module that takes in list and return value"""
from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    a function that take in parameters
    returns a tuple List
    """
    return [(i, len(i)) for i in lst]
