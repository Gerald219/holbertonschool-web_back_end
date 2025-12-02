#!/usr/bin/env python3
"""Module that defines a typed helper to sum mixed numeric values."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of ints and floats as a float."""
    return sum(mxd_lst)
