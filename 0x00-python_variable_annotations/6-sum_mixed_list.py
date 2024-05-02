#!/usr/bin/env python3


"""
This is a module which takes a list of
integers and floats and returns the
sum as a float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function returns the float sum of
    a mixed list
    """
    return (sum(mxd_lst))
