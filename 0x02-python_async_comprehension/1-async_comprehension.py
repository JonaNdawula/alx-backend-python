#!/usr/bin/env python3


"""
Module has the corutine async_comprehension
that collects random numbers from async_generator
"""


import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an
    async comprehensing over async_generator

    Returns:
    List[float]: A List of random numbers
    """
    async_generator = __import__('0-async_generator').async_generator
    return [i async for i in async_generator()]
