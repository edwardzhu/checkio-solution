import re
def checkio(sentense):
    word = re.split("\s+", sentense)
    result = ''
    for w in word:
        result += w + " "
    return result.strip()


if __name__ == '__main__':
    assert checkio('I  like   python') == "I like python", 'Test1'
    assert checkio('No double  whitespaces') == "No double whitespaces", "Test2"
    assert checkio('Normal text with whitespaces') == 'Normal text with whitespaces', 'Test3'
    assert checkio('Triple   spaces,   It   is   not   good.') == 'Triple spaces, It is not good.', 'Test4'
    assert checkio("One, Two,  Three,   Four,    Five,      Six.") == 'One, Two, Three, Four, Five, Six.', "Test5"

    assert checkio('a  b  c   d    e') == 'a b c d e', 'Random1'
    assert checkio('b   b   b') == 'b b b', 'Random2'
    assert checkio('a b  c   d    e') == 'a b c d e', 'Random3'