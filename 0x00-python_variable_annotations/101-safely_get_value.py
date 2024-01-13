#!/usr/bin/env python3
""" a module parameters """
from typing import Mapping, Union, Any, TypeVar, Generic


T = TypeVar('T')
def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    a function that take a dct
    """
    if key in dct:
        return dct[key]
    else:
        return default
