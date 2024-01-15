#!/usr/bin/env python3
"""a module that implements async routine"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    A function that list delays in asc order without using
    sort.
    Args:
        n: an integer value for the n times spawn
        max_delay: an integer value for delay
    Returns:
        a List of delays in asc order without sort
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
