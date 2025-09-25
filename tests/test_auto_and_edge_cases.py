from xnum import convert, NumeralSystem
from xnum.functions import detect_system, translate_digit

TEST_CASE_NAME = "Auto-detect & edge tests"


def test_auto_detect_mixed():
    assert convert("۰۱۲ and ٤٥٦ and ১২৩", target=NumeralSystem.ENGLISH) == "012 and 456 and 123"


def test_preserve_non_digits():
    assert convert("abc ۰۱۲!", target=NumeralSystem.ENGLISH) == "abc 012!"


def test_no_conversion_if_not_matching_source():
    assert convert("০১২ and ٤٥٦", source=NumeralSystem.ENGLISH, target=NumeralSystem.HINDI) == "০১২ and ٤٥٦"


def test_empty_string():
    assert convert("", target=NumeralSystem.ENGLISH) == ""


def test_mixed_language_context():
    text = "The result is ٤٥٦ and also ۰۱۲"
    expected = "The result is 456 and also 012"
    assert convert(text, target=NumeralSystem.ENGLISH) == expected


def test_detect_system_default():
    assert detect_system(" ") == NumeralSystem.ENGLISH


def test_translate_digit_pass():
    assert translate_digit(" ", NumeralSystem.ENGLISH) == " "
