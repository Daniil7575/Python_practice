def roots_of_quadratic_equation(a, b, c):
    roots = set()
    if a == 0 and b == 0:
        return ["all"] if c == 0 else ["false"]

    elif a != 0:
        if b != 0:
            d = (b**2) - 4 * a * c

            if d < 0:
                return ["no valid roots (only complex)"]

            roots.add((- b + d ** 0.5) / (2 * a))
            roots.add((- b - d ** 0.5) / (2 * a))

        else:
            return (-c / a) ** 0.5, -(-c / a) ** 0.5 if c * a < 0 else ["false"]

    else:
        roots.add(- c / b)

    return roots


# print(*sorted(roots_of_quadratic_equation(int(input()), int(input()), int(input()))))