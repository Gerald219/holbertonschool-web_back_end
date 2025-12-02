#!/usr/bin/env python3
"""Module that defines a zoom helper checked by static typing."""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a list where each item of the tuple is repeated factor times."""
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
