brothers = [[], []]
coincidences = 0

for i in range(int(input())):
    indicator = int(input())
    brothers[0].append(indicator)
    brothers[1].append(indicator)

for i in range(int(input())):
    brothers[int(input()) - 1][int(input())] += int(input())

for i in range(len(brothers[0])):
    if brothers[0][i] == brothers[1][i]:
        coincidences += 1

for i in range(len(brothers)):
    for j in brothers[i]:
        print(j, end=" ")
    print()

print(coincidences)



