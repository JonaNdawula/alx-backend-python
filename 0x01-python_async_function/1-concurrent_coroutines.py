#!/usr/bin/env python3


"""
This module executes
multiple coroutines at the same time
with aync
"""

import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This is an asynchronous coroutine that spawns
    wait_random n times

    parameters:
    n (int): The number of times to spawn wait_random
    max_delay (int): The maximum delay for wait_random

    Returns:
    List[Float]: The list of all the delays in ascending order
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for future in asyncio.as_completed(tasks):
        delay = await future
        delays.append(delay)
    return delays
