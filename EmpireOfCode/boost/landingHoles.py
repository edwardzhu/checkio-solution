def rotate(state, pipe_numbers):
    result = []
    for i in range(len(state)):
        s = all([state[j] == 1 for j in pipe_numbers])
        if s:
            result.append(i)
        state = [state[-1]] + state[0:-1]
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8], "Example"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [], "Mission impossible"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0], "Don't touch it"
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5], "Two cannonballs in the same pipe"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
