emp = {}
for i in range(int(input())):
    cur_emp = input()
    if cur_emp in emp:
        emp[cur_emp] += 1
    else:
        emp[cur_emp] = 1

out = 0
for e in emp:
    if emp[e] != 1:
        out += emp[e]

print(out)
