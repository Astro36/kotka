from kotka.yaminizer import encode_yamin


def test_encode_yamin():
    input = "나라의 말이 중국과 달라 한문·한자와 서로 통하지 아니하므로 이런 까닭으로 어리석은 백성들이 말하고자 하는 바가 있어도 끝내 제 뜻을 펴지 못하는 사람이 많다."
    output = encode_yamin(input)
    assert output == '나라익 말이 중국파 달라 한문·한자와 서로 듷하거 아니하므로 이런 까닭으로 어리석은 뿌성들이 말하끄자 하는 바가 있어도 곹LH 제 뜻을 펴거 못하는 사람이 많다.'
