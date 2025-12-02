#!/usr/bin/env python3
"""Module that defines a typed helper for element and length pairs."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return list of tuples with each element and its length."""
    return [(item, len(item)) for item in lst]
