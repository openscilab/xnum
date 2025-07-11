# -*- coding: utf-8 -*-
"""XNum functions."""
from .params import NumeralSystem, NUMERAL_MAPS, ALL_DIGIT_MAPS
from .params import INVALID_SOURCE_MESSAGE, INVALID_TARGET_MESSAGE, INVALID_TEXT_MESSAGE
import re

def detect_system(char: str) -> NumeralSystem:
    for system, digits in NUMERAL_MAPS.items():
        if char in digits:
            return NumeralSystem(system)
    return NumeralSystem.ENGLISH


def translate_digit(c: str, target: NumeralSystem) -> str:
    if c in ALL_DIGIT_MAPS:
        standard = ALL_DIGIT_MAPS[c]
        return NUMERAL_MAPS[target.value][int(standard)]
    return c


def convert(text: str, target: NumeralSystem, source: NumeralSystem = NumeralSystem.AUTO) -> str:
    if not isinstance(text, str):
        raise ValueError(INVALID_TEXT_MESSAGE)
    if not isinstance(target, NumeralSystem):
        raise ValueError(INVALID_TARGET_MESSAGE)
    if not isinstance(source, NumeralSystem):
        raise ValueError(INVALID_SOURCE_MESSAGE)

    def convert_match(match):
        token = match.group()

        result = []
        for c in token:
            detected = detect_system(c)
            if source == NumeralSystem.AUTO:
                result.append(translate_digit(c, target))
            elif detected == source:
                result.append(translate_digit(c, target))
            else:
                result.append(c)

        return ''.join(result)

    pattern = r'[{}]+'.format(''.join(re.escape(d) for digits in NUMERAL_MAPS.values() for d in digits))
    result = re.sub(pattern, convert_match, text)
    return result

