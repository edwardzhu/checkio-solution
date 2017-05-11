def reconstruct(number):
    f = fact(number)
    if len(f) == 0 or max(f) >= 10:
        return 0
    c2 = f.count(2)
    c8 = c2 // 3
    r2 = c2 % 3
    f = list(filter(lambda x: x != 2, f))
    f += [8]*c8
    c3 = f.count(3)
    c9 = c3 // 2
    r3  = c3 % 2
    f = list(filter(lambda x: x != 3, f))
    f += [9]*c9
    if r3 == 0 and r2 == 2:
        f += [4]
    elif r3 == 1 and r2 == 2:
        f += [2, 6]
    elif r3 == 1 and r2 == 1:
        f += [6]
    elif r3 == 1 and r2 == 0:
        f += [3]
    elif r3 == 0 and r2 == 1:
        f += [2]
    f = sorted(f)
    return int(''.join(map(str, f)))


def fact(number):
    result = []
    origin = number
    f = 2
    while f <= origin and f != number:
        if f >= 10:
            return []
        if origin % f == 0:
            result.append(f)
            origin /= f
        else:
            f += 1
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert reconstruct(1024) == 2888
    # assert reconstruct(20) == 45, "1st example"
    assert reconstruct(21) == 37, "2nd example"
    assert reconstruct(17) == 0, "3rd example"
    assert reconstruct(33) == 0, "4th example"
    assert reconstruct(3125) == 55555, "5th example"
    assert reconstruct(9973) == 0, "6th example"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")