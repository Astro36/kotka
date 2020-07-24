from kotka.shredder import shred_syllable


def test_shred_syllable_0():
    input = '개소리는 거짓말보다 더 큰 진리의 적이다.'
    output = shred_syllable(input, active_rate=1.0)
    assert output == 'ㄱㅐㅅㅗㄹㅣㄴㅡㄴ ㄱㅓㅈㅣㅅㅁㅏㄹㅂㅗㄷㅏ ㄷㅓ ㅋㅡㄴ ㅈㅣㄴㄹㅣㅇㅢ ㅈㅓㄱㅇㅣㄷㅏ.'


def test_shred_syllable_1():
    input = '개 짖는 소리 좀 안 나게 하라'
    output = shred_syllable(input, active_rate=1.0)
    assert output == 'ㄱㅐ ㅈㅣㅈㄴㅡㄴ ㅅㅗㄹㅣ ㅈㅗㅁ ㅇㅏㄴ ㄴㅏㄱㅔ ㅎㅏㄹㅏ'


def test_shred_syllable_2():
    input = '우리 개는 안 물어요'
    output = shred_syllable(input, active_rate=1.0)
    assert output == 'ㅇㅜㄹㅣ ㄱㅐㄴㅡㄴ ㅇㅏㄴ ㅁㅜㄹㅇㅓㅇㅛ'


def test_shred_syllable_3():
    input = '이 뭔 개소리야'
    output = shred_syllable(input, active_rate=1.0)
    assert output == 'ㅇㅣ ㅁㅝㄴ ㄱㅐㅅㅗㄹㅣㅇㅑ'


def test_shred_syllable_4():
    input = '여러분 이거 다 거짓말인 거 아시죠'
    output = shred_syllable(input, active_rate=1.0)
    assert output == 'ㅇㅕㄹㅓㅂㅜㄴ ㅇㅣㄱㅓ ㄷㅏ ㄱㅓㅈㅣㅅㅁㅏㄹㅇㅣㄴ ㄱㅓ ㅇㅏㅅㅣㅈㅛ'
