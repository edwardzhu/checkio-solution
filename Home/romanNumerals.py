SIG = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
VALUE = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


def checkio(number):
    result = ''
    idx = 0
    while number > 0:
        if VALUE[idx] > number:
            idx += 1
            continue
        else:
            result += SIG[idx]
            number -= VALUE[idx]
    return result


if __name__ == "__main__":
    assert checkio(6) == 'VI', "Case 1"
    assert checkio(76) == 'LXXVI', "Case 2"