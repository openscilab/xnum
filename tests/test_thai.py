from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Thai tests"


def test_identity_conversion():
    assert convert("๐๑๒๓๔๕๖๗๘๙", source=NumeralSystem.THAI, target=NumeralSystem.THAI) == "๐๑๒๓๔๕๖๗๘๙"


def test_thai_to_english1():
    assert convert("๐๑๒๓๔๕๖๗๘๙", source=NumeralSystem.THAI, target=NumeralSystem.ENGLISH) == "0123456789"


def test_thai_to_english2():
    assert convert("abc ๐๑๒๓๔๕๖๗๘๙ abc", source=NumeralSystem.THAI,
                   target=NumeralSystem.ENGLISH) == "abc 0123456789 abc"


def test_thai_to_hindi1():
    assert convert("๐๑๒๓๔๕๖๗๘๙", source=NumeralSystem.THAI, target=NumeralSystem.HINDI) == "०१२३४५६७८९"


def test_thai_to_hindi2():
    assert convert("abc ๐๑๒๓๔๕๖๗๘๙ abc", source=NumeralSystem.THAI,
                   target=NumeralSystem.HINDI) == "abc ०१२३४५६७८९ abc"


def test_thai_to_arabic_indic1():
    assert convert("๐๑๒๓๔๕๖๗๘๙", source=NumeralSystem.THAI, target=NumeralSystem.ARABIC_INDIC) == "٠١٢٣٤٥٦٧٨٩"


def test_thai_to_arabic_indic2():
    assert convert("abc ๐๑๒๓๔๕๖๗๘๙ abc", source=NumeralSystem.THAI,
                   target=NumeralSystem.ARABIC_INDIC) == "abc ٠١٢٣٤٥٦٧٨٩ abc"


def test_thai_to_bengali1():
    assert convert("๐๑๒๓๔๕๖๗๘๙", source=NumeralSystem.THAI, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"


def test_thai_to_bengali2():
    assert convert("abc ๐๑๒๓๔๕๖๗๘๙ abc", source=NumeralSystem.THAI,
                   target=NumeralSystem.BENGALI) == "abc ০১২৩৪৫৬৭৮৯ abc"


def test_thai_to_persian1():
    assert convert("๐๑๒๓๔๕๖๗๘๙", source=NumeralSystem.THAI, target=NumeralSystem.PERSIAN) == "۰۱۲۳۴۵۶۷۸۹"


def test_thai_to_persian2():
    assert convert("abc ๐๑๒๓๔๕๖๗๘๙ abc", source=NumeralSystem.THAI,
                   target=NumeralSystem.PERSIAN) == "abc ۰۱۲۳۴۵۶۷۸۹ abc"


def test_thai_to_khmer1():
    assert convert("๐๑๒๓๔๕๖๗๘๙", source=NumeralSystem.THAI, target=NumeralSystem.KHMER) == "០១២៣៤៥៦៧៨៩"


def test_thai_to_khmer2():
    assert convert("abc ๐๑๒๓๔๕๖๗๘๙ abc", source=NumeralSystem.THAI,
                   target=NumeralSystem.KHMER) == "abc ០១២៣៤៥៦៧៨៩ abc"


def test_thai_to_burmese1():
    assert convert("๐๑๒๓๔๕๖๗๘๙", source=NumeralSystem.THAI, target=NumeralSystem.BURMESE) == "၀၁၂၃၄၅၆၇၈၉"


def test_thai_to_burmese2():
    assert convert("abc ๐๑๒๓๔๕๖๗๘๙ abc", source=NumeralSystem.THAI,
                   target=NumeralSystem.BURMESE) == "abc ၀၁၂၃၄၅၆၇၈၉ abc"


def test_thai_to_tibetan1():
    assert convert("๐๑๒๓๔๕๖๗๘๙", source=NumeralSystem.THAI, target=NumeralSystem.TIBETAN) == "༠༡༢༣༤༥༦༧༨༩"


def test_thai_to_tibetan2():
    assert convert("abc ๐๑๒๓๔๕๖๗๘๙ abc", source=NumeralSystem.THAI,
                   target=NumeralSystem.TIBETAN) == "abc ༠༡༢༣༤༥༦༧༨༩ abc"


def test_thai_to_gujarati1():
    assert convert("๐๑๒๓๔๕๖๗๘๙", source=NumeralSystem.THAI, target=NumeralSystem.GUJARATI) == "૦૧૨૩૪૫૬૭૮૯"


def test_thai_to_gujarati2():
    assert convert("abc ๐๑๒๓๔๕๖๗๘๙ abc", source=NumeralSystem.THAI,
                   target=NumeralSystem.GUJARATI) == "abc ૦૧૨૩૪૫૬૭૮૯ abc"


def test_thai_to_odia1():
    assert convert("๐๑๒๓๔๕๖๗๘๙", source=NumeralSystem.THAI, target=NumeralSystem.ODIA) == "୦୧୨୩୪୫୬୭୮୯"


def test_thai_to_odia2():
    assert convert("abc ๐๑๒๓๔๕๖๗๘๙ abc", source=NumeralSystem.THAI,
                   target=NumeralSystem.ODIA) == "abc ୦୧୨୩୪୫୬୭୮୯ abc"
