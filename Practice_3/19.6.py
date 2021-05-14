def catalan(number):
    catalans_numbers = [1]
    if number == 0:
        return catalans_numbers[0]

    else:
        for i in range(0, number):
            catalans_numbers.append(0)

            for j in range(0, len(catalans_numbers) - 1):
                catalans_numbers[i + 1] += catalans_numbers[j] * catalans_numbers[i - j]

    return catalans_numbers[number]


# print(catalan(int(input())))