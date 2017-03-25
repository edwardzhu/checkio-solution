def checkio(n, m):
    count = 0
    while n > 0 or m > 0:
        count += (n & 1) ^ (m & 1)
        m >>= 1
        n >>= 1
    return count

if __name__ == '__main__':
    assert(checkio(117, 17) == 3), "First"
    assert(checkio(1, 2) == 2), "Second"
    assert(checkio(16, 15) == 5), "Third"