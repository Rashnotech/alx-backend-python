#!/usr/bin/env python3
""" a module that wait task random"""
import asyncio
import time
from typing import TypeVar



wait_random = __import__('0-basic_async_syntax').wait_random


T = TypeVar('T')
def task_wait_random(max_delay: int) -> T:
    """
    a Function that takes a maximum delay time 
    Args:
        max_delay: an integer value
    Returns:
        asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
