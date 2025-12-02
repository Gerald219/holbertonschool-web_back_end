#!/usr/bin/env python3
"""Module that defines a typed safe first element helper."""

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Return the first element of a sequence or None if it is empty."""
    if lst:
        return lst[0]
    return None
