CODE = {'0': '....', '1':'...-', '2':'..-.', '3':'..--', '4':'.-..', '5':'.-.-', '6':'.--.', '7':'.---', '8':'-...', '9':'-..-'}

def morse_time(time_string):
    hour,minute,second = [i.zfill(2) for i in time_string.split(':')]
    return CODE[hour[0]][-2:] + " " + CODE[hour[1]] + " : " + CODE[minute[0]][-3:] + " " + CODE[minute[1]] + " : " + CODE[second[0]][-3:] + " " + CODE[second[1]]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_time("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert morse_time("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert morse_time("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert morse_time("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")