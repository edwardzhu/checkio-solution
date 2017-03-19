ALPHABETS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
def safe_pawns(pawns):
    count = 0;
    for i in pawns:
        supports = getSupportPawn(i)
        for s in supports:
            if s in pawns:
                count += 1
                break
    return count

def getSupportPawn(pawn):
    item = list(pawn)
    idx = ALPHABETS.index(item[0])
    result = []
    row = int(item[1])
    if idx > 0 and row > 1:
        result.append(str.format("{0}{1}", ALPHABETS[idx-1], row-1))
    if idx < 7 and row > 1:
        result.append(str.format("{0}{1}", ALPHABETS[idx+1], row-1))
    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1