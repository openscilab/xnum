from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Persian tests"


def test_persian_to_english1():
    assert convert("۰۱۲۳۴۵۶۷۸۹", source=NumeralSystem.PERSIAN, target=NumeralSystem.ENGLISH) == "0123456789"


def test_persian_to_english2():
    assert convert("abc ۰۱۲۳۴۵۶۷۸۹ abc", source=NumeralSystem.PERSIAN,
                   target=NumeralSystem.ENGLISH) == "abc 0123456789 abc"


def test_persian_to_hindi1():
    assert convert("۰۱۲۳۴۵۶۷۸۹", source=NumeralSystem.PERSIAN, target=NumeralSystem.HINDI) == "०१२३४५६७८९"


def test_persian_to_hindi2():
    assert convert("abc ۰۱۲۳۴۵۶۷۸۹ abc", source=NumeralSystem.PERSIAN,
                   target=NumeralSystem.HINDI) == "abc ०१२३४५६७८९ abc"


def test_persian_to_arabic_indic1():
    assert convert("۰۱۲۳۴۵۶۷۸۹", source=NumeralSystem.PERSIAN, target=NumeralSystem.ARABIC_INDIC) == "٠١٢٣٤٥٦٧٨٩"


def test_persian_to_arabic_indic2():
    assert convert("abc ۰۱۲۳۴۵۶۷۸۹ abc", source=NumeralSystem.PERSIAN,
                   target=NumeralSystem.ARABIC_INDIC) == "abc ٠١٢٣٤٥٦٧٨٩ abc"


def test_persian_to_bengali1():
    assert convert("۰۱۲۳۴۵۶۷۸۹", source=NumeralSystem.PERSIAN, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"


def test_persian_to_bengali2():
    assert convert("abc ۰۱۲۳۴۵۶۷۸۹ abc", source=NumeralSystem.PERSIAN,
                   target=NumeralSystem.BENGALI) == "abc ০১২৩৪৫৬৭৮৯ abc"
