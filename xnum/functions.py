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

    all_digits = list(ALL_DIGIT_MAPS.keys())
    all_digits.sort(key=len, reverse=True)
    pattern = r"(?:{})".format("|".join(re.escape(digit) for digit in all_digits))

    def convert_match(match: Match[str]) -> str:
        """
        Provide a substitution string based on a regex match object, for use with re.sub.

        :param match: a regular expression match object
        """
        token = match.group()
        detected = detect_system(token)
        if source == NumeralSystem.AUTO:
            return translate_digit(token, target)
        elif detected == source:
            return translate_digit(token, target)
        return token

    result = re.sub(pattern, convert_match, text)
    return result
