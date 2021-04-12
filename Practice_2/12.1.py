white_list = []
out = []
for i in range(int(input())):
    white_list.append(input())
for i in range(int(input())):
    a = input()
    if a in white_list:
        out.append(a)

for i in out:
    print(i)
