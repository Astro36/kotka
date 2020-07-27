from typing import List, Tuple, Union
from hgtk.const import JONG
from hgtk.letter import compose, decompose

CharRecipe = Union[Tuple[str, str, str], str]


def has_phoneme(recipe: CharRecipe, target_phoneme: str) -> bool:
    return target_phoneme in recipe if isinstance(recipe, tuple) else recipe == target_phoneme


def replace_phoneme(recipe: CharRecipe, old_phoneme: str, new_phoneme: str) -> CharRecipe:
    if isinstance(recipe, tuple):
        return tuple([new_phoneme if phoneme == old_phoneme else phoneme for phoneme in recipe])
    return new_phoneme if recipe == old_phoneme else old_phoneme


def split_by_phoneme(text: str) -> List[CharRecipe]:
    return [decompose(char) if is_complete_syllable(char) else char for char in text]


def join_phonemes(phonemes: List[CharRecipe]) -> List[str]:
    return [compose(*recipe) if isinstance(recipe, tuple) else recipe for recipe in phonemes]


def create_possible_syllables(char: str) -> List[str]:
    recipe = decompose(char)
    characters = [compose(recipe[0], recipe[1], jong) for jong in JONG[1:]]
    return characters


def is_complete_syllable(char: str) -> bool:
    FRIST_HANGUL_UNICODE = 0xAC00
    LAST_HANGUL_UNICODE = 0xD7A3
    return len(char) == 1 and FRIST_HANGUL_UNICODE <= ord(char) <= LAST_HANGUL_UNICODE


def join_syllables(chars: List[str]) -> str:
    return ''.join(chars)
