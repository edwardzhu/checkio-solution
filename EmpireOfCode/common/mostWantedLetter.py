def most_letter(text, all_letters=False):
    r = dict()
    for t in text.lower():
        if 96 < ord(t) < 123:
            if t in r:
                r[t] += 1
            else:
                r[t] = 1
    l = sorted(r.items(), key=lambda x:x[0])
    l = sorted(l, key=lambda x:x[1], reverse=True)
    if not all_letters:
        candidates = sorted(list(filter(lambda i: i[1] == l[0][1], l)), key=lambda i: ord(i[0]))
        return candidates[0][0]
    return ''.join([i[0] for i in l])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank_1
    assert most_letter("Hello World!") == "l", "Hello test"
    assert most_letter("How do you do?") == "o", "O is most wanted"
    result = most_letter("One")
    assert len(result) == 1 and result in "one", "All letter only once."
    assert most_letter("Oops!") == "o", "Don't forget about lower case."
    result = most_letter("AAaooo!!!!")
    assert len(result) == 1 and result in "ao", "Only letters."
    result = most_letter("abe")
    assert len(result) == 1 and result in "abe", "The First."
    result = most_letter("Lorem ipsum dolor sit amet")
    assert len(result) == 1 and result in "mo", "Lorem 1."

    # Rank_2
    assert most_letter("Lorem ipsum dolor sit amet") == "m", "Lorem 2."
    assert most_letter("One") == "e", "One 2"
    assert most_letter("AAaooo!!!!") == "a", "Only letters. 2"
    assert most_letter("bcdefghijklmnaopqrstuvwxyz") == "a", "ABC"

    # Rank_3
    assert most_letter("Lorem ipsum dolor sit amet", True) == "moeilrstadpu", "Lorem 3."

    print("Use 'Check' to earn sweet rewards!")