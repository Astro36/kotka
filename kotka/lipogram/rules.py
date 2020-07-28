from typing import List
from ..utils.hangul import CharRecipe, has_phoneme, replace_phoneme


class PhonemeReplaceRule:
    def apply(self, recipe: CharRecipe, recipes: List[CharRecipe], index: int) -> CharRecipe:
        raise NotImplementedError


class SquareDog(PhonemeReplaceRule):
    """
    담신믄 네모네모 멈뭄미뫄 눈미 마주치고 말맜습니다.
    담신믄 미제 네모네모 멈뭄미믜 저주로 돔그란 글자를 칠 수 멊습니다. 멈멈!
    """

    def apply(self, recipe: CharRecipe, recipes: List[CharRecipe], index: int) -> CharRecipe:
        return replace_phoneme(recipe, 'ㅇ', 'ㅁ') if has_phoneme(recipe, 'ㅇ') else recipe


class CircleDog(PhonemeReplaceRule):
    """
    짠! 당신의 저주는 풀렸습니다!
    하지안 이제부터 당신은 동글동글 엉엉이와 눈이 아주치고 알았습니다!
    당신은 이제 동글동글 엉엉이의 저주로 네오난 글자를 칠 수 없습니다. 엉엉!
    """

    def apply(self, recipe: CharRecipe, recipes: List[CharRecipe], index: int) -> CharRecipe:
        return replace_phoneme(recipe, 'ㅁ', 'ㅇ') if has_phoneme(recipe, 'ㅁ') else recipe


class UShapedDog(PhonemeReplaceRule):
    """
    빠밤! 당신의 저주는 풀렸습니다!
    하지반 답신븐 법붑비 2협제봐 눈비 바주쳤습니다!
    답신븐 비제 법붑비 2협제븨 저주로 네보난 글자봐 돕그란 글자를 칠 수 벖습니다. 법법!
    """

    def apply(self, recipe: CharRecipe, recipes: List[CharRecipe], index: int) -> CharRecipe:
        return replace_phoneme(replace_phoneme(recipe, 'ㅁ', 'ㅂ'), 'ㅇ', 'ㅂ') \
            if has_phoneme(recipe, 'ㅁ') or has_phoneme(recipe, 'ㅇ') else recipe
