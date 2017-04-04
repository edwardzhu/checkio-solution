def super_root(number):
    c = 1
    while c ** c < number:
        c += 1
    if c ** c == number:
        return c
    return tetration(c-1, c, number)


def tetration(l, r, result):
    if l ** l > result - 0.001 and r ** r < result + 0.001:
        return (l + r) / 2
    mid = (l + r) / 2
    t = mid ** mid
    if t < result:
        return tetration(mid, r, result)
    else:
        return tetration(l, mid, result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False

    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")