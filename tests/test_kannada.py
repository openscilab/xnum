from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Kannada tests"
KANNADA_DIGITS = "೦೧೨೩೪೫೬೭೮೯"


def test_identity_conversion():
    assert convert(KANNADA_DIGITS, source=NumeralSystem.KANNADA, target=NumeralSystem.KANNADA) == "೦೧೨೩೪೫೬೭೮೯"


def test_kannada_to_english1():
    assert convert(KANNADA_DIGITS, source=NumeralSystem.KANNADA, target=NumeralSystem.ENGLISH) == "0123456789"


def test_kannada_to_english2():
    assert convert(f"abc {KANNADA_DIGITS} abc", source=NumeralSystem.KANNADA,
                   target=NumeralSystem.ENGLISH) == "abc 0123456789 abc"


def test_kannada_to_persian1():
    assert convert(KANNADA_DIGITS, source=NumeralSystem.KANNADA, target=NumeralSystem.PERSIAN) == "۰۱۲۳۴۵۶۷۸۹"


def test_kannada_to_persian2():
    assert convert(f"abc {KANNADA_DIGITS} abc", source=NumeralSystem.KANNADA,
                   target=NumeralSystem.PERSIAN) == "abc ۰۱۲۳۴۵۶۷۸۹ abc"


def test_kannada_to_hindi1():
    assert convert(KANNADA_DIGITS, source=NumeralSystem.KANNADA, target=NumeralSystem.HINDI) == "०१२३४५६७८९"


def test_kannada_to_hindi2():
    assert convert(f"abc {KANNADA_DIGITS} abc", source=NumeralSystem.KANNADA,
                   target=NumeralSystem.HINDI) == "abc ०१२३४५६७८९ abc"


def test_kannada_to_arabic_indic1():
    assert convert(KANNADA_DIGITS, source=NumeralSystem.KANNADA, target=NumeralSystem.ARABIC_INDIC) == "٠١٢٣٤٥٦٧٨٩"


def test_kannada_to_arabic_indic2():
    assert convert(f"abc {KANNADA_DIGITS} abc", source=NumeralSystem.KANNADA,
                   target=NumeralSystem.ARABIC_INDIC) == "abc ٠١٢٣٤٥٦٧٨٩ abc"


def test_kannada_to_bengali1():
    assert convert(KANNADA_DIGITS, source=NumeralSystem.KANNADA, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"


def test_kannada_to_bengali2():
    assert convert(f"abc {KANNADA_DIGITS} abc", source=NumeralSystem.KANNADA,
                   target=NumeralSystem.BENGALI) == "abc ০১২৩৪৫৬৭৮৯ abc"


def test_kannada_to_thai1():
    assert convert(KANNADA_DIGITS, source=NumeralSystem.KANNADA, target=NumeralSystem.THAI) == "๐๑๒๓๔๕๖๗๘๙"


def test_kannada_to_thai2():
    assert convert(f"abc {KANNADA_DIGITS} abc", source=NumeralSystem.KANNADA,
                   target=NumeralSystem.THAI) == "abc ๐๑๒๓๔๕๖๗๘๙ abc"


def test_kannada_to_khmer1():
    assert convert(KANNADA_DIGITS, source=NumeralSystem.KANNADA, target=NumeralSystem.KHMER) == "០១២៣៤៥៦៧៨៩"


def test_kannada_to_khmer2():
    assert convert(f"abc {KANNADA_DIGITS} abc", source=NumeralSystem.KANNADA,
                   target=NumeralSystem.KHMER) == "abc ០១២៣៤៥៦៧៨៩ abc"


def test_kannada_to_burmese1():
    assert convert(KANNADA_DIGITS, source=NumeralSystem.KANNADA, target=NumeralSystem.BURMESE) == "၀၁၂၃၄၅၆၇၈၉"


def test_kannada_to_burmese2():
    assert convert(f"abc {KANNADA_DIGITS} abc", source=NumeralSystem.KANNADA,
                   target=NumeralSystem.BURMESE) == "abc ၀၁၂၃၄၅၆၇၈၉ abc"


def test_kannada_to_tibetan1():
    assert convert(KANNADA_DIGITS, source=NumeralSystem.KANNADA, target=NumeralSystem.TIBETAN) == "༠༡༢༣༤༥༦༧༨༩"


def test_kannada_to_tibetan2():
    assert convert(f"abc {KANNADA_DIGITS} abc", source=NumeralSystem.KANNADA, target=NumeralSystem.TIBETAN) == "abc ༠༡༢༣༤༥༦༧༨༩ abc"


def test_kannada_to_gujarati1():
    assert convert(KANNADA_DIGITS, source=NumeralSystem.KANNADA, target=NumeralSystem.GUJARATI) == "૦૧૨૩૪૫૬૭૮૯"


def test_kannada_to_gujarati2():
    assert convert(f"abc {KANNADA_DIGITS} abc", source=NumeralSystem.KANNADA,
                   target=NumeralSystem.GUJARATI) == "abc ૦૧૨૩૪૫૬૭૮૯ abc"


def test_kannada_to_odia1():
    assert convert(KANNADA_DIGITS, source=NumeralSystem.KANNADA, target=NumeralSystem.ODIA) == "୦୧୨୩୪୫୬୭୮୯"


def test_kannada_to_odia2():
    assert convert(f"abc {KANNADA_DIGITS} abc", source=NumeralSystem.KANNADA,
                   target=NumeralSystem.ODIA) == "abc ୦୧୨୩୪୫୬୭୮୯ abc"


def test_kannada_to_telugu1():
    assert convert(KANNADA_DIGITS, source=NumeralSystem.KANNADA, target=NumeralSystem.TELUGU) == "౦౧౨౩౪౫౬౭౮౯"


def test_kannada_to_telugu2():
    assert convert(f"abc {KANNADA_DIGITS} abc", source=NumeralSystem.KANNADA,
                   target=NumeralSystem.TELUGU) == "abc ౦౧౨౩౪౫౬౭౮౯ abc"


def test_kannada_to_gurmukhi1():
    assert convert(KANNADA_DIGITS, source=NumeralSystem.KANNADA, target=NumeralSystem.GURMUKHI) == "੦੧੨੩੪੫੬੭੮੯"


def test_kannada_to_gurmukhi2():
    assert convert(f"abc {KANNADA_DIGITS} abc", source=NumeralSystem.KANNADA, target=NumeralSystem.GURMUKHI) == "abc ੦੧੨੩੪੫੬੭੮੯ abc"


def test_kannada_to_lao1():
    assert convert(KANNADA_DIGITS, source=NumeralSystem.KANNADA, target=NumeralSystem.LAO) == "໐໑໒໓໔໕໖໗໘໙"


def test_kannada_to_lao2():
    assert convert(f"abc {KANNADA_DIGITS} abc", source=NumeralSystem.KANNADA, target=NumeralSystem.LAO) == "abc ໐໑໒໓໔໕໖໗໘໙ abc"
