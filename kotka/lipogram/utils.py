from typing import List
from hgtk.letter import compose, decompose
from .typing import Char, CharRecipe
from ..hangul import is_complete_hangul


def has_phoneme(recipe: CharRecipe, target_phoneme: Char) -> bool:
    return target_phoneme in recipe if isinstance(recipe, tuple) else recipe == target_phoneme


def replace_phoneme(recipe: CharRecipe, old_phoneme: str, new_phoneme: str) -> str:
    if isinstance(recipe, tuple):
        return tuple([new_phoneme if phoneme == old_phoneme else phoneme for phoneme in recipe])
    return new_phoneme if recipe == old_phoneme else old_phoneme


def split_by_phoneme(text: str) -> List[CharRecipe]:
    return [decompose(char) if is_complete_hangul(char) else char for char in text]


def join_phonemes(phonemes: List[CharRecipe]) -> List[Char]:
    return [compose(*recipe) if isinstance(recipe, tuple) else recipe for recipe in phonemes]


def join_chars(chars: List[Char]) -> str:
    return ''.join(chars)
