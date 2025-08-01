from xnum import convert, NumeralSystem

TEST_CASE_NAME = "English tests"


def test_identity_conversion():
    assert convert("0123456789", source=NumeralSystem.ENGLISH, target=NumeralSystem.ENGLISH) == "0123456789"


def test_english_to_persian1():
    assert convert("0123456789", source=NumeralSystem.ENGLISH, target=NumeralSystem.PERSIAN) == "۰۱۲۳۴۵۶۷۸۹"


def test_english_to_persian2():
    assert convert("abc 0123456789 abc", source=NumeralSystem.ENGLISH,
                   target=NumeralSystem.PERSIAN) == "abc ۰۱۲۳۴۵۶۷۸۹ abc"


def test_english_to_hindi1():
    assert convert("0123456789", source=NumeralSystem.ENGLISH, target=NumeralSystem.HINDI) == "०१२३४५६७८९"


def test_english_to_hindi2():
    assert convert("abc 0123456789 abc", source=NumeralSystem.ENGLISH,
                   target=NumeralSystem.HINDI) == "abc ०१२३४५६७८९ abc"


def test_english_to_arabic_indic1():
    assert convert("0123456789", source=NumeralSystem.ENGLISH, target=NumeralSystem.ARABIC_INDIC) == "٠١٢٣٤٥٦٧٨٩"


def test_english_to_arabic_indic2():
    assert convert("abc 0123456789 abc", source=NumeralSystem.ENGLISH,
                   target=NumeralSystem.ARABIC_INDIC) == "abc ٠١٢٣٤٥٦٧٨٩ abc"


def test_english_to_bengali1():
    assert convert("0123456789", source=NumeralSystem.ENGLISH, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"


def test_english_to_bengali2():
    assert convert("abc 0123456789 abc", source=NumeralSystem.ENGLISH,
                   target=NumeralSystem.BENGALI) == "abc ০১২৩৪৫৬৭৮৯ abc"


def test_english_to_thai1():
    assert convert("0123456789", source=NumeralSystem.ENGLISH, target=NumeralSystem.THAI) == "๐๑๒๓๔๕๖๗๘๙"


def test_english_to_thai2():
    assert convert("abc 0123456789 abc", source=NumeralSystem.ENGLISH,
                   target=NumeralSystem.THAI) == "abc ๐๑๒๓๔๕๖๗๘๙ abc"


def test_english_to_khmer1():
    assert convert("0123456789", source=NumeralSystem.ENGLISH, target=NumeralSystem.KHMER) == "០១២៣៤៥៦៧៨៩"


def test_english_to_khmer2():
    assert convert("abc 0123456789 abc", source=NumeralSystem.ENGLISH,
                   target=NumeralSystem.KHMER) == "abc ០១២៣៤៥៦៧៨៩ abc"


def test_english_to_burmese1():
    assert convert("0123456789", source=NumeralSystem.ENGLISH, target=NumeralSystem.BURMESE) == "၀၁၂၃၄၅၆၇၈၉"


def test_english_to_burmese2():
    assert convert("abc 0123456789 abc", source=NumeralSystem.ENGLISH,
                   target=NumeralSystem.BURMESE) == "abc ၀၁၂၃၄၅၆၇၈၉ abc"


def test_english_to_tibetan1():
    assert convert("0123456789", source=NumeralSystem.ENGLISH, target=NumeralSystem.TIBETAN) == "༠༡༢༣༤༥༦༧༨༩"


def test_english_to_tibetan2():
    assert convert("abc 0123456789 abc", source=NumeralSystem.ENGLISH,
                   target=NumeralSystem.TIBETAN) == "abc ༠༡༢༣༤༥༦༧༨༩ abc"


def test_english_to_gujarati1():
    assert convert("0123456789", source=NumeralSystem.ENGLISH, target=NumeralSystem.GUJARATI) == "૦૧૨૩૪૫૬૭૮૯"


def test_english_to_gujarati2():
    assert convert("abc 0123456789 abc", source=NumeralSystem.ENGLISH,
                   target=NumeralSystem.GUJARATI) == "abc ૦૧૨૩૪૫૬૭૮૯ abc"


def test_english_to_odia1():
    assert convert("0123456789", source=NumeralSystem.ENGLISH, target=NumeralSystem.ODIA) == "୦୧୨୩୪୫୬୭୮୯"


def test_english_to_odia2():
    assert convert("abc 0123456789 abc", source=NumeralSystem.ENGLISH,
                   target=NumeralSystem.ODIA) == "abc ୦୧୨୩୪୫୬୭୮୯ abc"
