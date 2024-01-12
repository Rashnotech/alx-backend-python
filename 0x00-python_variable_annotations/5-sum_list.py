#!/usr/bin/env python3
"""a module that sum_list from input"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    a function that sum element of a list
    params:
        input_list: contains all elements in the list
    returns: a floating number
    """
    val = 0
    for num in input_list:
        val += num
    return val
