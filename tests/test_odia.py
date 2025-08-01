from xnum import convert, NumeralSystem


TEST_CASE_NAME = "Odia tests"


def test_identity_conversion():
    assert convert("୦୧୨୩୪୫୬୭୮୯", source=NumeralSystem.ODIA, target=NumeralSystem.ODIA) == "୦୧୨୩୪୫୬୭୮୯"


def test_odia_to_english1():
    assert convert("୦୧୨୩୪୫୬୭୮୯", source=NumeralSystem.ODIA, target=NumeralSystem.ENGLISH) == "0123456789"


def test_odia_to_english2():
    assert convert("abc ୦୧୨୩୪୫୬୭୮୯ abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.ENGLISH) == "abc 0123456789 abc"


def test_odia_to_hindi1():
    assert convert("୦୧୨୩୪୫୬୭୮୯", source=NumeralSystem.ODIA, target=NumeralSystem.HINDI) == "०१२३४५६७८९"


def test_odia_to_hindi2():
    assert convert("abc ୦୧୨୩୪୫୬୭୮୯ abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.HINDI) == "abc ०१२३४५६७८९ abc"


def test_odia_to_arabic_indic1():
    assert convert("୦୧୨୩୪୫୬୭୮୯", source=NumeralSystem.ODIA, target=NumeralSystem.ARABIC_INDIC) == "٠١٢٣٤٥٦٧٨٩"


def test_odia_to_arabic_indic2():
    assert convert("abc ୦୧୨୩୪୫୬୭୮୯ abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.ARABIC_INDIC) == "abc ٠١٢٣٤٥٦٧٨٩ abc"


def test_odia_to_bengali1():
    assert convert("୦୧୨୩୪୫୬୭୮୯", source=NumeralSystem.ODIA, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"


def test_odia_to_bengali2():
    assert convert("abc ୦୧୨୩୪୫୬୭୮୯ abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.BENGALI) == "abc ০১২৩৪৫৬৭৮৯ abc"


def test_odia_to_thai1():
    assert convert("୦୧୨୩୪୫୬୭୮୯", source=NumeralSystem.ODIA, target=NumeralSystem.THAI) == "๐๑๒๓๔๕๖๗๘๙"


def test_odia_to_thai2():
    assert convert("abc ୦୧୨୩୪୫୬୭୮୯ abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.THAI) == "abc ๐๑๒๓๔๕๖๗๘๙ abc"


def test_odia_to_khmer1():
    assert convert("୦୧୨୩୪୫୬୭୮୯", source=NumeralSystem.ODIA, target=NumeralSystem.KHMER) == "០១២៣៤៥៦៧៨៩"


def test_odia_to_khmer2():
    assert convert("abc ୦୧୨୩୪୫୬୭୮୯ abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.KHMER) == "abc ០១២៣៤៥៦៧៨៩ abc"


def test_odia_to_burmese1():
    assert convert("୦୧୨୩୪୫୬୭୮୯", source=NumeralSystem.ODIA, target=NumeralSystem.BURMESE) == "၀၁၂၃၄၅၆၇၈၉"


def test_odia_to_burmese2():
    assert convert("abc ୦୧୨୩୪୫୬୭୮୯ abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.BURMESE) == "abc ၀၁၂၃၄၅၆၇၈၉ abc"


def test_odia_to_tibetan1():
    assert convert("୦୧୨୩୪୫୬୭୮୯", source=NumeralSystem.ODIA, target=NumeralSystem.TIBETAN) == "༠༡༢༣༤༥༦༧༨༩"


def test_odia_to_tibetan2():
    assert convert("abc ୦୧୨୩୪୫୬୭୮୯ abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.TIBETAN) == "abc ༠༡༢༣༤༥༦༧༨༩ abc"


def test_odia_to_gujarati1():
    assert convert("୦୧୨୩୪୫୬୭୮୯", source=NumeralSystem.ODIA, target=NumeralSystem.GUJARATI) == "૦૧૨૩૪૫૬૭૮૯"


def test_odia_to_gujarati2():
    assert convert("abc ୦୧୨୩୪୫୬୭୮୯ abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.GUJARATI) == "abc ૦૧૨૩૪૫૬૭૮૯ abc"
