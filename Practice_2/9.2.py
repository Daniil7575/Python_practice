pupils = []
buffer = []

for m in range(int(input())):
    for n in range(int(input())):
        buffer.append(input())
    if m == 0:
        for p in buffer:
            pupils.append(p)
    else:
        for p in pupils:
            if not buffer.__contains__(p):
                pupils.remove(p)
    buffer.clear()

for p in pupils:
    print(p)
