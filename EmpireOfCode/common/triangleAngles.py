import math
def angles(a, b, c):
    if a + b <= c or abs(a-b) >= c:
        return [0, 0, 0]
    angleA = round(math.acos((b ** 2 + c ** 2 - a ** 2) / (2*b*c)) / math.pi * 180)
    angleB = round(math.acos((a ** 2 + c ** 2 - b ** 2) / (2*a*c)) / math.pi * 180)
    angleC = 180 - angleA - angleB
    return sorted([angleA, angleB, angleC])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It can not be a triangle"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")