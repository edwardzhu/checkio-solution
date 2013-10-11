def checkio(arr):
    arr.sort()
    arraylength = len(arr)
    if arraylength % 2 == 0:
        a, b = int(arraylength/2) -1, int(arraylength/2+1) - 1
        return (arr[a] + arr[b])/2
    index = int((arraylength+1)/2) - 1
    return arr[index]

if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "First"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Second"
    assert checkio([1, 300, 2, 200, 1]) == 2, "Third"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Fifth"
    print('All ok')
