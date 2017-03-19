def checkio(arr):
    multiple, checked, result = [], [], []
    for item in arr:
        if (item in checked) and not(item in multiple):
            multiple.append(item)
        else:
            checked.append(item)
    for item in arr:
        if item in multiple:
            result.append(item)
    return result

if __name__ == '__main__':
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], 'Test1'
    assert checkio([1, 2, 3, 4, 5]) == [], "Test2"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "Test3"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "Test4"
    assert checkio([]) == [], "Test5"
