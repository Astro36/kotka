def is_complete_hangul(char: str) -> bool:
    FRIST_HANGUL_UNICODE = 0xAC00
    LAST_HANGUL_UNICODE = 0xD7A3
    return len(char) == 1 and FRIST_HANGUL_UNICODE <= ord(char) <= LAST_HANGUL_UNICODE
