#!/usr/bin/env python3
""" a module that implements asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
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
