#!/usr/bin/env python3
"""Module that defines a typed helper to read from a mapping."""

from typing import Mapping, TypeVar, Any, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """Return value from mapping if key exists, else default."""
    if key in dct:
        return dct[key]
    return default
