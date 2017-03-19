def checkio(stones):
    avg = sum(stones) / len(stones)
    result = findSet(stones, avg)


def sum(stones):
    result = 0
    for i in stones:
        result += stones[i]
    return result


def findSet(stones, target):
    stones.sort(reverse=True)
    if stones[0] > target:
        return [stones[0]]


if __name__ == '__main__':
    assert checkio([10, 10]) == 0, 'First, with equal weights'
    assert checkio([10]) == 10, 'Second, with a single stone'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    assert checkio([5, 5, 6, 5]) == 1, 'Fourth'
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Fifth'
    assert checkio([1, 1, 1, 3]) == 0, "Six, don't forget - you can hold different quantity of parts"
    print('All is ok')