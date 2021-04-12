line = "0"

for i in range(int(input()) - 1):
    count = 0
    for j in range(len(line)):
        if line[j] == line[::-1][j]:
            count += 1
    line += str(count)

print(line)
