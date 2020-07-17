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


class SquareDog(PhonemeReplaceRule):
    """
    담신믄 네모네모 멈뭄미뫄 눈미 마주치고 말맜습니다.
    담신믄 미제 네모네모 멈뭄미믜 저주로 돔그란 글자를 칠 수 멊습니다. 멈멈!
    """

    def apply(self, recipe: CharRecipe, recipes: List[CharRecipe], index: int) -> CharRecipe:
        return replace_phoneme(recipe, 'ㅇ', 'ㅁ')

    def is_match(self, recipe: CharRecipe, recipes: List[CharRecipe], index: int) -> bool:
        return has_phoneme(recipe, 'ㅇ')


class CircleDog(PhonemeReplaceRule):
    """
    짠! 당신의 저주는 풀렸습니다!
    하지안 이제부터 당신은 동글동글 엉엉이와 눈이 아주치고 알았습니다!
    당신은 이제 동글동글 엉엉이의 저주로 네오난 글자를 칠 수 없습니다. 엉엉!
    """

    def apply(self, recipe: CharRecipe, recipes: List[CharRecipe], index: int) -> CharRecipe:
        return replace_phoneme(recipe, 'ㅁ', 'ㅇ')

    def is_match(self, recipe: CharRecipe, recipes: List[CharRecipe], index: int) -> bool:
        return has_phoneme(recipe, 'ㅁ')


class UShapedDog(PhonemeReplaceRule):
    """
    빠밤! 당신의 저주는 풀렸습니다!
    하지반 답신븐 법붑비 2협제봐 눈비 바주쳤습니다!
    답신븐 비제 법붑비 2협제븨 저주로 네보난 글자봐 돕그란 글자를 칠 수 벖습니다. 법법!
    """

    def apply(self, recipe: CharRecipe, recipes: List[CharRecipe], index: int) -> CharRecipe:
        return replace_phoneme(replace_phoneme(recipe, 'ㅁ', 'ㅂ'), 'ㅇ', 'ㅂ')

    def is_match(self, recipe: CharRecipe, recipes: List[CharRecipe], index: int) -> bool:
        return has_phoneme(recipe, 'ㅁ') or has_phoneme(recipe, 'ㅇ')


class SeaoCat(PhonemeReplaceRule):
    """
    안녕하새오 고양이애오 겨울 추어오 문 열어주새오
    가족 대려오개 감사해오 문 열어주새오
    """

    def apply(self, recipe: CharRecipe, recipes: List[CharRecipe], index: int) -> CharRecipe:
        recipe = replace_phoneme(recipe, 'ㅔ', 'ㅐ')
        recipe = replace_phoneme(recipe, 'ㅖ', 'ㅐ')
        recipe = replace_phoneme(recipe, 'ㅒ', 'ㅐ')
        recipe = replace_phoneme(recipe, 'ㅝ', 'ㅓ')
        recipe = replace_phoneme(recipe, 'ㅞ', 'ㅓ')
        recipe = replace_phoneme(recipe, 'ㅛ', 'ㅗ')
        return recipe

    def is_match(self, recipe: CharRecipe, recipes: List[CharRecipe], index: int) -> bool:
        return has_phoneme(recipe, 'ㅔ') or has_phoneme(recipe, 'ㅖ') or has_phoneme(recipe, 'ㅒ') \
            or has_phoneme(recipe, 'ㅝ') or has_phoneme(recipe, 'ㅞ') or has_phoneme(recipe, 'ㅛ')


def filter_rule(rules: List[BaseRule], rule_type: type) -> List[BaseRule]:
    return [rule for rule in rules if issubclass(rule.__class__, rule_type)]
