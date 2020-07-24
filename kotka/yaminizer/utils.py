from functools import cmp_to_key
from typing import List
from hgtk.const import JONG
from hgtk.letter import compose, decompose


def compare_priority(a: str, b: str) -> int:
    if len(a[0]) != len(b[0]):
        return 1 if len(a[0]) < len(b[0]) else -1
    return -1 if a[0] < b[0] else 1


def create_batchim_characters(char: str) -> List[str]:
    recipe = decompose(char)
    characters = [compose(recipe[0], recipe[1], jong) for jong in JONG[1:]]
    return characters


def sort_dictionary_by_key(dictionary: dict) -> dict:
    return dict(sorted(dictionary.items(), key=cmp_to_key(compare_priority)))
