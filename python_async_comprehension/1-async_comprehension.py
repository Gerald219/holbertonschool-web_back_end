#!/usr/bin/env python3
"""Module that defines an async comprehension over async_generator."""

from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Collect ten random numbers from async_generator into a list."""
    return [value async for value in async_generator()]
