from functools import cmp_to_key
from typing import Callable


def sort_by_key(dictionary: dict, cmp: Callable) -> dict:
    return dict(sorted(dictionary.items(), key=cmp_to_key(cmp)))
