def not_negative(a, b):
    if a - b <= 0:
        return 0
    return a - b


n = int(input())
field = [[int(input()) for j in range(n)]for i in range(n)]

k = int(input())
blob = [[int(input()) for j in range(2)] for i in range(k)]

for z in range(k):
    i, j = blob[z]

    field[i][j] = not_negative(field[i][j], 8)

    if i == 0:
        field[i + 1][j] = not_negative(field[i + 1][j], 4)

        if j == 0:
            field[i + 1][j + 1] = not_negative(field[i + 1][j + 1], 4)
            field[i][j + 1] = not_negative(field[i][j + 1], 4)

        elif j == n - 1:
            field[i + 1][j - 1] = not_negative(field[i + 1][j - 1], 4)
            field[i][j - 1] = not_negative(field[i][j - 1], 4)

        else:
            field[i + 1][j + 1] = not_negative(field[i + 1][j + 1], 4)
            field[i + 1][j - 1] = not_negative(field[i + 1][j - 1], 4)
            field[i][j + 1] = not_negative(field[i][j + 1], 4)
            field[i][j - 1] = not_negative(field[i][j - 1], 4)

    elif i == n - 1:
        field[i - 1][j] = not_negative(field[i - 1][j], 4)

        if j == 0:
            field[i - 1][j + 1] = not_negative(field[i - 1][j + 1], 4)
            field[i][j + 1] = not_negative(field[i][j + 1], 4)

        elif j == n - 1:
            field[i - 1][j - 1] = not_negative(field[i - 1][j - 1], 4)
            field[i][j - 1] = not_negative(field[i][j - 1], 4)

        else:
            field[i][j + 1] = not_negative(field[i][j + 1], 4)
            field[i][j - 1] = not_negative(field[i][j - 1], 4)
            field[i - 1][j + 1] = not_negative(field[i - 1][j + 1], 4)
            field[i - 1][j - 1] = not_negative(field[i - 1][j - 1], 4)

    else:
        field[i + 1][j] = not_negative(field[i + 1][j], 4)
        field[i - 1][j] = not_negative(field[i - 1][j], 4)
        if j == 0:
            field[i][j + 1] = not_negative(field[i][j + 1], 4)
            field[i + 1][j + 1] = not_negative(field[i + 1][j + 1], 4)
            field[i - 1][j + 1] = not_negative(field[i - 1][j + 1], 4)

        elif j == n - 1:
            field[i][j - 1] = not_negative(field[i][j - 1], 4)
            field[i + 1][j - 1] = not_negative(field[i + 1][j - 1], 4)
            field[i - 1][j - 1] = not_negative(field[i - 1][j - 1], 4)

        else:
            field[i][j + 1] = not_negative(field[i][j + 1], 4)
            field[i][j - 1] = not_negative(field[i][j - 1], 4)
            field[i + 1][j + 1] = not_negative(field[i + 1][j + 1], 4)
            field[i + 1][j - 1] = not_negative(field[i + 1][j - 1], 4)
            field[i - 1][j + 1] = not_negative(field[i - 1][j + 1], 4)
            field[i - 1][j - 1] = not_negative(field[i - 1][j - 1], 4)

for i in field:
    print(*i)



