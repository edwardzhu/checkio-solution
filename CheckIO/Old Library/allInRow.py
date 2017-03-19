def checkio(data):
    if not isinstance(data, list):
        return [data]

    result = []
    for item in data:
        result.extend(checkio(item))

    return result

if __name__=='__main__':
    assert checkio([1,2,3]) == [1,2,3], "Test1"
    assert checkio([1,[2,2,2],4]) == [1,2,2,2,4], "Test2"
    assert checkio([[[2]],[4,[5,6,[6],6,6,6],7]]) == [2,4,5,6,6,6,6,6,7], "Test3"
