permissions = [input().split("/")[1:] for i in range(int(input()))]

m = int(input())

for i in range(m):
    folder = input(). split("/")[1:]
    is_accept = False
    for j in permissions:

        if j[0] == folder[0]:
            for k in range(1, len(j)):
                if j[k] == folder[k] and k == len(j) - 1:
                    is_accept = True
                else:
                    break
    print("YES") if is_accept else print("NO")

