def min_max(args, key, compare):
    if len(args) == 0:
        return None
    if len(args) == 1:
        args = args[0]
    result = None
    for i in args:
        if result == None:
            result = i
        elif (compare(key(i), key(result))):
            result = i
    return result

def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if key == None:
        key = lambda x: x
    return min_max(args, key, lambda x,y: x < y)


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if key == None:
        key = lambda x: x
    return min_max(args, key, lambda x,y: x > y)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    assert min((9,)) == 9, "Test"
    assert min(abs(i) for i in range(-10, 10)) == 0, "Test"