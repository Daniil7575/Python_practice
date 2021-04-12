n = int(input())

queue = []

for i in range(n):
    event = input()
    if not("," in event):
        queue.append(event.split(" ")[0])
    elif "!" in event:
        queue.insert(queue.index(event.split("!")[0].split(" ")[1]) + 1,
                     event.split("!")[1].split(" ")[1])
    else:
        queue.remove(event.split(",")[0])

print(*queue, sep="\n")
