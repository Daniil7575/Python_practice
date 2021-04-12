symbol = input()
pos_save = 1
commands = input()
path = [symbol]
length = 0
depth = 0

for command in range(len(commands)):
    if commands[command] == ">":
        pos_save += 1
        path[depth] += symbol
    elif commands[command] == "<":
        path[depth] = path[depth].lstrip()
        path[depth] += symbol
        path[depth] = path[depth].rjust(len(path[depth - 1]))
        pos_save -= 1
    elif commands[command] == "V":
        depth += 1
        path.append(symbol)
        path[depth] = path[depth].rjust(pos_save)

for i in path:
    print(i)
