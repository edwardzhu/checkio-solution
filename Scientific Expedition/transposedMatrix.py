def checkio(matrix):
    return [list(i) for i in list(zip(*matrix))]

if __name__ == '__main__':
    assert checkio([[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]) == [[1, 4, 7],
                         [2, 5, 8],
                         [3, 6, 9]], 'First check'
    assert checkio([[1, 4, 3],
         [8, 2, 6],
         [7, 8, 3],
         [4, 9, 6],
         [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                         [4, 2, 8, 9, 8],
                         [3, 6, 3, 6, 1]], 'Second check'
    print('All OK')
