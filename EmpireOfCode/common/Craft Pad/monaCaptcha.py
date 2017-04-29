FONT = ("--X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-XX--"
        "-XX----X---X-X-X-X---X-----X-X-X-X-X-X-X-"
        "--X---XX--X--XXX-XX--XXX--X--XXX-XXX-X-X-"
        "--X--X-----X---X---X-X-X-X---X-X---X-X-X-"
        "--X--XXX-XXX---X-XX---XX-X---XXX-XX---XX-")


def recognize(image):
    letters = gen_letters()
    result = ""
    i = 0
    while i + 4 < len(image[0]):
        letter = [image[0][i:i+4], image[1][i:i+4], image[2][i:i+4], image[3][i:i+4], image[4][i:i+4]]
        num = find(letters, letter)
        if num is None:
            return None
        result += str(num)
        i += 4
    return int(result)


def gen_letters():
    l = list(FONT)
    letters = []
    for i in range(10):
        letters.append([l[i*4:i*4+4], l[i*4+41:i*4+45], l[i*4+82:i*4+86], l[i*4+123:i*4+127], l[i*4+164:i*4+168]])
    temp = letters[9]
    letters.remove(temp)
    letters.insert(0, temp)
    return letters


def find(letters, letter):
    for i in range(len(letters)):
        if match(letters[i], letter):
            return i
    return None


def match(letter, item):
    has_noise = False
    for i in range(len(letter)):
        for j in range(len(letter[0])):
            if (letter[i][j] == 'X') != (item[i][j] == 1) and not has_noise:
                has_noise = True
            elif (letter[i][j] == 'X') != (item[i][j] == 1):
                return False
    return True

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"

    assert recognize([[0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
                      [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                      [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                      [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0]]) == 789

    recognize([[0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0],
               [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
               [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
               [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
               [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0]]) == 1034

    print("Earn cool rewards by using the 'Check' button!")