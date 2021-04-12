def count_posts(sons_weight_flag, nodes):
    if len(sons_weight_flag[0]) != 0 and not sons_weight_flag[2]:
        for index in range(len(sons_weight_flag[0])):
            sons_weight_flag[1] += count_posts(nodes[sons_weight_flag[0][index]], nodes)

    sons_weight_flag[2] = True

    return sons_weight_flag[1]


n = int(input())

events = [input() for k in range(n)]
hierarchy = {}

for i in events:
    if "опубликовал" in i:
        hierarchy[i.split(" ")[0]] = [[], int(i.split(" ")[len(i.split(" ")) - 1]), False]

    elif "отрепостил" in i:
        hierarchy[i.split(" ")[0]] = [[], int(i.split(" ")[len(i.split(" ")) - 1]), False]

        for key, value in hierarchy.items():
            if key == i.split(" ")[4].split(",")[0]:
                value[0].append(i.split(" ")[0])

for key, value in hierarchy.items():
    if len(value[0]) != 0:
        temp = hierarchy.copy()
        value[1] = count_posts(value, temp)
        print(value[1])
    else:
        print(value[1])
