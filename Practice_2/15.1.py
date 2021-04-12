forbidden_letter = input()
words = input().split(" ")

for i in words:
    if forbidden_letter in i or forbidden_letter.upper() in i:
        print(i)