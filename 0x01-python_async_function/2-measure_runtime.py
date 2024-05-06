#!/usr/bin/env python3


"""
This module vontains the function measure_time which
measures the total execution time  for wait_n
"""


import asyncio
import time
from typing import Callable


def measure_time(n: int, max_delay: int) -> float:
    """
    This function measures the total execution time for  wait_n
    and returns total_time / n

    parameters:
    n (int): number of times to run wait_n
    max_delay (int): maximum delay for wait_n

    Returns: Average time for each call to wait_n
    """
    wait_n = __import__('1-concurrent_coroutines').wait_n
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
