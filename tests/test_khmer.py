from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Khmer tests"


def test_identity_conversion():
    assert convert("០១២៣៤៥៦៧៨៩", source=NumeralSystem.KHMER, target=NumeralSystem.KHMER) == "០១២៣៤៥៦៧៨៩"


def test_khmer_to_english1():
    assert convert("០១២៣៤៥៦៧៨៩", source=NumeralSystem.KHMER, target=NumeralSystem.ENGLISH) == "0123456789"


def test_khmer_to_english2():
    assert convert("abc ០១២៣៤៥៦៧៨៩ abc", source=NumeralSystem.KHMER,
                   target=NumeralSystem.ENGLISH) == "abc 0123456789 abc"


def test_khmer_to_hindi1():
    assert convert("០១២៣៤៥៦៧៨៩", source=NumeralSystem.KHMER, target=NumeralSystem.HINDI) == "०१२३४५६७८९"


def test_khmer_to_hindi2():
    assert convert("abc ០១២៣៤៥៦៧៨៩ abc", source=NumeralSystem.KHMER,
                   target=NumeralSystem.HINDI) == "abc ०१२३४५६७८९ abc"


def test_khmer_to_arabic_indic1():
    assert convert("០១២៣៤៥៦៧៨៩", source=NumeralSystem.KHMER, target=NumeralSystem.ARABIC_INDIC) == "٠١٢٣٤٥٦٧٨٩"


def test_khmer_to_arabic_indic2():
    assert convert("abc ០១២៣៤៥៦៧៨៩ abc", source=NumeralSystem.KHMER,
                   target=NumeralSystem.ARABIC_INDIC) == "abc ٠١٢٣٤٥٦٧٨٩ abc"


def test_khmer_to_bengali1():
    assert convert("០១២៣៤៥៦៧៨៩", source=NumeralSystem.KHMER, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"


def test_khmer_to_bengali2():
    assert convert("abc ០១២៣៤៥៦៧៨៩ abc", source=NumeralSystem.KHMER,
                   target=NumeralSystem.BENGALI) == "abc ০১২৩৪৫৬৭৮৯ abc"


def test_khmer_to_thai1():
    assert convert("០១២៣៤៥៦៧៨៩", source=NumeralSystem.KHMER, target=NumeralSystem.THAI) == "๐๑๒๓๔๕๖๗๘๙"


def test_khmer_to_thai2():
    assert convert("abc ០១២៣៤៥៦៧៨៩ abc", source=NumeralSystem.KHMER,
                   target=NumeralSystem.THAI) == "abc ๐๑๒๓๔๕๖๗๘๙ abc"


def test_khmer_to_persian1():
    assert convert("០១២៣៤៥៦៧៨៩", source=NumeralSystem.KHMER, target=NumeralSystem.PERSIAN) == "۰۱۲۳۴۵۶۷۸۹"


def test_khmer_to_persian2():
    assert convert("abc ០១២៣៤៥៦៧៨៩ abc", source=NumeralSystem.KHMER,
                   target=NumeralSystem.PERSIAN) == "abc ۰۱۲۳۴۵۶۷۸۹ abc"


def test_khmer_to_burmese1():
    assert convert("០១២៣៤៥៦៧៨៩", source=NumeralSystem.KHMER, target=NumeralSystem.BURMESE) == "၀၁၂၃၄၅၆၇၈၉"


def test_khmer_to_burmese2():
    assert convert("abc ០១២៣៤៥៦៧៨៩ abc", source=NumeralSystem.KHMER,
                   target=NumeralSystem.BURMESE) == "abc ၀၁၂၃၄၅၆၇၈၉ abc"


def test_khmer_to_tibetan1():
    assert convert("០១២៣៤៥៦៧៨៩", source=NumeralSystem.KHMER, target=NumeralSystem.TIBETAN) == "༠༡༢༣༤༥༦༧༨༩"


def test_khmer_to_tibetan2():
    assert convert("abc ០១២៣៤៥៦៧៨៩ abc", source=NumeralSystem.KHMER,
                   target=NumeralSystem.TIBETAN) == "abc ༠༡༢༣༤༥༦༧༨༩ abc"


def test_khmer_to_gujarati1():
    assert convert("០១២៣៤៥៦៧៨៩", source=NumeralSystem.KHMER, target=NumeralSystem.GUJARATI) == "૦૧૨૩૪૫૬૭૮૯"


def test_khmer_to_gujarati2():
    assert convert("abc ០១២៣៤៥៦៧៨៩ abc", source=NumeralSystem.KHMER,
                   target=NumeralSystem.GUJARATI) == "abc ૦૧૨૩૪૫૬૭૮૯ abc"


def test_khmer_to_odia1():
    assert convert("០១២៣៤៥៦៧៨៩", source=NumeralSystem.KHMER, target=NumeralSystem.ODIA) == "୦୧୨୩୪୫୬୭୮୯"


def test_khmer_to_odia2():
    assert convert("abc ០១២៣៤៥៦៧៨៩ abc", source=NumeralSystem.KHMER,
                   target=NumeralSystem.ODIA) == "abc ୦୧୨୩୪୫୬୭୮୯ abc"
