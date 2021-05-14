def hello(name):
    print(f"Здравствуйте, {name}! Вашу карту ищут...")


def search_card(name):
    print(f"Ваша карта с номером {base.index(name) + 1}" if name in base else "Ваша карта не найдена")


base = []
# for i in range(int(input("Введите число мед. карт\n"))):
#     base.append(input("Введите имя\n"))
#
# for i in range(int(input("Введите размер очереди\n"))):
#     inp = input("Введите имя\n")
#
#     hello(inp)
#     search_card(inp)
