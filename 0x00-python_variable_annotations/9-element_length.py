#!/usr/bin/env python3
"""Complex types - element_length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes Itarable and return its elements with len"""
    return [(i, len(i)) for i in lst]
