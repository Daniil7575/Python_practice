import re


check = []
error = []
is_true = False
true_cost = 0

count_cost = re.findall(r"\d+", input())
count_cost[0], count_cost[1] = int(count_cost[0]), int(count_cost[1])

for i in range(count_cost[0]):
    check = re.findall(r"\d+", input())
    true_cost += int(check[0]) * int(check[1])

    if int(check[0]) * int(check[1]) != int(check[2]):
        error.append(i)

if true_cost == count_cost[1]:
    print(count_cost[1] - true_cost)
else:
    print(count_cost[1] - true_cost)
    for a in error:
        print(a + 1, end=" ")
