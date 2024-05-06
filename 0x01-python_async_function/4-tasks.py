#!/usr/bin/env python3


"""
This module contains code for task_wait_n
"""


import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine

    parameters:
    n (int) number of times to produce task_wait_random
    max_delay (int): Maximum delay for task_wait_random

    Returns:
    List[float]: List of ll delays in ascending order
    """
    task_wait_random = __import__('3-tasks').task_wait_random

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for future in asyncio.as_completed(tasks):
        delay = await future
        delays.append(delay)
    return delays
