# -*- coding: utf-8 -*-
"""XNum parameters and constants."""
from enum import Enum

XNUM_VERSION = "1.2"

ENGLISH_DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ENGLISH_FULLWIDTH_DIGITS = ['０', '１', '２', '３', '４', '５', '６', '７', '８', '９']
ENGLISH_SUBSCRIPT_DIGITS = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']
ENGLISH_SUPERSCRIPT_DIGITS = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
ENGLISH_DOUBLE_STRUCK_DIGITS = ['𝟘', '𝟙', '𝟚', '𝟛', '𝟜', '𝟝', '𝟞', '𝟟', '𝟠', '𝟡']
ENGLISH_BOLD_DIGITS = ['𝟎', '𝟏', '𝟐', '𝟑', '𝟒', '𝟓', '𝟔', '𝟕', '𝟖', '𝟗']
ENGLISH_MONOSPACE_DIGITS = ['𝟶', '𝟷', '𝟸', '𝟹', '𝟺', '𝟻', '𝟼', '𝟽', '𝟾', '𝟿']
ENGLISH_SANS_SERIF_DIGITS = ['𝟢', '𝟣', '𝟤', '𝟥', '𝟦', '𝟧', '𝟨', '𝟩', '𝟪', '𝟫']
ENGLISH_SANS_SERIF_BOLD_DIGITS = ['𝟬', '𝟭', '𝟮', '𝟯', '𝟰', '𝟱', '𝟲', '𝟳', '𝟴', '𝟵']
ENGLISH_CIRCLED_DIGITS = ['⓪', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨']
ENGLISH_DINGBAT_CIRCLED_SANS_SERIF_DIGITS = ['🄋', '➀', '➁', '➂', '➃', '➄', '➅', '➆', '➇', '➈']
ENGLISH_DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGITS = ['🄌', '➊', '➋', '➌', '➍', '➎', '➏', '➐', '➑', '➒']
ENGLISH_KEYCAP_DIGITS = ['0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']
ENGLISH_EMOJI_DIGITS = ['0️', '1️', '2️', '3️', '4️', '5️', '6️', '7️', '8️', '9️']
PERSIAN_DIGITS = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']
HINDI_DIGITS = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९']
ARABIC_INDIC_DIGITS = ['٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩']
BENGALI_DIGITS = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']
THAI_DIGITS = ['๐', '๑', '๒', '๓', '๔', '๕', '๖', '๗', '๘', '๙']
KHMER_DIGITS = ['០', '១', '២', '៣', '៤', '៥', '៦', '៧', '៨', '៩']
BURMESE_DIGITS = ['၀', '၁', '၂', '၃', '၄', '၅', '၆', '၇', '၈', '၉']
TIBETAN_DIGITS = ['༠', '༡', '༢', '༣', '༤', '༥', '༦', '༧', '༨', '༩']
GUJARATI_DIGITS = ['૦', '૧', '૨', '૩', '૪', '૫', '૬', '૭', '૮', '૯']
ODIA_DIGITS = ['୦', '୧', '୨', '୩', '୪', '୫', '୬', '୭', '୮', '୯']
TELUGU_DIGITS = ['౦', '౧', '౨', '౩', '౪', '౫', '౬', '౭', '౮', '౯']
KANNADA_DIGITS = ['೦', '೧', '೨', '೩', '೪', '೫', '೬', '೭', '೮', '೯']
GURMUKHI_DIGITS = ['੦', '੧', '੨', '੩', '੪', '੫', '੬', '੭', '੮', '੯']
LAO_DIGITS = ['໐', '໑', '໒', '໓', '໔', '໕', '໖', '໗', '໘', '໙']
NKO_DIGITS = ['߀', '߁', '߂', '߃', '߄', '߅', '߆', '߇', '߈', '߉']  # RTL
MONGOLIAN_DIGITS = ['᠐', '᠑', '᠒', '᠓', '᠔', '᠕', '᠖', '᠗', '᠘', '᠙']
SINHALA_LITH_DIGITS = ['෦', '෧', '෨', '෩', '෪', '෫', '෬', '෭', '෮', '෯']
MYANMAR_SHAN_DIGITS = ['႐', '႑', '႒', '႓', '႔', '႕', '႖', '႗', '႘', '႙']
LIMBU_DIGITS = ['᥆', '᥇', '᥈', '᥉', '᥊', '᥋', '᥌', '᥍', '᥎', '᥏']
VAI_DIGITS = ['꘠', '꘡', '꘢', '꘣', '꘤', '꘥', '꘦', '꘧', '꘨', '꘩']
OL_CHIKI_DIGITS = ['᱐', '᱑', '᱒', '᱓', '᱔', '᱕', '᱖', '᱗', '᱘', '᱙']
BALINESE_DIGITS = ['᭐', '᭑', '᭒', '᭓', '᭔', '᭕', '᭖', '᭗', '᭘', '᭙']
NEW_TAI_LUE_DIGITS = ['᧐', '᧑', '᧒', '᧓', '᧔', '᧕', '᧖', '᧗', '᧘', '᧙']
SAURASHTRA_DIGITS = ['꣐', '꣑', '꣒', '꣓', '꣔', '꣕', '꣖', '꣗', '꣘', '꣙']
JAVANESE_DIGITS = ['꧐', '꧑', '꧒', '꧓', '꧔', '꧕', '꧖', '꧗', '꧘', '꧙']
CHAM_DIGITS = ['꩐', '꩑', '꩒', '꩓', '꩔', '꩕', '꩖', '꩗', '꩘', '꩙']
LEPCHA_DIGITS = ['᱀', '᱁', '᱂', '᱃', '᱄', '᱅', '᱆', '᱇', '᱈', '᱉']
SUNDANESE_DIGITS = ['᮰', '᮱', '᮲', '᮳', '᮴', '᮵', '᮶', '᮷', '᮸', '᮹']
DIVES_AKURU_DIGITS = ['𑥐', '𑥑', '𑥒', '𑥓', '𑥔', '𑥕', '𑥖', '𑥗', '𑥘', '𑥙']
MODI_DIGITS = ['𑙐', '𑙑', '𑙒', '𑙓', '𑙔', '𑙕', '𑙖', '𑙗', '𑙘', '𑙙']
TAKRI_DIGITS = ['𑛀', '𑛁', '𑛂', '𑛃', '𑛄', '𑛅', '𑛆', '𑛇', '𑛈', '𑛉']
NEWA_DIGITS = ['𑑐', '𑑑', '𑑒', '𑑓', '𑑔', '𑑕', '𑑖', '𑑗', '𑑘', '𑑙']
TIRHUTA_DIGITS = ['𑓐', '𑓑', '𑓒', '𑓓', '𑓔', '𑓕', '𑓖', '𑓗', '𑓘', '𑓙']
SHARADA_DIGITS = ['𑇐', '𑇑', '𑇒', '𑇓', '𑇔', '𑇕', '𑇖', '𑇗', '𑇘', '𑇙']
KHUDAWADI_DIGITS = ['𑋰', '𑋱', '𑋲', '𑋳', '𑋴', '𑋵', '𑋶', '𑋷', '𑋸', '𑋹']
CHAKMA_DIGITS = ['𑄶', '𑄷', '𑄸', '𑄹', '𑄺', '𑄻', '𑄼', '𑄽', '𑄾', '𑄿']
SORA_SOMPENG_DIGITS = ['𑃰', '𑃱', '𑃲', '𑃳', '𑃴', '𑃵', '𑃶', '𑃷', '𑃸', '𑃹']
HANIFI_ROHINGYA_DIGITS = ['𐴰', '𐴱', '𐴲', '𐴳', '𐴴', '𐴵', '𐴶', '𐴷', '𐴸', '𐴹']
OSMANYA_DIGITS = ['𐒠', '𐒡', '𐒢', '𐒣', '𐒤', '𐒥', '𐒦', '𐒧', '𐒨', '𐒩']
MEETEI_MAYEK_DIGITS = ['꯰', '꯱', '꯲', '꯳', '꯴', '꯵', '꯶', '꯷', '꯸', '꯹']
KAYAH_LI_DIGITS = ['꤀', '꤁', '꤂', '꤃', '꤄', '꤅', '꤆', '꤇', '꤈', '꤉']
GUNJALA_GONDI_DIGITS = ['𑶠', '𑶡', '𑶢', '𑶣', '𑶤', '𑶥', '𑶦', '𑶧', '𑶨', '𑶩']
MASARAM_GONDI_DIGITS = ['𑵐', '𑵑', '𑵒', '𑵓', '𑵔', '𑵕', '𑵖', '𑵗', '𑵘', '𑵙']
MRO_DIGITS = ['𖩠', '𖩡', '𖩢', '𖩣', '𖩤', '𖩥', '𖩦', '𖩧', '𖩨', '𖩩']
WANCHO_DIGITS = ['𞋰', '𞋱', '𞋲', '𞋳', '𞋴', '𞋵', '𞋶', '𞋷', '𞋸', '𞋹']
ADLAM_DIGITS = ['𞥐', '𞥑', '𞥒', '𞥓', '𞥔', '𞥕', '𞥖', '𞥗', '𞥘', '𞥙']  # RTL
TAI_THAM_HORA_DIGITS = ['᪀', '᪁', '᪂', '᪃', '᪄', '᪅', '᪆', '᪇', '᪈', '᪉']
TAI_THAM_THAM_DIGITS = ['᪐', '᪑', '᪒', '᪓', '᪔', '᪕', '᪖', '᪗', '᪘', '᪙']
NYIAKENG_PUACHUE_HMONG_DIGITS = ['𞅀', '𞅁', '𞅂', '𞅃', '𞅄', '𞅅', '𞅆', '𞅇', '𞅈', '𞅉']

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
    "english_dingbat_negative_circled_sans_serif": ENGLISH_DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF_DIGITS,
    "english_keycap": ENGLISH_KEYCAP_DIGITS,
    "english_emoji": ENGLISH_EMOJI_DIGITS,
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
    "tai_tham_hora": TAI_THAM_HORA_DIGITS,
    "tai_tham_tham": TAI_THAM_THAM_DIGITS,
    "nyiakeng_puachue_hmong": NYIAKENG_PUACHUE_HMONG_DIGITS,
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
    ENGLISH_DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF = "english_dingbat_negative_circled_sans_serif"
    ENGLISH_KEYCAP = "english_keycap"
    ENGLISH_EMOJI = "english_emoji"
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
    TAI_THAM_HORA = "tai_tham_hora"
    TAI_THAM_THAM = "tai_tham_tham"
    NYIAKENG_PUACHUE_HMONG = "nyiakeng_puachue_hmong"
    AUTO = "auto"


INVALID_SOURCE_MESSAGE = "Invalid value. `source` must be an instance of NumeralSystem enum."
INVALID_TARGET_MESSAGE1 = "Invalid value. `target` must be an instance of NumeralSystem enum."
INVALID_TARGET_MESSAGE2 = "Invalid value. `target` cannot be NumeralSystem.AUTO."
INVALID_TEXT_MESSAGE = "Invalid value. `text` must be a string."
