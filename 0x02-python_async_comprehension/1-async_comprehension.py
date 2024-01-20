#!/usr/bin/env python3
""" a module that use comprehensions """
import asyncio
import random
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A function that collect 10 random number
    Return:
        a list comprehension
    """
    random_numbers = [i async for i in async_generator()]
    return random_numbers
