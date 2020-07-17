from kotka.rule import BeSquareDog
from kotka.text import Obfuscator


def test_obfuscator():
    obfuscator = Obfuscator()
    obfuscator.add_rule(BeSquareDog())
    input = '당신은 네모네모 멈뭄미와 눈이 마주치고 말았습니다.'
    output = obfuscator.run(input)
    assert output == '담신믄 네모네모 멈뭄미뫄 눈미 마주치고 말맜습니다.'
