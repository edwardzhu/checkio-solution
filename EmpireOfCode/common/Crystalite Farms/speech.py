FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen",
              "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty",
              "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"
THOUSAND = "thousand"


def tell_number(number):
    result = ""
    if number == 0:
        return "zero"
    elif number < 0:
        result += "minus "
        number *= -1

    thousands = int(number/1000)
    if thousands > 0:
        result += tell_number(thousands) + " " + THOUSAND + " "
        number -= thousands * 1000

    result += tell_number_in_thousand(number)

    return result.strip()


def tell_number_in_thousand(number):
    if number == 0:
        return ""
    result = ""
    hundred = int(number/100)
    if hundred != 0:
        result = FIRST_TEN[hundred - 1] + " " + HUNDRED
        number -= hundred * 100

    midNumber = int(number/10)
    if midNumber == 1:
        result += " " + SECOND_TEN[number-10]
        number = 0
    elif midNumber != 1 and midNumber != 0:
        result += " " + OTHER_TENS[midNumber - 2]
        number -= midNumber * 10

    if number != 0:
        result += " " + FIRST_TEN[number - 1]

    return result.strip()

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # Rank 1
    assert tell_number(4) == 'four', "1st example"
    assert tell_number(133) == 'one hundred thirty three', "2nd example"
    assert tell_number(12) == 'twelve', "3rd example"
    assert tell_number(101) == 'one hundred one', "4th example"
    assert tell_number(212) == 'two hundred twelve', "5th example"
    assert tell_number(40) == 'forty', "6th example"
    assert not tell_number(212).endswith(' '), "Dont forget strip whitespaces at the end of string"

    # Rank 2
    assert tell_number(-133) == 'minus one hundred thirty three', "Minus"
    assert tell_number(0) == 'zero', "Zero"

    # Rank 3
    assert tell_number(42000) == 'forty two thousand', "42 many"
    assert (tell_number(-999999) ==
            "minus nine hundred ninety nine thousand nine hundred ninety nine"), "Abyss"

    print("Earn cool rewards by using the 'Check' button!")