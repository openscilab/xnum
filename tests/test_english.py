import pytest
from xnum import convert, NumeralSystem

TEST_CASE_NAME = "English tests"
ENGLISH_DIGITS = "0123456789"
ENGLISH_FULLWIDTH_DIGITS = "０１２３４５６７８９"
ENGLISH_SUBSCRIPT_DIGITS = "₀₁₂₃₄₅₆₇₈₉"
ENGLISH_SUPERSCRIPT_DIGITS = "⁰¹²³⁴⁵⁶⁷⁸⁹"
ENGLISH_DOUBLE_STRUCK_DIGITS = "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡"

CONVERSION_CASES = {
    NumeralSystem.ARABIC_INDIC: "٠١٢٣٤٥٦٧٨٩",
    NumeralSystem.ENGLISH: ENGLISH_DIGITS,
    NumeralSystem.ENGLISH_FULLWIDTH: ENGLISH_FULLWIDTH_DIGITS,
    NumeralSystem.ENGLISH_SUBSCRIPT: ENGLISH_SUBSCRIPT_DIGITS,
    NumeralSystem.ENGLISH_SUPERSCRIPT: ENGLISH_SUPERSCRIPT_DIGITS,
    NumeralSystem.ENGLISH_DOUBLE_STRUCK: ENGLISH_DOUBLE_STRUCK_DIGITS,
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

    assert convert(
        ENGLISH_FULLWIDTH_DIGITS,
        source=NumeralSystem.ENGLISH_FULLWIDTH,
        target=target,
    ) == expected

    assert convert(
        f"abc {ENGLISH_FULLWIDTH_DIGITS} abc",
        source=NumeralSystem.ENGLISH_FULLWIDTH,
        target=target,
    ) == f"abc {expected} abc"

    assert convert(
        ENGLISH_SUBSCRIPT_DIGITS,
        source=NumeralSystem.ENGLISH_SUBSCRIPT,
        target=target,
    ) == expected

    assert convert(
        f"abc {ENGLISH_SUBSCRIPT_DIGITS} abc",
        source=NumeralSystem.ENGLISH_SUBSCRIPT,
        target=target,
    ) == f"abc {expected} abc"

    assert convert(
        ENGLISH_SUPERSCRIPT_DIGITS,
        source=NumeralSystem.ENGLISH_SUPERSCRIPT,
        target=target,
    ) == expected

    assert convert(f"abc {ENGLISH_SUPERSCRIPT_DIGITS} abc",
                   source=NumeralSystem.ENGLISH_SUPERSCRIPT,
                   target=target,
                   ) == f"abc {expected} abc"

    assert convert(
        ENGLISH_DOUBLE_STRUCK_DIGITS,
        source=NumeralSystem.ENGLISH_DOUBLE_STRUCK,
        target=target,) == expected

    assert convert(f
                   "abc {ENGLISH_DOUBLE_STRUCK_DIGITS} abc",
                   source=NumeralSystem.ENGLISH_DOUBLE_STRUCK,
                   target=target,) == f"abc {expected} abc"
