cells = [0 for i in range(30000)]
pos = 0
index = 0

command_line = input()

while index < len(command_line):
    if command_line[index] == ">":
        pos = pos + 1

    elif command_line[index] == "<":
        pos = pos - 1

    elif command_line[index] == "+":
        cells[pos] += 1

        if cells[pos] > 255:
            cells[pos] = 0

    elif command_line[index] == "-":
        cells[pos] -= 1

        if cells[pos] < 0:
            cells[pos] = 255

    elif command_line[index] == ".":
        print(cells[pos])

    elif command_line[index] == "[":
        if cells[pos] == 0:
            j = index + 1
            temp = 1

            while True:
                if command_line[j] == "[":
                    temp += 1

                if command_line[j] == "]":
                    temp -= 1

                if temp == 0:
                    index = j
                    break
                j += 1
