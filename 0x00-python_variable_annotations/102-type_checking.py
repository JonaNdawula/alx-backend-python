#!/usr/bin/env python3


"""
This module is type checking
"""


from typing import Tuple, List, TypeVar


T = TypeVar('T')


def zoom_array(lst: Tuple[T, ...], factor: int = 2) -> List[T]:
    """
    Returns zoomed_in
    """
    zoomed_in: List[T] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
