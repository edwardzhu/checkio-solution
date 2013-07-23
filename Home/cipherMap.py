import operator
def checkio(arr):
    index = convertMapToTuples(arr[0])
    cube = convertCubeToList(arr[1])
    output = ''

    dimension = len(arr[0])
    for i in range(0, 4):
        index.sort(key=operator.itemgetter(0, 1))
        for idx in index:
            output = '{0}{1}'.format(output, cube[idx[0]][idx[1]])
        index = rotateCube(index, dimension)
    return output

def convertCubeToList(arr):
    result = []
    for i in range(len(arr)):
        row = []
        for j in range(len(arr[i])):
            row.append(arr[i][j])
        result.append(row)
    return result

def convertMapToTuples(arr):
    result = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != '.':
                result.append((i, j))
    return result

def rotateCube(tuples, dimension):
    result = []
    for item in tuples:
        result.append((item[1], dimension - item[0] - 1))
    return result

if __name__ == "__main__":
    assert checkio([[
'X...',
'..X.',
'X..X',
'....'],[
'itdf',
'gdce',
'aton',
'qrdi']
]) == 'icantforgetiddqd', 'Test1'

    assert checkio([[
'....',
'X..X',
'.X..',
'...X'],[
'xhwc',
'rsqx',
'xqzz',
'fyzr']
]) == 'rxqrwsfzxqxzhczy', "Test2"
