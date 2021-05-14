def golden_ratio(i):
    phib = [1, 1]

    for j in range(i - 1):
        phib.append(phib[0] + phib[1])
        phib.pop(0)

    print(phib[1] / phib[0])


golden_ratio(5)
