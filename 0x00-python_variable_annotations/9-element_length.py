#!/usr/bin/env python3


"""
This module returns values
with appropriate types
"""


from typing import List, Tuple, Iterable, Sequence


def element_length(lst:Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Retuns values with appropriate types
    """
    return ([(i, len(i)) for i in lst])
