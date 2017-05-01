def can_pass(matrix, first, second):
    m = [list(i) for i in matrix]
    left = (first[0], first[1] - 1)
    right = (first[0], first[1] + 1)
    up = (first[0] - 1, first[1])
    down = (first[0] + 1, first[1])
    start_value = m[first[0]][first[1]]
    m[first[0]][first[1]] = int(~start_value)

    r = False
    if left[1] > -1 and m[left[0]][left[1]] == start_value:
        if left == second:
            return True
        r |= can_pass(m, left, second)
    if not r and right[1] < len(m[0]) and m[right[0]][right[1]] == start_value:
        if right == second:
            return True
        r |= can_pass(m, right, second)
    if not r and up[0] > -1 and m[up[0]][up[1]] == start_value:
        if up == second:
            return True
        r |= can_pass(m, up, second)
    if not r and down[0] < len(m) and m[down[0]][down[1]] == start_value:
        if down == second:
            return True
        r |= can_pass(m, down, second)
    return r


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)), 'First example'
    assert not can_pass(((0, 0, 0, 0, 0, 0),
                         (0, 2, 2, 2, 3, 2),
                         (0, 2, 0, 0, 0, 2),
                         (0, 2, 0, 2, 0, 2),
                         (0, 2, 2, 2, 0, 2),
                         (0, 0, 0, 0, 0, 2),
                         (2, 2, 2, 2, 2, 2),),
                        (3, 3), (6, 0)), 'Second example'

    print("Earn cool rewards by using the 'Check' button!")