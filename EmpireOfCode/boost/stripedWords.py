VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


import re


def striped_words(text):
    items = re.split("\W+", text.upper())
    count = 0
    for t in items:
        if t == "" or len(t) == 1 or any([not str.isalpha(i) for i in t]):
            continue
        flag = True
        for i in range(len(t)-1):
            if (VOWELS.find(t[i]) > -1 and VOWELS.find(t[i+1]) > -1) or (CONSONANTS.find(t[i]) > -1 and CONSONANTS.find(t[i+1]) > -1):
                flag = False
        if flag:
            count += 1
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert striped_words("My name is ...") == 3, "All words are striped"
    assert striped_words("Hello world") == 0, "No one"
    assert striped_words("A quantity of striped words.") == 1, "Only of"
    assert striped_words("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert striped_words("1st 2a ab3er root rate") == 1

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")