#!/usr/bin/env python3


"""
This modules  has an
asynchronous coroutine
that takes in an integer argument
and returns that waits for a random delay between 0 and max_delay (
included and float value) seconds and eventually returns it.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function generates a random number
    and returns a random delay

    Parameters:
    max_delay: The actual delay. Default 10

    Returns:
    float: The actual delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
