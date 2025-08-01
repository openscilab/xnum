from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Tibetan tests"


def test_identity_conversion():
    assert convert("༠༡༢༣༤༥༦༧༨༩", source=NumeralSystem.TIBETAN, target=NumeralSystem.TIBETAN) == "༠༡༢༣༤༥༦༧༨༩"


def test_tibetan_to_english1():
    assert convert("༠༡༢༣༤༥༦༧༨༩", source=NumeralSystem.TIBETAN, target=NumeralSystem.ENGLISH) == "0123456789"


def test_tibetan_to_english2():
    assert convert("abc ༠༡༢༣༤༥༦༧༨༩ abc", source=NumeralSystem.TIBETAN,
                   target=NumeralSystem.ENGLISH) == "abc 0123456789 abc"


def test_tibetan_to_hindi1():
    assert convert("༠༡༢༣༤༥༦༧༨༩", source=NumeralSystem.TIBETAN, target=NumeralSystem.HINDI) == "०१२३४५६७८९"


def test_tibetan_to_hindi2():
    assert convert("abc ༠༡༢༣༤༥༦༧༨༩ abc", source=NumeralSystem.TIBETAN,
                   target=NumeralSystem.HINDI) == "abc ०१२३४५६७८९ abc"


def test_tibetan_to_arabic_indic1():
    assert convert("༠༡༢༣༤༥༦༧༨༩", source=NumeralSystem.TIBETAN, target=NumeralSystem.ARABIC_INDIC) == "٠١٢٣٤٥٦٧٨٩"


def test_tibetan_to_arabic_indic2():
    assert convert("abc ༠༡༢༣༤༥༦༧༨༩ abc", source=NumeralSystem.TIBETAN,
                   target=NumeralSystem.ARABIC_INDIC) == "abc ٠١٢٣٤٥٦٧٨٩ abc"


def test_tibetan_to_bengali1():
    assert convert("༠༡༢༣༤༥༦༧༨༩", source=NumeralSystem.TIBETAN, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"


def test_tibetan_to_bengali2():
    assert convert("abc ༠༡༢༣༤༥༦༧༨༩ abc", source=NumeralSystem.TIBETAN,
                   target=NumeralSystem.BENGALI) == "abc ০১২৩৪৫৬৭৮৯ abc"


def test_tibetan_to_thai1():
    assert convert("༠༡༢༣༤༥༦༧༨༩", source=NumeralSystem.TIBETAN, target=NumeralSystem.THAI) == "๐๑๒๓๔๕๖๗๘๙"


def test_tibetan_to_thai2():
    assert convert("abc ༠༡༢༣༤༥༦༧༨༩ abc", source=NumeralSystem.TIBETAN,
                   target=NumeralSystem.THAI) == "abc ๐๑๒๓๔๕๖๗๘๙ abc"


def test_tibetan_to_khmer1():
    assert convert("༠༡༢༣༤༥༦༧༨༩", source=NumeralSystem.TIBETAN, target=NumeralSystem.KHMER) == "០១២៣៤៥៦៧៨៩"


def test_tibetan_to_khmer2():
    assert convert("abc ༠༡༢༣༤༥༦༧༨༩ abc", source=NumeralSystem.TIBETAN,
                   target=NumeralSystem.KHMER) == "abc ០១២៣៤៥៦៧៨៩ abc"


def test_tibetan_to_burmese1():
    assert convert("༠༡༢༣༤༥༦༧༨༩", source=NumeralSystem.TIBETAN, target=NumeralSystem.BURMESE) == "၀၁၂၃၄၅၆၇၈၉"


def test_tibetan_to_burmese2():
    assert convert("abc ༠༡༢༣༤༥༦༧༨༩ abc", source=NumeralSystem.TIBETAN,
                   target=NumeralSystem.BURMESE) == "abc ၀၁၂၃၄၅၆၇၈၉ abc"


def test_tibetan_to_persian1():
    assert convert("༠༡༢༣༤༥༦༧༨༩", source=NumeralSystem.TIBETAN, target=NumeralSystem.PERSIAN) == "۰۱۲۳۴۵۶۷۸۹"


def test_tibetan_to_persian2():
    assert convert("abc ༠༡༢༣༤༥༦༧༨༩ abc", source=NumeralSystem.TIBETAN,
                   target=NumeralSystem.PERSIAN) == "abc ۰۱۲۳۴۵۶۷۸۹ abc"


def test_tibetan_to_gujarati1():
    assert convert("༠༡༢༣༤༥༦༧༨༩", source=NumeralSystem.TIBETAN, target=NumeralSystem.GUJARATI) == "૦૧૨૩૪૫૬૭૮૯"


def test_tibetan_to_gujarati2():
    assert convert("abc ༠༡༢༣༤༥༦༧༨༩ abc", source=NumeralSystem.TIBETAN,
                   target=NumeralSystem.GUJARATI) == "abc ૦૧૨૩૪૫૬૭૮૯ abc"


def test_tibetan_to_odia1():
    assert convert("༠༡༢༣༤༥༦༧༨༩", source=NumeralSystem.TIBETAN, target=NumeralSystem.ODIA) == "୦୧୨୩୪୫୬୭୮୯"


def test_tibetan_to_odia2():
    assert convert("abc ༠༡༢༣༤༥༦༧༨༩ abc", source=NumeralSystem.TIBETAN,
                   target=NumeralSystem.ODIA) == "abc ୦୧୨୩୪୫୬୭୮୯ abc"
