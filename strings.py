
def alphabet():
    return ['ภ', 'ถ', 'ค', 'ต', 'จ', 'ข', 'ช', 'ฎ', 'ฑ', 'พ', 'ธ', 'ณ',
            'ร', 'น', 'ญ', 'ย', 'ฐ', 'บ', 'ล', 'ฅ', 'ฃ', 'ฟ', 'ฆ', 'ห',
            'ฏ', 'ก', 'ด', 'ฌ', 'ษ', 'ศ', 'ส', 'ซ', 'ว', 'ง', 'ผ', 'ป',
            'ฉ', 'ฮ', 'อ', 'ท', 'ฒ', 'ม', 'ฬ', 'ฝ']


def vowels():
    return ["ุ", "ู", "ึ", "ไ", "ำ", "ะ", "ั", "ี", "๊", "โ", "เ", "็", "็", "๋",
            "่", "ิ", "ื", "ใ", "ฦ", "ฤ"]


# len แบบไม่นับสระ
def count_no_vowels(word):
    vowel_list = vowels()
    count = 0
    for char in word:
        if char not in vowel_list:
            count += 1
    return count


# len นับแต่สระ
def count_vowels_only(word):
    vowel_list = vowels()
    count = 0
    for char in word:
        if char in vowel_list:
            count += 1
    return count


class ThaiStr:

    def __init__(self, word):
        self.word = word
        self.len = len(word)
        self.thai_cons = count_no_vowels(word)
        self.thai_vows = count_vowels_only(word)
