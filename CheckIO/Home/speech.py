def checkio(number):
    ldigit = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    mdigit = ["", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninty"]
    ten2twenty = ["ten", "eleven", "twelve", "thirteen", "forteen", "fifteen", "sixteen", "seventeen", "eighteen",
                  "nineteen"]

    result = ""
    highNumber = int(number / 100)
    if highNumber != 0:
        result = ldigit[highNumber - 1] + " hundred"
        number -= highNumber * 100

    midNumber = int(number / 10)
    if midNumber == 1:
        result += " " + ten2twenty[number - 10]
        number = 0
    elif midNumber != 1 and midNumber != 0:
        result += " " + mdigit[midNumber - 1]
        number -= midNumber * 10

    if number != 0:
        result += " " + ldigit[number - 1]

    return result.strip()


if __name__ == '__main__':
    assert checkio(4) == 'four', "First"
    assert checkio(133) == 'one hundred thirty three', "Second"
    assert checkio(12) == 'twelve', "Third"
    assert checkio(101) == 'one hundred one', "Fifth"
    assert checkio(212) == "two hundred twelve", "Sixth"
    assert checkio(40) == 'forty', "Seventh, forty - it is correct"
    print('All ok')