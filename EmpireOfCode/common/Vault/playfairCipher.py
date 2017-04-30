import re, string


def encode(message, key):
    pairs = prepare(message)
    cube = prepare_key(key)
    result = ""
    for p in pairs:
        first = find_index(p[0], cube)
        second = find_index(p[1], cube)
        if first[0] == second[0]:
            first = (first[0], (first[1] + 1) % 6)
            second = (second[0], (second[1] + 1) % 6)
        elif first[1] == second[1]:
            first = ((first[0] + 1) % 6, first[1])
            second = ((second[0] + 1) % 6, second[1])
        else:
            first, second = (first[0], second[1]), (second[0], first[1])
        result += cube[first[0]][first[1]] + cube[second[0]][second[1]]
    return result


def decode(message, key):
    cube = prepare_key(key)
    pairs = [message[i*2:i*2+2] for i in range(len(message) // 2)]
    result = ""
    for p in pairs:
        first = find_index(p[0], cube)
        second = find_index(p[1], cube)
        if first[0] == second[0]:
            first = (first[0], first[1] -1 if first[1] != 0 else len(cube) - 1)
            second = (second[0], second[1] - 1 if second[1] != 0 else len(cube) - 1)
        elif first[1] == second[1]:
            first = (first[0] - 1 if first[0] != 0 else len(cube) - 1, first[1])
            second = (second[0] - 1 if second[0] != 0 else len(cube) - 1, second[1])
        else:
            first, second = (first[0], second[1]), (second[0], first[1])
        result += cube[first[0]][first[1]] + cube[second[0]][second[1]]
    return result


def prepare(message):
    pattern = re.compile('[\W_]+')
    message = pattern.sub('', message).lower()
    result = message
    idx = need_insert(result)
    while idx[0] != -1:
        result = result[:idx[0]] + idx[1] + result[idx[0]:]
        idx = need_insert(result)
    if len(result) % 2 == 1:
        result += "x" if result[-1] == "z" else "z"
    return [result[i*2:i*2+2] for i in range(len(result)//2)]


def prepare_key(key):
    pattern = string.ascii_lowercase + string.digits
    result = []
    for i in key:
        if i not in result:
            result.append(i)
            pattern = pattern.replace(i, '')
    result.extend(pattern)
    return [list(result[i*6:i*6+6]) for i in range(6)]


def need_insert(message):
    for i in range(0, len(message), 2):
        if i + 1 < len(message) and message[i] == message[i + 1]:
            return i+1, 'z' if message[i] == 'x' else 'x'
    return -1, ""


def find_index(c, cube):
    for i in range(len(cube)):
        if c in cube[i]:
            return i, cube[i].index(c)
    return -1, -1


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert encode("Fizz Buzz is x89 XX.", "checkio101") == 'do2y7mt22kry94y2y2', "Encode fizz buzz"
    assert decode("do2y7mt22kry94y2y2", "checkio101") == 'fizxzbuzzisx89xzxz', "Decode fizz buzz"
    assert encode("How are you?", "hello") == 'ea2imb1ht0', "Encode How are you"
    assert decode("ea2imb1ht0", "hello") == 'howareyouz', "Decode How are you"
    assert encode("My name is Alex!!!", "alexander") == 'i1dlkxjqlexn', "Encode Alex"
    assert decode("i1dlkxjqlexn", "alexander") == 'mynameisalex', "Decode Alex"
    assert encode("Who are you?", "human") == 'rnvftc1jd5', "Encode WHo"
    assert decode("rnvftc1jd5", "human") == 'whoareyouz', "Decode Who"
    assert encode("ATTACK AT DAWN", "general") == 'ewwektewhnua', "Encode attack"
    assert decode("ewwektewhnua", "general") == 'attackatdawn', "Decode attack"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")