a = [" * ", "* *", "***", "* *", "* *"]
b = ["** ", "* *", "** ", "* *", "** "]
c = [" **", "*  ", "*  ", "*  ", " **"]
out5line = ["", "", "", "", ""]

line = input()

for i in line:
    if i == "A":
        for j in range(5):
            out5line[j] += a[j] + "  "
    elif i == "B":
        for j in range(5):
            out5line[j] += b[j] + "  "
    elif i == "C":
        for j in range(5):
            out5line[j] += c[j] + "  "

for i in out5line:
    print(i)
