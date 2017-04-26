import math
from decimal import *


def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=('', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')):
    index = 0
    while abs(number) >= base and index < len(powers) - 1:
        number = Decimal(number) / Decimal(base)
        index += 1
    if decimals == 0:
        if number > 0:
            number = round(math.floor(number * 10 ** decimals) / 10 ** decimals)
        else:
            number = round(math.ceil(number * 10 ** decimals) / 10 ** decimals)
    else:
        number = round(number, decimals)
    r = ("{0:."+str(decimals)+"f}").format(number)
    return r + powers[index] + suffix


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
    assert friendly_number(-150, base=100, powers=['','d','D']) == '-1d', '-1d'
    assert friendly_number(-155, base=100, decimals=1, powers=['','d','D']) == '-1.6d', '-1.6d'
    assert friendly_number(255000000000, powers=['','k','M']) == '255000M', '255000M'
    assert friendly_number(100000000000000000000000000000000) == "100000000Y", "100000000Y"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")