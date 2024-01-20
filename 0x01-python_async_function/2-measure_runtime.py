#!/usr/bin/env python3
""" a module that create measure time"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    A function that measure total exection time for wait function
    Args:
        n: an integer value that show number of times
        max_delay: an integer value for delay time
    Returns:
        a float value that calculates the execution time
    """
    start_time = time.time()

    async def main():
        await wait_n(n, max_delay)
    
    asyncio.run(main())
    end_time = time.time()
    total_time = end_time - start_time
    avg_time = total_time / n
    return avg_time
