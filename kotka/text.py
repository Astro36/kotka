from .rule import BaseRule, PhonemeReplaceRule, CharacterReplaceRule, filter_rule
from .utils import split_by_phoneme, join_phonemes, join_chars


class Obfuscator:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule: BaseRule):
        self.rules.append(rule)

    def run(self, text: str) -> str:
        phoneme_rules = filter_rule(self.rules, PhonemeReplaceRule)
        character_rules = filter_rule(self.rules, CharacterReplaceRule)

        phonemes = split_by_phoneme(text)
        for rule in phoneme_rules:
            for index, recipe in enumerate(phonemes):
                phonemes[index] = rule.apply(recipe, phonemes, index)

        chars = join_phonemes(phonemes)
        for rule in character_rules:
            for index, char in enumerate(chars):
                chars[index] = rule.apply(char, chars, index)

        text = join_chars(chars)
        return text
