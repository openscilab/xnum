import pytest
from xnum import convert, NumeralSystem

TEST_CASE_NAME = "English tests"
ENGLISH_DIGITS = "0123456789"

CONVERSION_CASES = {
    NumeralSystem.ARABIC_INDIC: "٠١٢٣٤٥٦٧٨٩",
    NumeralSystem.ENGLISH: ENGLISH_DIGITS,
    NumeralSystem.PERSIAN: "۰۱۲۳۴۵۶۷۸۹",
    NumeralSystem.HINDI: "०१२३४५६७८९",
    NumeralSystem.BENGALI: "০১২৩৪৫৬৭৮৯",
    NumeralSystem.THAI: "๐๑๒๓๔๕๖๗๘๙",
    NumeralSystem.KHMER: "០១២៣៤៥៦៧៨៩",
    NumeralSystem.BURMESE: "၀၁၂၃၄၅၆၇၈၉",
    NumeralSystem.TIBETAN: "༠༡༢༣༤༥༦༧༨༩",
    NumeralSystem.GUJARATI: "૦૧૨૩૪૫૬૭૮૯",
    NumeralSystem.ODIA: "୦୧୨୩୪୫୬୭୮୯",
    NumeralSystem.TELUGU: "౦౧౨౩౪౫౬౭౮౯",
    NumeralSystem.KANNADA: "೦೧೨೩೪೫೬೭೮೯",
    NumeralSystem.GURMUKHI: "੦੧੨੩੪੫੬੭੮੯",
    NumeralSystem.LAO: "໐໑໒໓໔໕໖໗໘໙",
}


@pytest.mark.parametrize("target,expected", CONVERSION_CASES.items())
def test_english_to_other_systems(target, expected):

    assert convert(
        ENGLISH_DIGITS,
        source=NumeralSystem.ENGLISH,
        target=target,
    ) == expected

    assert convert(
        f"abc {ENGLISH_DIGITS} abc",
        source=NumeralSystem.ENGLISH,
        target=target,
    ) == f"abc {expected} abc"