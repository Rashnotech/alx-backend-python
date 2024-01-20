#!/usr/bin/env python3
""" a module that wait task random"""
import asyncio
import time
from typing import Any


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """
    A Function that takes a maximum delay time
    Args:
        max_delay: an integer value
    Returns:
        asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
