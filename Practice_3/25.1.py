import string
import random


def generate_password(m):
    illegal_symbols = "1loOI0"
    symbols = [str(i) for i in string.ascii_letters + string.digits if i not in illegal_symbols]

    password = ""

    choice = random.choice(symbols)

    while len(password) < m:
        while choice in password:
            choice = random.choice(symbols)

        password += choice
        choice = random.choice(symbols)

    return password


def main(n, m):
    return [generate_password(m) for i in range(n)]


# print(*main(10, 5), sep="\n")
