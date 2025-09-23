import pytest
import xnum.params
from xnum import convert, NumeralSystem

TEST_CASE_NAME = "English tests"
ENGLISH_DIGITS = "0123456789"
ENGLISH_FULLWIDTH_DIGITS = "０１２３４５６７８９"
ENGLISH_SUBSCRIPT_DIGITS = "₀₁₂₃₄₅₆₇₈₉"
ENGLISH_SUPERSCRIPT_DIGITS = "⁰¹²³⁴⁵⁶⁷⁸⁹"
ENGLISH_DOUBLE_STRUCK_DIGITS = "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡"
ENGLISH_BOLD_DIGITS = "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"
ENGLISH_MONOSPACE_DIGITS = "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"
ENGLISH_SANS_SERIF_DIGITS = "𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫"
ENGLISH_SANS_SERIF_BOLD_DIGITS = "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"

CONVERSION_CASES = {
    NumeralSystem.ARABIC_INDIC: "٠١٢٣٤٥٦٧٨٩",
    NumeralSystem.ENGLISH: ENGLISH_DIGITS,
    NumeralSystem.ENGLISH_FULLWIDTH: ENGLISH_FULLWIDTH_DIGITS,
    NumeralSystem.ENGLISH_SUBSCRIPT: ENGLISH_SUBSCRIPT_DIGITS,
    NumeralSystem.ENGLISH_SUPERSCRIPT: ENGLISH_SUPERSCRIPT_DIGITS,
    NumeralSystem.ENGLISH_DOUBLE_STRUCK: ENGLISH_DOUBLE_STRUCK_DIGITS,
    NumeralSystem.ENGLISH_BOLD: ENGLISH_BOLD_DIGITS,
    NumeralSystem.ENGLISH_MONOSPACE: ENGLISH_MONOSPACE_DIGITS,
    NumeralSystem.ENGLISH_SANS_SERIF: ENGLISH_SANS_SERIF_DIGITS,
    NumeralSystem.ENGLISH_SANS_SERIF_BOLD: ENGLISH_SANS_SERIF_BOLD_DIGITS,
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
    NumeralSystem.MONGOLIAN: "᠐᠑᠒᠓᠔᠕᠖᠗᠘᠙",
    NumeralSystem.SINHALA_LITH: "෦෧෨෩෪෫෬෭෮෯",
    NumeralSystem.MYANMAR_SHAN: "႐႑႒႓႔႕႖႗႘႙",
    NumeralSystem.LIMBU: "᥆᥇᥈᥉᥊᥋᥌᥍᥎᥏",
    NumeralSystem.VAI: "꘠꘡꘢꘣꘤꘥꘦꘧꘨꘩",
    NumeralSystem.OL_CHIKI: "᱐᱑᱒᱓᱔᱕᱖᱗᱘᱙",
    NumeralSystem.BALINESE: "᭐᭑᭒᭓᭔᭕᭖᭗᭘᭙",
    NumeralSystem.NEW_TAI_LUE: "᧐᧑᧒᧓᧔᧕᧖᧗᧘᧙",
    NumeralSystem.SAURASHTRA: "꣐꣑꣒꣓꣔꣕꣖꣗꣘꣙",
    NumeralSystem.JAVANESE: "꧐꧑꧒꧓꧔꧕꧖꧗꧘꧙",
    NumeralSystem.CHAM: "꩐꩑꩒꩓꩔꩕꩖꩗꩘꩙",
    NumeralSystem.LEPCHA: "᱀᱁᱂᱃᱄᱅᱆᱇᱈᱉",
    NumeralSystem.SUNDANESE: "᮰᮱᮲᮳᮴᮵᮶᮷᮸᮹",
}


def test_english_digits():

    assert ENGLISH_DIGITS == xnum.params.ENGLISH_DIGITS
    assert list(map(int, ENGLISH_DIGITS)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert ENGLISH_FULLWIDTH_DIGITS == xnum.params.ENGLISH_FULLWIDTH_DIGITS
    assert list(map(int, ENGLISH_FULLWIDTH_DIGITS)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert ENGLISH_DOUBLE_STRUCK_DIGITS == xnum.params.ENGLISH_DOUBLE_STRUCK_DIGITS
    assert list(map(int, ENGLISH_DOUBLE_STRUCK_DIGITS)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert ENGLISH_BOLD_DIGITS == xnum.params.ENGLISH_BOLD_DIGITS
    assert list(map(int, ENGLISH_BOLD_DIGITS)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert ENGLISH_MONOSPACE_DIGITS == xnum.params.ENGLISH_MONOSPACE_DIGITS
    assert list(map(int, ENGLISH_MONOSPACE_DIGITS)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert ENGLISH_SANS_SERIF_DIGITS == xnum.params.ENGLISH_SANS_SERIF_DIGITS
    assert list(map(int, ENGLISH_SANS_SERIF_DIGITS)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert ENGLISH_SANS_SERIF_BOLD_DIGITS == xnum.params.ENGLISH_SANS_SERIF_BOLD_DIGITS
    assert list(map(int, ENGLISH_SANS_SERIF_BOLD_DIGITS)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


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

    assert convert(
        f"abc {ENGLISH_DOUBLE_STRUCK_DIGITS} abc",
        source=NumeralSystem.ENGLISH_DOUBLE_STRUCK,
        target=target,) == f"abc {expected} abc"

    assert convert(
        ENGLISH_BOLD_DIGITS,
        source=NumeralSystem.ENGLISH_BOLD,
        target=target, ) == expected

    assert convert(
        f"abc {ENGLISH_BOLD_DIGITS} abc", source=NumeralSystem.ENGLISH_BOLD, target=target,) == f"abc {expected} abc"

    assert convert(
        ENGLISH_MONOSPACE_DIGITS,
        source=NumeralSystem.ENGLISH_MONOSPACE,
        target=target,
    ) == expected

    assert convert(f"abc {ENGLISH_MONOSPACE_DIGITS} abc",
                   source=NumeralSystem.ENGLISH_MONOSPACE,
                   target=target,
                   ) == f"abc {expected} abc"

    assert convert(
        ENGLISH_SANS_SERIF_DIGITS,
        source=NumeralSystem.ENGLISH_SANS_SERIF,
        target=target,
    ) == expected

    assert convert(
        f"abc {ENGLISH_SANS_SERIF_DIGITS} abc",
        source=NumeralSystem.ENGLISH_SANS_SERIF,
        target=target,
    ) == f"abc {expected} abc"

    assert convert(
        ENGLISH_SANS_SERIF_BOLD_DIGITS,
        source=NumeralSystem.ENGLISH_SANS_SERIF_BOLD,
        target=target,
    ) == expected

    assert convert(
        f"abc {ENGLISH_SANS_SERIF_BOLD_DIGITS} abc",
        source=NumeralSystem.ENGLISH_SANS_SERIF_BOLD,
        target=target,
    ) == f"abc {expected} abc"
