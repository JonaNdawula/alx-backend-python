#!/usr/bin/env python3


"""
Module contains the corutine measure_runtime that
that measures the total runtime of async_comprehension
"""


import asyncio
import time


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times
    in parallel using asyncio.gather
    which  measures the total runtime

    Returns:
    float: Total runtime
    """
    async_comp = __import__('1-async_comprehension').async_comprehension
    st_time = time.time()
    await asyncio.gather(*(async_comp() for _ in range(4)))
    en_time = time.time()
    return en_time - st_time
