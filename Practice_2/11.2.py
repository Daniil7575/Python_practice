cnt = int(input())
for i in range(cnt):
    inp = input()
    if inp.startswith("%%"):
        inp = inp.replace("%%", "")
        print(inp)
    elif inp.startswith("####"):
        pass
    else:
        print(inp)
    