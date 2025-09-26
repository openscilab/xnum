# -*- coding: utf-8 -*-
"""XNum parameters and constants."""
from enum import Enum

XNUM_VERSION = "0.8"

ENGLISH_DIGITS = "0123456789"
ENGLISH_FULLWIDTH_DIGITS = "０１２３４５６７８９"
ENGLISH_SUBSCRIPT_DIGITS = "₀₁₂₃₄₅₆₇₈₉"
ENGLISH_SUPERSCRIPT_DIGITS = "⁰¹²³⁴⁵⁶⁷⁸⁹"
ENGLISH_DOUBLE_STRUCK_DIGITS = "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡"
ENGLISH_BOLD_DIGITS = "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"
ENGLISH_MONOSPACE_DIGITS = "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"
ENGLISH_SANS_SERIF_DIGITS = "𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫"
ENGLISH_SANS_SERIF_BOLD_DIGITS = "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
PERSIAN_DIGITS = "۰۱۲۳۴۵۶۷۸۹"
HINDI_DIGITS = "०१२३४५६७८९"
ARABIC_INDIC_DIGITS = "٠١٢٣٤٥٦٧٨٩"
BENGALI_DIGITS = "০১২৩৪৫৬৭৮৯"
THAI_DIGITS = "๐๑๒๓๔๕๖๗๘๙"
KHMER_DIGITS = "០១២៣៤៥៦៧៨៩"
BURMESE_DIGITS = "၀၁၂၃၄၅၆၇၈၉"
TIBETAN_DIGITS = "༠༡༢༣༤༥༦༧༨༩"
GUJARATI_DIGITS = "૦૧૨૩૪૫૬૭૮૯"
ODIA_DIGITS = "୦୧୨୩୪୫୬୭୮୯"
TELUGU_DIGITS = "౦౧౨౩౪౫౬౭౮౯"
KANNADA_DIGITS = "೦೧೨೩೪೫೬೭೮೯"
GURMUKHI_DIGITS = "੦੧੨੩੪੫੬੭੮੯"
LAO_DIGITS = "໐໑໒໓໔໕໖໗໘໙"
NKO_DIGITS = "߀߁߂߃߄߅߆߇߈߉"  # RTL
MONGOLIAN_DIGITS = "᠐᠑᠒᠓᠔᠕᠖᠗᠘᠙"
SINHALA_LITH_DIGITS = "෦෧෨෩෪෫෬෭෮෯"
MYANMAR_SHAN_DIGITS = "႐႑႒႓႔႕႖႗႘႙"
LIMBU_DIGITS = "᥆᥇᥈᥉᥊᥋᥌᥍᥎᥏"
VAI_DIGITS = "꘠꘡꘢꘣꘤꘥꘦꘧꘨꘩"
OL_CHIKI_DIGITS = "᱐᱑᱒᱓᱔᱕᱖᱗᱘᱙"
BALINESE_DIGITS = "᭐᭑᭒᭓᭔᭕᭖᭗᭘᭙"
NEW_TAI_LUE_DIGITS = "᧐᧑᧒᧓᧔᧕᧖᧗᧘᧙"
SAURASHTRA_DIGITS = "꣐꣑꣒꣓꣔꣕꣖꣗꣘꣙"
JAVANESE_DIGITS = "꧐꧑꧒꧓꧔꧕꧖꧗꧘꧙"
CHAM_DIGITS = "꩐꩑꩒꩓꩔꩕꩖꩗꩘꩙"
LEPCHA_DIGITS = "᱀᱁᱂᱃᱄᱅᱆᱇᱈᱉"
SUNDANESE_DIGITS = "᮰᮱᮲᮳᮴᮵᮶᮷᮸᮹"


NUMERAL_MAPS = {
    "english": ENGLISH_DIGITS,
    "english_fullwidth": ENGLISH_FULLWIDTH_DIGITS,
    "english_subscript": ENGLISH_SUBSCRIPT_DIGITS,
    "english_superscript": ENGLISH_SUPERSCRIPT_DIGITS,
    "english_double_struck": ENGLISH_DOUBLE_STRUCK_DIGITS,
    "english_bold": ENGLISH_BOLD_DIGITS,
    "english_monospace": ENGLISH_MONOSPACE_DIGITS,
    "english_sans_serif": ENGLISH_SANS_SERIF_DIGITS,
    "english_sans_serif_bold": ENGLISH_SANS_SERIF_BOLD_DIGITS,
    "persian": PERSIAN_DIGITS,
    "hindi": HINDI_DIGITS,
    "arabic_indic": ARABIC_INDIC_DIGITS,
    "bengali": BENGALI_DIGITS,
    "thai": THAI_DIGITS,
    "khmer": KHMER_DIGITS,
    "burmese": BURMESE_DIGITS,
    "tibetan": TIBETAN_DIGITS,
    "gujarati": GUJARATI_DIGITS,
    "odia": ODIA_DIGITS,
    "telugu": TELUGU_DIGITS,
    "kannada": KANNADA_DIGITS,
    "gurmukhi": GURMUKHI_DIGITS,
    "lao": LAO_DIGITS,
    "nko": NKO_DIGITS,
    "mongolian": MONGOLIAN_DIGITS,
    "sinhala_lith": SINHALA_LITH_DIGITS,
    "myanmar_shan": MYANMAR_SHAN_DIGITS,
    "limbu": LIMBU_DIGITS,
    "vai": VAI_DIGITS,
    "ol_chiki": OL_CHIKI_DIGITS,
    "balinese": BALINESE_DIGITS,
    "new_tai_lue": NEW_TAI_LUE_DIGITS,
    "saurashtra": SAURASHTRA_DIGITS,
    "javanese": JAVANESE_DIGITS,
    "cham": CHAM_DIGITS,
    "lepcha": LEPCHA_DIGITS,
    "sundanese": SUNDANESE_DIGITS,
}

ALL_DIGIT_MAPS = {}
for system, digits in NUMERAL_MAPS.items():
    for index, char in enumerate(digits):
        ALL_DIGIT_MAPS[char] = str(index)


class NumeralSystem(Enum):
    """Numeral System enum."""

    ENGLISH = "english"
    ENGLISH_FULLWIDTH = "english_fullwidth"
    ENGLISH_SUBSCRIPT = "english_subscript"
    ENGLISH_SUPERSCRIPT = "english_superscript"
    ENGLISH_DOUBLE_STRUCK = "english_double_struck"
    ENGLISH_BOLD = "english_bold"
    ENGLISH_MONOSPACE = "english_monospace"
    ENGLISH_SANS_SERIF = "english_sans_serif"
    ENGLISH_SANS_SERIF_BOLD = "english_sans_serif_bold"
    PERSIAN = "persian"
    HINDI = "hindi"
    ARABIC_INDIC = "arabic_indic"
    BENGALI = "bengali"
    THAI = "thai"
    KHMER = "khmer"
    BURMESE = "burmese"
    TIBETAN = "tibetan"
    GUJARATI = "gujarati"
    ODIA = "odia"
    TELUGU = "telugu"
    KANNADA = "kannada"
    GURMUKHI = "gurmukhi"
    LAO = "lao"
    NKO = "nko"
    MONGOLIAN = "mongolian"
    SINHALA_LITH = "sinhala_lith"
    MYANMAR_SHAN = "myanmar_shan"
    LIMBU = "limbu"
    VAI = "vai"
    OL_CHIKI = "ol_chiki"
    BALINESE = "balinese"
    NEW_TAI_LUE = "new_tai_lue"
    SAURASHTRA = "saurashtra"
    JAVANESE = "javanese"
    CHAM = "cham"
    LEPCHA = "lepcha"
    SUNDANESE = "sundanese"
    AUTO = "auto"


INVALID_SOURCE_MESSAGE = "Invalid value. `source` must be an instance of NumeralSystem enum."
INVALID_TARGET_MESSAGE1 = "Invalid value. `target` must be an instance of NumeralSystem enum."
INVALID_TARGET_MESSAGE2 = "Invalid value. `target` cannot be NumeralSystem.AUTO."
INVALID_TEXT_MESSAGE = "Invalid value. `text` must be a string."
