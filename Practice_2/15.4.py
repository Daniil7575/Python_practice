def median(temp_list):
    temp_list.sort()
    return temp_list[len(temp_list) // 2]


def mode(list_):
    count = 0
    number = []
    for j in list_:
        if list_.count(j) > count:
            count = list_.count(j)

    for j in list_:
        if list_.count(j) == count:
            if not(j in number):
                number.append(j)
    return number


n = int(input())
set_of_numbers = []
medians = []
modes = []

for i in range(n):
    set_of_numbers.append(input().split(" "))

for i in set_of_numbers:
    m = median(i)
    medians.append(m)
    print(m, end=" ")

print()

for i in set_of_numbers:
    m = mode(i)
    modes.append(*m)
    print(*m, end=" ")

print()

print(median(medians))
print(*mode(modes), sep=" ")

print(median(sum(set_of_numbers, [])))
print(*mode((sum(set_of_numbers, []))))
