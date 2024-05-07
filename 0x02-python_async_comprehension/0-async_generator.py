#!/usr/bin/env python3


"""
This module contains a corutine
async_generator taking no arguments
that asynchronously yielsd random numbers
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    corutine which loops 10 times
    each time asynchronously

    Yield:
    float: Random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
