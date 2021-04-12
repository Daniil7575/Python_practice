import re


def insert_dash(string, index, insert):
    return string[:index] + insert + string[index:]


def space_deleter(line):
    if " " in line:
        spaces = []
        regex = re.findall(r"[ ]+", line)
        for r in regex:
            spaces.append(str(r))
        temp = " ".join(line.split())
        if line.find(spaces[0]) == 0:
            temp = insert_dash(temp, 0, spaces[0])
        return temp
    else:
        return line


def quotes_detector(line):

    temp = line.split("\'")
    temp.pop(0)
    temp.pop(len(temp) - 1)
    quotes_a = 1
    is_closed = False
    out_str = ""
    out = []
    for a in temp:
        if not is_closed:
            a = a[::-1]
            count = 0

            for char_ in a:
                if char_ == "\\":
                    count += 1
                else:
                    break

            if count % 2 == 1:
                out_str += a[::-1]
                out_str += "\'"

            else:
                out_str += a[::-1]
                quotes_a ^= 1
                out.append(out_str)
                out_str = ""
                is_closed = True
        else:
            if "#" in a:
                break
            is_closed = False

    for a in range(len(out)):
        if len(out[a]) == 0:
            out.pop(a)

    return out


def main(line):
    lattice_ind = line.find("#")
    quote_ind = line.find("\'")

    if quote_ind == lattice_ind:
        line = space_deleter(line)

    elif quote_ind != -1 and lattice_ind != -1:
        if quote_ind < lattice_ind:
            untouchable_words = quotes_detector(line)
            for asd in range(len(untouchable_words)):
                line = line.replace(untouchable_words[asd], f"\\{asd}")
            line = line.split("#")[0]
            line = space_deleter(line)
            asd = 0
            for asd in range(len(untouchable_words)):
                line = line.replace(f"\\{asd}", untouchable_words[asd])
        else:
            line = line.split("#")[0]
            line = space_deleter(line)

    elif quote_ind != -1 and lattice_ind == -1:
        untouchable_words = quotes_detector(line)
        for asd in range(len(untouchable_words)):
            line = line.replace(untouchable_words[asd], f"\\{asd}")
        line = line.split("#")[0]
        line = space_deleter(line)
        asd = 0
        for asd in range(len(untouchable_words)):
            line = line.replace(f"\\{asd}", untouchable_words[asd])

    else:
        line = line.split("#")[0]
        line = space_deleter(line)

    return line


for i in range(int(input())):
    print(main(input()))
