def checkio(n):
    return feed(n, 1, 0)


def feed(n, pigeon, last):
    if n <= last:
        return last
    if last < n <= pigeon:
        return n
    if n > pigeon:
        return feed(n - pigeon, 2 * pigeon - last + 1, pigeon)


if __name__ == '__main__':
    assert checkio(0) == 0, 0
    assert checkio(1) == 1, 1
    assert checkio(2) == 1, 2
    assert checkio(5) == 3, 5
    assert checkio(10) == 6, 10
    print('All OK')
