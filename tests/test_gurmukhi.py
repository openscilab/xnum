from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Gurmukhi tests"
GURMUKHI_DIGITS = "੦੧੨੩੪੫੬੭੮੯"


def test_identity_conversion():
    assert convert(GURMUKHI_DIGITS, source=NumeralSystem.GURMUKHI, target=NumeralSystem.GURMUKHI) == GURMUKHI_DIGITS


def test_gurmukhi_to_english1():
    assert convert(GURMUKHI_DIGITS, source=NumeralSystem.GURMUKHI, target=NumeralSystem.ENGLISH) == "0123456789"


def test_gurmukhi_to_english2():
    assert convert(f"abc {GURMUKHI_DIGITS} abc", source=NumeralSystem.GURMUKHI,
                   target=NumeralSystem.ENGLISH) == "abc 0123456789 abc"


def test_gurmukhi_to_persian1():
    assert convert(GURMUKHI_DIGITS, source=NumeralSystem.GURMUKHI, target=NumeralSystem.PERSIAN) == "۰۱۲۳۴۵۶۷۸۹"


def test_gurmukhi_to_persian2():
    assert convert(f"abc {GURMUKHI_DIGITS} abc", source=NumeralSystem.GURMUKHI,
                   target=NumeralSystem.PERSIAN) == "abc ۰۱۲۳۴۵۶۷۸۹ abc"


def test_gurmukhi_to_hindi1():
    assert convert(GURMUKHI_DIGITS, source=NumeralSystem.GURMUKHI, target=NumeralSystem.HINDI) == "०१२३४५६७८९"


def test_gurmukhi_to_hindi2():
    assert convert(f"abc {GURMUKHI_DIGITS} abc", source=NumeralSystem.GURMUKHI,
                   target=NumeralSystem.HINDI) == "abc ०१२३४५६७८९ abc"


def test_gurmukhi_to_arabic_indic1():
    assert convert(GURMUKHI_DIGITS, source=NumeralSystem.GURMUKHI, target=NumeralSystem.ARABIC_INDIC) == "٠١٢٣٤٥٦٧٨٩"


def test_gurmukhi_to_arabic_indic2():
    assert convert(f"abc {GURMUKHI_DIGITS} abc", source=NumeralSystem.GURMUKHI,
                   target=NumeralSystem.ARABIC_INDIC) == "abc ٠١٢٣٤٥٦٧٨٩ abc"


def test_gurmukhi_to_bengali1():
    assert convert(GURMUKHI_DIGITS, source=NumeralSystem.GURMUKHI, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"


def test_gurmukhi_to_bengali2():
    assert convert(f"abc {GURMUKHI_DIGITS} abc", source=NumeralSystem.GURMUKHI,
                   target=NumeralSystem.BENGALI) == "abc ০১২৩৪৫৬৭৮৯ abc"


def test_gurmukhi_to_thai1():
    assert convert(GURMUKHI_DIGITS, source=NumeralSystem.GURMUKHI, target=NumeralSystem.THAI) == "๐๑๒๓๔๕๖๗๘๙"


def test_gurmukhi_to_thai2():
    assert convert(f"abc {GURMUKHI_DIGITS} abc", source=NumeralSystem.GURMUKHI,
                   target=NumeralSystem.THAI) == "abc ๐๑๒๓๔๕๖๗๘๙ abc"


def test_gurmukhi_to_khmer1():
    assert convert(GURMUKHI_DIGITS, source=NumeralSystem.GURMUKHI, target=NumeralSystem.KHMER) == "០១២៣៤៥៦៧៨៩"


def test_gurmukhi_to_khmer2():
    assert convert(f"abc {GURMUKHI_DIGITS} abc", source=NumeralSystem.GURMUKHI,
                   target=NumeralSystem.KHMER) == "abc ០១២៣៤៥៦៧៨៩ abc"


def test_gurmukhi_to_burmese1():
    assert convert(GURMUKHI_DIGITS, source=NumeralSystem.GURMUKHI, target=NumeralSystem.BURMESE) == "၀၁၂၃၄၅၆၇၈၉"


def test_gurmukhi_to_burmese2():
    assert convert(f"abc {GURMUKHI_DIGITS} abc", source=NumeralSystem.GURMUKHI,
                   target=NumeralSystem.BURMESE) == "abc ၀၁၂၃၄၅၆၇၈၉ abc"


def test_gurmukhi_to_tibetan1():
    assert convert(GURMUKHI_DIGITS, source=NumeralSystem.GURMUKHI, target=NumeralSystem.TIBETAN) == "༠༡༢༣༤༥༦༧༨༩"


def test_gurmukhi_to_tibetan2():
    assert convert(f"abc {GURMUKHI_DIGITS} abc", source=NumeralSystem.GURMUKHI,
                   target=NumeralSystem.TIBETAN) == "abc ༠༡༢༣༤༥༦༧༨༩ abc"


def test_gurmukhi_to_gujarati1():
    assert convert(GURMUKHI_DIGITS, source=NumeralSystem.GURMUKHI, target=NumeralSystem.GUJARATI) == "૦૧૨૩૪૫૬૭૮૯"


def test_gurmukhi_to_gujarati2():
    assert convert(f"abc {GURMUKHI_DIGITS} abc", source=NumeralSystem.GURMUKHI,
                   target=NumeralSystem.GUJARATI) == "abc ૦૧૨૩૪૫૬૭૮૯ abc"


def test_gurmukhi_to_odia1():
    assert convert(GURMUKHI_DIGITS, source=NumeralSystem.GURMUKHI, target=NumeralSystem.ODIA) == "୦୧୨୩୪୫୬୭୮୯"


def test_gurmukhi_to_odia2():
    assert convert(f"abc {GURMUKHI_DIGITS} abc", source=NumeralSystem.GURMUKHI,
                   target=NumeralSystem.ODIA) == "abc ୦୧୨୩୪୫୬୭୮୯ abc"


def test_gurmukhi_to_telugu1():
    assert convert(GURMUKHI_DIGITS, source=NumeralSystem.GURMUKHI, target=NumeralSystem.TELUGU) == "౦౧౨౩౪౫౬౭౮౯"


def test_gurmukhi_to_telugu2():
    assert convert(f"abc {GURMUKHI_DIGITS} abc", source=NumeralSystem.GURMUKHI,
                   target=NumeralSystem.TELUGU) == "abc ౦౧౨౩౪౫౬౭౮౯ abc"


def test_gurmukhi_to_kannada1():
    assert convert(GURMUKHI_DIGITS, source=NumeralSystem.GURMUKHI, target=NumeralSystem.KANNADA) == "೦೧೨೩೪೫೬೭೮೯"


def test_gurmukhi_to_kannada2():
    assert convert(f"abc {GURMUKHI_DIGITS} abc", source=NumeralSystem.GURMUKHI,
                   target=NumeralSystem.KANNADA) == "abc ೦೧೨೩೪೫೬೭೮೯ abc"


def test_gurmukhi_to_lao1():
    assert convert(GURMUKHI_DIGITS, source=NumeralSystem.GURMUKHI, target=NumeralSystem.LAO) == "໐໑໒໓໔໕໖໗໘໙"


def test_gurmukhi_to_lao2():
    assert convert(f"abc {GURMUKHI_DIGITS} abc", source=NumeralSystem.GURMUKHI,
                   target=NumeralSystem.LAO) == "abc ໐໑໒໓໔໕໖໗໘໙ abc"
