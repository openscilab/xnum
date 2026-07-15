from xnum import convert, NumeralSystem
from xnum.functions import _detect_digit_system, _translate_digit

TEST_CASE_NAME = "Auto-detect & edge tests"


def test_auto_detect_mixed():
    assert convert("۰۱۲ and ٤٥٦ and ১২৩", target=NumeralSystem.ENGLISH) == "012 and 456 and 123"


def test_preserve_non_digits():
    assert convert("abc ۰۱۲!", target=NumeralSystem.ENGLISH) == "abc 012!"


def test_no_conversion_if_not_matching_source():
    assert convert("০১২ and ٤٥٦", source=NumeralSystem.ENGLISH, target=NumeralSystem.HINDI) == "০১২ and ٤٥٦"


def test_empty_string():
    assert convert("", target=NumeralSystem.ENGLISH) == ""


def test_mixed_language_context1():
    text = "The result is ٤٥٦ and also ۰۱۲"
    expected = "The result is 456 and also 012"
    assert convert(text, target=NumeralSystem.ENGLISH) == expected


def test_mixed_language_context2():
    text = "The result is 012૩૪૫۶۷۸۹"
    expected = "The result is 012৩৪৫۶۷۸۹"
    assert convert(text, source=NumeralSystem.GUJARATI, target=NumeralSystem.BENGALI) == expected


def test_mixed_language_context3():
    text = "The result is 012૩૪૫۶۷۸۹"
    expected = "The result is 012③④⑤۶۷۸۹"
    assert convert(text, source=NumeralSystem.GUJARATI, target=NumeralSystem.ENGLISH_CIRCLED) == expected


def test_detect_digit_system_default():
    assert _detect_digit_system(" ") == NumeralSystem.ENGLISH


def test_translate_digit_pass():
    assert _translate_digit(" ", NumeralSystem.ENGLISH) == " "
