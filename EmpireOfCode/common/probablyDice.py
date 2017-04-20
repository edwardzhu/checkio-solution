def probability(dice_number, sides, target):
    total = sides ** dice_number
    cases = calc_probability(dice_number, sides, target)
    return cases / total


def calc_probability(dice_number, sides, target):
    result = 0
    if target > dice_number * sides or target <= 0:
        return result
    if dice_number == 1 or dice_number * sides == target:
        return 1
    for i in range(sides):
        result += calc_probability(dice_number-1, sides, target-i-1)
    return result

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