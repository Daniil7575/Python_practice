def contains(sub, pri):
    M, N = len(pri), len(sub)
    i, LAST = 0, M-N+1
    while True:
        try:
            found = pri.index(sub[0], i, LAST)
        except ValueError:
            return False
        if pri[found:found+N] == sub:
            return [found, found+N-1]
        else:
            i = found+1


fridge = []
receipts = dict()
for i in range(int(input())):
    fridge.append(input())

for i in range(int(input())):
    name = input()
    list = []
    for k in range(int(input())):
        list.append(input())
    receipts[name] = list

for i in receipts:
    if contains(receipts[i], fridge):
        print(i)
