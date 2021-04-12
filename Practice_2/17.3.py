import operator


n = int(input())

birthday = sorted([input().split(" ") for i in range(n)], key=operator.itemgetter(2, 1))

for i in range(int(input())):
    is_found = False

    month = input()

    for j in birthday:
        if month in j:
            is_found = True
            print(j[0] + " " + j[1], end=" ")

    if not is_found:
        print("", end=" ")

    print()
