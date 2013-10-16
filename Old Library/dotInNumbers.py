def checkio(string):
    words = string.split(" ")
    result = ""

    for word in words:
        if str.isdigit(word):
            result += '{:,}'.format(int(word)).replace(",", ".") + " "
        else:
            result += word + " "
    return result.strip(" ")


if __name__ == "__main__":
    assert checkio('123456') == '123.456', "First"
    assert checkio('333') == '333', "Second"
    assert checkio('9999999') == '9.999.999', "Third"
    assert checkio('123456 567890') == '123.456 567.890', "Four"
    assert checkio('price is 5799') == 'price is 5.799', "Five"
    assert checkio('he was born in 1966th') == 'he was born in 1966th', "Six"
