import pytest
from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Telugu tests"
TELUGU_DIGITS = "౦౧౨౩౪౫౬౭౮౯"


CONVERSION_CASES = {
    NumeralSystem.ARABIC_INDIC: "٠١٢٣٤٥٦٧٨٩",
    NumeralSystem.ENGLISH: "0123456789",
    NumeralSystem.ENGLISH_FULLWIDTH: "０１２３４５６７８９",
    NumeralSystem.ENGLISH_SUBSCRIPT: "₀₁₂₃₄₅₆₇₈₉",
    NumeralSystem.ENGLISH_SUPERSCRIPT: "⁰¹²³⁴⁵⁶⁷⁸⁹",
    NumeralSystem.PERSIAN: "۰۱۲۳۴۵۶۷۸۹",
    NumeralSystem.HINDI: "०१२३४५६७८९",
    NumeralSystem.BENGALI: "০১২৩৪৫৬৭৮৯",
    NumeralSystem.THAI: "๐๑๒๓๔๕๖๗๘๙",
    NumeralSystem.KHMER: "០១២៣៤៥៦៧៨៩",
    NumeralSystem.BURMESE: "၀၁၂၃၄၅၆၇၈၉",
    NumeralSystem.TIBETAN: "༠༡༢༣༤༥༦༧༨༩",
    NumeralSystem.GUJARATI: "૦૧૨૩૪૫૬૭૮૯",
    NumeralSystem.ODIA: "୦୧୨୩୪୫୬୭୮୯",
    NumeralSystem.TELUGU: TELUGU_DIGITS,
    NumeralSystem.KANNADA: "೦೧೨೩೪೫೬೭೮೯",
    NumeralSystem.GURMUKHI: "੦੧੨੩੪੫੬੭੮੯",
    NumeralSystem.LAO: "໐໑໒໓໔໕໖໗໘໙",
}


@pytest.mark.parametrize("target,expected", CONVERSION_CASES.items())
def test_telugu_to_other_systems(target, expected):

    assert convert(
        TELUGU_DIGITS,
        source=NumeralSystem.TELUGU,
        target=target,
    ) == expected

    assert convert(
        f"abc {TELUGU_DIGITS} abc",
        source=NumeralSystem.TELUGU,
        target=target,
    ) == f"abc {expected} abc"
