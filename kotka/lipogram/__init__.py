from .rules import PhonemeReplaceRule
from .utils import split_by_phoneme, join_phonemes, join_chars


def replace_phoneme(text: str, rules: PhonemeReplaceRule) -> str:
    phonemes = split_by_phoneme(text)
    for rule in rules:
        for index, recipe in enumerate(phonemes):
            phonemes[index] = rule.apply(recipe, phonemes, index)

    chars = join_phonemes(phonemes)
    text = join_chars(chars)
    return text
