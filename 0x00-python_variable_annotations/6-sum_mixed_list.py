#!/usr/bin/env python3
"""a module that sum element in list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
     a function that sum element in a list
     returns:
        a floating point value
    """
    val = 0
    for num in mxd_lst:
        val += num
    return val
