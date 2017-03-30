def check_grid(grid):
    for g in grid:
        for i in range(len(g)-1):
            if g[i] == g[i+1]:
                return False

    for i in range(len(grid)-1):
        for j in range(len(grid[i])):
            if grid[i][j] == grid[i+1][j]:
                return False
    return True


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_grid([["X", "Z"], ["Z", "X"]]), "2x2 Good"
    assert check_grid([["X", "Z", "X"],
                       ["Z", "X", "Z"],
                       ["X", "Z", "X"]]), "3x3 Good"
    assert check_grid([["X", "Z", "X", "Z"],
                       ["Z", "X", "Z", "X"]]), "2x4 Good"
    assert not check_grid([["X", "X"],
                           ["X", "X"]]), "2x2 Bad"
    assert not check_grid([["X", "Z", "X"],
                           ["Z", "Z", "Z"],
                           ["X", "Z", "X"]]), "3x3 Bad"
    assert not check_grid([["X", "Z", "X", "Z"],
                           ["X", "Z", "X", "Z"]]), "2x4 Bad"

    print("Use 'Check' to earn sweet rewards!")