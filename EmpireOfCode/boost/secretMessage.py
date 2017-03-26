def find_message(text):
    result = [i for i in text if i.upper() == i and ord(i) in range(65, 91)]
    return ''.join(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"

    print("Earn cool rewards by using the 'Check' button!")