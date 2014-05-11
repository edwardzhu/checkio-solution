def checkio(land):
    result = 0
    rocks = unmatched(land)
    if len(rocks) == 0:
        return len(land) * len(land[0])

    for i in range(len(land)):
        for j in range(len(land[i])):
            temp = count(land, i, j, rocks, len(land), len(land[i]))
            if temp > result:
                result = temp
    return result


def unmatched(land):
    result = []
    for i in range(len(land)):
        for j in range(len(land[i])):
            if land[i][j] != 'G' and land[i][j] != 'S':
                result.append([i, j])
    return result


def count(land, i, j, rocks, lbound, rbound):
    if [i, j] in rocks:
        return 0
    possibleRocks = [e for e in rocks if i <= e[0] < lbound and j <= e[1] < rbound]
    if len(possibleRocks) == 0:
        return (lbound - i) * (rbound - j)

    condition1 = 0
    if len(possibleRocks) > 0:
        possibleRocks.sort(key=lambda x: x[0])
        lbounditem = possibleRocks[0]
        condition1 = count(land, i, j, rocks, lbound, lbounditem[1])
    else:
        lbounditem = [lbound, j]

    condition2 = 0
    if (len(possibleRocks)) > 0:
        possibleRocks.sort(key=lambda x: x[1])
        rbounditem = possibleRocks[0]
        condition2 = count(land, i, j, rocks, rbounditem[0], rbound)
    else:
        rbounditem = [i, rbound]

    if len(rbounditem) > 0 and len(lbounditem) > 0:
        condition3 = (lbounditem[0] - i) * (rbounditem[1] - j)

    return max(condition1, condition2, condition3)


if __name__ == '__main__':
    assert checkio(['G']) == 1, 'First'
    assert checkio(['GS', 'GS']) == 4, 'Second'
    assert checkio(['GT', 'GG']) == 2, 'Third'
    assert checkio(['GGTGG', 'TGGGG', 'GSSGT', 'GGGGT', 'GWGGG', 'RGTRT', 'RTGWT', 'WTWGR']) == 9, 'Forth'