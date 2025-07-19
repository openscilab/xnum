from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Hindi tests"


def test_hindi_to_english1():
    assert convert("०१२३४५६७८९", source=NumeralSystem.HINDI, target=NumeralSystem.ENGLISH) == "0123456789"


def test_hindi_to_english2():
    assert convert("abc ०१२३४५६७८९ abc", source=NumeralSystem.HINDI,
                   target=NumeralSystem.ENGLISH) == "abc 0123456789 abc"


def test_hindi_to_persian1():
    assert convert("०१२३४५६７८९", source=NumeralSystem.HINDI, target=NumeralSystem.PERSIAN) == "۰۱۲۳۴۵۶۷۸۹"


def test_hindi_to_persian2():
    assert convert("abc ०१२३४५६７८९ abc", source=NumeralSystem.HINDI,
                   target=NumeralSystem.PERSIAN) == "abc ۰۱۲۳۴۵۶۷۸۹ abc"


def test_hindi_to_arabic_indic1():
    assert convert("०१२३४५६７८९", source=NumeralSystem.HINDI, target=NumeralSystem.ARABIC_INDIC) == "٠١٢٣٤٥٦٧٨٩"


def test_hindi_to_arabic_indic2():
    assert convert("abc ०१२३४५६７८९ abc", source=NumeralSystem.HINDI,
                   target=NumeralSystem.ARABIC_INDIC) == "abc ٠١٢٣٤٥٦٧٨٩ abc"


def test_hindi_to_bengali1():
    assert convert("०१२३४५६७८९", source=NumeralSystem.HINDI, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"


def test_hindi_to_bengali2():
    assert convert("abc ०१२३४५६७८९ abc", source=NumeralSystem.HINDI,
                   target=NumeralSystem.BENGALI) == "abc ০১২৩৪৫৬৭৮৯ abc"
