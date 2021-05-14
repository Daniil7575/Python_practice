def solve(*coefficients):
    if 0 < len(coefficients) <= 3:
        coeff = list(coefficients[::])

        for i in range(2):
            if len(coeff) == 3:
                break
            coeff.insert(0, 0)

        a, b, c = float(coeff[0]), float(coeff[1]), float(coeff[2])

        roots = set()

        if a == 0 and b == 0:
            return ["all"] if c == 0 else ["false"]

        elif a != 0:
            if b != 0:
                d = (b ** 2) - 4 * a * c

                if d < 0:
                    return ["no valid roots (only complex)"]

                roots.add((- b + d ** 0.5) / (2 * a))
                roots.add((- b - d ** 0.5) / (2 * a))

            else:
                return (-c / a) ** 0.5, -(-c / a) ** 0.5 if c * a < 0 else ["false"]

        else:
            roots.add(- c / b)

        return roots

    else:
        return None


print(*solve(*input().split(" ")))
