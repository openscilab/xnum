from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Persian tests"
PERSIAN_DIGITS = "۰۱۲۳۴۵۶۷۸۹"


def test_identity_conversion():
    assert convert(PERSIAN_DIGITS, source=NumeralSystem.PERSIAN, target=NumeralSystem.PERSIAN) == PERSIAN_DIGITS


def test_persian_to_english1():
    assert convert(PERSIAN_DIGITS, source=NumeralSystem.PERSIAN, target=NumeralSystem.ENGLISH) == "0123456789"


def test_persian_to_english2():
    assert convert(f"abc {PERSIAN_DIGITS} abc", source=NumeralSystem.PERSIAN,
                   target=NumeralSystem.ENGLISH) == "abc 0123456789 abc"


def test_persian_to_hindi1():
    assert convert(PERSIAN_DIGITS, source=NumeralSystem.PERSIAN, target=NumeralSystem.HINDI) == "०१२३४५६७८९"


def test_persian_to_hindi2():
    assert convert(f"abc {PERSIAN_DIGITS} abc", source=NumeralSystem.PERSIAN,
                   target=NumeralSystem.HINDI) == "abc ०१२३४५६७८९ abc"


def test_persian_to_arabic_indic1():
    assert convert(PERSIAN_DIGITS, source=NumeralSystem.PERSIAN, target=NumeralSystem.ARABIC_INDIC) == "٠١٢٣٤٥٦٧٨٩"


def test_persian_to_arabic_indic2():
    assert convert(f"abc {PERSIAN_DIGITS} abc", source=NumeralSystem.PERSIAN,
                   target=NumeralSystem.ARABIC_INDIC) == "abc ٠١٢٣٤٥٦٧٨٩ abc"


def test_persian_to_bengali1():
    assert convert(PERSIAN_DIGITS, source=NumeralSystem.PERSIAN, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"


def test_persian_to_bengali2():
    assert convert(f"abc {PERSIAN_DIGITS} abc", source=NumeralSystem.PERSIAN,
                   target=NumeralSystem.BENGALI) == "abc ০১২৩৪৫৬৭৮৯ abc"


def test_persian_to_thai1():
    assert convert(PERSIAN_DIGITS, source=NumeralSystem.PERSIAN, target=NumeralSystem.THAI) == "๐๑๒๓๔๕๖๗๘๙"


def test_persian_to_thai2():
    assert convert(f"abc {PERSIAN_DIGITS} abc", source=NumeralSystem.PERSIAN,
                   target=NumeralSystem.THAI) == "abc ๐๑๒๓๔๕๖๗๘๙ abc"


def test_persian_to_khmer1():
    assert convert(PERSIAN_DIGITS, source=NumeralSystem.PERSIAN, target=NumeralSystem.KHMER) == "០១២៣៤៥៦៧៨៩"


def test_persian_to_khmer2():
    assert convert(f"abc {PERSIAN_DIGITS} abc", source=NumeralSystem.PERSIAN,
                   target=NumeralSystem.KHMER) == "abc ០១២៣៤៥៦៧៨៩ abc"


def test_persian_to_burmese1():
    assert convert(PERSIAN_DIGITS, source=NumeralSystem.PERSIAN, target=NumeralSystem.BURMESE) == "၀၁၂၃၄၅၆၇၈၉"


def test_persian_to_burmese2():
    assert convert(f"abc {PERSIAN_DIGITS} abc", source=NumeralSystem.PERSIAN,
                   target=NumeralSystem.BURMESE) == "abc ၀၁၂၃၄၅၆၇၈၉ abc"


def test_persian_to_tibetan1():
    assert convert(PERSIAN_DIGITS, source=NumeralSystem.PERSIAN, target=NumeralSystem.TIBETAN) == "༠༡༢༣༤༥༦༧༨༩"


def test_persian_to_tibetan2():
    assert convert(f"abc {PERSIAN_DIGITS} abc", source=NumeralSystem.PERSIAN,
                   target=NumeralSystem.TIBETAN) == "abc ༠༡༢༣༤༥༦༧༨༩ abc"


def test_persian_to_gujarati1():
    assert convert(PERSIAN_DIGITS, source=NumeralSystem.PERSIAN, target=NumeralSystem.GUJARATI) == "૦૧૨૩૪૫૬૭૮૯"


def test_persian_to_gujarati2():
    assert convert(f"abc {PERSIAN_DIGITS} abc", source=NumeralSystem.PERSIAN,
                   target=NumeralSystem.GUJARATI) == "abc ૦૧૨૩૪૫૬૭૮૯ abc"


def test_persian_to_odia1():
    assert convert(PERSIAN_DIGITS, source=NumeralSystem.PERSIAN, target=NumeralSystem.ODIA) == "୦୧୨୩୪୫୬୭୮୯"


def test_persian_to_odia2():
    assert convert(f"abc {PERSIAN_DIGITS} abc", source=NumeralSystem.PERSIAN,
                   target=NumeralSystem.ODIA) == "abc ୦୧୨୩୪୫୬୭୮୯ abc"


def test_persian_to_telugu1():
    assert convert(PERSIAN_DIGITS, source=NumeralSystem.PERSIAN, target=NumeralSystem.TELUGU) == "౦౧౨౩౪౫౬౭౮౯"


def test_persian_to_telugu2():
    assert convert(f"abc {PERSIAN_DIGITS} abc", source=NumeralSystem.PERSIAN,
                   target=NumeralSystem.TELUGU) == "abc ౦౧౨౩౪౫౬౭౮౯ abc"


def test_persian_to_kannada1():
    assert convert(PERSIAN_DIGITS, source=NumeralSystem.PERSIAN, target=NumeralSystem.KANNADA) == "೦೧೨೩೪೫೬೭೮೯"


def test_persian_to_kannada2():
    assert convert(f"abc {PERSIAN_DIGITS} abc", source=NumeralSystem.PERSIAN,
                   target=NumeralSystem.KANNADA) == "abc ೦೧೨೩೪೫೬೭೮೯ abc"


def test_persian_to_gurmukhi1():
    assert convert(PERSIAN_DIGITS, source=NumeralSystem.PERSIAN, target=NumeralSystem.GURMUKHI) == "੦੧੨੩੪੫੬੭੮੯"


def test_persian_to_gurmukhi2():
    assert convert(f"abc {PERSIAN_DIGITS} abc", source=NumeralSystem.PERSIAN, target=NumeralSystem.GURMUKHI) == "abc ੦੧੨੩੪੫੬੭੮੯ abc"


def test_persian_to_lao1():
    assert convert(PERSIAN_DIGITS, source=NumeralSystem.PERSIAN, target=NumeralSystem.LAO) == "໐໑໒໓໔໕໖໗໘໙"


def test_persian_to_lao2():
    assert convert(f"abc {PERSIAN_DIGITS} abc", source=NumeralSystem.PERSIAN, target=NumeralSystem.LAO) == "abc ໐໑໒໓໔໕໖໗໘໙ abc"
