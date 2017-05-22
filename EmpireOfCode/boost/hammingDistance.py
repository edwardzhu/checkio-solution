def hamming(n, m):
    nb, mb = "{0:b}".format(n), "{0:b}".format(m)
    maxlen = max(len(nb), len(mb))
    nb, mb = nb.zfill(maxlen), mb.zfill(maxlen)
    counter = 0
    for i in range(maxlen):
        if nb[i] != mb[i]:
            counter += 1
    return counter

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert hamming(117, 17) == 3, "First example"
    assert hamming(1, 2) == 2, "Second example"
    assert hamming(16, 15) == 5, "Third example"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")