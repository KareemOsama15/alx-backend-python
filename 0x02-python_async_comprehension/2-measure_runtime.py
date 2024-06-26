#!/usr/bin/env python3
"""
module provides an asynchronous function
"""
import asyncio
import time
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronous function that measures and returns the runtime of
    running 4 instances of the async_comprehension function.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
