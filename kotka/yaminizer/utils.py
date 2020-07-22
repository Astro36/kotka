from functools import cmp_to_key
from typing import List
from hgtk.const import JONG
from hgtk.letter import compose, decompose


def compare_priority(a: str, b: str) -> int:
    if len(a[0]) != len(b[0]):
        return 1 if len(a[0]) < len(b[0]) else -1
    elif a[0] != b[0]:
        return -1 if a[0] < b[0] else 1
    return 0


def create_batchim_characters(char: str) -> List[str]:
    recipe = decompose(char)
    characters = [compose(recipe[0], recipe[1], jong) for jong in JONG[1:]]
    return characters


def is_complete_hangul_character(char: str) -> str:
    FRIST_HANGUL_UNICODE = 0xAC00
    LAST_HANGUL_UNICODE = 0xD7A3
    return len(char) == 1 and FRIST_HANGUL_UNICODE <= ord(char) <= LAST_HANGUL_UNICODE


def sort_dictionary_by_key(dictionary: dict) -> dict:
    return dict(sorted(dictionary.items(), key=cmp_to_key(compare_priority)))
