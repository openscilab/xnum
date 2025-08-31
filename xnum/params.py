# -*- coding: utf-8 -*-
"""XNum parameters and constants."""
from enum import Enum

XNUM_VERSION = "0.5"

ENGLISH_DIGITS = "0123456789"
ENGLISH_FULLWIDTH_DIGITS = "０１２３４５６７８９"
ENGLISH_SUBSCRIPT_DIGITS = "₀₁₂₃₄₅₆₇₈₉"
ENGLISH_SUPERSCRIPT_DIGITS = "⁰¹²³⁴⁵⁶⁷⁸⁹"
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


NUMERAL_MAPS = {
    "english": ENGLISH_DIGITS,
    "english_fullwidth": ENGLISH_FULLWIDTH_DIGITS,
    "english_subscript": ENGLISH_SUBSCRIPT_DIGITS,
    "english_superscript": ENGLISH_SUPERSCRIPT_DIGITS,
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
    "lao": LAO_DIGITS
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
    AUTO = "auto"


INVALID_SOURCE_MESSAGE = "Invalid value. `source` must be an instance of NumeralSystem enum."
INVALID_TARGET_MESSAGE1 = "Invalid value. `target` must be an instance of NumeralSystem enum."
INVALID_TARGET_MESSAGE2 = "Invalid value. `target` cannot be NumeralSystem.AUTO."
INVALID_TEXT_MESSAGE = "Invalid value. `text` must be a string."
