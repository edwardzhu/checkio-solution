def probability(dice_number, sides, target):
    total, result, case = sides ** dice_number, [[]], 0
    result[0] = sides * [1] + sides * (dice_number - 1) * [0]
    for i in range(1, dice_number):
        result.append([0])
        for j in range(1, sides * dice_number):
            result[i].append(0)
            for k in range(max(j-sides, 0), j):
                result[i][j] += result[i-1][k]
    if target > dice_number * sides or target < 1:
        return 0
    return result[dice_number - 1][target - 1] / total


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")