# -*- coding: utf-8 -*-
"""XNum parameters and constants."""
from enum import Enum

XNUM_VERSION = "0.1"

ENGLISH_DIGITS = "0123456789"
PERSIAN_DIGITS = "۰۱۲۳۴۵۶۷۸۹"
HINDI_DIGITS   = "०१२३४५६७८९"
ARABIC_INDIC_DIGITS = "٠١٢٣٤٥٦٧٨٩"
BENGALI_DIGITS = "০১২৩৪৫৬৭৮৯"

NUMERAL_MAPS = {
    "english": ENGLISH_DIGITS,
    "persian": PERSIAN_DIGITS,
    "hindi": HINDI_DIGITS,
    "arabic_indic": ARABIC_INDIC_DIGITS,
    "bengali": BENGALI_DIGITS
}

ALL_DIGIT_MAPS = {}
for system, digits in NUMERAL_MAPS.items():
    for index, char in enumerate(digits):
        ALL_DIGIT_MAPS[char] = str(index)

class NumeralSystem(Enum):
    ENGLISH = "english"
    PERSIAN = "persian"
    HINDI = "hindi"
    ARABIC_INDIC = "arabic_indic"
    BENGALI = "bengali"
    AUTO = "auto"

INVALID_SOURCE_MESSAGE = "Invalid value. `source` must be an instance of NumeralSystem enum."
INVALID_TARGET_MESSAGE = "Invalid value. `target` must be an instance of NumeralSystem enum."
INVALID_TEXT_MESSAGE = "Invalid value. `text` must be a string."
