#!/usr/bin/env python3
"""Complex types - make_multiplier"""
from typing import Tuple, Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns function that multiplies a float by multiplier"""
    def func(x: float) -> float:
        return x * multiplier
    return func
