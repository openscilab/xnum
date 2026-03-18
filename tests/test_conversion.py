import pytest
import xnum.params
from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Conversion tests"

INT_EXCEPTED_NUMERAL_SYSTEMS = [
    NumeralSystem.ENGLISH_SUBSCRIPT,
    NumeralSystem.ENGLISH_SUPERSCRIPT,
    NumeralSystem.ENGLISH_CIRCLED,
    NumeralSystem.ENGLISH_DINGBAT_CIRCLED_SANS_SERIF,
    NumeralSystem.ENGLISH_DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF,
    NumeralSystem.ENGLISH_KEYCAP,
    NumeralSystem.ENGLISH_EMOJI,
    NumeralSystem.ENGLISH_FULL_STOP,
    NumeralSystem.ENGLISH_COMMA,
    NumeralSystem.ENGLISH_SEGMENTED,
    NumeralSystem.WANCHO,
    NumeralSystem.DIVES_AKURU,
    NumeralSystem.NYIAKENG_PUACHUE_HMONG]

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
    NumeralSystem.ENGLISH_CIRCLED: "⓪①②③④⑤⑥⑦⑧⑨",
    NumeralSystem.ENGLISH_DINGBAT_CIRCLED_SANS_SERIF: "🄋➀➁➂➃➄➅➆➇➈",
    NumeralSystem.ENGLISH_DINGBAT_NEGATIVE_CIRCLED_SANS_SERIF: "🄌➊➋➌➍➎➏➐➑➒",
    NumeralSystem.ENGLISH_KEYCAP: "0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣",
    NumeralSystem.ENGLISH_EMOJI: "0️1️2️3️4️5️6️7️8️9️",
    NumeralSystem.ENGLISH_FULL_STOP: "🄀⒈⒉⒊⒋⒌⒍⒎⒏⒐",
    NumeralSystem.ENGLISH_COMMA: "🄁🄂🄃🄄🄅🄆🄇🄈🄉🄊",
    NumeralSystem.ENGLISH_SEGMENTED: "🯰🯱🯲🯳🯴🯵🯶🯷🯸🯹",
    NumeralSystem.PERSIAN: "۰۱۲۳۴۵۶۷۸۹",
    NumeralSystem.HINDI: "०१२३४५६७८९",
    NumeralSystem.BENGALI: "০১২৩৪৫৬৭৮৯",
    NumeralSystem.THAI: "๐๑๒๓๔๕๖๗๘๙",
    NumeralSystem.KHMER: "០១២៣៤៥៦៧៨៩",
    NumeralSystem.MYANMAR: "၀၁၂၃၄၅၆၇၈၉",
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
    NumeralSystem.DIVES_AKURU: "𑥐𑥑𑥒𑥓𑥔𑥕𑥖𑥗𑥘𑥙",
    NumeralSystem.MODI: "𑙐𑙑𑙒𑙓𑙔𑙕𑙖𑙗𑙘𑙙",
    NumeralSystem.TAKRI: "𑛀𑛁𑛂𑛃𑛄𑛅𑛆𑛇𑛈𑛉",
    NumeralSystem.NEWA: "𑑐𑑑𑑒𑑓𑑔𑑕𑑖𑑗𑑘𑑙",
    NumeralSystem.TIRHUTA: "𑓐𑓑𑓒𑓓𑓔𑓕𑓖𑓗𑓘𑓙",
    NumeralSystem.SHARADA: "𑇐𑇑𑇒𑇓𑇔𑇕𑇖𑇗𑇘𑇙",
    NumeralSystem.KHUDAWADI: "𑋰𑋱𑋲𑋳𑋴𑋵𑋶𑋷𑋸𑋹",
    NumeralSystem.CHAKMA: "𑄶𑄷𑄸𑄹𑄺𑄻𑄼𑄽𑄾𑄿",
    NumeralSystem.SORA_SOMPENG: "𑃰𑃱𑃲𑃳𑃴𑃵𑃶𑃷𑃸𑃹",
    NumeralSystem.HANIFI_ROHINGYA: "𐴰𐴱𐴲𐴳𐴴𐴵𐴶𐴷𐴸𐴹",
    NumeralSystem.OSMANYA: "𐒠𐒡𐒢𐒣𐒤𐒥𐒦𐒧𐒨𐒩",
    NumeralSystem.MEETEI_MAYEK: "꯰꯱꯲꯳꯴꯵꯶꯷꯸꯹",
    NumeralSystem.KAYAH_LI: "꤀꤁꤂꤃꤄꤅꤆꤇꤈꤉",
    NumeralSystem.GUNJALA_GONDI: "𑶠𑶡𑶢𑶣𑶤𑶥𑶦𑶧𑶨𑶩",
    NumeralSystem.MASARAM_GONDI: "𑵐𑵑𑵒𑵓𑵔𑵕𑵖𑵗𑵘𑵙",
    NumeralSystem.MRO: "𖩠𖩡𖩢𖩣𖩤𖩥𖩦𖩧𖩨𖩩",
    NumeralSystem.WANCHO: "𞋰𞋱𞋲𞋳𞋴𞋵𞋶𞋷𞋸𞋹",
    NumeralSystem.ADLAM: "𞥐𞥑𞥒𞥓𞥔𞥕𞥖𞥗𞥘𞥙",
    NumeralSystem.TAI_THAM_HORA: "᪀᪁᪂᪃᪄᪅᪆᪇᪈᪉",
    NumeralSystem.TAI_THAM_THAM: "᪐᪑᪒᪓᪔᪕᪖᪗᪘᪙",
    NumeralSystem.NYIAKENG_PUACHUE_HMONG: "𞅀𞅁𞅂𞅃𞅄𞅅𞅆𞅇𞅈𞅉",
    NumeralSystem.MALAYALAM: "൦൧൨൩൪൫൬൭൮൯",
    NumeralSystem.BRAHMI: "𑁦𑁧𑁨𑁩𑁪𑁫𑁬𑁭𑁮𑁯",
    NumeralSystem.MYANMAR_TAI_LAING: "꧰꧱꧲꧳꧴꧵꧶꧷꧸꧹",
    NumeralSystem.AHOM: "𑜰𑜱𑜲𑜳𑜴𑜵𑜶𑜷𑜸𑜹",
    NumeralSystem.WARANG_CITI: "𑣠𑣡𑣢𑣣𑣤𑣥𑣦𑣧𑣨𑣩",
    NumeralSystem.BHAIKSUKI: "𑱐𑱑𑱒𑱓𑱔𑱕𑱖𑱗𑱘𑱙",
    NumeralSystem.TAMIL: "௦௧௨௩௪௫௬௭௮௯",
    NumeralSystem.PAHAWH_HMONG: "𖭐𖭑𖭒𖭓𖭔𖭕𖭖𖭗𖭘𖭙",
    NumeralSystem.GARAY: '𐵀𐵁𐵂𐵃𐵄𐵅𐵆𐵇𐵈𐵉',
}

def test_numeral_system_length():
    for digits in xnum.params.NUMERAL_MAPS.values():
        assert len(digits) == 10


def test_numeral_system_digits():
    for system, digits in CONVERSION_CASES.items():
        attr_name = system.name + "_DIGITS"
        assert "".join(getattr(xnum.params, attr_name)) == digits
        if system not in INT_EXCEPTED_NUMERAL_SYSTEMS:
            assert list(map(int, digits)) == list(range(10))


@pytest.mark.parametrize("source,source_digits", CONVERSION_CASES.items())
@pytest.mark.parametrize("target,target_digits", CONVERSION_CASES.items())
def test_conversion_between_systems(source, source_digits, target, target_digits):
    assert convert(source_digits, source=source, target=target) == target_digits
    text = "abc {source_digits} abc".format(source_digits=source_digits)
    expected = "abc {target_digits} abc".format(target_digits=target_digits)
    assert convert(text, source=source, target=target) == expected
