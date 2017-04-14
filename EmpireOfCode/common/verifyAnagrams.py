def verify_anagrams(first_word, second_word):
    first = list(first_word.upper())
    second = list(second_word.upper())
    for i in first:
        if i != " ":
            if second.__contains__(i):
                second.remove(i)
            else:
                return False
    return second.count(" ") == len(second)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")