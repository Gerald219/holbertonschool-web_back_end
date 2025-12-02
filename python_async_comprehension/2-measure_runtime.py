#!/usr/bin/env python3
"""Module that measures time for running async comprehensions in parallel."""

import asyncio
import time


from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """Run four async comprehensions at once and return total time in seconds."""
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    end = time.time()
    return end - start
