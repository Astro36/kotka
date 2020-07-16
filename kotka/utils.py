from typing import List
from hgtk.checker import is_hangul
from hgtk.letter import compose, decompose


def from_chars(chars: List[str]) -> str:
    return ''.join(chars)


def to_chars(text: str) -> List[str]:
    return list(text)


def has_phoneme(char: str, phoneme: str) -> bool:
    return is_hangul(char) \
        and phoneme in decompose(char)


def replace_phoneme(char: str, old_phoneme: str, new_phoneme: str) -> str:
    phonemes = [new_phoneme if phoneme == old_phoneme else phoneme
                for phoneme in decompose(char)]
    return compose(*phonemes)
