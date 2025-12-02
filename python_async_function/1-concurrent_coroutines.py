#!/usr/bin/env python3
"""This module provides wait_n, a coroutine that runs several
wait_random calls at the same time and returns their delays
in ascending order.
"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times with max_delay and return sorted delays."""
    # create one task for each random delay call
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []
    # collect delays in the order tasks finish
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
