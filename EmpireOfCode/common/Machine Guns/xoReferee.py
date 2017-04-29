def xo_referee(game_result):
    s = len(game_result)-2
    x, o = (0, 0)
    for i in range(s):
        for j in range(s):
            matrix = [game_result[t][j:j+3] for t in range(i, i+3)]
            r = referee(matrix)
            x = x | r[0]
            o = o | r[1]
    return "D" if x == o else ("X" if x == 1 else "O")


def referee(matrix):
    x, o = 0, 0
    # horizontal check
    for i in matrix:
        if i == 'XXX':
            x = 1
        elif i == 'OOO':
            o = 1

    for i in range(3):
        if matrix[0][i] == matrix[1][i] == matrix[2][i]:
            if matrix[0][i] == 'X':
                x = 1
            elif matrix[0][i] == 'O':
                o = 1

    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        if matrix[0][0] == 'X':
            x = 1
        elif matrix[0][0] == 'O':
            o = 1

    if matrix[2][0] == matrix[1][1] == matrix[0][2]:
        if matrix[2][0] == 'X':
            x = 1
        elif matrix[2][0] == 'O':
            o = 1
    return x, o

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert xo_referee([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert xo_referee([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert xo_referee([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert xo_referee([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

    # Rank 2
    assert xo_referee([
        ".OX",
        ".OX",
        ".OX"]) == "D", "Mexican Vertical Duel"
    assert xo_referee([
        '.XO',
        'XXX',
        'OOO']) == "D", "Mexican Horizontal Duel"

    # Rank 3
    assert xo_referee([
        'XOO.',
        '.X.O',
        'X.OO',
        'XXOX']) == "D", "4WD"
    assert xo_referee([
        'XOO.',
        '.X.O',
        'XXOO',
        'XXOX']) == "X", "4X4"
    print("Earn cool rewards by using the 'Check' button!")
