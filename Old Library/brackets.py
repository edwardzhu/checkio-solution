def checkio(data):
    stack = []
    for ch in data:
        if ch == '{' or ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == '}':
            if len(stack) == 0:
                return False
            c = stack.pop()
            if c != '{':
                return False
        elif ch == ']':
            if len(stack) == 0:
                return False
            c = stack.pop()
            if c != '[':
                return False
        elif ch == ')':
            if len(stack) == 0:
                return False
            c = stack.pop()
            if c != '(':
                return False
    return len(stack) == 0

if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") is True, "Test1"
    assert checkio("{[(3+1)+2]+}") is True, "Test2"
    assert checkio("(3+{1-1)}") is False, "Test3"
    assert checkio("[1+1]+(2*2)-{3/3}") is True, "Test4"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") is False, "Test5"
