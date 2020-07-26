from kotka.lipogram import replace_phoneme
from kotka.lipogram.rules import SquareDog, CircleDog, UShapedDog, SeaoCat


def test_replace_phoneme_square_dog_0():
    input = '당신은 네모네모 멍뭉이와 눈이 마주치고 말았습니다.'
    output = replace_phoneme(input, rule=SquareDog())
    assert output == '담신믄 네모네모 멈뭄미뫄 눈미 마주치고 말맜습니다.'


def test_replace_phoneme_square_dog_1():
    input = '그치만... 이런 행동이 아니면... 오니쨩... 내게 관심도 없는 걸!'
    output = replace_phoneme(input, rule=SquareDog())
    assert output == '그치만... 미런 햄돔미 마니면... 모니쨤... 내게 관심도 멊는 걸!'


def test_replace_phoneme_circle_dog_0():
    input = '하지만 이제부터 당신은 동글동글 멍멍이와 눈이 마주치고 말았습니다!'
    output = replace_phoneme(input, rule=CircleDog())
    assert output == '하지안 이제부터 당신은 동글동글 엉엉이와 눈이 아주치고 알았습니다!'


def test_replace_phoneme_circle_dog_1():
    input = '사람이 언제 죽는다고 생각하나? 사람들에게서 잊혀졌을 때다!!! 내가 사라져도 내 꿈은 이루어진다.'
    output = replace_phoneme(input, rule=CircleDog())
    assert output == '사랑이 언제 죽는다고 생각하나? 사랑들에게서 잊혀졌을 때다!!! 내가 사라져도 내 꿍은 이루어진다.'


def test_replace_phoneme_u_shaped_dog_0():
    input = '하지만 당신은 멍뭉이 2형제와 눈이 마주쳤습니다!'
    output = replace_phoneme(input, rule=UShapedDog())
    assert output == '하지반 답신븐 법붑비 2협제봐 눈비 바주쳤습니다!'


def test_replace_phoneme_u_shaped_dog_1():
    input = '"ㅁㄴ암ㄴㅇ모앱자" 판사님 이 글은 저희집 고양이가 썼습니다'
    output = replace_phoneme(input, rule=UShapedDog())
    assert output == '"ㅇㄴ밥ㄴㅇ보뱁자" 판사닙 비 글븐 저희집 고뱝비가 썼습니다'


def test_replace_phoneme_seao_cat_0():
    input = '안녕하세요 고양이예요 겨울 추워요 문 열어주세요'
    output = replace_phoneme(input, rule=SeaoCat())
    assert output == '안녕하새오 고양이애오 겨울 추어오 문 열어주새오'


def test_replace_phoneme_seao_cat_1():
    input = '너 때문에 흥이 다 깨져버렸으니까 책임져'
    output = replace_phoneme(input, rule=SeaoCat())
    assert output == '너 때문애 흥이 다 깨져버렸으니까 책임져'
