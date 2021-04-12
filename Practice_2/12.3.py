purchases = []
for i in range(int(input())):
    purchases.append((input(), int(input())))
purchases = dict(purchases[::-1])
for i in purchases:
    print(i + " " + str(purchases[i]))

