#!/usr/bash/env python3

import asyncio
import random


"""
This modules  has an
asynchronous coroutine
that takes in an integer argument
and returns that waits for a random delay between 0 and max_delay (
included and float value) seconds and eventually returns it.
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    This function returns a random delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
