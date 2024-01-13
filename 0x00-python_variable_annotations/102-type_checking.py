#!/usr/bin/env python3
"""a sample code to fix"""
from typing import List, Tuple, Any


def zoom_array(lst: list, factor: Any = 2) -> list:
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
