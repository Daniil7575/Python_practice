repository = [[j for j in input().split(",")] for i in range(int(input()))]

# Заменим символ запятой на "@c", а символ перехода на новую строку - "@n"
# То есть, если нужно записать строку "пример, пример" в одну ячейку, то
# нужно записать туда "пример@c пример" (аналогично с переходм на новую строку)

for k in range(int(input())):
    i, j = input().split(",")
    z = repository[int(i)][int(j)]

    if "@c" in z:
        z = z.replace("@c", ",")
        print(z)

    elif "@n" in z:
        z = z.replace("@n", "\n")
        print(z)

    else:
        print(z)
