import string
import random


def generate_password(m):
    symbols = [[i for i in string.ascii_lowercase if i != "l" and i != "o"],
               [i for i in string.ascii_uppercase if i != "I" and i != "O"],
               [i for i in string.digits if i != "1" and i != "0"]]

    password = ["", False, False, False]

    choice = random.choice(random.choice(symbols))

    while len(password[0]) < m:
        choice = random.choice(random.choice(symbols))

        while choice in password[0]:
            choice = random.choice(random.choice(symbols))

        if choice in string.ascii_lowercase:
            password[1] = True

        if choice in string.ascii_uppercase:
            password[2] = True

        if choice in string.digits:
            password[3] = True

        password[0] += choice

        if len(password[0]) - m == 0 and not all(password[1:]):
            password = ["", False, False, False]

    return password[0]


def main(n, m):
    return [generate_password(m) for i in range(n)]


# print(*main(5, 56), sep="\n")
