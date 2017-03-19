from math import acos, pi


def checkio(a, b, c):
    if a + b <= c or abs(a - b) >= c:
        return [0, 0, 0]
    arr = [get_angle(a, b, c), get_angle(b, c, a), get_angle(c, a, b)]
    arr.sort()
    return arr


def get_angle(a, b, c):
    return round(acos((a ** 2 + b ** 2 - c ** 2) / 2 / a / b) / pi * 180)


if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "First"
    assert checkio(3, 4, 5) == [37, 53, 90], "Second"
    assert checkio(2, 2, 5) == [0, 0, 0], "Third"
