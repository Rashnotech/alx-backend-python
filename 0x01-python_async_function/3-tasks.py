#!/usr/bin/env python3
""" a module that wait task random"""
from asyncio import Task
import asyncio
import time


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    A Function that takes a maximum delay time
    Args:
        max_delay: an integer value
    Returns:
        asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
