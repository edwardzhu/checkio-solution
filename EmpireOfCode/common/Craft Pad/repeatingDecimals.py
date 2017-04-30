def convert(numerator, denominator):
    result = str(numerator // denominator) + "."
    r = numerator % denominator
    remaining = []
    quotient = []
    while r != 0 and r not in remaining:
        remaining.append(r)
        r *= 10
        quotient.append(r // denominator)
        r = r % denominator
    if r == 0:
        result += "".join(str(x) for x in quotient)
    else:
        index = remaining.index(r)
        result += "".join(str(x) for x in quotient[0:index])
        result += "(" + "".join(str(x) for x in quotient[index:len(quotient)]) + ")"
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"

    print("Earn cool rewards by using the 'Check' button!")