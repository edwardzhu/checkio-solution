import operator
def recall_password(cipher_grille, ciphered_password):
    index = convertMapToTuples(cipher_grille)
    cube = convertCubeToList(ciphered_password)
    output = ''

    dimension = len(cipher_grille)
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
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
