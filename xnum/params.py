# -*- coding: utf-8 -*-
"""XNum parameters and constants."""
from enum import Enum

XNUM_VERSION = "1.0"

ENGLISH_DIGITS = "0123456789"
ENGLISH_FULLWIDTH_DIGITS = "０１２３４５６７８９"
ENGLISH_SUBSCRIPT_DIGITS = "₀₁₂₃₄₅₆₇₈₉"
ENGLISH_SUPERSCRIPT_DIGITS = "⁰¹²³⁴⁵⁶⁷⁸⁹"
ENGLISH_DOUBLE_STRUCK_DIGITS = "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡"
ENGLISH_BOLD_DIGITS = "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"
ENGLISH_MONOSPACE_DIGITS = "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"
ENGLISH_SANS_SERIF_DIGITS = "𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫"
ENGLISH_SANS_SERIF_BOLD_DIGITS = "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"
ENGLISH_CIRCLED_DIGITS = "⓪①②③④⑤⑥⑦⑧⑨"
ENGLISH_DINGBAT_CIRCLED_SANS_SERIF_DIGITS = "🄋➀➁➂➃➄➅➆➇➈"
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
DIVES_AKURU_DIGITS = "𑥐𑥑𑥒𑥓𑥔𑥕𑥖𑥗𑥘𑥙"
MODI_DIGITS = "𑙐𑙑𑙒𑙓𑙔𑙕𑙖𑙗𑙘𑙙"
TAKRI_DIGITS = "𑛀𑛁𑛂𑛃𑛄𑛅𑛆𑛇𑛈𑛉"
NEWA_DIGITS = "𑑐𑑑𑑒𑑓𑑔𑑕𑑖𑑗𑑘𑑙"
TIRHUTA_DIGITS = "𑓐𑓑𑓒𑓓𑓔𑓕𑓖𑓗𑓘𑓙"
SHARADA_DIGITS = "𑇐𑇑𑇒𑇓𑇔𑇕𑇖𑇗𑇘𑇙"
KHUDAWADI_DIGITS = "𑋰𑋱𑋲𑋳𑋴𑋵𑋶𑋷𑋸𑋹"
CHAKMA_DIGITS = "𑄶𑄷𑄸𑄹𑄺𑄻𑄼𑄽𑄾𑄿"
SORA_SOMPENG_DIGITS = "𑃰𑃱𑃲𑃳𑃴𑃵𑃶𑃷𑃸𑃹"
HANIFI_ROHINGYA_DIGITS = "𐴰𐴱𐴲𐴳𐴴𐴵𐴶𐴷𐴸𐴹"
OSMANYA_DIGITS = "𐒠𐒡𐒢𐒣𐒤𐒥𐒦𐒧𐒨𐒩"
MEETEI_MAYEK_DIGITS = "꯰꯱꯲꯳꯴꯵꯶꯷꯸꯹"
KAYAH_LI_DIGITS = "꤀꤁꤂꤃꤄꤅꤆꤇꤈꤉"
GUNJALA_GONDI_DIGITS = "𑶠𑶡𑶢𑶣𑶤𑶥𑶦𑶧𑶨𑶩"
MASARAM_GONDI_DIGITS = "𑵐𑵑𑵒𑵓𑵔𑵕𑵖𑵗𑵘𑵙"
MRO_DIGITS = "𖩠𖩡𖩢𖩣𖩤𖩥𖩦𖩧𖩨𖩩"
WANCHO_DIGITS = "𞋰𞋱𞋲𞋳𞋴𞋵𞋶𞋷𞋸𞋹"
ADLAM_DIGITS = "𞥐𞥑𞥒𞥓𞥔𞥕𞥖𞥗𞥘𞥙"  # RTL

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
    "english_circled": ENGLISH_CIRCLED_DIGITS,
    "english_dingbat_circled_sans_serif": ENGLISH_DINGBAT_CIRCLED_SANS_SERIF_DIGITS,
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
    "dives_akuru": DIVES_AKURU_DIGITS,
    "modi": MODI_DIGITS,
    "takri": TAKRI_DIGITS,
    "newa": NEWA_DIGITS,
    "tirhuta": TIRHUTA_DIGITS,
    "sharada": SHARADA_DIGITS,
    "khudawadi": KHUDAWADI_DIGITS,
    "chakma": CHAKMA_DIGITS,
    "sora_sompeng": SORA_SOMPENG_DIGITS,
    "hanifi_rohingya": HANIFI_ROHINGYA_DIGITS,
    "osmanya": OSMANYA_DIGITS,
    "meetei_mayek": MEETEI_MAYEK_DIGITS,
    "kayah_li": KAYAH_LI_DIGITS,
    "gunjala_gondi": GUNJALA_GONDI_DIGITS,
    "masaram_gondi": MASARAM_GONDI_DIGITS,
    "mro": MRO_DIGITS,
    "wancho": WANCHO_DIGITS,
    "adlam": ADLAM_DIGITS,
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
    ENGLISH_CIRCLED = "english_circled"
    ENGLISH_DINGBAT_CIRCLED_SANS_SERIF = "english_dingbat_circled_sans_serif"
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
    DIVES_AKURU = "dives_akuru"
    MODI = "modi"
    TAKRI = "takri"
    NEWA = "newa"
    TIRHUTA = "tirhuta"
    SHARADA = "sharada"
    KHUDAWADI = "khudawadi"
    CHAKMA = "chakma"
    SORA_SOMPENG = "sora_sompeng"
    HANIFI_ROHINGYA = "hanifi_rohingya"
    OSMANYA = "osmanya"
    MEETEI_MAYEK = "meetei_mayek"
    KAYAH_LI = "kayah_li"
    GUNJALA_GONDI = "gunjala_gondi"
    MASARAM_GONDI = "masaram_gondi"
    MRO = "mro"
    WANCHO = "wancho"
    ADLAM = "adlam"
    AUTO = "auto"


INVALID_SOURCE_MESSAGE = "Invalid value. `source` must be an instance of NumeralSystem enum."
INVALID_TARGET_MESSAGE1 = "Invalid value. `target` must be an instance of NumeralSystem enum."
INVALID_TARGET_MESSAGE2 = "Invalid value. `target` cannot be NumeralSystem.AUTO."
INVALID_TEXT_MESSAGE = "Invalid value. `text` must be a string."
