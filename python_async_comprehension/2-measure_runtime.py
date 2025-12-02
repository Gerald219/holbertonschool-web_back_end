#!/usr/bin/env python3
"""Measure how long four async comprehensions take to run together."""

import asyncio
import time
from typing import List

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Run async_comprehension four times in parallel
    and return the total runtime in seconds.
    """
    start = time.time()
    tasks: List = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end = time.time()
    return end - start
