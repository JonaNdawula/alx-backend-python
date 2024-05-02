#!/usr/bin/env python3


"""
This module returns values
with appropriate types
"""


from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Retuns values with appropriate types
    """
    return ([(i, len(i)) for i in lst])
