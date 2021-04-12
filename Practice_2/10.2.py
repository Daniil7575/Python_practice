# более костыльной реализации этой программы быть не может
alp = "абвгдежзийклмнопрстуфхцчшщъыьэюя"


def caesar(inp, rotor):
    rotor %= len(alp)
    temp = inp
    b = ""
    for i in range(len(temp)):
        mall = alp.index(temp[i]) + rotor
        while mall >= len(alp):
            mall -= len(alp)
        b += alp[mall]
    return b


result = ""
rotor = int(input())
inp = input()

for i in inp:
    if alp.__contains__(i):
        result += caesar(i, rotor)
    else:
        result += i

print(result)
