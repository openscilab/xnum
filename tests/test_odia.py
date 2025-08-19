from xnum import convert, NumeralSystem


TEST_CASE_NAME = "Odia tests"
ODIA_DIGITS = "୦୧୨୩୪୫୬୭୮୯"


def test_identity_conversion():
    assert convert(ODIA_DIGITS, source=NumeralSystem.ODIA, target=NumeralSystem.ODIA) == ODIA_DIGITS


def test_odia_to_english1():
    assert convert(ODIA_DIGITS, source=NumeralSystem.ODIA, target=NumeralSystem.ENGLISH) == "0123456789"


def test_odia_to_english2():
    assert convert(f"abc {ODIA_DIGITS} abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.ENGLISH) == "abc 0123456789 abc"


def test_odia_to_persian1():
    assert convert(ODIA_DIGITS, source=NumeralSystem.ODIA, target=NumeralSystem.PERSIAN) == "۰۱۲۳۴۵۶۷۸۹"


def test_odia_to_persian2():
    assert convert(f"abc {ODIA_DIGITS} abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.PERSIAN) == "abc ۰۱۲۳۴۵۶۷۸۹ abc"


def test_odia_to_hindi1():
    assert convert(ODIA_DIGITS, source=NumeralSystem.ODIA, target=NumeralSystem.HINDI) == "०१२३४५६७८९"


def test_odia_to_hindi2():
    assert convert(f"abc {ODIA_DIGITS} abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.HINDI) == "abc ०१२३४५६७८९ abc"


def test_odia_to_arabic_indic1():
    assert convert(ODIA_DIGITS, source=NumeralSystem.ODIA, target=NumeralSystem.ARABIC_INDIC) == "٠١٢٣٤٥٦٧٨٩"


def test_odia_to_arabic_indic2():
    assert convert(f"abc {ODIA_DIGITS} abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.ARABIC_INDIC) == "abc ٠١٢٣٤٥٦٧٨٩ abc"


def test_odia_to_bengali1():
    assert convert(ODIA_DIGITS, source=NumeralSystem.ODIA, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"


def test_odia_to_bengali2():
    assert convert(f"abc {ODIA_DIGITS} abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.BENGALI) == "abc ০১২৩৪৫৬৭৮৯ abc"


def test_odia_to_thai1():
    assert convert(ODIA_DIGITS, source=NumeralSystem.ODIA, target=NumeralSystem.THAI) == "๐๑๒๓๔๕๖๗๘๙"


def test_odia_to_thai2():
    assert convert(f"abc {ODIA_DIGITS} abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.THAI) == "abc ๐๑๒๓๔๕๖๗๘๙ abc"


def test_odia_to_khmer1():
    assert convert(ODIA_DIGITS, source=NumeralSystem.ODIA, target=NumeralSystem.KHMER) == "០១២៣៤៥៦៧៨៩"


def test_odia_to_khmer2():
    assert convert(f"abc {ODIA_DIGITS} abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.KHMER) == "abc ០១២៣៤៥៦៧៨៩ abc"


def test_odia_to_burmese1():
    assert convert(ODIA_DIGITS, source=NumeralSystem.ODIA, target=NumeralSystem.BURMESE) == "၀၁၂၃၄၅၆၇၈၉"


def test_odia_to_burmese2():
    assert convert(f"abc {ODIA_DIGITS} abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.BURMESE) == "abc ၀၁၂၃၄၅၆၇၈၉ abc"


def test_odia_to_tibetan1():
    assert convert(ODIA_DIGITS, source=NumeralSystem.ODIA, target=NumeralSystem.TIBETAN) == "༠༡༢༣༤༥༦༧༨༩"


def test_odia_to_tibetan2():
    assert convert(f"abc {ODIA_DIGITS} abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.TIBETAN) == "abc ༠༡༢༣༤༥༦༧༨༩ abc"


def test_odia_to_gujarati1():
    assert convert(ODIA_DIGITS, source=NumeralSystem.ODIA, target=NumeralSystem.GUJARATI) == "૦૧૨૩૪૫૬૭૮૯"


def test_odia_to_gujarati2():
    assert convert(f"abc {ODIA_DIGITS} abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.GUJARATI) == "abc ૦૧૨૩૪૫૬૭૮૯ abc"


def test_odia_to_telugu1():
    assert convert(ODIA_DIGITS, source=NumeralSystem.ODIA, target=NumeralSystem.TELUGU) == "౦౧౨౩౪౫౬౭౮౯"


def test_odia_to_telugu2():
    assert convert(f"abc {ODIA_DIGITS} abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.TELUGU) == "abc ౦౧౨౩౪౫౬౭౮౯ abc"


def test_odia_to_kannada1():
    assert convert(ODIA_DIGITS, source=NumeralSystem.ODIA, target=NumeralSystem.KANNADA) == "೦೧೨೩೪೫೬೭೮೯"


def test_odia_to_kannada2():
    assert convert(f"abc {ODIA_DIGITS} abc", source=NumeralSystem.ODIA,
                   target=NumeralSystem.KANNADA) == "abc ೦೧೨೩೪೫೬೭೮೯ abc"


def test_odia_to_gurmukhi1():
    assert convert(ODIA_DIGITS, source=NumeralSystem.ODIA, target=NumeralSystem.GURMUKHI) == "੦੧੨੩੪੫੬੭੮੯"


def test_odia_to_gurmukhi2():
    assert convert(f"abc {ODIA_DIGITS} abc", source=NumeralSystem.ODIA, target=NumeralSystem.GURMUKHI) == "abc ੦੧੨੩੪੫੬੭੮੯ abc"


def test_odia_to_lao1():
    assert convert(ODIA_DIGITS, source=NumeralSystem.ODIA, target=NumeralSystem.LAO) == "໐໑໒໓໔໕໖໗໘໙"


def test_odia_to_lao2():
    assert convert(f"abc {ODIA_DIGITS} abc", source=NumeralSystem.ODIA, target=NumeralSystem.LAO) == "abc ໐໑໒໓໔໕໖໗໘໙ abc"
