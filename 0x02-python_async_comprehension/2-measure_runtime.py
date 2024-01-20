#!/usr/bin/env python3
"""a module that measure run time"""
import asyncio
from typing import Generator
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A function that measure run time in async comprehension
    """
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.time()
    return end_time - start_time
