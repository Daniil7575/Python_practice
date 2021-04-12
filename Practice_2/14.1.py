recipe = []

n = int(input())
for i in range(n):
    line = input()
    if "лук" in line:
        pass
    else:
        if i == n - 1:
            recipe.append(line)
        else:
            recipe.append(line + ", ")

for i in recipe:
    print(i, end="")
