from kotka.yaminizer import encode_yamin


def test_encode_yamin_0():
    input = "나라의 말이 중국과 달라 한문·한자와 서로 통하지 아니하므로 이런 까닭으로 어리석은 백성들이 말하고자 하는 바가 있어도 끝내 제 뜻을 펴지 못하는 사람이 많다."
    output = encode_yamin(input)
    assert output == '나라익 말이 중국파 달라 한문·한자와 서로 듷하거 아니하므로 이런 까닭으로 어리석은 뿌성들이 말하끄자 하는 바가 있어도 곹LH 제 뜻을 펴거 못하는 사람이 많다.'


def test_encode_yamin_1():
    input = "내가 이를 불쌍히 여겨 새로 스물여덟 글자를 만드니 사람마다 하여금 쉽게 익혀 날마다 씀에 편하게 하고자 할 따름이다."
    output = encode_yamin(input)
    assert output == 'LH가 이를 눨쌍히 억저 새로 亼물억틻 글자를 만드니 사람마다 하억금 쉽게 의혀 날마다 씀에 편하게 하끄자 할 따름이다.'


def test_encode_yamin_2():
    input = "이달에 임금이 친히 언문 28자를 지었는데, 그 글자가 옛 전자를 모방하고, 초성·중성·종성으로 나누어 합한 연후에야 글자를 이루었다."
    output = encode_yamin(input)
    assert output == '이달에 읜금이 친히 언문 28자를 거었는데, 그 글자가 옛 견자를 모방하끄, 초성·중성·종성으로 나누어 합한 연후에OF 글자를 이루었다.'


def test_encode_yamin_3():
    input = "무릇 문자에 관한 것과 이어에 관한 것을 모두 쓸 수 있고, 글자는 비록 쉽고 요약하지마는 전환하는 것이 무궁하니, 이것을 훈민정음이라고 일렀다."
    output = encode_yamin(input)
    assert output == '무릇 문자에 판한 짓파 이어에 판한 짓을 모득 쓸 수 있끄, 글자는 네록 쉽끄 인약하거마는 견환하는 짓이 무궁하니, 이짓을 훈민경음이라끄 읟렀다.'


def test_encode_yamin_4():
    input = "He is black cow"
    output = encode_yamin(input)
    assert output == 'He is lo|ack cow'
