def mark_patterns(pattern, image):
    l,h = len(image[0]),len(image)
    pl,ph = len(pattern[0]),len(pattern)
    for i in range(h-ph+1):
        for j in range(l-pl+1):
            if isMatch(pattern, image, (i,j)):
                image = replace(pattern, image, (i,j))
    return image


def isMatch(pattern, image, pos):
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            if image[pos[0]+i][pos[1]+j] != pattern[i][j]:
                return False
    return True


def replace(pattern, image, pos):
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
                image[pos[0]+i][pos[1]+j] += 2
    return image

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert mark_patterns([[1, 0], [1, 1]],
                         [[0, 1, 0, 1, 0],
                          [0, 1, 1, 0, 0],
                          [1, 0, 1, 1, 0],
                          [1, 1, 0, 1, 1],
                          [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                                                [0, 3, 3, 0, 0],
                                                [3, 2, 1, 3, 2],
                                                [3, 3, 0, 3, 3],
                                                [0, 1, 1, 0, 0]], "1st"
    assert mark_patterns([[1, 1], [1, 1]],
                         [[1, 1, 1],
                          [1, 1, 1],
                          [1, 1, 1]]) == [[3, 3, 1],
                                          [3, 3, 1],
                                          [1, 1, 1]], "2nd"
    assert mark_patterns([[0, 1, 0], [1, 1, 1]],
                         [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                          [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                          [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                          [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                          [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                          [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [[0, 2, 3, 2, 0, 0, 0, 2, 3, 2],
                                                               [0, 3, 3, 3, 0, 0, 0, 3, 3, 3],
                                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                               [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
                                                               [2, 3, 2, 0, 3, 3, 3, 0, 1, 0],
                                                               [3, 3, 3, 0, 0, 0, 0, 0, 1, 1],
                                                               [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                                                               [0, 0, 1, 0, 0, 0, 2, 3, 2, 0],
                                                               [0, 1, 1, 0, 0, 0, 3, 3, 3, 0],
                                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], "3rd"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
