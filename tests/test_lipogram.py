from kotka.lipogram import replace_phoneme
from kotka.lipogram.rules import SquareDog, CircleDog, UShapedDog, SeaoCat


def test_square_dog():
    input = '당신은 네모네모 멍뭉이와 눈이 마주치고 말았습니다.'
    rules = [SquareDog()]
    output = replace_phoneme(input, rules)
    assert output == '담신믄 네모네모 멈뭄미뫄 눈미 마주치고 말맜습니다.'


def test_circle_dog():
    input = '하지만 이제부터 당신은 동글동글 멍멍이와 눈이 마주치고 말았습니다!'
    rules = [CircleDog()]
    output = replace_phoneme(input, rules)
    assert output == '하지안 이제부터 당신은 동글동글 엉엉이와 눈이 아주치고 알았습니다!'


def test_u_shaped_dog():
    input = '하지만 당신은 멍뭉이 2형제와 눈이 마주쳤습니다!'
    rules = [UShapedDog()]
    output = replace_phoneme(input, rules)
    assert output == '하지반 답신븐 법붑비 2협제봐 눈비 바주쳤습니다!'


def test_seao_cat():
    input = '안녕하세요 고양이예요 겨울 추워요 문 열어주세요'
    rules = [SeaoCat()]
    output = replace_phoneme(input, rules)
    assert output == '안녕하새오 고양이애오 겨울 추어오 문 열어주새오'
