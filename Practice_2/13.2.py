out = []

for i in range(int(input())):
    out.append(int(input()))
out.sort()

for i in out[::-1]:
    print(i)
