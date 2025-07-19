from xnum import convert, NumeralSystem

TEST_CASE_NAME = "English tests"

def test_english_to_persian1():
    assert convert("0123456789", source=NumeralSystem.ENGLISH, target=NumeralSystem.PERSIAN) == "۰۱۲۳۴۵۶۷۸۹"

def test_english_to_persian2():
    assert convert("abc 0123456789 abc", source=NumeralSystem.ENGLISH, target=NumeralSystem.PERSIAN) == "abc ۰۱۲۳۴۵۶۷۸۹ abc"

def test_english_to_hindi1():
    assert convert("0123456789", source=NumeralSystem.ENGLISH, target=NumeralSystem.HINDI) == "०१२३४५६७८९"

def test_english_to_hindi2():
    assert convert("abc 0123456789 abc", source=NumeralSystem.ENGLISH, target=NumeralSystem.HINDI) == "abc ०१२३४५६७८९ abc"

def test_english_to_arabic_indic1():
    assert convert("0123456789", source=NumeralSystem.ENGLISH, target=NumeralSystem.ARABIC_INDIC) == "٠١٢٣٤٥٦٧٨٩"

def test_english_to_arabic_indic2():
    assert convert("abc 0123456789 abc", source=NumeralSystem.ENGLISH, target=NumeralSystem.ARABIC_INDIC) == "abc ٠١٢٣٤٥٦٧٨٩ abc"

def test_english_to_bengali1():
    assert convert("0123456789", source=NumeralSystem.ENGLISH, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"

def test_english_to_bengali2():
    assert convert("abc 0123456789 abc", source=NumeralSystem.ENGLISH, target=NumeralSystem.BENGALI) == "abc ০১২৩৪৫৬৭৮৯ abc"