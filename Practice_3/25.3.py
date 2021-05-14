import random

a = 0
for j in range(55):
    in_circle = 0
    for i in range(10000):
        if ((random.randint(0, 1000) / 1000) ** 2 + (random.randint(0, 1000) / 1000) ** 2) <= 1:
            in_circle += 1
    a += (in_circle / 10000) * 4

print(a / 55)
