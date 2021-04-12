import math


names = []
decimation_list = []
n = int(input())

for i in range(n):
    names.append(input())

k = int(input())

for i in range(math.ceil(n / k) + 1):
    temp = names[::k]
    for j in range(len(temp)):
        decimation_list.append(names.pop(names.index(temp[j])))

for i in decimation_list:
    print(i)


