#!/usr/bin/env python3


"""
This module takes a string
and an int or floatas args and returns
a tuple
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function returns a tuple
    """
    return(k, v**2)
