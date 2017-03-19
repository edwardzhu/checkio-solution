from datetime import date, timedelta

def checkio(start, end):
    if end < start:
        start, end = end, start
    days = (end - start).days.numerator
    weeks, remaining = divmod(days, 7)
    return weeks * 2 + sum((start + timedelta(days=d)).isoweekday() == 6 or (start + timedelta(days=d)).isoweekday() == 7 for d in range(remaining + 1))

if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "First"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "Second"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "Third"
