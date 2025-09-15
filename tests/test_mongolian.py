import pytest
from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Mongolian tests"
MONGOLIAN_DIGITS = "᠐᠑᠒᠓᠔᠕᠖᠗᠘᠙"


CONVERSION_CASES = {
    NumeralSystem.ARABIC_INDIC: "٠١٢٣٤٥٦٧٨٩",
    NumeralSystem.ENGLISH: "0123456789",
    NumeralSystem.ENGLISH_FULLWIDTH: "０１２３４５６７８９",
    NumeralSystem.ENGLISH_SUBSCRIPT: "₀₁₂₃₄₅₆₇₈₉",
    NumeralSystem.ENGLISH_SUPERSCRIPT: "⁰¹²³⁴⁵⁶⁷⁸⁹",
    NumeralSystem.ENGLISH_DOUBLE_STRUCK: "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡",
    NumeralSystem.ENGLISH_BOLD: "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗",
    NumeralSystem.ENGLISH_MONOSPACE: "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿",
    NumeralSystem.ENGLISH_SANS_SERIF: "𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫",
    NumeralSystem.ENGLISH_SANS_SERIF_BOLD: "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵",
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
    NumeralSystem.NKO: "߀߁߂߃߄߅߆߇߈߉",
    NumeralSystem.MONGOLIAN: MONGOLIAN_DIGITS,
    NumeralSystem.SINHALA_LITH: "෦෧෨෩෪෫෬෭෮෯",
    NumeralSystem.MYANMAR_SHAN: "႐႑႒႓႔႕႖႗႘႙",
    NumeralSystem.LIMBU: "᥆᥇᥈᥉᥊᥋᥌᥍᥎᥏",
}


@pytest.mark.parametrize("target,expected", CONVERSION_CASES.items())
def test_mongolian_to_other_systems(target, expected):

    assert convert(
        MONGOLIAN_DIGITS,
        source=NumeralSystem.MONGOLIAN,
        target=target,
    ) == expected

    assert convert(
        f"abc {MONGOLIAN_DIGITS} abc",
        source=NumeralSystem.MONGOLIAN,
        target=target,
    ) == f"abc {expected} abc"
