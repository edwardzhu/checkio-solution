def checkio(offers):
    """
        the amount of money that Petr will pay for the ride
    """
    initial_petr, raise_petr, initial_driver, reduction_driver = offers
    petr = initial_petr
    driver = initial_driver

    while petr < driver:
        petr += raise_petr
        if petr <= driver:
            driver -= reduction_driver

    return petr


if __name__ == '__main__':
    assert checkio([150, 50, 1000, 100]) == 450, 'First'
    assert checkio([150, 50, 900, 100]) == 400, 'Second'
    print('All is ok')