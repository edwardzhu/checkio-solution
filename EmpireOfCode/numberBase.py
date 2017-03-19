def convert(str_number, radix):
    l = list(str_number)
    lens = len(l)
    result = 0
    for i in range(lens):
        v = ord(l[i]) - 55
        if v < 3 and int(l[i]) < radix:
            result += int(l[i]) * (radix ** (lens - i - 1))
        elif radix > v > 2:
            result += v * (radix ** (lens - i - 1))
        else:
            return -1
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert("AF", 16) == 175, "Hex"
    assert convert("101", 2) == 5, "Bin"
    assert convert("101", 5) == 26, "5 base"
    assert convert("Z", 36) == 35, "Z base"
    assert convert("AB", 10) == -1, "B > A > 10"
    assert convert("909", 9) == -1, "909"

    print("Use 'Check' to earn sweet rewards!")