def partial_sums(*numbers):
    sums = [0]

    for i in range(1, len(numbers) + 1):
        tmp = 0

        for j in range(i):
            tmp += numbers[j]

        sums.append(tmp)

    return sums


# print(partial_sums(1, 0.5, 0.25, 0.125))
