VOWELS = "aeiouy"


def translate(phrase):
    r = ""
    for i in phrase.split(" "):
        r += translate_in(i) + " "
    return r.strip()


def translate_in(phrase):
    r = []
    p = iter(phrase)
    for l in p:
        r.append(l)
        if l not in VOWELS:
            next(p)
        elif l in VOWELS:
            next(p)
            next(p)
    return "".join(r)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")