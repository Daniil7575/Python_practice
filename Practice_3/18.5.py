def equation(a, b):
    a, b = a.split(";"), b.split(";")

    x, y = float(a[1]) - float(b[1]), float(b[0]) - float(a[0])

    c = float(a[0]) * float(b[1]) - float(b[0]) * float(a[1])

    answer = []

    if y == 0 and x != 0:
        answer.append(0 - (c / x))

    elif y != 0 and x == 0:
        answer.append(0 - (c / y))

    elif y != 0 and x != 0:
        answer.append(x / (- y))
        answer.append((abs(c / (- y)))) if c == 0 else c / (- y)

    else:
        answer.append(c)

    print(*answer)


equation("0;0", "0;4")
