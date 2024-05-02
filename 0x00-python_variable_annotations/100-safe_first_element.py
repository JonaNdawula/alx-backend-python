#!/usr/bin/env python3


"""
This module shows Duck type annotated code
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns lst
    """
    if lst:
        return lst[0]
    else:
        return None
