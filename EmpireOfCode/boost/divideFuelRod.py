def disjoint(number):
    i = 1
    while i * (i + 1) / 2 < number:
        j, r, l = i, 0, []
        while r < number:
            t = j * (j + 1) / 2
            l.append(t)
            r += t
            if r == number:
                return l
            j += 1
        i += 1
    return []


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert disjoint(64) == [15, 21, 28], "1st example"
    assert disjoint(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert disjoint(225) == [105, 120], "1st example"
    assert disjoint(882) == [], "1st example"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")