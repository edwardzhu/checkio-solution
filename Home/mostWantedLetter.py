def checkio(word):
    word = word.lower()
    arr = dict()
    for i in range(len(word)):
        char = word[i]
        if not str.isalpha(char):
            continue
        if not arr.__contains__(char):
            arr[char] = 0
        arr[char] = arr[char] + 1
    result = ""
    counter = 0
    for k, v in arr.items():
        if counter < v or (ord(k) < ord(result) and counter == v):
            result = k
            counter = v
    return result

if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "First"
    assert checkio("How do you do?") == "o", "Second"
    assert checkio("One") == "e", "Third"
    assert checkio("") == "", "Final"
    print('All ok')
