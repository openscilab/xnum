import pytest
from xnum import XNumError, XNumValidationError
from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Errors tests"


def test_error_inheritance():
    assert issubclass(XNumError, Exception)
    assert issubclass(XNumValidationError, PixoraError)
    assert issubclass(XNumValidationError, ValueError)


def test_text_error():
    with pytest.raises(XNumValidationError, match=r"Invalid value. `text` must be a string."):
        _ = convert(2, target=NumeralSystem.PERSIAN, source=NumeralSystem.ENGLISH)


def test_target_error1():
    with pytest.raises(XNumValidationError, match=r"Invalid value. `target` must be an instance of NumeralSystem enum."):
        _ = convert("۱۲۳۴۵", target="English", source=NumeralSystem.PERSIAN)


def test_target_error2():
    with pytest.raises(XNumValidationError, match=r"Invalid value. `target` cannot be NumeralSystem.AUTO."):
        _ = convert("۱۲۳۴۵", target=NumeralSystem.AUTO, source=NumeralSystem.PERSIAN)


def test_source_error():
    with pytest.raises(XNumValidationError, match=r"Invalid value. `source` must be an instance of NumeralSystem enum."):
        _ = convert("12345", target=NumeralSystem.PERSIAN, source="English")
