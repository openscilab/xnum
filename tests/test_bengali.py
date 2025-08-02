from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Bengali tests"


def test_identity_conversion():
    assert convert("০১২৩৪৫৬৭৮৯", source=NumeralSystem.BENGALI, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"


def test_bengali_to_english1():
    assert convert("০১২৩৪৫৬৭৮৯", source=NumeralSystem.BENGALI, target=NumeralSystem.ENGLISH) == "0123456789"


def test_bengali_to_english2():
    assert convert("abc ০১২৩৪৫৬৭৮৯ abc", source=NumeralSystem.BENGALI,
                   target=NumeralSystem.ENGLISH) == "abc 0123456789 abc"


def test_bengali_to_persian1():
    assert convert("০১২৩৪৫৬৭৮৯", source=NumeralSystem.BENGALI, target=NumeralSystem.PERSIAN) == "۰۱۲۳۴۵۶۷۸۹"


def test_bengali_to_persian2():
    assert convert("abc ০১২৩৪৫৬৭৮৯ abc", source=NumeralSystem.BENGALI,
                   target=NumeralSystem.PERSIAN) == "abc ۰۱۲۳۴۵۶۷۸۹ abc"


def test_bengali_to_hindi1():
    assert convert("০১২৩৪৫৬৭৮৯", source=NumeralSystem.BENGALI, target=NumeralSystem.HINDI) == "०१२३४५६७८९"


def test_bengali_to_hindi2():
    assert convert("abc ০১২৩৪৫৬৭৮৯ abc", source=NumeralSystem.BENGALI,
                   target=NumeralSystem.HINDI) == "abc ०१२३४५६७८९ abc"


def test_bengali_to_arabic_indic1():
    assert convert("০১২৩৪৫৬৭৮৯", source=NumeralSystem.BENGALI, target=NumeralSystem.ARABIC_INDIC) == "٠١٢٣٤٥٦٧٨٩"


def test_bengali_to_arabic_indic2():
    assert convert("abc ০১২৩৪৫৬৭৮৯ abc", source=NumeralSystem.BENGALI,
                   target=NumeralSystem.ARABIC_INDIC) == "abc ٠١٢٣٤٥٦٧٨٩ abc"


def test_bengali_to_thai1():
    assert convert("০১২৩৪৫৬৭৮৯", source=NumeralSystem.BENGALI, target=NumeralSystem.THAI) == "๐๑๒๓๔๕๖๗๘๙"


def test_bengali_to_thai2():
    assert convert("abc ০১২৩৪৫৬৭৮৯ abc", source=NumeralSystem.BENGALI,
                   target=NumeralSystem.THAI) == "abc ๐๑๒๓๔๕๖๗๘๙ abc"


def test_bengali_to_khmer1():
    assert convert("০১২৩৪৫৬৭৮৯", source=NumeralSystem.BENGALI, target=NumeralSystem.KHMER) == "០១២៣៤៥៦៧៨៩"


def test_bengali_to_khmer2():
    assert convert("abc ০১২৩৪৫৬৭৮৯ abc", source=NumeralSystem.BENGALI,
                   target=NumeralSystem.KHMER) == "abc ០១២៣៤៥៦៧៨៩ abc"


def test_bengali_to_burmese1():
    assert convert("০১২৩৪৫৬৭৮৯", source=NumeralSystem.BENGALI, target=NumeralSystem.BURMESE) == "၀၁၂၃၄၅၆၇၈၉"


def test_bengali_to_burmese2():
    assert convert("abc ০১২৩৪৫৬৭৮৯ abc", source=NumeralSystem.BENGALI,
                   target=NumeralSystem.BURMESE) == "abc ၀၁၂၃၄၅၆၇၈၉ abc"


def test_bengali_to_tibetan1():
    assert convert("০১২৩৪৫৬৭৮৯", source=NumeralSystem.BENGALI, target=NumeralSystem.TIBETAN) == "༠༡༢༣༤༥༦༧༨༩"


def test_bengali_to_tibetan2():
    assert convert("abc ০১২৩৪৫৬৭৮৯ abc", source=NumeralSystem.BENGALI,
                   target=NumeralSystem.TIBETAN) == "abc ༠༡༢༣༤༥༦༧༨༩ abc"


def test_bengali_to_gujarati1():
    assert convert("০১২৩৪৫৬৭৮৯", source=NumeralSystem.BENGALI, target=NumeralSystem.GUJARATI) == "૦૧૨૩૪૫૬૭૮૯"


def test_bengali_to_gujarati2():
    assert convert("abc ০১২৩৪৫৬৭৮৯ abc", source=NumeralSystem.BENGALI,
                   target=NumeralSystem.GUJARATI) == "abc ૦૧૨૩૪૫૬૭૮૯ abc"


def test_bengali_to_odia1():
    assert convert("০১২৩৪৫৬৭৮৯", source=NumeralSystem.BENGALI, target=NumeralSystem.ODIA) == "୦୧୨୩୪୫୬୭୮୯"


def test_bengali_to_odia2():
    assert convert("abc ০১২৩৪৫৬৭৮৯ abc", source=NumeralSystem.BENGALI,
                   target=NumeralSystem.ODIA) == "abc ୦୧୨୩୪୫୬୭୮୯ abc"
