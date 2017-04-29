import math


def total_cost(calls):
    total = 0
    lastday = ""
    totalinday = 0
    for c in calls:
        day, time, duration = c.split(" ")
        if lastday != day:
            totalinday = 0
            lastday = day
        d = math.ceil(int(duration) / 60)
        if d + totalinday >= 100 and totalinday <= 100:
            total += (d + totalinday - 100) * 2 + (100 - totalinday)
        elif d + totalinday < 100:
            total += d
        else:
            total += d * 2
        totalinday += d
    return total


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"

    print("All set? Click 'Check' to review your code and earn rewards!")
