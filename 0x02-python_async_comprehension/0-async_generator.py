#!/usr/bin/env python3
"""a module that implements an async generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    A function that loops with an asynchronously wait and yield an integer
    Return:
        random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
