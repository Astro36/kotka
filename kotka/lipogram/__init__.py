from .rules import PhonemeReplaceRule
from ..utils.hangul import split_by_phoneme, join_phonemes, join_syllables


def replace_phoneme(text: str, *, rule: PhonemeReplaceRule) -> str:
    phonemes = split_by_phoneme(text)
    for index, recipe in enumerate(phonemes):
        phonemes[index] = rule.apply(recipe, phonemes, index)

    chars = join_phonemes(phonemes)
    text = join_syllables(chars)
    return text
