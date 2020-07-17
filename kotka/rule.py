from typing import List
from .typing import Char, CharRecipe
from .utils import has_phoneme, replace_phoneme


class BaseRule:
    pass


class PhonemeReplaceRule(BaseRule):
    def apply(self, recipe: CharRecipe, recipes: List[CharRecipe], index: int) -> CharRecipe:
        pass

    def is_match(self, recipe: CharRecipe, recipes: List[CharRecipe], index: int) -> bool:
        pass


class CharacterReplaceRule(BaseRule):
    def apply(self, char: Char, chars: List[Char], index: int) -> Char:
        pass

    def is_match(self, char: Char, chars: List[Char], index: int) -> bool:
        pass


class BeSquareDog(PhonemeReplaceRule):
    """
    담신믄 네모네모 멈뭄미뫄 눈미 마주치고 말맜습니다.
    담신믄 미제 네모네모 멈뭄미믜 저주로 돔그란 글자를 칠 수 멊습니다. 멈멈!
    """

    def apply(self, recipe: CharRecipe, recipes: List[CharRecipe], index: int) -> CharRecipe:
        return replace_phoneme(recipe, 'ㅇ', 'ㅁ')

    def is_match(self, recipe: CharRecipe, recipes: List[CharRecipe], index: int) -> bool:
        return has_phoneme(recipe, 'ㅇ')


def filter_rule(rules: List[BaseRule], rule_type: type) -> List[BaseRule]:
    return [rule for rule in rules if issubclass(rule.__class__, rule_type)]
