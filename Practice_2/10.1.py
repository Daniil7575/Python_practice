word = input()
c = int(input()) - 1
if 0 <= c < len(word):
    print(word[c])
else:
    print("ОШИБКА")
