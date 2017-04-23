def flat_list(array):
    result = []
    for i in array:
        if isinstance(i, (list, tuple)):
            r = flat_list(i)
            for j in r:
                result.append(j)
        else:
            result.append(i)
    return result

if __name__ == "__main__":
    assert flat_list([1, 2, 3]) == [1, 2, 3], "Flat"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "One"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Nested"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "In In"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")