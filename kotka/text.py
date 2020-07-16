from .strategy import CharacterStrategy
from .utils import from_chars, to_chars


class Obfuscator:
    def __init__(self):
        self.strategies = []

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    def run(self, text):
        for strategy in self.strategies:
            if issubclass(strategy.__class__, CharacterStrategy):
                chars = to_chars(text)
                for index, char in enumerate(chars):
                    if strategy.is_match(char, chars, index):
                        print('match', char)
                        chars[index] = strategy.apply(char, chars, index)
                text = from_chars(chars)
        return text
