import math
import operator


teams_and_score = []

for i in range(int(input())):
    teams_and_score.append((input(), int(input())))

teams_and_score = sorted(teams_and_score, key=operator.itemgetter(1), reverse=True)
final = sorted(teams_and_score[:math.ceil(len(teams_and_score)/2)], key=operator.itemgetter(0))

for i in final:
    print(teams_and_score.pop(teams_and_score.index(i))[0])

for i in sorted(teams_and_score, key=operator.itemgetter(0)):
    print(i[0])




