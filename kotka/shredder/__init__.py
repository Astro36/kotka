from random import random
from hgtk.checker import is_hangul
from hgtk.letter import decompose


def shred_syllable(text: str, active_rate=0.1) -> str:
    output = ''
    for char in text:
        if random() < active_rate and is_hangul(char):
            output += ''.join(decompose(char))
        else:
            output += char
    return output
