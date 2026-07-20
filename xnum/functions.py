# -*- coding: utf-8 -*-
"""XNum functions."""
import re
from typing import Match, List, Any
from .errors import XNumValidationError
from .params import NumeralSystem, SYSTEM_TO_DIGITS_MAP, DIGIT_TO_VALUE_MAP, DIGIT_SYSTEM_MAP
from .params import INVALID_SOURCE_MESSAGE, INVALID_TEXT_MESSAGE
from .params import INVALID_TARGET_MESSAGE1, INVALID_TARGET_MESSAGE2


def _detect_digit_system(digit: str) -> NumeralSystem:
    """
    Detect a digit numeral system.

    :param digit: input digit
    """
    return DIGIT_SYSTEM_MAP.get(digit, NumeralSystem.ENGLISH)


def _translate_digit(digit: str, target: NumeralSystem) -> str:
    """
    Translate digit.

    :param digit: input digit
    :param target: target numeral system
    """
    if digit in DIGIT_TO_VALUE_MAP:
        standard = DIGIT_TO_VALUE_MAP[digit]
        return SYSTEM_TO_DIGITS_MAP[target.value][int(standard)]
    return digit


def _validate_convert(text: Any, target: Any, source: Any) -> bool:
    """
    Validate convert inputs.

    :param text: input text
    :param target: target numeral system
    :param source: source numeral system
    """
    if not isinstance(text, str):
        raise XNumValidationError(INVALID_TEXT_MESSAGE)
    if not isinstance(target, NumeralSystem):
        raise XNumValidationError(INVALID_TARGET_MESSAGE1)
    if target == NumeralSystem.AUTO:
        raise XNumValidationError(INVALID_TARGET_MESSAGE2)
    if not isinstance(source, NumeralSystem):
        raise XNumValidationError(INVALID_SOURCE_MESSAGE)
    return True


def convert(text: str, target: NumeralSystem, source: NumeralSystem = NumeralSystem.AUTO) -> str:
    """
    Convert function.

    :param text: input text
    :param target: target numeral system
    :param source: source numeral system
    """
    _validate_convert(text=text, target=target, source=source)
    all_digits = list(DIGIT_TO_VALUE_MAP.keys())
    all_digits.sort(key=len, reverse=True)
    pattern = r"(?:{})".format("|".join(re.escape(digit) for digit in all_digits))

    def convert_match(match: Match[str]) -> str:
        """
        Provide a substitution string based on a regex match object, for use with re.sub.

        :param match: a regular expression match object
        """
        token = match.group()
        detected = _detect_digit_system(token)
        if source == NumeralSystem.AUTO:
            return _translate_digit(token, target)
        elif detected == source:
            return _translate_digit(token, target)
        return token

    result = re.sub(pattern, convert_match, text)
    return result


def available_systems() -> List[str]:
    """Return all supported numeral systems."""
    return sorted(SYSTEM_TO_DIGITS_MAP.keys())
