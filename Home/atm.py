import math


def checkio(data):
    balance, withdrawal = data
    for item in withdrawal:
        if (balance - 1.01 * item - 0.5) > 0 and item > 5:
            balance = balance - 1.01 * item - 0.5
            balance = math.floor(balance)

    return balance


if __name__ == '__main__':
    assert checkio([120, [10, 20, 30]]) == 57, 'First'

    # With one Insufficient Funds, and then withdraw 10 $
    assert checkio([120, [200, 10]]) == 109, 'Second'

    #with one incorrect amount
    assert checkio([120, [3, 10]]) == 109, 'Third'

    assert checkio([120, [200, 119]]) == 120, 'Fourth'

    assert checkio([120, [120, 10, 122, 2, 10, 10, 30, 1]]) == 56, "It's mixed all base tests"

    print('All Ok')