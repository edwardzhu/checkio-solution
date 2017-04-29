from fractions import Fraction


def divide_pie(groups):
    total = sum(abs(i) for i in groups)
    remaining = Fraction(total, total)
    for num in groups:
        remaining = remaining - Fraction(num, total) if num > 0 else remaining * (1 - Fraction(-num, total))
    return (remaining.numerator, remaining.denominator) if remaining.numerator != 0 else (0,1)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")