def count_reports(full_report, from_date, to_date):
    l = str.split(full_report, '\n')
    d = dict([str.split(i, " ") for i in l])
    result = 0
    for key in d.keys():
        if from_date <= key <= to_date:
            scores = str.split(d[key], ",")
            for v in scores:
                s = v.lower()
                result += (ord(s[0]) - ord('a')) * 9 + int(s[1])
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_reports("2015-01-01 A1,B2\n"
                         "2015-01-05 C3,C2,C1\n"
                         "2015-02-01 B4\n"
                         "2015-01-03 Z9,Z9",
                         "2015-01-01", "2015-01-31") == 540, "Normal"
    assert count_reports("2000-02-02 Z2,Z1\n"
                         "2000-02-01 Z2,Z1\n"
                         "2000-02-03 Z2,Z1",
                         "2000-02-04", "2000-02-28") == 0, "Zero"
    assert count_reports("2999-12-31 Z9,A1", "2000-01-01", "2999-12-31") == 235, "Millenium"

    print("Earn cool rewards by using the 'Check' button!")