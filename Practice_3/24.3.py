def cage_detect(line):
    if "#" in line:
        return line.split("# ")[1]


commands = []
inp = input().lstrip().rstrip()

while inp != "":
    commands.append(inp)
    inp = input().lstrip().rstrip()

comments = list(map(lambda x: cage_detect(x), commands))

print(*[f"Line {i + 1}: {comments[i]}" for i in range(len(comments)) if comments[i] is not None], sep="\n")
