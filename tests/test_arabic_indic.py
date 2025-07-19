from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Arabic-Indic tests"

def test_arabic_indic_to_english1():
    assert convert("٠١٢٣٤٥٦٧٨٩", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.ENGLISH) == "0123456789"

def test_arabic_indic_to_english2():
    assert convert("abc ٠١٢٣٤٥٦٧٨٩ abc", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.ENGLISH) == "abc 0123456789 abc"

def test_arabic_indic_to_persian1():
    assert convert("٠١٢٣٤٥٦٧٨٩", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.PERSIAN) == "۰۱۲۳۴۵۶۷۸۹"

def test_arabic_indic_to_persian2():
    assert convert("abc ٠١٢٣٤٥٦٧٨٩ abc", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.PERSIAN) == "abc ۰۱۲۳۴۵۶۷۸۹ abc"

def test_arabic_indic_to_hindi1():
    assert convert("٠١٢٣٤٥٦٧٨٩", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.HINDI) == "०१२३४५६７८९"

def test_arabic_indic_to_hindi2():
    assert convert("abc ٠١٢٣٤٥٦٧٨٩ abc", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.HINDI) == "abc ०१२३४५६７८९ abc"

def test_arabic_indic_to_bengali1():
    assert convert("٠١٢٣٤٥٦٧٨٩", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"

def test_arabic_indic_to_bengali2():
    assert convert("abc ٠١٢٣٤٥٦٧٨٩ abc", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.BENGALI) == "abc ০১২৩৪৫৬৭৮৯ abc"