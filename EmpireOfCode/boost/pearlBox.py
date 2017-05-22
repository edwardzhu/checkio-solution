d = {}


def probability(marbles, step):
    w, b = marbles.count("w"), marbles.count("b")
    return probable((w, b), step)


def probable(item, step):
    if step == 1:
        return item[0] / (item[0] + item[1])
    if item[1] == 0:
        return calculate((item[0] - 1, item[1] + 1), step - 1) * item[0] / (item[0] + item[1])
    if item[0] == 0:
        return calculate((item[0] + 1, item[1] - 1), step - 1) * item[1] / (item[0] + item[1])
    return calculate((item[0] - 1, item[1] + 1), step - 1) * item[0] / (item[0] + item[1]) + calculate((item[0] + 1, item[1] - 1), step - 1) * item[1] / (item[0] + item[1])


def calculate(item, step):
    key = (item, step)
    if key not in d:
        d[key] = probable(item, step)
    return d[key]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(probability('bbw', 3), 0.48), "1st example"
    assert almost_equal(probability('wwb', 3), 0.52), "2nd example"
    assert almost_equal(probability('www', 3), 0.56), "3rd example"
    assert almost_equal(probability('bbbb', 1), 0), "4th example"
    assert almost_equal(probability('wwbb', 4), 0.5), "5th example"
    assert almost_equal(probability('bwbwbwb', 5), 0.48), "6th example"

    print("All done? Earn rewards by using the 'Check' button!")