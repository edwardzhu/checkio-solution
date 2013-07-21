def checkio(arr):
    result = test(arr, 0)
    part1 = result[1]
    for item in part1:
        arr.remove(item)
    part2 = arr

    print(part1, "vs.", part2, ":", result[0])
    return result[0]

def test(arr, target):
    if len(arr) == 1:
        return [abs(arr[0] - target), []]

    diff = abs(sum(arr) - target)
    rArr = []
    for item in arr:
        tmp = arr.copy()
        tmp.remove(item)
        expect = target + item

        result = test(tmp, expect)
        if result[0] < diff:
            diff = result[0]
            if not result[1]:
                rArr = [item]
            else:
                result[1].insert(0, item)
                rArr = result[1]

    return [diff, rArr]

def sum(arr):
    result = 0
    for item in arr:
        result += item

    return result

if __name__ == '__main__':
    assert checkio([10, 10]) == 0, 'Test1'
    assert checkio([10]) == 10, 'Test2'
    assert checkio([5, 8, 13, 27, 14]) == 3, 'Test3'
    assert checkio([5, 5, 6, 5]) == 1, 'Test4'
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Test5'
    assert checkio([1, 1, 1, 3]) == 0, 'Test6'
