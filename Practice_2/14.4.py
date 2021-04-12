numbers = input().split(" ")
h = int(max(numbers))

print("*" * (len(numbers) + 2) + "\n*" + " " * len(numbers) + "*")
line = ""

for i in range(h):
    for j in range(len(numbers)):
        if int(numbers[j]) >= h - i:
            line += "*"
        else:
            line += " "
    print("*" + line + "*")
    line = ""
