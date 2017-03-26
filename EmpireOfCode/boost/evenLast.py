def even_last(array):
    if len(array) == 0:
        return 0
    return array[-1] * sum([array[i] for i in range(len(array)) if i % 2 == 0])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert even_last([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert even_last([1, 3, 5]) == 30, "(1+5)*5=30"
    assert even_last([6]) == 36, "(6)*6=36"
    assert even_last([]) == 0, "An empty array = 0"
    assert even_last([-37, -36, -19, -99, 29, 20, 3, -7, -64, 84, 36, 62, 26, -76, 55, -24, 84, 49, -65, 41]) == 1968, "Last"

    print("Use 'Check' to earn sweet rewards!")