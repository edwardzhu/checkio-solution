import datetime


def broken_clock(starting_time, wrong_time, error_description):
    i = parse_error(error_description)
    wrong = datetime.datetime.strptime(wrong_time, "%H:%M:%S")
    start = datetime.datetime.strptime(starting_time, "%H:%M:%S")
    delta = wrong - start
    unit = diff_time(i[1]).total_seconds() + diff_time(i[0]).total_seconds()
    amount = delta.total_seconds() / unit
    result = start + datetime.timedelta(seconds=amount * diff_time(i[1]).total_seconds())
    output = result.strftime("%H:%M:%S")
    return output


def parse_error(error_description):
    items = error_description.split(" ")
    return [(int(items[0]), items[1]), (int(items[3]), items[4])]


def diff_time(entry):
    if entry[1].startswith("second"):
        return datetime.timedelta(seconds=entry[0])
    if entry[1].startswith("hour"):
        return datetime.timedelta(hours=entry[0])
    return datetime.timedelta(minutes=entry[0])


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")