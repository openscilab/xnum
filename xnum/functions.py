# -*- coding: utf-8 -*-
"""XNum functions."""
import re
from typing import Match
from .params import NumeralSystem, NUMERAL_MAPS, ALL_DIGIT_MAPS
from .params import INVALID_SOURCE_MESSAGE, INVALID_TEXT_MESSAGE
from .params import INVALID_TARGET_MESSAGE1, INVALID_TARGET_MESSAGE2


def detect_system(char: str) -> NumeralSystem:
    """
    Detect numeral system.

    :param char: character
    """
    for system, digits in NUMERAL_MAPS.items():
        if char in digits:
            return NumeralSystem(system)
    return NumeralSystem.ENGLISH


def translate_digit(char: str, target: NumeralSystem) -> str:
    """
    Translate digit.

    :param char: character
    :param target: target numeral system
    """
    if char in ALL_DIGIT_MAPS:
        standard = ALL_DIGIT_MAPS[char]
        return NUMERAL_MAPS[target.value][int(standard)]
    return char


def convert(text: str, target: NumeralSystem, source: NumeralSystem = NumeralSystem.AUTO) -> str:
    """
    Convert function.

    :param text: input text
    :param target: target numeral system
    :param source: source numeral system
    """
    if not isinstance(text, str):
        raise ValueError(INVALID_TEXT_MESSAGE)
    if not isinstance(target, NumeralSystem):
        raise ValueError(INVALID_TARGET_MESSAGE1)
    if target == NumeralSystem.AUTO:
        raise ValueError(INVALID_TARGET_MESSAGE2)
    if not isinstance(source, NumeralSystem):
        raise ValueError(INVALID_SOURCE_MESSAGE)

    def convert_match(match: Match[str]):
        """
        Provide a substitution string based on a regex match object, for use with re.sub.

        :param match: a regular expression match object
        """
        token = match.group()
        result = []
        for char in token:
            detected = detect_system(char)
            if source == NumeralSystem.AUTO:
                result.append(translate_digit(char, target))
            elif detected == source:
                result.append(translate_digit(char, target))
            else:
                result.append(char)

        return ''.join(result)

    pattern = r'[{}]+'.format(''.join(re.escape(digit) for digits in NUMERAL_MAPS.values() for digit in digits))
    result = re.sub(pattern, convert_match, text)
    return result
