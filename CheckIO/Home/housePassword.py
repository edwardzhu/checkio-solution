def checkio(data):
    if len(data) < 10:
        return False
    num, upper, lower = False, False, False

    for c in data:
        num |= c.isnumeric()
        upper |= c.isupper()
        lower |= c.islower()

    return num and upper and lower


if __name__ == '__main__':
    assert checkio('A1213pokl') == False, 'First'
    assert checkio('bAse730onE4') == True, 'Second'
    assert checkio('asasasasasasasaas') == False, 'Third'
    assert checkio('QWERTYqwerty') == False, 'Fourth'
    assert checkio('123456123456') == False, 'Fifth'
    assert checkio('QwErTy911poqqqq') == True, 'Sixth'
    print('All ok')