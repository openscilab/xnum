import pytest
from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Arabic-Indic tests"
ARABIC_INDIC_DIGITS = "٠١٢٣٤٥٦٧٨٩"

CONVERSION_CASES = {
    NumeralSystem.ARABIC_INDIC: ARABIC_INDIC_DIGITS,
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
    NumeralSystem.TELUGU: "౦౧౨౩౪౫౬౭౮౯",
    NumeralSystem.KANNADA: "೦೧೨೩೪೫೬೭೮೯",
    NumeralSystem.GURMUKHI: "੦੧੨੩੪੫੬੭੮੯",
    NumeralSystem.LAO: "໐໑໒໓໔໕໖໗໘໙",
}


@pytest.mark.parametrize("target,expected", CONVERSION_CASES.items())
def test_arabic_indic_to_other_systems(target, expected):

    assert convert(
        ARABIC_INDIC_DIGITS,
        source=NumeralSystem.ARABIC_INDIC,
        target=target,
    ) == expected

    assert convert(
        f"abc {ARABIC_INDIC_DIGITS} abc",
        source=NumeralSystem.ARABIC_INDIC,
        target=target,
    ) == f"abc {expected} abc"
