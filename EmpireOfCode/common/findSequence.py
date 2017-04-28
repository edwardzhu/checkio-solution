def has_sequence(matrix):
    for i in range(0, len(matrix)-3):
        for j in range(0, len(matrix[0])-3):
            m = []
            for k in range(4):
                m.append(matrix[i+k][j:j+4])
            if check(m):
                return True
    return False


def check(matrix):
    for m in matrix:
        if min(m) == max(m):
            return True
    for i in range(len(matrix)):
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == matrix[3][i]:
            return True

    return matrix[0][0] == matrix[1][1] == matrix[2][2] == matrix[3][3] or matrix[0][3] == matrix[1][2] == matrix[2][1] == matrix[3][0]

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert has_sequence([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]), "Vertical"
    assert not has_sequence([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]), "Nothing here"
    assert has_sequence([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]), "Long Horizontal"
    assert has_sequence([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]), "Diagonal"

    print("All set? Click 'Check' to review your code and earn rewards!")