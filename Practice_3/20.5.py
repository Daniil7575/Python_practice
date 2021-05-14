def lucky(ticket):
    ticket = str(ticket)

    if len(ticket) < 6:
        ticket = ("000000" + ticket)[:-7:-1][::-1]

    a, b, last_a, last_b = 0, 0, 0, 0

    for i in range(0, len(ticket) // 2):
        a += int(ticket[i])
        last_a += int(str(last_ticket)[i])

    for i in range(len(ticket) // 2, len(ticket)):
        b += int(ticket[i])
        last_b += int(str(last_ticket)[i])

    return "Счастливый" if a == b and last_a == last_b else "Несчастливый"


# last_ticket = int(input("lastticket = "))
# print(lucky(int(input("ticket = "))))
