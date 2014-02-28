def checkio(array):
    if (array[0][0] == array[0][1] == array[0][2] or array[0][0] == array[1][0] == array[2][0] or array[0][0] == array[1][1] == array[2][2]) and array[0][0] != '.':
        return array[0][0]
    if (array[1][0] == array[1][1] == array[1][2] or array[0][1] == array[1][1] == array[2][1] or array[2][0] == array[1][1] == array[0][2]) and array[1][1] != '.':
        return array[1][1]
    if (array[2][0] == array[2][1] == array[2][2] or array[0][2] == array[1][2] == array[2][2]) and array[2][2] != '.' :
        return array[2][2]
    return "D"

if __name__ == '__main__':
    assert checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X", "Xs wins"
    assert checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O", "Os wins"
    assert checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D", "Draw"
    assert checkio([
        "...",
        "XXO",
        "XXO"
    ]) == "D", "Draw"
