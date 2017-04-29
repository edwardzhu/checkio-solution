def letter_queue(commands):
    result = []
    for c in commands:
        if c.startswith("POP"):
            pop_list(result)
        elif c.startswith("PUSH"):
            push_list(result, c.split(" ")[1])
    return ''.join(result)


def pop_list(output):
    if len(output) > 0:
        output.pop(0)


def push_list(output, x):
    output.append(x)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(("PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T")) == "DOT", "dot example"
    assert letter_queue(("POP", "POP")) == "", "Pop, Pop, empty"
    assert letter_queue(("PUSH H", "PUSH I")) == "HI", "Hi!"
    assert letter_queue(()) == "", "Nothing"

    print("All done? Earn rewards by using the 'Check' button!")