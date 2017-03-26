def checkio(data):
    if len(data) == 0:
        return 0
    return data.pop() + checkio(data)

if __name__=='__main__':
    assert(checkio([1, 2, 3]) == 6), "First"
    assert(checkio([2, 2, 2, 2, 2, 2]) == 12), "Second"