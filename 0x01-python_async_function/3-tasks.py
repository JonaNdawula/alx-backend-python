#!/usr/bin/env python3


"""
This module contains task_wait_random
which returns an asyncio.Task
"""

import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes an integer max_delay and
    returns asyncio.Task

    parameters:
    max_delay (int): Maximum delay for wait_random

    Returns:
    asyncio.Task: The Task object
    """
    wait_random = __import__('0-basic_async_syntax').wait_random
    task = asyncio.create_task(wait_random(max_delay))
    return task
