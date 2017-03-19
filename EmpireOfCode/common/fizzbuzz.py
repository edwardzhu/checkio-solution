def fizz_buzz(number):
    # replace this for solution
    if number % 15 == 0:
        return "Fizz Buzz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return "Fizz"
    return str(number)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert fizz_buzz(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert fizz_buzz(6) == "Fizz", "6 is divisible by 3"
    assert fizz_buzz(5) == "Buzz", "5 is divisible by 5"
    assert fizz_buzz(7) == "7", "7 is not divisible by 3 or 5"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")