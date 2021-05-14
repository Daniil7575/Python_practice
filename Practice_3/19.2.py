def todigit(cell):
    return ord(cell[0]) % 65, int(cell[1]) - 1


def tostr(dig1, dig2):
    return chr(dig1 + 65) + "" + str(dig2 + 1)


def possible_turns(cell):
    turns = []

    delta1 = [1, 1, -1, -1]
    delta2 = [2, -2, 2, -2]

    cell = todigit(cell)

    for i in range(4):
        if 0 <= delta1[i] + cell[0] <= 7 and 0 <= delta2[i] + cell[1] <= 7:
            turns.append(tostr(delta1[i] + cell[0], delta2[i] + cell[1]))

        if 0 <= delta2[i] + cell[0] <= 7 and 0 <= delta1[i] + cell[1] <= 7:
            turns.append(tostr(delta2[i] + cell[0], delta1[i] + cell[1]))

    turns.sort()

    return turns


# print(possible_turns("H8"))
