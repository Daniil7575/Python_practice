inp = input().lower()
max_ent = 0
for i in inp:
    if inp.count(i) > max_ent:
        max_ent = inp.count(i)

print(max_ent)
