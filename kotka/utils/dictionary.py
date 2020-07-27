from functools import cmp_to_key
from typing import Callable, Dict, OrderedDict, Tuple


def sort_by_key(dictionary: Dict[str, str], cmp: Callable[[Tuple[str, str], Tuple[str, str]], int]) -> OrderedDict[str, str]:
    return OrderedDict(sorted(dictionary.items(), key=cmp_to_key(cmp)))
