line = input() + " "
count = 0
out = []
prev_digit = line[0]
for i in range(0, len(line)):

    if prev_digit == line[i]:
        count += 1

    else:
        out.append(f"{count} " + line[i - 1])
        count = 1
        prev_digit = line[i]

for a in out:
    print(a)
