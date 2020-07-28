# Kotka

> Korean Obfuscation ToolKit Advanced

[![PyPI](https://img.shields.io/pypi/v/kotka?logo=pypi&logoColor=white&style=for-the-badge)](https://pypi.org/project/kotka/)
[![Python](https://img.shields.io/pypi/pyversions/kotka?logo=python&logoColor=white&style=for-the-badge)](https://www.python.org/)
[![GitHub Workflow](https://img.shields.io/github/workflow/status/Astro36/kotka/Python?logo=github&logoColor=white&style=for-the-badge)](https://github.com/Astro36/kotka/actions)
[![Codecov](https://img.shields.io/codecov/c/gh/Astro36/kotka?logo=codecov&logoColor=white&style=for-the-badge)](https://codecov.io/gh/Astro36/kotka)
[![Downloads](https://img.shields.io/pypi/dm/kotka?logo=pypi&logoColor=white&style=for-the-badge)](https://pypi.org/project/kotka/)
[![License](https://img.shields.io/pypi/l/kotka?style=for-the-badge)](./LICENSE)

## ChangeLog

See [CHANGELOG](./CHANGELOG.md)

## Features

### Text Obfuscation

- [네모네모 멈뭄미의 저주 시리즈](https://namu.wiki/w/네모네모%20멈뭄미): "안녕하세요" -> "만념하세묘"
- [야민정음](https://namu.wiki/w/야민정음): "명작" -> "띵작"
- 확률적 자음/모음 분리: "안녕하세요" -> "안ㄴㅕㅇ하ㅅㅔ요"

## Installation

- Install with [PyPI](https://pypi.org/):

```bash
pip install kotka
```

- Clone the repo:

```bash
git clone https://github.com/Astro36/kotka.git
```

## Usage

### Example

문장을 [네모네모 멈뭄미의 저주 시리즈](https://namu.wiki/w/네모네모%20멈뭄미)를 이용해 변환합니다:

```python
from kotka.lipogram import replace_phoneme
from kotka.lipogram.rules import SquareDog

print(replace_phoneme('너 인성문제 있어?', rule=SquareDog()))  # '너 민섬문제 밌머?'
```

문장을 [야민정음](https://namu.wiki/w/야민정음)을 이용해 변환합니다:

```python
from kotka.yaminizer import encode_yamin

print(encode_yamin('명작'))  # '띵작'
print(encode_yamin('대구광역시'))  # '머구팡역시'
print(encode_yamin('충무공 이순신'))  # '충무끙 이순신'
```

일부 글자의 자모를 분리해 읽기 어렵게 만듭니다:

```python
from kotka.shredder import shred_syllable

print(shred_syllable('반으로 갈라져서 죽어', active_rate=0.5))  # '반ㅇㅡㄹㅗ 갈ㄹㅏ져ㅅㅓ 죽어'
```

## License

```text
Copyright (c) 2020 Seungjae Park

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

Kotka is licensed under the [MIT License](./LICENSE).
