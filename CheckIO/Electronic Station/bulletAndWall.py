import math

def checkio(list):
    bound1 = calcAngle(list[2], list[0])
    bound2 = calcAngle(list[2], list[1])
    check = calcAngle(list[2], list[3])
    if math.fabs(bound2 - bound1) < math.pi:
        return min(bound1, bound2) <= check <= max(bound1, bound2)
    else:
        return 0 <= check <= min(bound1, bound2) or max(bound1, bound2) <= check <= math.pi * 2

def calcAngle(start, end):
    angle = math.atan2((end[1] - start[1]), (end[0] - start[0]))
    if angle < 0:
        angle += 2 * math.pi
    return angle

if __name__ == '__main__':
    assert checkio([[0, 0], [0, 2], [5, 1], [3, 1]]) is True, "Test7"

    assert checkio([[0, 0], [0, 2], [5, 1], [3, 1]]) is True, "Test1"
    assert checkio([[0, 0], [0, 2], [3, 1], [5, 1]]) is False, "Test2"
    assert checkio([[0, 0], [2, 2], [6, 0], [3, 1]]) is True, "Test3"
    assert checkio([[6, 0], [5, 5], [4, 0], [5, 6]]) is False, "Test4"
    assert checkio([[0, 0], [1, 1], [3, 3], [2, 2]]) is True, "Test5"
    assert checkio([[0, 0], [1, 1], [3, 2], [2, 1]]) is False, "Test6"
    assert checkio([[0, 0], [0, 2], [5, 1], [3, 1]]) is True, "Test7"

