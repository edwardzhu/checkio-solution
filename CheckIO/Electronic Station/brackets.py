BRACKET_PAIRS = ['()', '{}', '[]', '<>']
OPEN_BRACKETS = {a for a, _ in BRACKET_PAIRS}
CLOSE_BRACKETS = {b: a for a, b in BRACKET_PAIRS}

def checkio(data):
    stack = []
    for ch in data:
        if ch in OPEN_BRACKETS:
            stack.append(ch)
        elif ch in CLOSE_BRACKETS:
            if not stack or stack[-1] != CLOSE_BRACKETS[ch]:
                return False
            stack.pop()
    return not stack

if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") is True, "Test1"
    assert checkio("{[(3+1)+2]+}") is True, "Test2"
    assert checkio("(3+{1-1)}") is False, "Test3"
    assert checkio("[1+1]+(2*2)-{3/3}") is True, "Test4"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") is False, "Test5"
