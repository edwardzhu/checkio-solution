golf = lambda p:(len(p)>9)&(p.lower()>p>p.upper())&(':'>min(p))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert golf('A1213pokl') == False
    assert golf('bAse730onE') == True
    assert golf('asasasasasasasaas') == False
    assert golf('QWERTYqwerty') == False
    assert golf('123456123456') == False
    assert golf('QwErTy911poqqqq') == True
    print("Use 'Check' to earn sweet rewards!")