import pytest
from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Bengali tests"
BENGALI_DIGITS = "০১২৩৪৫৬৭৮৯"

CONVERSION_CASES = {
    NumeralSystem.ARABIC_INDIC: "٠١٢٣٤٥٦٧٨٩",
    NumeralSystem.ENGLISH: "0123456789",
    NumeralSystem.ENGLISH_FULLWIDTH: "０１２３４５６７８９",
    NumeralSystem.ENGLISH_SUBSCRIPT: "₀₁₂₃₄₅₆₇₈₉",
    NumeralSystem.ENGLISH_SUPERSCRIPT: "⁰¹²³⁴⁵⁶⁷⁸⁹",
    NumeralSystem.PERSIAN: "۰۱۲۳۴۵۶۷۸۹",
    NumeralSystem.HINDI: "०१२३४५६७८९",
    NumeralSystem.BENGALI: BENGALI_DIGITS,
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
def test_bengali_to_other_systems(target, expected):

    assert convert(
        BENGALI_DIGITS,
        source=NumeralSystem.BENGALI,
        target=target,
    ) == expected

    assert convert(
        f"abc {BENGALI_DIGITS} abc",
        source=NumeralSystem.BENGALI,
        target=target,
    ) == f"abc {expected} abc"
