#!/usr/bin/env python3
"""Module that defines a typed multiplier maker."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given number."""
    def inner(value: float) -> float:
        """Multiply a float by the outer number."""
        return value * multiplier

    return inner
