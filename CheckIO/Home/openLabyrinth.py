def checkio(item):
    return walk((1, 1), item, '', (10,10))

def walk(position, puzzle, steps, target):
    if position == target:
        return steps
    (a, b) = position
    puzzle[a][b] = 1
    result = ""
    if puzzle[a][b+1] == 0:
        result = walk((a, b+1), puzzle, steps+'E', target)
        if result != "":
            return result

    if puzzle[a+1][b] == 0:
        result = walk((a+1, b), puzzle, steps+'S', target)
        if result != "":
            return result

    if puzzle[a][b-1] == 0:
        result = walk((a, b-1), puzzle, steps+'W', target)
        if result != "":
            return result

    if puzzle[a-1][b] == 0:
        result =walk((a-1, b), puzzle, steps+'N', target)
        if result != "":
            return result

    return result

if __name__ == '__main__':
    print(checkio([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                   [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
                   [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
                   [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
                   [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))
