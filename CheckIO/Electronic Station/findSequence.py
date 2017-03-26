def checkio(matrix):
    rotated = rotate_matrix(matrix)
    diagnosal = generate_diagonal(matrix)
    return check_row(matrix) | check_row(rotated) | check_row(diagnosal)


def rotate_matrix(matrix):
    result = []
    for i in range(len(matrix)):
        result.append([row[i] for row in matrix])
    return result


def check_row(matrix):
    for l in matrix:
        for i in range(0,len(l)-3):
            if is_sequence(l[i:i+4]):
                return True
    return False


def generate_diagonal(matrix):
    result = []
    length = len(matrix)
    for i in range(length):
        for j in range(length):
            if i + 3 < length and j + 3 < length:
                result.append([matrix[i+offset][j+offset] for offset in range(0,4)])
            elif i - 3 > -1 and j + 3 < length:
                result.append([matrix[i-offset][j+offset] for offset in range(0,4)])
    return result


def is_sequence(list):
    return min(list) == max(list)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"