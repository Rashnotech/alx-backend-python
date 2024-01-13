#!/usr/bin/env python3
""" a module for safe first """
from typing import List, Tuple, Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    The types of the elements of the input are not know
    """
    if lst:
        return lst[0]
    else:
        return None
