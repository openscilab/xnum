import pytest
from xnum import convert, NumeralSystem

TEST_CASE_NAME = "Wancho tests"
WANCHO_DIGITS = "𞋰𞋱𞋲𞋳𞋴𞋵𞋶𞋷𞋸𞋹"


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
    NumeralSystem.WANCHO: WANCHO_DIGITS,
    NumeralSystem.ADLAM: "𞥐𞥑𞥒𞥓𞥔𞥕𞥖𞥗𞥘𞥙",
    NumeralSystem.TAI_THAM_HORA: "᪀᪁᪂᪃᪄᪅᪆᪇᪈᪉",
}


@pytest.mark.parametrize("target,expected", CONVERSION_CASES.items())
def test_wancho_to_other_systems(target, expected):

    assert convert(
        WANCHO_DIGITS,
        source=NumeralSystem.WANCHO,
        target=target,
    ) == expected

    assert convert(
        f"abc {WANCHO_DIGITS} abc",
        source=NumeralSystem.WANCHO,
        target=target,
    ) == f"abc {expected} abc"
