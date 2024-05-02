#!/usr/bin/env/ python3


"""
This module takes a float
multiplier as an arg and returns a
function that multiplies a float
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function returns another
    function that multiplies floats
    """
    return lambda x: x * multiplier
