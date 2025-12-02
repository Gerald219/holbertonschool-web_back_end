#!/usr/bin/env python3
"""Collect random numbers from the async generator using a comprehension."""

from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Return a list with ten random floats from async_generator."""
    return [value async for value in async_generator()]
