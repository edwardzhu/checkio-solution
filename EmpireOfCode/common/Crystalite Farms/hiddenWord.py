def find_word(text, word):
    text_line = [l.replace(" ", "") for l in text.split("\n")]
    l = [list(i) for i in text_line]
    transferred = transfer(text_line)
    r = find_text(text_line, word)
    if r is None:
        r = find_text(transferred, word)
        if r is not None:
            return [r[1], r[0], r[3], r[2]]
    return r


def find_text(text_list, word):
    for i in range(len(text_list)):
        r = ''.join(text_list[i]).upper().find(word.upper())
        if r >= 0:
            return [i+1, r+1, i+1, r+len(word)]
    return None


def transfer(text_list):
    matrix = []
    for j in range(max([len(t) for t in text_list])):
        r = []
        for i in range(len(text_list)):
            if len(text_list[i]) <= j:
                r.append("")
            else:
                r.append(text_list[i][j])
        matrix.append(r)
    return matrix


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]

    assert find_word("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]

    assert find_word("""Twas brillig, and the slithy toves
     Did gyre and gimble in the wabe; 
     All mimsy were the borogoves, 
     And the mome raths outgrabe.""", "stog") == [1, 19, 4, 19]

    assert find_word("""xa
    xb
    x""", "ab") == [1,2,2,2]

    print("Use 'Check' to earn sweet rewards!")