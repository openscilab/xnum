from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Telugu tests"

TELUGU_DIGITS = "౦౧౨౩౪౫౬౭౮౯"

def test_identity_conversion():
    assert convert(TELUGU_DIGITS, source=NumeralSystem.TELUGU, target=NumeralSystem.TELUGU) == TELUGU_DIGITS

def test_telugu_to_english():
    assert convert(TELUGU_DIGITS, source=NumeralSystem.TELUGU, target=NumeralSystem.ENGLISH) == "0123456789"

def test_telugu_to_english_mixed():
    assert convert(f"abc {TELUGU_DIGITS} abc", source=NumeralSystem.TELUGU, target=NumeralSystem.ENGLISH) == "abc 0123456789 abc"

def test_telugu_to_persian():
    assert convert(TELUGU_DIGITS, source=NumeralSystem.TELUGU, target=NumeralSystem.PERSIAN) == "۰۱۲۳۴۵۶۷۸۹"

def test_telugu_to_persian_mixed():
    assert convert(f"abc {TELUGU_DIGITS} abc", source=NumeralSystem.TELUGU, target=NumeralSystem.PERSIAN) == "abc ۰۱۲۳۴۵۶۷۸۹ abc"

def test_telugu_to_hindi():
    assert convert(TELUGU_DIGITS, source=NumeralSystem.TELUGU, target=NumeralSystem.HINDI) == "०१२३४५६७८९"

def test_telugu_to_hindi_mixed():
    assert convert(f"abc {TELUGU_DIGITS} abc", source=NumeralSystem.TELUGU, target=NumeralSystem.HINDI) == "abc ०१२३४५६७८९ abc"

def test_telugu_to_arabic_indic():
    assert convert(TELUGU_DIGITS, source=NumeralSystem.TELUGU, target=NumeralSystem.ARABIC_INDIC) == "٠١٢٣٤٥٦٧٨٩"

def test_telugu_to_arabic_indic_mixed():
    assert convert(f"abc {TELUGU_DIGITS} abc", source=NumeralSystem.TELUGU, target=NumeralSystem.ARABIC_INDIC) == "abc ٠١٢٣٤٥٦٧٨٩ abc"

def test_telugu_to_bengali():
    assert convert(TELUGU_DIGITS, source=NumeralSystem.TELUGU, target=NumeralSystem.BENGALI) == "০১২৩৪৫৬৭৮৯"

def test_telugu_to_bengali_mixed():
    assert convert(f"abc {TELUGU_DIGITS} abc", source=NumeralSystem.TELUGU, target=NumeralSystem.BENGALI) == "abc ০১২৩৪৫৬৭৮৯ abc"

def test_telugu_to_thai():
    assert convert(TELUGU_DIGITS, source=NumeralSystem.TELUGU, target=NumeralSystem.THAI) == "๐๑๒๓๔๕๖๗๘๙"

def test_telugu_to_thai_mixed():
    assert convert(f"abc {TELUGU_DIGITS} abc", source=NumeralSystem.TELUGU, target=NumeralSystem.THAI) == "abc ๐๑๒๓๔๕๖๗๘๙ abc"

def test_telugu_to_khmer():
    assert convert(TELUGU_DIGITS, source=NumeralSystem.TELUGU, target=NumeralSystem.KHMER) == "០១២៣៤៥៦៧៨៩"

def test_telugu_to_khmer_mixed():
    assert convert(f"abc {TELUGU_DIGITS} abc", source=NumeralSystem.TELUGU, target=NumeralSystem.KHMER) == "abc ០១២៣៤៥៦៧៨៩ abc"

def test_telugu_to_burmese():
    assert convert(TELUGU_DIGITS, source=NumeralSystem.TELUGU, target=NumeralSystem.BURMESE) == "၀၁၂၃၄၅၆၇၈၉"

def test_telugu_to_burmese_mixed():
    assert convert(f"abc {TELUGU_DIGITS} abc", source=NumeralSystem.TELUGU, target=NumeralSystem.BURMESE) == "abc ၀၁၂၃၄၅၆၇၈၉ abc"

def test_telugu_to_tibetan():
    assert convert(TELUGU_DIGITS, source=NumeralSystem.TELUGU, target=NumeralSystem.TIBETAN) == "༠༡༢༣༤༥༦༧༨༩"

def test_telugu_to_tibetan_mixed():
    assert convert(f"abc {TELUGU_DIGITS} abc", source=NumeralSystem.TELUGU, target=NumeralSystem.TIBETAN) == "abc ༠༡༢༣༤༥༦༧༨༩ abc"

def test_telugu_to_gujarati():
    assert convert(TELUGU_DIGITS, source=NumeralSystem.TELUGU, target=NumeralSystem.GUJARATI) == "૦૧૨૩૪૫૬૭૮૯"

def test_telugu_to_gujarati_mixed():
    assert convert(f"abc {TELUGU_DIGITS} abc", source=NumeralSystem.TELUGU, target=NumeralSystem.GUJARATI) == "abc ૦૧૨૩૪૫૬૭૮૯ abc"

def test_telugu_to_odia():
    assert convert(TELUGU_DIGITS, source=NumeralSystem.TELUGU, target=NumeralSystem.ODIA) == "୦୧୨୩୪୫୬୭୮୯"

def test_telugu_to_odia_mixed():
    assert convert(f"abc {TELUGU_DIGITS} abc", source=NumeralSystem.TELUGU, target=NumeralSystem.ODIA) == "abc ୦୧୨୩୪୫୬୭୮୯ abc"

def test_telugu_to_kannada():
    assert convert(TELUGU_DIGITS, source=NumeralSystem.TELUGU, target=NumeralSystem.KANNADA) == "೦೧೨೩೪೫೬೭೮೯"

def test_telugu_to_kannada_mixed():
    assert convert(f"abc {TELUGU_DIGITS} abc", source=NumeralSystem.TELUGU, target=NumeralSystem.KANNADA) == "abc ೦೧೨೩೪೫೬೭೮೯ abc"
