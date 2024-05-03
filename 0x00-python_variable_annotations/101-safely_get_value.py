#!/usr/bin/env python3
"""Duck typing"""
from typing import Any, Sequence, Union, Optional, Mapping, TypeVar
T = TypeVar('T')

# The types of the elements of the input are not know


def safely_get_value(dct: Mapping,
                     key: Any,
                     default:
                     Optional[Union[T, None]] = None) -> Union[Any, T]:
    """First element of a sequence"""
    if key in dct:
        return dct[key]
    else:
        return default
