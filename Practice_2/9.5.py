dishes = []

for i in range(int(input())):
    dishes.append(input())

for i in range(int(input())):
    for k in range(int(input())):
        dish = input()
        if dishes.__contains__(dish):
            dishes.remove(dish)

for d in dishes:
    print(d)
