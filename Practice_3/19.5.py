def prime(number):
    if 1 < number < 4:
        return "Простое"
    if number == 1:
        return "Ни простое ни составное"

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return "Составное"

        else:
            pass

    return "Простое"


# print(prime(int(input())))
