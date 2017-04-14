def check_structure(pattern, structure, pattern_level=2):
    flag = convert(pattern, pattern_level)
    s = list(structure[::-1])
    if len(flag) > len(s):
        return False
    result = True
    for i in range(len(s)):
        if i >= len(flag):
            result &= match(0, s[i], pattern_level)
        else:
            result &= match(flag[i], s[i], pattern_level)
    return result


def convert(pattern, level):
    d = pattern
    result = []
    while d > 0:
        result.append(d % level)
        d = d // level
    return result


def match(flag, c, level):
    return (flag == 0 and 47 < ord(c) < 58) or (level == 2 and flag == 1 and 64 < ord(c.upper()) < 91) or (level > 2 and flag == 1 and 96 < ord(c) < 123) or (level > 2 and flag == 2 and 64 < ord(c) < 91) or (flag == 3 and c == " ")


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert check_structure(42, "12a0b3e4"), "42 is the answer"
    assert not check_structure(101, "ab23b4zz"), "one hundred plus one"
    assert check_structure(0, "478103487120470129"), "Any number"
    assert check_structure(127, "Checkio"), "Uppercase"
    assert not check_structure(7, "Hello"), "Only full match"
    assert not check_structure(8, "a"), "Too short command"
    assert check_structure(5, "H2O"), "Water"
    assert not check_structure(42, "C2H5OH"), "Yep, this is not the Answer"

    # Rank 2
    assert check_structure(1823, 'CheckiO', 3), "up and down"
    assert not check_structure(1826, 'CheckiO', 3), "wrong up and down"
    assert check_structure(66431, '9z1b2c4d6a7Z', 3), "Various"

    # Rank 3
    assert not check_structure(39294315, 'Kill Them ALL', 4), "Don't kill"
    assert not check_structure(29, 'aXz', 4), "A Z"
    assert check_structure(39294442, 'Feed Them ALL', 4), "Feed them"
    assert check_structure(2385166685525, 'C3PO and 300 spartans', 4), "C3PO"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")