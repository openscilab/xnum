from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Burmese tests"


def test_identity_conversion():
    assert convert("၀၁၂၃၄၅၆၇၈၉", source=NumeralSystem.BURMESE, target=NumeralSystem.BURMESE) == "၀၁၂၃၄၅၆၇၈၉"


def test_burmese_to_english1():
    assert convert("၀၁၂၃၄၅၆၇၈၉", source=NumeralSystem.BURMESE, target=NumeralSystem.ENGLISH) == "0123456789"


def test_burmese_to_english2():
    assert convert("abc ၀၁၂၃၄၅၆၇၈၉ abc", source=NumeralSystem.BURMESE,
                   target=NumeralSystem.ENGLISH) == "abc 0123456789 abc"


def test_burmese_to_hindi1():
    assert convert("၀၁၂၃၄၅၆၇၈၉", source=NumeralSystem.BURMESE, target=NumeralSystem.HINDI) == "०१२३४५६७८९"


def test_burmese_to_hindi2():
    assert convert("abc ၀၁၂၃၄၅၆၇၈၉ abc", source=NumeralSystem.BURMESE,
                   target=NumeralSystem.HINDI) == "abc ०१२३४५६७८९ abc"


def test_burmese_to_arabic_indic1():
    assert convert("၀၁၂၃၄၅၆၇၈၉", source=NumeralSystem.BURMESE, target=NumeralSystem.ARABIC_INDIC) == "٠١٢٣٤٥٦٧٨٩"


def test_burmese_to_arabic_indic2():
    assert convert("abc ၀၁၂၃၄၅၆၇၈၉ abc", source=NumeralSystem.BURMESE,
                   target=NumeralSystem.ARABIC_INDIC) == "abc ٠١٢٣٤٥٦٧٨٩ abc"


def test_burmese_to_bengali1():
    assert convert("၀၁၂၃၄၅၆၇၈၉", source=NumeralSystem.BURMESE, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"


def test_burmese_to_bengali2():
    assert convert("abc ၀၁၂၃၄၅၆၇၈၉ abc", source=NumeralSystem.BURMESE,
                   target=NumeralSystem.BENGALI) == "abc ০১২৩৪৫৬৭৮৯ abc"


def test_burmese_to_thai1():
    assert convert("၀၁၂၃၄၅၆၇၈၉", source=NumeralSystem.BURMESE, target=NumeralSystem.THAI) == "๐๑๒๓๔๕๖๗๘๙"


def test_burmese_to_thai2():
    assert convert("abc ၀၁၂၃၄၅၆၇၈၉ abc", source=NumeralSystem.BURMESE,
                   target=NumeralSystem.THAI) == "abc ๐๑๒๓๔๕๖๗๘๙ abc"


def test_burmese_to_khmer1():
    assert convert("၀၁၂၃၄၅၆၇၈၉", source=NumeralSystem.BURMESE, target=NumeralSystem.KHMER) == "០១២៣៤៥៦៧៨៩"


def test_burmese_to_khmer2():
    assert convert("abc ၀၁၂၃၄၅၆၇၈၉ abc", source=NumeralSystem.BURMESE,
                   target=NumeralSystem.KHMER) == "abc ០១២៣៤៥៦៧៨៩ abc"


def test_burmese_to_persian1():
    assert convert("၀၁၂၃၄၅၆၇၈၉", source=NumeralSystem.BURMESE, target=NumeralSystem.PERSIAN) == "۰۱۲۳۴۵۶۷۸۹"


def test_burmese_to_persian2():
    assert convert("abc ၀၁၂၃၄၅၆၇၈၉ abc", source=NumeralSystem.BURMESE,
                   target=NumeralSystem.PERSIAN) == "abc ۰۱۲۳۴۵۶۷۸۹ abc"


def test_burmese_to_tibetan1():
    assert convert("၀၁၂၃၄၅၆၇၈၉", source=NumeralSystem.BURMESE, target=NumeralSystem.TIBETAN) == "༠༡༢༣༤༥༦༧༨༩"


def test_burmese_to_tibetan2():
    assert convert("abc ၀၁၂၃၄၅၆၇၈၉ abc", source=NumeralSystem.BURMESE,
                   target=NumeralSystem.TIBETAN) == "abc ༠༡༢༣༤༥༦༧༨༩ abc"


def test_burmese_to_gujarati1():
    assert convert("၀၁၂၃၄၅၆၇၈၉", source=NumeralSystem.BURMESE, target=NumeralSystem.GUJARATI) == "૦૧૨૩૪૫૬૭૮૯"


def test_burmese_to_gujarati2():
    assert convert("abc ၀၁၂၃၄၅၆၇၈၉ abc", source=NumeralSystem.BURMESE,
                   target=NumeralSystem.GUJARATI) == "abc ૦૧૨૩૪૫૬૭૮૯ abc"


def test_burmese_to_odia1():
    assert convert("၀၁၂၃၄၅၆၇၈၉", source=NumeralSystem.BURMESE, target=NumeralSystem.ODIA) == "୦୧୨୩୪୫୬୭୮୯"


def test_burmese_to_odia2():
    assert convert("abc ၀၁၂၃၄၅၆၇၈၉ abc", source=NumeralSystem.BURMESE,
                   target=NumeralSystem.ODIA) == "abc ୦୧୨୩୪୫୬୭୮୯ abc"
