import pytest
from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Persian tests"
PERSIAN_DIGITS = "۰۱۲۳۴۵۶۷۸۹"


CONVERSION_CASES = {
    NumeralSystem.ARABIC_INDIC: "٠١٢٣٤٥٦٧٨٩",
    NumeralSystem.ENGLISH: "0123456789",
    NumeralSystem.ENGLISH_FULLWIDTH: "０１２３４５６７８９",
    NumeralSystem.ENGLISH_SUBSCRIPT: "₀₁₂₃₄₅₆₇₈₉",
    NumeralSystem.ENGLISH_SUPERSCRIPT: "⁰¹²³⁴⁵⁶⁷⁸⁹",
    NumeralSystem.ENGLISH_DOUBLE_STRUCK: "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡",
    NumeralSystem.ENGLISH_BOLD: "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗",
    NumeralSystem.ENGLISH_SANS_SERIF: "𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫",
    NumeralSystem.PERSIAN: PERSIAN_DIGITS,
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
def test_persian_to_other_systems(target, expected):

    assert convert(
        PERSIAN_DIGITS,
        source=NumeralSystem.PERSIAN,
        target=target,
    ) == expected

    assert convert(
        f"abc {PERSIAN_DIGITS} abc",
        source=NumeralSystem.PERSIAN,
        target=target,
    ) == f"abc {expected} abc"
