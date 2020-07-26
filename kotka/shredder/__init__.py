from random import random
from hgtk.letter import decompose
from ..utils.hangul import is_complete_syllable


def shred_syllable(text: str, *, active_rate=0.1) -> str:
    output = ''
    for char in text:
        if random() < active_rate and is_complete_syllable(char):
            output += ''.join(decompose(char))
        else:
            output += char
    return output
