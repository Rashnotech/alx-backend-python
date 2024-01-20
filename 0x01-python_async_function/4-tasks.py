#!/usr/bin/env python3
"""a module that """
import asyncio
import time
import random
from typing import List


async def task_wait_random(max_delay: int = 10) -> float:
    """
    A function that implements asynchronous coroutine
    Args:
        max_delay: params for waiting time
    Returns:
        a floating point value
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    A function that list delays in asc order without using
    sort.
    Args:
        n: an integer value for the n times spawn
        max_delay: an integer value for delay
    Returns:
        a List of delays in asc order without sort
    """
    delays = await asyncio.gather(*(task_wait_random(max_delay)
                                    for _ in range(n)))
    return sorted(delays)
