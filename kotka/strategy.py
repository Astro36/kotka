from typing import List
from .utils import has_phoneme, replace_phoneme


class BaseStrategy:
    pass


class CharacterStrategy(BaseStrategy):
    def apply(self, char: str, chars: List[str], index: int) -> str:
        pass

    def is_match(self, char: str, chars: List[str], index: int) -> bool:
        pass


class BeSquareDog(CharacterStrategy):
    """
    담신믄 네모네모 멈뭄미뫄 눈미 마주치고 말맜습니다.
    담신믄 미제 네모네모 멈뭄미믜 저주로 돔그란 글자를 칠 수 멊습니다. 멈멈!
    """

    def apply(self, char: str, chars: List[str], index: int) -> str:
        return replace_phoneme(char, 'ㅇ', 'ㅁ')

    def is_match(self, char: str, chars: List[str], index: int) -> bool:
        return has_phoneme(char, 'ㅇ')
