n = int(input())

phone_book = [input().split(" ") for i in range(n)]

for i in range(int(input())):
    name = input()
    is_found = False

    for j in phone_book:
        if name in j:
            is_found = True
            print(j[0], end=" ")

    if not is_found:
        print("Нет телефона в телефонной книге", end=" ")

    print()
