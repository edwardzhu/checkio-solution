def checkio(time):
    parts = str.split(time, ':')
    result = formatNumber(parts[0], [2, 4])
    for i in range(1, 3):
        result += formatNumber(parts[i], [3, 4])
    result = result.strip(" :")
    print(result)
    return result


def formatNumber(number, length):
    result = ''
    number = str("{0:02d}".format(int(number)))
    for i in range(0, len(length)):
        f = "{0:0"+str(length[i])+"b}"
        item = f.format(int(number[i])).replace('0', '.').replace('1', '-')
        result += item + " "
    return result + ": "

if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:01:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
    assert checkio("0:10:2") == ".. .... : ..- .... : ... ..-.", "Fifth Test"