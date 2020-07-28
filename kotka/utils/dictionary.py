from collections import OrderedDict
from functools import cmp_to_key
from typing import Callable, Dict, Tuple


def sort_by_key(dictionary: Dict[str, str], cmp: Callable[[Tuple[str, str], Tuple[str, str]], int]) -> Dict[str, str]:
    return OrderedDict(sorted(dictionary.items(), key=cmp_to_key(cmp)))
