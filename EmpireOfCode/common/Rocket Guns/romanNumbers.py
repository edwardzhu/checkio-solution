SIG = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
VALUE = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


def roman(number):
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


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert roman(6) == 'VI', '6'
    assert roman(76) == 'LXXVI', '76'
    assert roman(499) == 'CDXCIX', '499'
    assert roman(3888) == 'MMMDCCCLXXXVIII', '3888'
    print("Earn cool rewards by using the 'Check' button!")