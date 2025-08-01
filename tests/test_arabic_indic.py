from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Arabic-Indic tests"


def test_identity_conversion():
    assert convert("٠١٢٣٤٥٦٧٨٩", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.ARABIC_INDIC) == "٠١٢٣٤٥٦٧٨٩"


def test_arabic_indic_to_english1():
    assert convert("٠١٢٣٤٥٦٧٨٩", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.ENGLISH) == "0123456789"


def test_arabic_indic_to_english2():
    assert convert("abc ٠١٢٣٤٥٦٧٨٩ abc", source=NumeralSystem.ARABIC_INDIC,
                   target=NumeralSystem.ENGLISH) == "abc 0123456789 abc"


def test_arabic_indic_to_persian1():
    assert convert("٠١٢٣٤٥٦٧٨٩", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.PERSIAN) == "۰۱۲۳۴۵۶۷۸۹"


def test_arabic_indic_to_persian2():
    assert convert("abc ٠١٢٣٤٥٦٧٨٩ abc", source=NumeralSystem.ARABIC_INDIC,
                   target=NumeralSystem.PERSIAN) == "abc ۰۱۲۳۴۵۶۷۸۹ abc"


def test_arabic_indic_to_hindi1():
    assert convert("٠١٢٣٤٥٦٧٨٩", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.HINDI) == "०१२३४५६७८९"


def test_arabic_indic_to_hindi2():
    assert convert("abc ٠١٢٣٤٥٦٧٨٩ abc", source=NumeralSystem.ARABIC_INDIC,
                   target=NumeralSystem.HINDI) == "abc ०१२३४५६७८९ abc"


def test_arabic_indic_to_bengali1():
    assert convert("٠١٢٣٤٥٦٧٨٩", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"


def test_arabic_indic_to_bengali2():
    assert convert("abc ٠١٢٣٤٥٦٧٨٩ abc", source=NumeralSystem.ARABIC_INDIC,
                   target=NumeralSystem.BENGALI) == "abc ০১২৩৪৫৬৭৮৯ abc"


def test_arabic_indic_to_thai1():
    assert convert("٠١٢٣٤٥٦٧٨٩", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.THAI) == "๐๑๒๓๔๕๖๗๘๙"


def test_arabic_indic_to_thai2():
    assert convert("abc ٠١٢٣٤٥٦٧٨٩ abc", source=NumeralSystem.ARABIC_INDIC,
                   target=NumeralSystem.THAI) == "abc ๐๑๒๓๔๕๖๗๘๙ abc"


def test_arabic_indic_to_khmer1():
    assert convert("٠١٢٣٤٥٦٧٨٩", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.KHMER) == "០១២៣៤៥៦៧៨៩"


def test_arabic_indic_to_khmer2():
    assert convert("abc ٠١٢٣٤٥٦٧٨٩ abc", source=NumeralSystem.ARABIC_INDIC,
                   target=NumeralSystem.KHMER) == "abc ០១២៣៤៥៦៧៨៩ abc"


def test_arabic_indic_to_burmese1():
    assert convert("٠١٢٣٤٥٦٧٨٩", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.BURMESE) == "၀၁၂၃၄၅၆၇၈၉"


def test_arabic_indic_to_burmese2():
    assert convert("abc ٠١٢٣٤٥٦٧٨٩ abc", source=NumeralSystem.ARABIC_INDIC,
                   target=NumeralSystem.BURMESE) == "abc ၀၁၂၃၄၅၆၇၈၉ abc"


def test_arabic_indic_to_tibetan1():
    assert convert("٠١٢٣٤٥٦٧٨٩", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.TIBETAN) == "༠༡༢༣༤༥༦༧༨༩"


def test_arabic_indic_to_tibetan2():
    assert convert("abc ٠١٢٣٤٥٦٧٨٩ abc", source=NumeralSystem.ARABIC_INDIC,
                   target=NumeralSystem.TIBETAN) == "abc ༠༡༢༣༤༥༦༧༨༩ abc"


def test_arabic_indic_to_gujarati1():
    assert convert("٠١٢٣٤٥٦٧٨٩", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.GUJARATI) == "૦૧૨૩૪૫૬૭૮૯"


def test_arabic_indic_to_gujarati2():
    assert convert("abc ٠١٢٣٤٥٦٧٨٩ abc", source=NumeralSystem.ARABIC_INDIC,
                   target=NumeralSystem.GUJARATI) == "abc ૦૧૨૩૪૫૬૭૮૯ abc"


def test_arabic_indic_to_odia1():
    assert convert("٠١٢٣٤٥٦٧٨٩", source=NumeralSystem.ARABIC_INDIC, target=NumeralSystem.ODIA) == "୦୧୨୩୪୫୬୭୮୯"


def test_arabic_indic_to_odia2():
    assert convert("abc ٠١٢٣٤٥٦٧٨٩ abc", source=NumeralSystem.ARABIC_INDIC,
                   target=NumeralSystem.ODIA) == "abc ୦୧୨୩୪୫୬୭୮୯ abc"
