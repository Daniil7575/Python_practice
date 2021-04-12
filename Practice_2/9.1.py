m = int(input())
n = int(input())

storage = [input() for i in range(m)]

for i in range(n):
    print("YES") if input() in storage else print("NO")
