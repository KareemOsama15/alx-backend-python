#!/usr/bin/env python3
"""Complex types - sum list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats"""
    sum: float = 0.0
    for num in input_list:
        sum += num
    return sum
